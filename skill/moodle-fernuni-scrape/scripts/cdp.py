#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pilote un navigateur Chromium (Chrome ou Edge) via le Chrome DevTools Protocol.

Pourquoi ce fichier existe : la version precedente du skill pilotait Chrome par
AppleScript, ce qui la rendait inutilisable ailleurs que sur macOS. CDP parle le
meme protocole sur macOS, Windows et Linux, et sur Chrome comme sur Edge.

Aucune dependance externe : le client WebSocket est implemente ici en stdlib
(RFC 6455, cote client). Un etudiant n'a donc rien a installer via pip.

Contrainte imposee par Chrome 136+ : --remote-debugging-port est refuse sur le
profil par defaut. On lance donc le navigateur avec un profil dedie
(~/.kaido/chrome-profile). Ce profil demarre vierge : l'etudiant s'y connecte a
Moodle une fois, puis la session persiste d'une execution a l'autre.
"""

import base64
import json
import os
import platform
import shutil
import socket
import struct
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

DEFAULT_PORT = int(os.environ.get("KAIDO_CDP_PORT", "9222"))
PROFILE_DIR = Path(os.environ.get("KAIDO_CDP_PROFILE", str(Path.home() / ".kaido" / "chrome-profile")))


# --------------------------------------------------------------------------
# Client WebSocket minimal (client only, masquage obligatoire cote client)
# --------------------------------------------------------------------------

class WebSocket:
    def __init__(self, url, timeout=300):
        u = urllib.parse.urlparse(url)
        port = u.port or 80
        self.sock = socket.create_connection((u.hostname, port), timeout=15)
        self.sock.settimeout(timeout)
        key = base64.b64encode(os.urandom(16)).decode()
        path = u.path + (("?" + u.query) if u.query else "")
        req = (
            "GET %s HTTP/1.1\r\n"
            "Host: %s:%d\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            "Sec-WebSocket-Key: %s\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n" % (path, u.hostname, port, key)
        )
        self.sock.sendall(req.encode("ascii"))
        buf = b""
        while b"\r\n\r\n" not in buf:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise RuntimeError("handshake WebSocket interrompu")
            buf += chunk
        head, _, rest = buf.partition(b"\r\n\r\n")
        status = head.split(b"\r\n")[0].decode("latin-1")
        if "101" not in status:
            raise RuntimeError("handshake WebSocket refuse : %s" % status)
        self._buf = rest

    def _read(self, n):
        while len(self._buf) < n:
            chunk = self.sock.recv(max(4096, n - len(self._buf)))
            if not chunk:
                raise RuntimeError("connexion WebSocket fermee par le navigateur")
            self._buf += chunk
        out, self._buf = self._buf[:n], self._buf[n:]
        return out

    def send(self, text):
        payload = text.encode("utf-8")
        header = bytearray([0x81])  # FIN + opcode texte
        mask = os.urandom(4)
        n = len(payload)
        if n < 126:
            header.append(0x80 | n)
        elif n < 65536:
            header.append(0x80 | 126)
            header += struct.pack(">H", n)
        else:
            header.append(0x80 | 127)
            header += struct.pack(">Q", n)
        header += mask
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.sock.sendall(bytes(header) + masked)

    def recv(self):
        """Retourne le prochain message texte complet (reassemble les fragments)."""
        chunks = []
        while True:
            b0, b1 = self._read(2)
            fin = b0 & 0x80
            opcode = b0 & 0x0F
            length = b1 & 0x7F
            if length == 126:
                length = struct.unpack(">H", self._read(2))[0]
            elif length == 127:
                length = struct.unpack(">Q", self._read(8))[0]
            data = self._read(length) if length else b""
            if opcode == 0x8:  # close
                raise RuntimeError("le navigateur a ferme la connexion CDP")
            if opcode == 0x9:  # ping -> pong
                self.sock.sendall(b"\x8a" + bytes([0x80 | len(data)]) + os.urandom(4)
                                  + bytes(d ^ 0 for d in data))
                continue
            if opcode == 0xA:  # pong
                continue
            chunks.append(data)
            if fin:
                return b"".join(chunks).decode("utf-8", "replace")

    def close(self):
        try:
            self.sock.close()
        except Exception:
            pass


# --------------------------------------------------------------------------
# Endpoint HTTP du navigateur
# --------------------------------------------------------------------------

def http_json(port, path="/json/list", timeout=5):
    url = "http://127.0.0.1:%d%s" % (port, path)
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))


def is_up(port=DEFAULT_PORT):
    try:
        http_json(port, "/json/version", timeout=2)
        return True
    except Exception:
        return False


def tabs(port=DEFAULT_PORT):
    return [t for t in http_json(port) if t.get("type") == "page"]


def find_tab(match, port=DEFAULT_PORT):
    """Premier onglet dont l'URL contient `match`. None si aucun."""
    for t in tabs(port):
        if match in (t.get("url") or ""):
            return t
    return None


