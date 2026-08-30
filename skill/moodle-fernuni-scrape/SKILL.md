---
name: moodle-fernuni-scrape
description: Récupère tous les supports d'un cours Moodle FernUni/UniDistance (PDF, docx, pptx, pages, dossiers) et les vidéos de cours hébergées sur SWITCHtube (tube.switch.ch) dans data_sources/, en pilotant un navigateur Chrome ou Edge via le Chrome DevTools Protocol. Fonctionne sur macOS, Windows et Linux. À utiliser quand l'utilisateur demande de télécharger/aspirer/récupérer/pomper les supports, documents ou vidéos d'un module Moodle, ou fournit un lien moodle.fernuni.ch/course/view.php ou tube.switch.ch.
---

# Aspiration d'un cours Moodle FernUni

Objectif : télécharger **tous** les documents clés d'un cours Moodle (PDF, Word, PowerPoint,
pages HTML de contenu, dossiers de fichiers) et les vidéos SWITCHtube, et les déposer dans
`data_sources/` du répertoire de travail courant.

**Multiplateforme.** Tout passe par le Chrome DevTools Protocol (CDP), identique sur macOS,
Windows et Linux, et sur Chrome comme sur Edge. Les scripts sont en Python : ils s'exécutent
aussi bien depuis bash que depuis PowerShell, ce qui compte car sur Windows sans Git for
Windows, Claude Code exécute du PowerShell et ne peut pas lancer de `.sh`.

Pourquoi piloter un navigateur plutôt que `curl` : la session Moodle vit dans les cookies du
navigateur. Sur macOS, le profil Chrome est protégé par TCC et illisible depuis le terminal ;
partout, l'authentification SWITCH edu-ID est trop tortueuse à rejouer en ligne de commande.
On fait donc faire les requêtes **par la page elle-même**, qui est déjà authentifiée.

## Prérequis

| Élément | Vérification | Si absent |
|---|---|---|
| Python 3.8+ | `python3 --version` (macOS/Linux) ou `python --version` (Windows) | macOS : déjà là. Windows : `winget install Python.Python.3.12` |
| Chrome ou Edge | détecté automatiquement | installer Chrome |
| `curl` | `curl --version` | présent sur macOS et Windows 10 1803+. Sinon repli automatique sur urllib |
| `ffmpeg`/`ffprobe` | **optionnel**, seulement pour vérifier les vidéos | `brew install ffmpeg` / `winget install Gyan.FFmpeg` |

### Choisir l'interpréteur, une fois pour toutes

Sur Windows, `python3` est un stub qui ouvre le Microsoft Store. **Déterminer l'interpréteur
au début de la session et le réutiliser partout** :

```bash
python3 --version || python --version
```

Dans la suite, `PY` désigne la commande qui a répondu, et `SD` le répertoire du skill
(`~/.claude/skills/moodle-fernuni-scrape/scripts` sur macOS/Linux,
`%USERPROFILE%\.claude\skills\moodle-fernuni-scrape\scripts` sur Windows).

## Préconditions : lancer le navigateur piloté

Depuis **Chrome 136**, `--remote-debugging-port` est refusé sur le profil par défaut. Le skill
lance donc un **profil dédié** (`~/.kaido/chrome-profile`), séparé du profil personnel.

```bash
PY SD/cdp.py launch "https://moodle.fernuni.ch/"
```

Ce profil démarre **vierge**. À la première utilisation seulement :

1. Se connecter à Moodle (SWITCH edu-ID) dans la fenêtre qui s'ouvre.
2. Ouvrir aussi `https://tube.switch.ch/` et s'y connecter, si des vidéos sont attendues.
3. Ouvrir l'onglet du cours : `moodle.fernuni.ch/course/view.php?id=<ID>`.

Les sessions persistent ensuite d'une exécution à l'autre. Vérifier l'état :

```bash
PY SD/cdp.py status
```

Sortie attendue : `OK Chrome/<version> (profil ...)` suivi de la liste des onglets. Si la
réponse est `HORS_LIGNE`, relancer `launch`. **Ne pas continuer tant que `status` n'affiche pas
l'onglet du cours.**

Ajouter `--edge` à `launch` pour piloter Edge au lieu de Chrome.

