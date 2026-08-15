---
title: Comprendre avant d'installer
---

# Comprendre avant d'installer

Version écrite des [vidéos 1 et 2](parcours-video.md). Quatre idées. Si vous les tenez, la suite n'est que de la manipulation de fichiers.

## 1. Un LLM prédit le mot suivant

Écrivez `Je suis à Londres et le ciel est ...` et donnez-le au modèle. Il ne consulte pas une base de connaissances météo. Il calcule, sur tous les mots possibles, une distribution de probabilités :

| Mot candidat | Probabilité |
|---|---|
| gris | très élevée |
| bleu | faible |
| couvert | faible |
| vert | négligeable |

Il en tire un, l'ajoute au texte, et recommence. Rien d'autre.

Changez une entrée : `Je suis en Valais et le ciel est ...` et la distribution bascule vers `bleu`. Le mot "Valais" a suffi.

C'est le passage qui dissout l'intuition la plus coûteuse en matière d'apprentissage : **le modèle ne "sait" pas, il continue.** Une réponse fluide, bien construite et fausse a exactement la même signature qu'une réponse fluide, bien construite et juste. Vous ne pouvez pas les distinguer au ton.

## 2. Ce qui entre détermine ce qui sort

Corollaire immédiat, et il porte tout le reste du site.

Si le contexte contient vos supports de cours, vous obtenez des réponses sur votre cours. S'il ne contient rien, vous obtenez la moyenne d'internet, formulée avec le même aplomb. Le travail utile ne consiste donc presque jamais à mieux formuler la question. Il consiste à **maîtriser ce qui entre**.

C'est la raison d'être de toute la section installation. Un chatbot vous laisse deviner ce qu'il a en tête. Un agent vous laisse le lire dans un fichier.

## 3. Chatbot ou agent

| | Chatbot | Agent |
|---|---|---|
| Ce qu'il fait | Répond | Agit, en boucle, jusqu'à un objectif |
| Mémoire | Le fil de conversation | Des fichiers sur votre disque, que vous lisez |
| Outils | Cachés sous le capot | Explicites : lire, écrire, chercher, exécuter |
| Contexte | Choisi pour vous | Choisi par vous |
| Configuration | Une zone de texte dans une interface | Des fichiers markdown versionnables |

Les projets ChatGPT ou les dossiers Claude sont un intermédiaire honnête : vous versez des PDF et vous donnez des consignes. Mais la configuration reste dans une interface, la découpe du contexte reste opaque, et vous ne pouvez ni la relire ligne à ligne ni la partager à un camarade.

## 4. L'agent est un comportement, le harnais est l'infrastructure

**Agent = LLM + harnais.**

Le LLM est au centre : il raisonne, il décide. Le harnais est tout autour : la boucle, l'accès aux fichiers, les outils, la mémoire, les garde-fous.

La boucle agentique, en une phrase : un objectif entre, le modèle raisonne, dresse une liste de tâches, appelle des outils, lit les résultats, révise la liste, et recommence jusqu'à ce que l'objectif soit atteint.

| Éditeur | Harnais |
|---|---|
| Anthropic | Claude Code |
| OpenAI | Codex |
| Google | Gemini CLI, Antigravity |
| Communauté | de nombreux harnais open source |

!!! tip "Le diagnostic qui change tout"
    Quand "l'IA se trompe", demandez-vous d'abord si c'est le modèle ou le harnais. Une mauvaise réponse sur votre cours parce que le fichier n'a jamais été lu est un problème de harnais et de contexte, pas d'intelligence. Confondre les deux, c'est généraliser une mauvaise expérience en règle définitive sur l'IA, et se priver de l'outil pour de mauvaises raisons.

## Vérifiez que ça tient

Sans relire la page, répondez à voix haute. Si une réponse ne vient pas, c'est le moment de remonter, pas après l'installation.

1. Pourquoi le modèle répond-il "gris" à Londres et "bleu" en Valais ?
2. Pourquoi une réponse fausse a-t-elle l'air aussi assurée qu'une réponse juste ?
3. Quelle est la différence entre un agent et un harnais ?
4. Citez deux choses qu'un agent peut faire et qu'un chatbot ne peut pas.
5. Vous obtenez une réponse à côté de la plaque sur votre cours. Quelle est la première hypothèse à tester ?

Cette liste n'est pas décorative : se tester est plus efficace que relire, et l'écart entre "je crois savoir" et "je sais" ne se voit qu'ici. Voir [Concepts](../methode/concepts.md).

Ensuite : [Installer Claude Code et VS Code](installer-claude-code.md).
