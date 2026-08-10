# Chaîne YouTube KaiDO , dossier de lancement

État : **chaîne créée** , [https://www.youtube.com/@KaiDO-m2](https://www.youtube.com/@KaiDO-m2). Visuels prêts à téléverser, aucune vidéo en ligne. Les deux vidéos restent auto-hébergées sur [https://alogean.github.io/kaido/videos/](https://alogean.github.io/kaido/videos/).

Ce que je ne peux pas faire à ta place : authentifier la chaîne, téléverser, publier. Tout ce qui suit est prêt à copier-coller.

**Décisions arrêtées :** compte de marque, nom `KaiDO`, avatar monogramme, vidéo courte publique au lancement, vidéo longue **non répertoriée** en attendant l'arbitrage du §7.

**Point ouvert : le handle.** `-m2` est le suffixe que YouTube ajoute automatiquement quand aucun handle n'est choisi à la création. Il se lit comme un identifiant technique et il apparaîtra dans chaque lien partagé. Modifiable dans Studio → Personnalisation → Informations de base, deux fois par 14 jours. À trancher maintenant, tant qu'aucun lien n'est diffusé : `@kaido-learning`, `@kaidolearning`, ou le garder si le `m2` est délibéré.

---

## 1. Décisions à prendre avant de créer quoi que ce soit

| Décision                               | Recommandation                                           | Pourquoi                                                                                                                                                              |
| --------------------------------------- | -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chaîne personnelle ou compte de marque | **Compte de marque** ("Brand Account")             | Détachable de ton compte Gmail perso, transférable, plusieurs gestionnaires. Changer après coup est pénible.                                                      |
| Nom                                     | **KaiDO**                                          | Cohérent avec le dépôt et le site.                                                                                                                                 |
| Handle                                  | `@KaiDO-m2` (attribué d'office)                    | Suffixe automatique faute de choix à la création. Encore modifiable, voir l'en-tête.                                                                              |
| Langue                                  | Français pour les vidéos, métadonnées bilingues      | Les vidéos sont en français. Le site est en anglais. Assume les deux plutôt que de faire semblant.                                                                 |
| Visibilité au lancement                | **Non répertoriée** pour les deux, puis publique | Tu vérifies l'encodage, les chapitres et les sous-titres avant que quiconque tombe dessus.                                                                           |
| Auto-hébergement gardé ?              | Oui, au moins un temps                                   | La page`docs/videos.md` marche déjà. Si tu bascules sur YouTube, remplace les balises `<video>` par des iframes et supprime les `.mp4` du dépôt (voir §6). |

---

## 2. Identité de chaîne

**Nom :** KaiDO

**Slogan / description courte (moins de 100 caractères) :**

> L'art d'apprendre avec l'IA. Sciences de l'apprentissage, sans bullshit.

**Description longue (à coller dans "À propos") :**

```
KaiDO, l'art d'apprendre avec l'IA.

Des explications au tableau blanc sur ce que fait vraiment l'IA générative, et sur ce
qu'elle fait à votre apprentissage. Pas de démos magiques, pas de promesses : des
mécanismes.

Le fil rouge : l'IA peut amorcer la construction de vos connaissances ou la
court-circuiter. Une réponse complète et confiante fait gagner du temps en supprimant
exactement l'effort qui produit l'apprentissage. Chaque vidéo essaie de dire où est la
frontière.

Base de connaissances, sources et concepts : https://alogean.github.io/kaido/
Code et contributions : https://github.com/alogean/kaido
```

**Mots-clés de chaîne :** `IA générative`, `apprentissage`, `sciences cognitives`, `charge cognitive`, `LLM`, `agent IA`, `étudiants`, `enseignement supérieur`, `ChatGPT`, `Claude`

**Visuels : faits.** Les PNG sont dans ce dossier, prêts à téléverser. Les sources SVG sont dans `youtube/src/`, modifiables et réexportables.

| Fichier                      | Usage                    | Format    | Source                |
| ---------------------------- | ------------------------ | --------- | --------------------- |
| `avatar-800.png`             | Photo de profil          | 800x800   | `src/avatar.svg`      |
| `banner-2560x1440.png`       | Bannière de chaîne       | 2560x1440 | `src/banner.svg`      |
| `thumb-1-apprendre.png`      | Miniature vidéo longue   | 1280x720  | `src/thumb-1.svg`     |
| `thumb-2-agent-harnais.png`  | Miniature vidéo courte   | 1280x720  | `src/thumb-2.svg`     |

**Avatar :** monogramme `K` encre `#1A1A1A` et point rouge `#9E2B25` sur crème `#F4EFE6`. Choisi contre le mot-complet `KaiDO` parce que l'avatar s'affiche en cercle à 48 px : cinq glyphes y deviennent une tache grise, une lettre reste une lettre. Les deux variantes écartées restent dans `src/avatar-alt-*.svg`.

**Bannière :** crème, mot-complet en encre avec `ai` en rouge, filet à point rouge, baseline "L'ART D'APPRENDRE AVEC L'IA". Tout le contenu tient dans la zone sûre centrale 1546x423, donc rien n'est amputé sur mobile.

**Miniatures :** typographiques, pas des captures. Les images extraites du tournage montrent la webcam et la barre d'enregistrement, et un tableau blanc photographié est illisible à 210 px de large dans le fil de recommandations. La 1 rejoue le moment mémorable de la vidéo (« Le ciel est ... » et la distribution de probabilités), la 2 pose l'opposition `AGENT ≠ HARNAIS`.

Réexport après modification d'un SVG (`brew install librsvg` si besoin) :

```bash
rsvg-convert -w 800 -h 800 youtube/src/avatar.svg -o youtube/avatar-800.png
rsvg-convert -w 2560 -h 1440 youtube/src/banner.svg -o youtube/banner-2560x1440.png
rsvg-convert -w 1280 -h 720 youtube/src/thumb-1.svg -o youtube/thumb-1-apprendre.png
rsvg-convert -w 1280 -h 720 youtube/src/thumb-2.svg -o youtube/thumb-2-agent-harnais.png
```

---

## 3. Checklist de création (à faire par toi, environ 15 minutes)

1. ~~youtube.com → créer une chaîne → **Utiliser un nom personnalisé** (crée le compte de marque).~~ **Fait.**
2. ~~Nom `KaiDO`~~ **fait.** Handle : `@KaiDO-m2`, à confirmer ou à changer avant de diffuser le moindre lien.
3. YouTube Studio → Personnalisation → avatar, bannière, description, liens (site, GitHub).
4. Paramètres → Chaîne → **Paramètres avancés** : déclarer "Non, ce ne sont pas des vidéos destinées aux enfants" au niveau de la chaîne.
5. Paramètres → Importations par défaut : visibilité **Non répertoriée**, langue **Français**, licence YouTube standard, commentaires **avec approbation** (une chaîne éducative attire les donneurs de leçons).
6. Vérifier le compte par téléphone : sans ça, pas de miniatures personnalisées ni de vidéos de plus de 15 minutes. **La vidéo longue fait 23 minutes, cette étape est bloquante.**
7. Créer la playlist "Comprendre l'IA générative".

---

## 4. Métadonnées , Vidéo 1

**Fichier :** `docs/assets/video/apprendre-avec-lia-generative.mp4` (23 min 16 s, 1080p, 47 Mo)

**Titre :**

> Apprendre avec l'IA générative : comment ça marche vraiment (et où ça vous vole l'apprentissage)

**Description :**

```
De l'IA au LLM, puis du chatbot à l'agent. Au tableau blanc, sans slides.

Ce que fait réellement un modèle de langage quand il vous répond : il prédit le mot
suivant. Une fois que vous avez vu la distribution de probabilités écrite au tableau,
vous ne lisez plus jamais une réponse de la même façon.

Chapitres
00:00 Introduction
00:35 Octobre 2022 : ChatGPT arrive au milieu de mon bachelor
01:20 L'IA comme béquille : ce que j'ai perdu à faire résumer les articles
02:48 IA, machine learning, data science : qui contient quoi
04:41 Le moment historique : l'arrivée de l'IA générative
06:09 L'interface en langage naturel, le vrai basculement
08:03 Le LLM et la prédiction du mot suivant
08:41 "Le ciel est..." : la distribution de probabilités au tableau
10:09 Ce qui entre détermine ce qui sort
11:06 Le paysage : OpenAI et ChatGPT
13:01 Anthropic et la famille Claude : Opus, Sonnet, Haiku
14:53 Google, xAI, et les modèles ouverts
18:29 Chatbot ou agent ?
21:03 L'agent : un LLM au centre, un harnais autour

Base de connaissances, concepts et sources : https://alogean.github.io/kaido/
Dépôt : https://github.com/alogean/kaido

Les noms de modèles et numéros de version cités datent du tournage. Cette partie vieillit
en semaines. Les mécanismes, non.
```

**Tags :** `IA générative`, `LLM`, `ChatGPT`, `Claude`, `agent IA`, `prédiction du mot suivant`, `apprendre avec l'IA`, `intelligence artificielle expliquée`, `étudiants`, `sciences de l'apprentissage`

**Playlist :** Comprendre l'IA générative (position 1)
**Miniature :** `docs/assets/video/apprendre-avec-lia-generative.jpg` à retravailler, ou capture du tableau "Chatbot ? Agent" avec titre en encre sur crème.

---

## 5. Métadonnées , Vidéo 2

**Fichier :** `docs/assets/video/agent-ia-et-harnais.mp4` (4 min 42 s, 1080p, 8 Mo)

**Titre :**

> Agent IA et harnais : la distinction que presque personne ne fait

**Description :**

```
L'agent est un comportement. Le harnais est l'infrastructure. Confondre les deux, c'est
attribuer au modèle des erreurs qui viennent de l'outillage.

La boucle agentique en cinq minutes : un objectif entre, le modèle raisonne, appelle des
outils (recherche web, un shell dans un conteneur, produire un fichier), lit le résultat,
et recommence jusqu'à ce que l'objectif soit atteint.

Chapitres
00:00 Introduction
00:13 L'agent est un comportement, le harnais une infrastructure
00:42 La boucle : objectif, raisonnement, outils
02:02 Claude Code, un harnais à forte agentivité
02:33 Ce qu'on appelle un comportement agentique
03:20 Les autres harnais : Codex, Gemini CLI, Antigravity, open source

Base de connaissances, concepts et sources : https://alogean.github.io/kaido/
Dépôt : https://github.com/alogean/kaido
```

**Tags :** `agent IA`, `harnais`, `boucle agentique`, `Claude Code`, `Codex`, `Gemini CLI`, `MCP`, `outils IA`, `LLM`

**Playlist :** Comprendre l'IA générative (position 2)

---

## 6. Ce qui manque encore

| Manque                             | Effet                                                                                                                                                                                                                             | Coût                                                                |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| ~~Sous-titres~~                   | **Fait.** `.srt` français pour les deux vidéos, dans `docs/assets/video/`, à charger tels quels dans YouTube Studio. Transcription locale avec whisper-cpp (large-v3-turbo), corrections limitées aux noms propres. | ,                                                                    |
| ~~Chapitres vérifiés~~          | **Fait.** Les horodatages ci-dessus sont calés sur la transcription, plus sur un échantillonnage d'images.                                                                                                                | ,                                                                    |
| ~~Miniatures~~                     | **Fait.** Deux miniatures typographiques 1280x720 dans ce dossier, gabarit crème/encre/rouge réutilisable pour les prochaines vidéos.                                                                                       | ,                                                                    |
| ~~Bannière et avatar PNG~~        | **Fait.** Exportés depuis `src/`, dans ce dossier.                                                                                                                                                                                | ,                                                                    |
| **Écran de fin, filigrane** | Renvoi vers le site et l'autre vidéo.                                                                                                                                                                                            | À faire après la mise en ligne.                                    |

## 7. À arbitrer avant de rendre la vidéo longue publique

La transcription fait apparaître quatre choses qui ne se voient pas au tableau. Aucune n'est
grave, toutes méritent une décision consciente plutôt qu'une découverte en commentaire.

| Passage                                                                                                                      | Horodatage | Le problème                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Ce qui serait cool, c'est de faire un monthly call, une date bien précise, chacun vient et dit j'ai essayé ça"           | ~07:20     | La vidéo s'adresse à un groupe identifié, pas à un public. Sur une chaîne ouverte, l'invitation devient une promesse à des inconnus. Soit tu la coupes, soit tu l'assumes et tu ouvres vraiment le call. |
| "Les forces du mal, donc c'est xAI, c'est Elon Musk"                                                                         | ~15:45     | Une pique. Drôle en interne, moins quand elle est indexée par la recherche YouTube à côté du nom de la boîte.                                                                                            |
| L'exemple des garde-fous illustré par "c'est quoi le national-socialisme, quelle est la différence avec l'extrême droite" | ~16:00     | L'exemple est pertinent, la section de commentaires ne le sera pas. Un exemple équivalent et moins inflammable ferait le même travail pédagogique.                                                          |
| "Je fais ça un peu à l'arrache, j'improvise, ce n'est pas vraiment préparé"                                              | 00:05      | Tu t'excuses avant d'avoir commencé. Le contenu est bon, l'excuse le déprécie et donne au spectateur une raison de partir dans les dix premières secondes. Candidate au montage.                           |

Décision recommandée : mettre la vidéo courte en public (rien à arbitrer dedans) et garder la
longue en **non répertoriée** le temps de trancher ces quatre points. Le lien non répertorié
reste partageable avec ton groupe, ce qui couvre l'usage immédiat.

## 8. Bascule du site vers YouTube (si tu le décides plus tard)

Le jour où les vidéos sont sur YouTube, dans `docs/videos.md` : remplacer chaque bloc
`<video>` par une iframe `youtube-nocookie.com`, puis
`git rm docs/assets/video/*.mp4`. Attention : `git rm` retire les fichiers du site mais
**pas de l'historique git**. Le dépôt restera lourd de 55 Mo sauf réécriture d'historique.
C'est le prix de l'auto-hébergement d'aujourd'hui, et c'est la raison pour laquelle il ne
faut pas ajouter une troisième vidéo par ce chemin.
