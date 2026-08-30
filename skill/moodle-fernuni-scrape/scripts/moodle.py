#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aspiration d'un cours Moodle FernUni/UniDistance, multiplateforme.

Remplace les scripts .sh AppleScript de la version macOS. Tout passe par cdp.py,
donc par le Chrome DevTools Protocol : identique sur macOS, Windows et Linux, et
sur Chrome comme sur Edge. Invocable depuis bash comme depuis PowerShell.

Sous-commandes :
  expand    <match>                             deplie les sections repliees du cours
  enumerate <match>                             liste files / pages / links / subcourses (JSON)
  capture   <match> <dest.md>                   ecrit le texte de la page courante
  page      <url> <match> <dest.md>             navigue puis capture une mod/page
  folder    <match> <url_dossier>               liste les pluginfile d'un mod/folder (une par ligne)
  fetch     <match> <url> <dest_dir> <nom>      telecharge un fichier (PDF, docx, pptx...)
  resolve   <match> [urls... | -]               resout des mod/url vers leur cible (TSV)
  video     <url_page> <dest_dir> <nom> [rendu] telecharge une video SWITCHtube
  check     <dest_dir>                          verifie l'integrite de ce qui a ete aspire
"""

import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cdp  # noqa: E402

SCRIPTS = Path(__file__).resolve().parent


def die(msg, code=2):
    print(msg, file=sys.stderr)
    raise SystemExit(code)


def run_js_file(match, filename):
    tab = cdp.attach(match)
    try:
        return tab.evaluate((SCRIPTS / filename).read_text(encoding="utf-8"))
    finally:
        tab.close()


def js_string(s):
    """Injecte une chaine Python dans du JS sans risque de quoting."""
    return json.dumps(s)


# --------------------------------------------------------------------------

def cmd_expand(match):
    print(run_js_file(match, "expand_sections.js"))


def cmd_enumerate(match):
    print(run_js_file(match, "enumerate.js"))


def cmd_capture(match, dest):
    raw = run_js_file(match, "capture_page.js")
    data = json.loads(raw)
    out = Path(dest)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("# %s\n\nSource : %s\n\n%s\n" % (data["title"], data["url"], data["text"]),
                   encoding="utf-8")
    print("OK %s (%d caracteres)" % (out, len(data["text"])))


def cmd_page(url, match, dest):
    """Navigue un onglet vers une mod/page puis capture son texte."""
    cdp.require_browser()
    t = cdp.find_tab(match) or cdp.open_tab("about:blank")
    tab = cdp.Tab(t)
    try:
        if tab.navigate(url, timeout=30) is None:
            die("TIMEOUT_NAVIGATION %s" % url, 3)
        raw = tab.evaluate((SCRIPTS / "capture_page.js").read_text(encoding="utf-8"))
    finally:
        tab.close()
    data = json.loads(raw)
    out = Path(dest)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("# %s\n\nSource : %s\n\n%s\n" % (data["title"], data["url"], data["text"]),
                   encoding="utf-8")
    print("OK %s (%d caracteres)" % (out, len(data["text"])))


def cmd_folder(match, url):
    """Un mod/folder ne se telecharge pas : on extrait ses liens pluginfile."""
    js = """
    (function(){
      return fetch(%s,{credentials:"include"}).then(function(r){return r.text();})
        .then(function(html){
          var d=document.implementation.createHTMLDocument("");
          d.documentElement.innerHTML=html;
          var seen={}, out=[];
          [].slice.call(d.querySelectorAll("a[href]")).forEach(function(a){
            var h=a.href;
            if(/pluginfile\\.php/.test(h) && !seen[h]){ seen[h]=1; out.push(h); }
          });
          return JSON.stringify(out);
        });
    })();""" % js_string(url)
    tab = cdp.attach(match)
    try:
        raw = tab.evaluate(js)
    finally:
        tab.close()
    for u in json.loads(raw):
        print(u)


def cmd_fetch(match, url, dest_dir, want):
    """Telecharge un fichier par fetch(credentials:include) dans l'onglet du cours.

    Meme origine donc session authentifiee. Le contenu revient en base64 par CDP,
    en un seul appel : awaitPromise resout la promesse cote navigateur.
    """
    furl = url + ("&" if "?" in url else "?") + "redirect=1"
    js = """
    (function(){
      return fetch(%s,{credentials:"include"}).then(function(r){
        var cd=r.headers.get("content-disposition")||"";
        var ct=r.headers.get("content-type")||"";
        var m=/filename\\*?=(?:UTF-8''|")?([^";]+)/i.exec(cd);
        var fn=m?decodeURIComponent(m[1].replace(/"/g,"")):((r.url.split("/").pop()||"download").split("?")[0]);
        return r.arrayBuffer().then(function(buf){
          var bytes=new Uint8Array(buf), bin="", CH=0x8000;
          for(var i=0;i<bytes.length;i+=CH){bin+=String.fromCharCode.apply(null,bytes.subarray(i,i+CH));}
          return JSON.stringify({ok:true,fn:fn,ct:ct,b64:btoa(bin)});
        });
      }).catch(function(e){ return JSON.stringify({ok:false,err:String(e)}); });
    })();""" % js_string(furl)

    tab = cdp.attach(match)
    try:
        raw = tab.evaluate(js)
    finally:
        tab.close()
    data = json.loads(raw)
    if not data.get("ok"):
        die("ECHEC_FETCH (%s) pour : %s" % (data.get("err"), url), 3)

    import base64
    fn, ct = data["fn"], data["ct"]
    ext = fn.rsplit(".", 1)[-1] if "." in fn else ""
    if not ext or len(ext) > 5:
        low = ct.lower()
        ext = ("pdf" if "pdf" in low else
               "docx" if ("word" in low or "docx" in low) else
               "pptx" if ("powerpoint" in low or "presentation" in low) else
               "xlsx" if ("sheet" in low or "excel" in low) else
               "zip" if "zip" in low else "bin")
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)
    target = dest / ("%s.%s" % (want, ext))
    target.write_bytes(base64.b64decode(data["b64"]))
    size = target.stat().st_size
    if size == 0:
        target.unlink(missing_ok=True)
        die("FICHIER_VIDE pour : %s" % url, 4)
    print("OK %s (%d o)" % (target, size))


def cmd_resolve(match, args):
    if args == ["-"] or not args:
        urls = [l.strip() for l in sys.stdin if l.strip()]
    else:
        urls = args
    if not urls:
        die("aucune URL a resoudre")
    js = """
    (function(){
      var urls=%s, out={};
      function next(i){
        if(i>=urls.length) return Promise.resolve(JSON.stringify(out));
        var u=urls[i], sep=u.indexOf("?")>=0?"&":"?";
        return fetch(u+sep+"redirect=0",{credentials:"include"})
          .then(function(r){return r.text();})
          .then(function(h){
            var d=document.implementation.createHTMLDocument("");
            d.documentElement.innerHTML=h;
            var main=d.querySelector("#region-main")||d.body;
            var a=main.querySelector(".urlworkaround a[href]");
            var href=a?a.getAttribute("href"):null;
            if(!href){
              var e=main.querySelector("iframe[src],object[data]");
              if(e) href=e.getAttribute("src")||e.getAttribute("data");
            }
            if(!href){
              var ext=[].slice.call(main.querySelectorAll("a[href]"))
                .map(function(x){return x.getAttribute("href");})
                .filter(function(x){return x && /^https?:/.test(x) && x.indexOf("moodle.fernuni.ch")<0;});
              if(ext.length===1) href=ext[0];
            }
            out[u]=href||"ECHEC";
            return next(i+1);
          })
          .catch(function(){ out[u]="ECHEC"; return next(i+1); });
      }
      return next(0);
    })();""" % json.dumps(urls)

    tab = cdp.attach(match, timeout=600)
    try:
        raw = tab.evaluate(js)
    finally:
        tab.close()
    for k, v in json.loads(raw).items():
        print("%s\t%s" % (k, v or "ECHEC"))


# --------------------------------------------------------------------------
# Videos SWITCHtube
# --------------------------------------------------------------------------

PROBE_JS = """
(function(){
  var srcs={}, v=document.querySelector("video");
  if(v){
    [].slice.call(v.querySelectorAll("source")).forEach(function(s){
      var m=/\\/(h264-\\d+p|audio)\\.(mp4|mp3)/.exec(s.src);
      if(m) srcs[m[1].replace("h264-","")]=s.src;
    });
    if(!Object.keys(srcs).length && v.src) srcs["direct"]=v.src;
  }
  return JSON.stringify({n:Object.keys(srcs).length, srcs:srcs,
                         title:(document.title||"").trim(), url:location.href});
})();"""

FALLBACK = {
    "1080p": ["1080p", "720p", "540p", "direct"],
    "720p": ["720p", "1080p", "540p", "direct"],
    "540p": ["540p", "720p", "1080p", "direct"],
    "audio": ["audio"],
}


def _curl():
    """curl est present sur macOS, sur Windows 10 1803+ (curl.exe) et sur la
    plupart des Linux. On le prefere a urllib parce qu'il utilise le magasin de
    certificats du systeme : les installeurs python.org de macOS livrent un
    Python sans CA configurees, et urllib y echoue en CERTIFICATE_VERIFY_FAILED.
    urllib reste le repli si curl est absent."""
    return shutil.which("curl")


def remote_size(url):
    """Taille totale via un GET par plage.

    Jamais un HEAD : la signature AWS SigV4 couvre le verbe HTTP, un HEAD sur une
    URL pre-signee valide renvoie 403.
    """
    c = _curl()
    if c:
        # -L : certains hebergeurs redirigent avant de servir le fichier.
        # -D - vide alors les en-tetes de TOUTES les reponses : on garde la derniere.
        r = subprocess.run([c, "-sL", "-r", "0-0", "-D", "-", "-o", os.devnull, url],
                           capture_output=True, text=True)
        found = re.findall(r"^content-range:\s*bytes\s+\d+-\d+/(\d+)", r.stdout, re.I | re.M)
        return int(found[-1]) if found else None
    req = urllib.request.Request(url, headers={"Range": "bytes=0-0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            cr = r.headers.get("Content-Range") or ""
    except urllib.error.URLError:
        return None
    m = re.search(r"/(\d+)\s*$", cr)
    return int(m.group(1)) if m else None


def stream_download(url, target, total=None, tries=3):
    """Telechargement en flux, reprenable."""
    c = _curl()
    if c:
        base = [c, "-fL", "--retry", "3", "--retry-delay", "2", "-o", str(target), url]
        r = subprocess.run(base[:1] + ["-C", "-"] + base[1:], capture_output=True)
        if r.returncode != 0:
            # -C - echoue si le fichier est absent ou deja complet cote serveur.
            r = subprocess.run(base, capture_output=True)
            if r.returncode != 0:
                raise RuntimeError("curl a echoue (%d) : %s"
                                   % (r.returncode, r.stderr.decode("utf-8", "replace")[:300]))
        return target.stat().st_size

    for attempt in range(1, tries + 1):
        have = target.stat().st_size if target.exists() else 0
        if total is not None and have == total:
            return have
        headers = {"Range": "bytes=%d-" % have} if have else {}
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=120) as r, \
                    open(target, "ab" if have else "wb") as f:
                shutil.copyfileobj(r, f, 1024 * 256)
            return target.stat().st_size
        except Exception:
            if attempt == tries:
                raise
            time.sleep(2 * attempt)
    return target.stat().st_size


def cmd_video(page_url, dest_dir, want, rendu="720p"):
    cdp.require_browser()
    t = cdp.find_tab("tube.switch.ch") or cdp.open_tab("about:blank")
    tab = cdp.Tab(t)
    try:
        if tab.navigate(page_url, timeout=30) is None:
            die("ECHEC_NAVIGATION %s" % page_url, 2)
        probe = None
        for _ in range(50):
            time.sleep(0.6)
            try:
                probe = json.loads(tab.evaluate(PROBE_JS, await_promise=False))
            except Exception:
                continue
            if probe.get("n"):
                break
    finally:
        tab.close()

    if not probe or not probe.get("n"):
        die("AUCUNE_SOURCE pour %s (page de connexion ? video restreinte ?)\n"
            "Verifie que le profil dedie est connecte a SWITCHtube." % page_url, 3)

    srcs = probe["srcs"]
    url = ext = None
    for k in FALLBACK.get(rendu, FALLBACK["720p"]):
        if k in srcs:
            url, ext = srcs[k], ("mp3" if k == "audio" else "mp4")
            break
    if not url:
        die("RENDU_INDISPONIBLE (%s) pour %s ; dispo : %s"
            % (rendu, page_url, ", ".join(srcs)), 4)

    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)
    target = dest / ("%s.%s" % (want, ext))
    total = remote_size(url)
    if total is not None and target.exists() and target.stat().st_size == total:
        print("SKIP %s (deja complet)" % target)
        return
    size = stream_download(url, target, total)
    if size == 0:
        target.unlink(missing_ok=True)
        die("FICHIER_VIDE %s" % page_url, 6)
    if total is not None and size != total:
        die("TAILLE_INCOMPLETE %s (%d / %d o)" % (target, size, total), 7)
    print("OK %s (%d o)" % (target, size))


# --------------------------------------------------------------------------

def cmd_check(dest_dir):
    """Verifie ce qui a ete aspire. Remplace les boucles shell BSD du SKILL.md.

    ffprobe est optionnel : son absence est signalee explicitement, elle ne fait
    pas passer les videos pour valides.
    """
    root = Path(dest_dir)
    if not root.exists():
        die("REPERTOIRE_ABSENT %s" % root)
    problems = 0

    pdfs = sorted(root.rglob("*.pdf"))
    for p in pdfs:
        head = p.open("rb").read(4)
        if head != b"%PDF":
            print("SUSPECT %s : en-tete %r, probablement une page d'erreur HTML" % (p, head))
            problems += 1
    print("PDF verifies : %d, suspects : %d" % (len(pdfs), problems))

    vids = sorted(list(root.rglob("*.mp4")) + list(root.rglob("*.mp3")))
    ffprobe = shutil.which("ffprobe")
    if not vids:
        print("Aucune video a verifier.")
    elif not ffprobe:
        print("ffprobe ABSENT : les %d fichiers video ne sont PAS verifies." % len(vids))
        print("  Sans ffprobe, une video tronquee passe inapercue.")
        print("  macOS : brew install ffmpeg   |   Windows : winget install Gyan.FFmpeg")
    else:
        bad = 0
        for v in vids:
            r = subprocess.run([ffprobe, "-v", "error", "-show_entries", "format=duration",
                                "-of", "csv=p=0", str(v)],
                               capture_output=True, text=True)
            dur = (r.stdout or "").strip()
            if r.returncode != 0 or not dur:
                print("ILLISIBLE %s" % v)
                bad += 1
        print("Videos verifiees : %d, illisibles : %d" % (len(vids), bad))
        problems += bad

    empties = [f for f in root.rglob("*") if f.is_file() and f.stat().st_size == 0]
    for f in empties:
        print("VIDE %s" % f)
    problems += len(empties)
    print("TOTAL problemes : %d" % problems)
    return 1 if problems else 0


# --------------------------------------------------------------------------

def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, a = argv[0], argv[1:]
    try:
        if cmd == "expand":
            cmd_expand(a[0])
        elif cmd == "enumerate":
            cmd_enumerate(a[0])
        elif cmd == "capture":
            cmd_capture(a[0], a[1])
        elif cmd == "page":
            cmd_page(a[0], a[1], a[2])
        elif cmd == "folder":
            cmd_folder(a[0], a[1])
        elif cmd == "fetch":
            cmd_fetch(a[0], a[1], a[2], a[3])
        elif cmd == "resolve":
            cmd_resolve(a[0], a[1:])
        elif cmd == "video":
            cmd_video(a[0], a[1], a[2], a[3] if len(a) > 3 else "720p")
        elif cmd == "check":
            return cmd_check(a[0])
        else:
            print(__doc__, file=sys.stderr)
            return 2
    except IndexError:
        die("arguments manquants pour %r.\n%s" % (cmd, __doc__))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
