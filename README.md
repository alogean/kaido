# KaiDO , l'art d'apprendre avec l'IA

Le compagnon écrit de la chaîne YouTube [@KaiDO-learning](https://www.youtube.com/@KaiDO-learning). Les vidéos montrent, ce dépôt documente.

**Site publié :** <https://alogean.github.io/kaido/>

Le fil rouge : l'IA peut amorcer la construction des connaissances ou la court-circuiter. Une réponse complète et confiante fait gagner du temps en supprimant exactement l'effort qui produit l'apprentissage. Tout ici essaie de dire où passe la frontière.

## Les trois sections

| Section | Question | Source |
|---|---|---|
| **1. Installation et outils** | Qu'est-ce que je mets en place ? | [`docs/outils/`](docs/outils/) |
| **2. Bachelor en psychologie** | Qu'est-ce que je verse dedans ? | [`docs/psycho/`](docs/psycho/) et [`modules/`](modules/) |
| **3. Méthodologie d'apprentissage** | Pourquoi ça marche, ou pas ? | [`docs/methode/`](docs/methode/) |

Les cinq vidéos de la chaîne sont intégrées dans [`docs/outils/parcours-video.md`](docs/outils/parcours-video.md).

## Les modules

`modules/` est découpé par niveau d'études :

| Niveau | Répertoire | Modules |
|---|---|---|
| Bachelor | `modules/Bachelor/` | M00 à M18 |
| Master | `modules/Master/` | MES2, PSY2, SAE6, TOF6 |

Un sous-répertoire par module, sur le gabarit de `Bachelor/M17` : un `CLAUDE.md` qui configure l'agent, un `README.md`, un `.gitignore`.

> **Les supports de cours ne montent jamais ici.** Polycopiés, diapositives, articles sous licence et énoncés d'examen appartiennent à leurs auteurs, et ce dépôt est public. Chaque module ignore `data-source/`, `generated-artifacts/` et `memory/`. Ce qui se partage entre étudiants, c'est le `CLAUDE.md`, pas le PDF.

## Les skills

Deux skills installables, distribuées depuis [`skill/`](skill/).

**KaiDO** , transforme n'importe quel assistant IA capable en compagnon d'apprentissage correct :

- [`skill/kaido/SKILL.md`](skill/kaido/SKILL.md) , le fichier (en-tête YAML + corps markdown). **En anglais**, pour rester installable partout.
- [`docs/outils/skill-kaido.md`](docs/outils/skill-kaido.md) , comment l'installer dans Claude, ChatGPT ou Gemini ([page publiée](https://alogean.github.io/kaido/outils/skill-kaido/)).

**Moodle** , télécharge les supports et les vidéos d'un cours UniDistance dans `data_sources/` :

- [`skill/moodle-fernuni-scrape/`](skill/moodle-fernuni-scrape/) , un `SKILL.md` et cinq scripts. Pilote Chrome ou Edge par le Chrome DevTools Protocol : macOS, Windows et Linux. Aucune dépendance à installer, la bibliothèque standard de Python suffit.
- [`docs/outils/skill-moodle.md`](docs/outils/skill-moodle.md) , l'installation et les pièges ([page publiée](https://alogean.github.io/kaido/outils/skill-moodle/)).

## Le site

Construit avec [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), publié sur GitHub Pages par le workflow `Deploy site` à chaque push sur `main`.

Aperçu local :

```bash
pip install mkdocs-material
mkdocs serve
```

Toute nouvelle page doit être ajoutée à la `nav` de `mkdocs.yml`, sinon elle existe sans exister.

## Conventions

- Markdown simple. Site en français ; la skill portable reste en anglais.
- Clé de fiabilité des sources : 🟢 recherche primaire ou autoritative, 🟠 journalisme sérieux ou institutionnel, 🔴 blog, éditeur de logiciel ou revue faible.
- Aucune référence inventée, jamais.
- **Aucun tiret cadratin ni demi-cadratin nulle part** : utiliser ":" ou ",".

## Archive

[`archive/`](archive/) contient les pages anglaises d'avant la refonte du 15 août 2026. Ce répertoire est hors du site : MkDocs ne construit que `docs/`.
