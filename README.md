# Kaido , The Art of Learning with AI

A curated, open knowledge base on learning science and the responsible use of AI for learning.

**Live site:** https://alogean.github.io/kaido/

## Contents

The source markdown lives in [`docs/`](docs/):

- [`docs/learning_science_concepts.md`](docs/learning_science_concepts.md) , 15 learning-science concepts mapped to a student/lecturer Domain Map (S1:S7 / T1:T7), with relevance notes for AI learning assistants.
- [`docs/cognitive_load_theory.md`](docs/cognitive_load_theory.md) , a deep-dive content note on Cognitive Load Theory and germane cognitive load, with an AI-for-learning angle.
- [`docs/ai_in_education_articles.md`](docs/ai_in_education_articles.md) , curated bibliography of AI-in-education articles and reports with reliability ratings.

## The Kaido skill

A portable skill that turns any capable AI assistant into a sound learning companion grounded in this knowledge base:

- [`skill/kaido/SKILL.md`](skill/kaido/SKILL.md) , the skill file (YAML front matter + Markdown instruction body).
- [`docs/skill.md`](docs/skill.md) , how to add it to Claude, ChatGPT, or Gemini ([live page](https://alogean.github.io/kaido/skill/)).

## Site

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and published to GitHub Pages by the `Deploy site` GitHub Actions workflow on every push to `main`.

To preview locally:

```bash
pip install mkdocs-material
mkdocs serve
```

## Conventions

- Plain Markdown.
- Source reliability key: 🟢 primary research / authoritative, 🟠 serious journalism / institutional, 🔴 blog / vendor / low-quality journal.
- No em dash or en dash anywhere: use ":" or "," instead.