## Procédure

Toutes les commandes prennent un `<match>` : une sous-chaîne de l'URL identifiant l'onglet à
piloter, typiquement `course/view.php?id=<ID>`.

### 1. Déplier toutes les sections

Certaines sections du cours sont repliées et leurs liens absents du DOM.

```bash
PY SD/moodle.py expand "course/view.php?id=<ID>"
```

### 2. Énumérer les ressources

```bash
PY SD/moodle.py enumerate "course/view.php?id=<ID>"
```

Retourne un JSON : `{ title, files:[…], pages:[…], links:[…], subcourses:[…] }`.

- `files` : fichiers directs (`mod/resource`, `pluginfile`, `mod/folder`, extensions .pdf/.docx/…).
- `pages` : contenu HTML (`mod/page`, `mod/book`) à capturer en texte.
- `links` : `mod/url` et liens vidéo directs. **C'est là que vivent les vidéos de cours.**
  Un module peut n'avoir aucun `pages` et quarante vidéos, toutes derrière des `mod/url`.
  Le champ `kind` (`video` / `lien`) est une simple heuristique sur le libellé : un lien Zoom
  nommé « regroupement » sort en `video`. **Ne pas s'y fier**, c'est le host de la cible
  résolue (étape 5) qui tranche.

### 3. Capturer la page de cours elle-même (sommaire/planning)

Elle contient le plan, le planning, les dates. L'onglet est déjà dessus :

```bash
PY SD/moodle.py capture "course/view.php?id=<ID>" "data_sources/moodle-page-<module>-<session>.md"
```

### 4. Télécharger chaque fichier

Pour chaque entrée de `files`, avec un nom lisible (kebab-case, préfixé par le thème) :

```bash
PY SD/moodle.py fetch "course/view.php?id=<ID>" "<url>" "data_sources" "<nom-sans-extension>"
```

Le script fait un `fetch(credentials:include)` **dans l'onglet du cours** (même origine =
session authentifiée), rapatrie le contenu en base64 via CDP, et écrit les octets. L'extension
est déduite du nom réel ou du content-type. Aucun passage par le dossier Téléchargements, donc
aucun blocage Chrome des « téléchargements automatiques multiples ».

Un **`mod/folder`** ne se télécharge pas directement. Lister d'abord son contenu :

```bash
PY SD/moodle.py folder "course/view.php?id=<ID>" "<url_du_dossier>"
```

Une URL `pluginfile.php` par ligne, à passer ensuite à `fetch`.

### 5. Capturer les pages HTML de contenu

Pour chaque entrée de `pages` (navigation et capture en une commande) :

```bash
PY SD/moodle.py page "<url>" "course/view.php?id=<ID>" "data_sources/<nom>.md"
```

### 6. Vidéos de cours (SWITCHtube)

Les vidéos ne sont presque jamais posées en clair : elles sont derrière des `mod/url` qui
pointent vers `tube.switch.ch`. Deux temps : résoudre, puis aspirer.

**6a. Résoudre les `mod/url` vers leur cible externe.** Tout se fait par `fetch` dans l'onglet
du cours, sans aucune navigation :

```bash
# URLs en arguments, ou "-" pour les lire sur stdin (une par ligne)
PY SD/moodle.py resolve "course/view.php?id=<ID>" - < urlmods.txt
```

Sortie TSV `<url_mod>\t<url_cible>`. Trier ensuite **par host** : `tube.switch.ch` se
télécharge, un `zoom.us` de regroupement non (le noter dans le manifeste comme non
téléchargeable, ne pas le compter comme un échec).

**6b. Télécharger chaque vidéo :**

```bash
PY SD/moodle.py video "<url_page_video>" "data_sources/<section>" "<nom>" 720p
```

Rendus : `1080p`, `720p` (défaut), `540p`, `audio`. Repli automatique vers le plus proche
disponible. Le script dit `OK`, `SKIP` (déjà complet, vérifié par la taille) ou échoue.

