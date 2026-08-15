---
title: Les cinq vidéos
---

# Les cinq vidéos

La série complète de la chaîne [@KaiDO-learning](https://www.youtube.com/@KaiDO-learning), dans l'ordre. Filmées en une prise, au tableau blanc, sans slides. **En français.**

Les deux premières expliquent ce que fait la machine. Les trois suivantes la mettent en place chez vous. L'ordre compte : installer un agent sans comprendre ce qu'est un contexte, c'est apprendre les gestes sans le métier.

---

## 1. Apprendre avec l'IA générative

<div class="kaido-embed">
<iframe src="https://www.youtube-nocookie.com/embed/Y5Y4OP-vAxA" title="Apprendre avec l'IA générative" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*23 min.* [Voir sur YouTube](https://www.youtube.com/watch?v=Y5Y4OP-vAxA)

Une visite guidée depuis le début : de l'IA au LLM, puis du chatbot à l'agent.

- **L'effet béquille, raconté de l'intérieur.** Quatre ans de bachelor avec ChatGPT disponible, et le verdict honnête sur une habitude : faire résumer systématiquement les articles scientifiques au lieu de les lire. La conclusion n'est pas "l'IA c'est mal", c'est "les articles qui comptent doivent être lus, même quand ça fait mal, sinon il ne reste rien". C'est de la charge utile dépensée ou économisée, décrite de l'intérieur. Voir [Charge cognitive](../methode/charge-cognitive.md).
- **Où se situe l'IA générative** dans l'IA, le machine learning et la data science, et pourquoi octobre 2022 est une rupture : pas le modèle, mais l'interface en langage naturel, qui rend la technologie utilisable par quiconque sait aligner des mots.
- **Ce que fait un LLM, mécaniquement :** la prédiction du mot suivant, déroulée sur "je suis à Londres et le ciel est ...", avec la distribution de probabilités écrite au tableau. C'est le passage qui dissout l'intuition "il connaît la réponse", et qui installe la vraie leçon : **ce qui entre détermine ce qui sort.**
- **Qui construit quoi :** OpenAI et ChatGPT, Anthropic et la famille Claude, Google avec Gemini et NotebookLM, xAI et Grok, plus les modèles ouverts. La distinction entre open source et open weight y est faite correctement, ce qui est plus rare qu'il ne devrait.
- **Chatbot ou agent,** et la première esquisse du harnais.

!!! warning "Où l'IA volerait l'apprentissage ici"
    Faire résumer cette vidéo par un chatbot vous donne un vocabulaire que vous pouvez réciter et pas utiliser. Le mécanisme ne tient que si vous essayez de prédire la distribution vous-même, avant que le tableau ne la révèle.

---

## 2. Claude Code = Claude (LLM) + harnais

<div class="kaido-embed">
<iframe src="https://www.youtube-nocookie.com/embed/V5XM5p7d8ss" title="Claude Code = Claude (LLM) + harnais (couche agentique)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*5 min.* [Voir sur YouTube](https://www.youtube.com/watch?v=V5XM5p7d8ss)

Une seule distinction, faite proprement : **l'agent est un comportement, le harnais est l'infrastructure.**

- La boucle agentique : un objectif entre, le modèle raisonne, dresse une liste de tâches, appelle des outils (recherche web, un shell, produire un fichier), lit le résultat, révise la liste, et recommence jusqu'à l'objectif atteint.
- Le harnais est la couche logicielle qui enveloppe le modèle et rend cela possible. Même modèle, autre harnais, autre comportement.
- Concrètement : Codex chez OpenAI, Claude Code chez Anthropic, Gemini CLI et Antigravity chez Google, plus un ensemble croissant de harnais open source.

!!! note "Pourquoi ça compte pour apprendre"
    "L'IA s'est trompée" est presque toujours une question de harnais, pas de modèle. Un étudiant incapable de distinguer les deux ne peut pas diagnostiquer son propre usage, et va généraliser une mauvaise expérience en règle sur l'IA.

---

## 3. Le couple gagnant : Claude Code + VS Code

<div class="kaido-embed">
<iframe src="https://www.youtube-nocookie.com/embed/CxYWxovkL3w" title="Le couple gagnant : Claude Code + VS Code" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*23 min.* [Voir sur YouTube](https://www.youtube.com/watch?v=CxYWxovkL3w)

Ce qu'on installe et pourquoi, avant de l'installer.

- **La ligne de commande,** et l'argument qui la justifie : un contrôle total et sans filtre sur ce que fait le modèle. Dès qu'une interface s'interpose, vous savez moins.
- **VS Code comme carrosserie,** Claude Code comme moteur. L'analogie tient parce que toute la configuration se fait dans des fichiers, et qu'un éditeur de fichiers est exactement ce qu'il faut.
- **Le markdown,** format à la fois lisible par un humain et formel pour la machine, et pourquoi c'est dans ce format que vous allez programmer le cerveau de votre agent.
- **Un agent, concrètement : un répertoire plus un fichier `CLAUDE.md`.** Trois lignes ou dix-sept pages, au choix. C'est la démystification la plus utile de la série.
- Le coût : environ 20 francs par mois, présentés comme un investissement plutôt qu'une dépense.

Voir [Ligne de commande et markdown](ligne-de-commande-et-markdown.md) pour la version écrite, avec la table des signes markdown.

---

## 4. Installer VS Code et Claude Code sur Windows

<div class="kaido-embed">
<iframe src="https://www.youtube-nocookie.com/embed/3-fxlz9H5YM" title="Installer VS Code et Claude Code sur Windows" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*6 min.* [Voir sur YouTube](https://www.youtube.com/watch?v=3-fxlz9H5YM)

L'installation filmée sur un PC Windows et un compte neuf, pour reproduire ce que vous avez à la maison. Téléchargement de VS Code, extension Claude Code, connexion au compte, premier "salut, qui es-tu ?".

!!! danger "Le piège du choix de connexion"
    Au moment de se connecter, choisissez **Claude AI subscription**, pas l'API. L'API se facture à l'usage et coûte nettement plus cher pour cet usage.

Version écrite, Windows et macOS : [Installer Claude Code et VS Code](installer-claude-code.md).

---

## 5. Créer et configurer son agent dans VS Code

<div class="kaido-embed">
<iframe src="https://www.youtube-nocookie.com/embed/E7mzdtUUB28" title="Créer et configurer son agent Claude Code dans VS Code" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

*16 min.* [Voir sur YouTube](https://www.youtube.com/watch?v=E7mzdtUUB28)

La construction, en direct, d'un agent de révision pour un module de psychopathologie.

- Créer le répertoire du module, ses sous-répertoires `data-source` et `generated-artifacts`, et un `CLAUDE.md` vide.
- **Dicter la configuration en langage naturel** et laisser l'agent l'écrire lui-même dans `CLAUDE.md` : identité, langue, personnalité, d'où viennent les sources, où vont les productions.
- Ajouter un répertoire `memory` et laisser l'agent proposer sa propre découpe.
- **L'instruction décisive :** contraindre l'agent à ne répondre que depuis `data-source`, sans culture générale ni recherche web. C'est là que l'outil devient un agent de révision plutôt qu'un chatbot de plus.
- Relire ce qu'il a écrit, et le déplacer quand il l'a rangé au mauvais endroit. La configuration reste la vôtre.

Version écrite et gabarit réutilisable : [Créer son agent](creer-son-agent.md) et [Module M17](../psycho/m17.md).

---

## Ce que la série ne dit pas encore

GitHub, le versionnage des modules et le partage entre étudiants sont annoncés dans la vidéo 3 et pas encore filmés. En attendant, la convention de répertoire est documentée dans [Bachelor en psychologie](../psycho/index.md).

Les noms de modèles et les prix visibles au tableau datent du tournage. Cette partie vieillit en semaines. Les mécanismes, non.