# --------------------------------------------------------------------------
# Session CDP sur un onglet
# --------------------------------------------------------------------------

class Tab:
    def __init__(self, target, timeout=300):
        self.target = target
        self.ws = WebSocket(target["webSocketDebuggerUrl"], timeout=timeout)
        self._id = 0

    def call(self, method, **params):
        self._id += 1
        mid = self._id
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") != mid:
                continue  # evenement CDP non sollicite
            if "error" in msg:
                raise RuntimeError("CDP %s : %s" % (method, msg["error"].get("message")))
            return msg.get("result", {})

    def evaluate(self, expression, await_promise=True):
        """Evalue du JS dans la page et retourne la valeur JSON.

        await_promise resout les promesses cote navigateur : plus besoin de la
        boucle de scrutation sur window.__xxx qu'imposait AppleScript.
        """
        res = self.call(
            "Runtime.evaluate",
            expression=expression,
            awaitPromise=await_promise,
            returnByValue=True,
            userGesture=True,
        )
        if res.get("exceptionDetails"):
            det = res["exceptionDetails"]
            desc = (det.get("exception") or {}).get("description") or det.get("text")
            raise RuntimeError("exception JS : %s" % desc)
        return res.get("result", {}).get("value")

    def navigate(self, url, timeout=30):
        self.call("Page.enable")
        self.call("Page.navigate", url=url)
        deadline = time.time() + timeout
        while time.time() < deadline:
            time.sleep(0.4)
            try:
                state = self.evaluate("document.readyState", await_promise=False)
                here = self.evaluate("location.href", await_promise=False)
            except Exception:
                continue
            if state == "complete" and here and here != "about:blank":
                return here
        return None

    def close(self):
        self.ws.close()


def open_tab(url, port=DEFAULT_PORT):
    """Cree un onglet et retourne sa description."""
    q = urllib.parse.quote(url, safe="")
    with urllib.request.urlopen("http://127.0.0.1:%d/json/new?%s" % (port, q),
                                data=b"", timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))


def require_browser(port=DEFAULT_PORT):
    if not is_up(port):
        raise SystemExit(
            "NAVIGATEUR_HORS_LIGNE : rien n'ecoute sur le port %d.\n"
            "Lance-le d'abord :\n"
            "  python3 %s launch https://moodle.fernuni.ch/\n"
            "puis connecte-toi a Moodle dans la fenetre qui s'ouvre." % (port, Path(__file__).name)
        )


def attach(match, port=DEFAULT_PORT, timeout=300):
    require_browser(port)
    t = find_tab(match, port)
    if t is None:
        raise SystemExit(
            "AUCUN_ONGLET correspondant a %r.\n"
            "Onglets ouverts :\n  %s" % (match, "\n  ".join(x.get("url", "") for x in tabs(port)) or "(aucun)")
        )
    return Tab(t, timeout=timeout)


# --------------------------------------------------------------------------
# Lancement du navigateur, multiplateforme
# --------------------------------------------------------------------------