**Comment ça marche.** La page vidéo expose dans son `<video>` des URLs S3 **pré-signées**
(AWS SigV4, `X-Amz-Expires=28800`, soit 8 h). Elles s'authentifient seules : une fois extraites
du DOM, elles se téléchargent en flux direct, sans cookie. C'est pourquoi les vidéos ne passent
pas par le base64 de `fetch` : rapatrier 500 Mo encodés à travers CDP ferait exploser la mémoire.

**Conséquences pratiques, toutes déjà payées une fois :**

| Piège | Ce qui se passe | Conduite |
|---|---|---|
| HEAD sur une URL pré-signée | **403**, alors que l'URL est bonne | La signature couvre le verbe HTTP. Le script sonde par plage (`Range: bytes=0-0`), jamais par HEAD |
| Signature expirée | 403 après 8 h | Résoudre la page **juste avant** de télécharger, pas 43 pages d'avance |
| Aucune `<source>` après le délai | page de connexion ou vidéo restreinte | Le script sort en `AUCUNE_SOURCE` : vérifier que le profil dédié est connecté à SWITCHtube |
| Python sans CA configurées | `CERTIFICATE_VERIFY_FAILED` | Connu sur les installeurs python.org de macOS. Le script préfère `curl`, qui utilise le magasin du système |

**Volume** : compter ~50 Mo par vidéo en 720p, soit plusieurs Go pour un module complet.
Vérifier l'espace disque avant de lancer. Si le but est de faire des fiches ou des quiz plutôt
que de regarder, le rendu `audio` (~2 Mo par vidéo) suffit et se transcrit aussi bien.

### 7. Vérification

```bash
PY SD/moodle.py check "data_sources"
```

Contrôle que les PDF commencent bien par `%PDF` (et ne sont pas des pages d'erreur HTML), que
les vidéos ont une durée lisible, et qu'aucun fichier n'est vide. **`ffprobe` est optionnel :
s'il est absent, le script le dit explicitement et ne fait pas passer les vidéos pour
vérifiées.** Une vidéo tronquée s'ouvre parfois quand même et s'arrête au milieu.

### 8. Manifeste

Écrire `data_sources/_manifeste.md` : date, URL du cours, et pour chaque élément le nom de
fichier local, l'URL source, le type (fichier / page / vidéo), et le statut (OK / échec / non
téléchargeable). Pour les vidéos, conserver l'**URL de la page SWITCHtube** (stable), pas l'URL
S3 signée (périmée en 8 h, donc inutile à archiver). Mettre à jour `memory/journal.md` et
`memory/examen.md` avec ce qui a été trouvé (dates, format d'examen, plan).

## Bonnes pratiques

- Noms de fichiers **explicites en français, kebab-case**, préfixés par le thème
  (`planning-sp26.pdf`, `diapositives-devis-experimentaux.pdf`).
- Ne pas ré-télécharger un fichier déjà présent et identique.
- Rester dans le périmètre du cours demandé ; ne pas suivre des liens vers d'autres cours sans
  accord explicite.
- Les supports et vidéos sont sous droits et restent **locaux** : `data_sources/` est couvert
  par le `.gitignore` du module. Ne jamais les committer ni les republier.

## Inventaire des scripts

| Script | Rôle |
|---|---|
| `cdp.py` | Pilote CDP : lancement du navigateur, attachement à un onglet, évaluation de JS. Client WebSocket en stdlib, aucune dépendance à installer. Socle de tout le reste |
| `moodle.py` | Toutes les sous-commandes métier : `expand`, `enumerate`, `capture`, `page`, `folder`, `fetch`, `resolve`, `video`, `check` |
| `expand_sections.js` | Déplie les sections repliées du cours |
| `enumerate.js` | Énumère `files` / `pages` / `links` / `subcourses` |
| `capture_page.js` | Extrait le texte d'une page |
| `legacy-macos-applescript/` | Ancienne implémentation AppleScript, macOS et Chrome uniquement. Conservée pour référence, **ne plus utiliser** |

## Variables d'environnement

| Variable | Effet |
|---|---|
| `KAIDO_CDP_PORT` | Port de débogage (défaut 9222) |
| `KAIDO_CDP_PROFILE` | Répertoire du profil dédié (défaut `~/.kaido/chrome-profile`) |
| `KAIDO_CDP_BROWSER` | Chemin explicite du binaire, si la détection automatique échoue |
