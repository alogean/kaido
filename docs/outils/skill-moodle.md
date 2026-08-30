---
title: La skill Moodle
---

# La skill Moodle

Verser ses supports de cours dans `data-source/` est l'étape la plus fastidieuse de la [méthode par module](../psycho/methode-module.md) : trente clics droits, trente « Enregistrer sous », trente fichiers nommés `document(3).pdf`. La skill Moodle fait ce travail à votre place, une fois, proprement nommé.

**Le dépôt :** [`skill/moodle-fernuni-scrape/`](https://github.com/alogean/kaido/tree/main/skill/moodle-fernuni-scrape)

!!! warning "Elle ne vous dispense de rien"
    Aspirer un module en quatre minutes ne le fait pas entrer dans votre tête. Cette skill règle un problème de logistique, pas un problème d'apprentissage. Lisez la section [Le raccourci qui coûte cher](#le-raccourci-qui-coute-cher) avant de la lancer : elle est là pour une raison.

## Ce qu'elle fait

| Elle récupère | Elle ne récupère pas |
|---|---|
| PDF, Word, PowerPoint, Excel | Ce à quoi votre compte n'a pas accès |
| Dossiers de fichiers (`mod/folder`) | Les liens Zoom de regroupement, qui ne sont pas des documents |
| Pages de contenu (`mod/page`, `mod/book`), en texte | Les forums, devoirs, quiz |
| La page de cours elle-même : plan, planning, dates | Les cours où vous n'êtes pas inscrit |
| Les vidéos de cours sur SWITCHtube, y compris en piste audio seule | |

Tout atterrit dans `data_sources/` du répertoire courant, avec un `_manifeste.md` qui dit d'où vient chaque fichier.

## Prérequis

| Élément | Vérifier | Si absent |
|---|---|---|
| Claude Code | [page d'installation](installer-claude-code.md) | |
| Python 3.8 ou plus | `python3 --version` sur macOS, `python --version` sur Windows | macOS : déjà installé. Windows : `winget install Python.Python.3.12` |
| Google Chrome ou Microsoft Edge | | installer l'un des deux |

Aucune bibliothèque à installer : la skill n'utilise que la bibliothèque standard de Python.

## L'installer

=== "macOS et Linux"

    ```bash
    SKILL=~/.claude/skills/moodle-fernuni-scrape
    BASE=https://raw.githubusercontent.com/alogean/kaido/main/skill/moodle-fernuni-scrape

    mkdir -p "$SKILL/scripts"
    curl -sL "$BASE/SKILL.md" -o "$SKILL/SKILL.md"
    for f in cdp.py moodle.py capture_page.js enumerate.js expand_sections.js; do
      curl -sL "$BASE/scripts/$f" -o "$SKILL/scripts/$f"
    done
    ```

=== "Windows (PowerShell)"

    ```powershell
    $skill = "$env:USERPROFILE\.claude\skills\moodle-fernuni-scrape"
    $base  = "https://raw.githubusercontent.com/alogean/kaido/main/skill/moodle-fernuni-scrape"

    New-Item -ItemType Directory -Force -Path "$skill\scripts" | Out-Null
    Invoke-WebRequest "$base/SKILL.md" -OutFile "$skill\SKILL.md"
    foreach ($f in "cdp.py","moodle.py","capture_page.js","enumerate.js","expand_sections.js") {
      Invoke-WebRequest "$base/scripts/$f" -OutFile "$skill\scripts\$f"
    }
    ```

Ouvrez ensuite une **nouvelle** session Claude Code : les skills sont lues au démarrage.

## La première utilisation

La skill pilote un navigateur, mais **pas le vôtre**. Elle en lance un second, avec un profil séparé rangé dans `~/.kaido/chrome-profile`.

Ce profil démarre vierge. Une seule fois, au premier usage :

1. Demandez à Claude de lancer le navigateur piloté.
2. Dans la fenêtre qui s'ouvre, connectez-vous à Moodle avec votre SWITCH edu-ID.
3. Si vous voulez les vidéos, ouvrez aussi `tube.switch.ch` et connectez-vous.
4. Ouvrez l'onglet du cours à aspirer.

Ensuite, dites simplement :

> Aspire le module M17 depuis Moodle, l'onglet est ouvert.

La session reste valable d'une fois sur l'autre. Vous ne referez ces quatre étapes que si vous vous déconnectez.

??? question "Pourquoi un second navigateur, et pas le mien ?"
    Depuis Chrome 136, le mode pilotable est refusé sur le profil par défaut. C'est une bonne décision de Google : un programme capable de piloter votre profil principal peut lire vos cookies bancaires aussi facilement que ceux de Moodle. Le profil dédié isole l'aspiration du reste de votre vie numérique. Le coût est une connexion à refaire, une fois.

## Les vidéos

Un module de bachelor peut contenir quarante enregistrements de séance. En 720p, comptez environ 50 Mo pièce, donc plusieurs gigaoctets. Vérifiez votre espace disque.

**Si votre but est de réviser plutôt que de regarder, demandez le rendu `audio`** : environ 2 Mo par vidéo, et une transcription tout aussi bonne. Un agent lit une transcription, pas une image.

## Le raccourci qui coûte cher

Cette skill est un aspirateur. Un aspirateur ne fait pas le ménage à votre place, il déplace la poussière. Trois manières de vous tromper avec :

**Confondre « j'ai les fichiers » et « j'ai le cours ».** Le sentiment de maîtrise que procure un répertoire bien rempli est réel, et parfaitement trompeur. C'est le même mécanisme que le surlignage : une trace visible d'un travail qui n'a pas eu lieu. Le module n'a pas bougé d'un millimètre dans votre mémoire.

**Tout aspirer sans trier.** La [méthode par module](../psycho/methode-module.md) dit quelles ressources verser et lesquelles jamais, et ce n'est pas décoratif. Un manuel de 600 pages dans `data-source` noie le polycopié qui, lui, fait foi à l'examen. La facilité de l'aspiration rend la tentation d'aspirer tout beaucoup plus forte : résistez-y explicitement.

**Enchaîner sur « fais-moi un résumé ».** C'est le geste décrit dans la [vidéo 1](parcours-video.md) comme celui qui n'a rien laissé après quatre ans. Le travail de compression est exactement celui qui produit la mémorisation. Le déléguer à la machine juste après avoir délégué le téléchargement, c'est avoir automatisé l'intégralité de son bachelor sauf la partie qui compte.

L'usage correct : aspirer, trier, puis demander à l'agent de **vous interroger** sur ces documents. Voir [Apprendre ou utiliser ?](../methode/apprendre-ou-utiliser.md).

## Droits d'auteur

Les polycopiés, diapositives, articles et enregistrements appartiennent à leurs auteurs et à l'institution. Ils sont mis à votre disposition pour vos études, pas pour être redistribués.

!!! danger "Ce qui n'est jamais poussé"
    Ce que la skill télécharge reste sur votre disque. Si vous versionnez votre travail, ignorez `modules/` en entier plutôt que d'y trier fichier par fichier. Ne le commitez jamais, ne le republiez jamais, ne le partagez pas hors du cadre du cours. Ce qui se partage utilement entre étudiants, c'est le `CLAUDE.md` qui a bien marché, pas le PDF.

## Quand ça coince

| Symptôme | Cause probable | Conduite |
|---|---|---|
| `NAVIGATEUR_HORS_LIGNE` | le navigateur piloté n'est pas lancé | demandez à Claude de le relancer |
| `AUCUN_ONGLET` | l'onglet du cours n'est pas ouvert dans le profil dédié | ouvrez-le dans la bonne fenêtre, pas dans votre Chrome habituel |
| `AUCUNE_SOURCE` sur une vidéo | pas connecté à SWITCHtube dans le profil dédié | ouvrez `tube.switch.ch` et connectez-vous |
| PDF minuscules et illisibles | Moodle a renvoyé une page d'erreur | la session a expiré : reconnectez-vous, relancez |
| `NAVIGATEUR_INTROUVABLE` | Chrome installé ailleurs que par défaut | la skill accepte la variable `KAIDO_CDP_BROWSER` |
| `python3` ouvre le Microsoft Store | Windows, Python absent | `winget install Python.Python.3.12` |

La skill vérifie son propre travail : elle contrôle que les PDF sont bien des PDF et non des pages d'erreur déguisées, et que les vidéos ne sont pas tronquées. Demandez-lui le rapport de vérification après l'aspiration.

## Portée

Elle est écrite pour Moodle de FernUni/UniDistance et pour SWITCHtube. Sur une autre instance Moodle, l'énumération a de bonnes chances de fonctionner, la résolution des liens vidéo beaucoup moins. Elle fonctionne sur macOS, Windows et Linux, avec Chrome ou Edge.