def browser_candidates(prefer=None):
    system = platform.system()
    chrome, edge = [], []
    if system == "Darwin":
        chrome = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                  str(Path.home()) + "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
        edge = ["/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"]
    elif system == "Windows":
        pf = os.environ.get("ProgramFiles", r"C:\Program Files")
        pf86 = os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")
        lad = os.environ.get("LOCALAPPDATA", "")
        chrome = [os.path.join(pf, r"Google\Chrome\Application\chrome.exe"),
                  os.path.join(pf86, r"Google\Chrome\Application\chrome.exe"),
                  os.path.join(lad, r"Google\Chrome\Application\chrome.exe")]
        edge = [os.path.join(pf86, r"Microsoft\Edge\Application\msedge.exe"),
                os.path.join(pf, r"Microsoft\Edge\Application\msedge.exe")]
    else:
        chrome = [p for p in (shutil.which("google-chrome"), shutil.which("google-chrome-stable"),
                              shutil.which("chromium"), shutil.which("chromium-browser")) if p]
        edge = [p for p in (shutil.which("microsoft-edge"),) if p]
    order = {"chrome": [chrome, edge], "edge": [edge, chrome]}.get(prefer, [chrome, edge])
    return [p for group in order for p in group if p and os.path.exists(p)]


def launch(url=None, port=DEFAULT_PORT, prefer=None):
    if is_up(port):
        return "DEJA_LANCE port=%d profil=%s" % (port, PROFILE_DIR)
    cands = browser_candidates(prefer)
    if not cands:
        raise SystemExit(
            "NAVIGATEUR_INTROUVABLE : ni Chrome ni Edge n'ont ete trouves.\n"
            "Installe Google Chrome, ou indique le binaire avec KAIDO_CDP_BROWSER."
        )
    binary = os.environ.get("KAIDO_CDP_BROWSER") or cands[0]
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)
    args = [binary,
            "--remote-debugging-port=%d" % port,
            "--user-data-dir=%s" % PROFILE_DIR,
            "--no-first-run",
            "--no-default-browser-check"]
    if url:
        args.append(url)
    kwargs = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    if platform.system() == "Windows":
        kwargs["creationflags"] = 0x00000008 | 0x00000200  # DETACHED_PROCESS | NEW_PROCESS_GROUP
    else:
        kwargs["start_new_session"] = True
    subprocess.Popen(args, **kwargs)
    deadline = time.time() + 30
    while time.time() < deadline:
        if is_up(port):
            return "LANCE %s port=%d profil=%s" % (os.path.basename(binary), port, PROFILE_DIR)
        time.sleep(0.5)
    raise SystemExit("ECHEC_LANCEMENT : le navigateur n'ecoute pas sur le port %d" % port)


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

USAGE = """Usage :
  cdp.py launch [url] [--edge]     lance le navigateur avec le profil dedie
  cdp.py status                    verifie la connexion et liste les onglets
  cdp.py eval <match> [fichier.js] evalue du JS dans l'onglet (sinon stdin)
  cdp.py open <url> <match>        navigue un onglet vers une URL et attend
"""


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(USAGE)
        return 0
    cmd, rest = argv[0], argv[1:]
    port = DEFAULT_PORT

    if cmd == "launch":
        prefer = "edge" if "--edge" in rest else "chrome"
        url = next((a for a in rest if not a.startswith("--")), None)
        print(launch(url, port, prefer))
        return 0

    if cmd == "status":
        if not is_up(port):
            print("HORS_LIGNE : aucun navigateur en ecoute sur le port %d.\n"
                  "Lance-le avec :  python3 cdp.py launch" % port)
            return 1
        v = http_json(port, "/json/version")
        print("OK %s (profil %s)" % (v.get("Browser", "?"), PROFILE_DIR))
        for t in tabs(port):
            print("  - %s" % t.get("url", ""))
        return 0

    if cmd == "eval":
        match = rest[0]
        js = Path(rest[1]).read_text(encoding="utf-8") if len(rest) > 1 else sys.stdin.read()
        tab = attach(match, port)
        try:
            out = tab.evaluate(js)
        finally:
            tab.close()
        print(out if isinstance(out, str) else json.dumps(out, ensure_ascii=False))
        return 0

    if cmd == "open":
        url, match = rest[0], rest[1]
        t = find_tab(match, port)
        tab = Tab(t) if t else Tab(open_tab("about:blank", port))
        try:
            final = tab.navigate(url, timeout=int(rest[2]) if len(rest) > 2 else 30)
        finally:
            tab.close()
        if final is None:
            print("TIMEOUT %s" % url, file=sys.stderr)
            return 1
        print(final)
        return 0

    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
