---
title: La skill KaiDO
---

# La skill KaiDO

KaiDO est aussi distribué comme **skill portable** : un seul fichier d'instructions qui transforme n'importe quel assistant IA capable en compagnon d'apprentissage correct. Elle privilégie la découverte guidée plutôt que la réponse offerte, situe chaque demande sur la carte des domaines (S1:S7 / T1:T7), et raisonne par mécanisme (charge cognitive, récupération, ICAP, métacognition) plutôt que par opinion.

**Le fichier :** [`skill/kaido/SKILL.md`](https://github.com/alogean/kaido/blob/main/skill/kaido/SKILL.md) ([version brute à copier](https://raw.githubusercontent.com/alogean/kaido/main/skill/kaido/SKILL.md))

!!! note "La skill reste en anglais"
    Le reste du site est en français, la skill non : elle est faite pour être installée dans n'importe quel assistant, et l'anglais y est le format le plus portable. Elle répond en revanche dans la langue où vous lui parlez.

Le fichier a deux parties : un petit en-tête YAML (`name`, `description`) utilisé par les plateformes qui gèrent les skills nativement, et un corps en markdown qui fonctionne comme prompt système partout ailleurs. Selon la plateforme, vous déposez le fichier entier, ou vous collez le **corps** (tout ce qui suit le second `---`).

## Différence avec un agent de module

| | Skill KaiDO | Agent de module |
|---|---|---|
| Portée | Toute question d'apprentissage | Un module précis |
| Sources | Aucune : elle apporte une méthode | Vos supports de cours dans `data-source` |
| Où elle vit | Dans votre assistant, globalement | Dans un répertoire, avec son `CLAUDE.md` |
| À quoi elle sert | Empêcher l'assistant de faire le travail à votre place | Réviser un cours donné |

Les deux se combinent : la skill installée globalement, l'agent de module par-dessus. Voir [Créer son agent](creer-son-agent.md).

## L'installer dans Claude

Claude gère les skills nativement : le fichier s'utilise tel quel.

=== "Claude Code (terminal ou VS Code)"

    Déposez le fichier dans un répertoire de skills, Claude le charge automatiquement :

    - Personnel, tous projets : `~/.claude/skills/kaido/SKILL.md`
    - Un seul projet : `<projet>/.claude/skills/kaido/SKILL.md`

    ```bash
    mkdir -p ~/.claude/skills/kaido
    curl -sL https://raw.githubusercontent.com/alogean/kaido/main/skill/kaido/SKILL.md \
      -o ~/.claude/skills/kaido/SKILL.md
    ```

    Ouvrez une nouvelle session, puis demandez d'utiliser la skill kaido, ou posez simplement une question d'apprentissage : elle se déclenche depuis sa `description`.

=== "Applications Claude (claude.ai, Desktop)"

    1. Ouvrir **Paramètres → Capacités → Skills**.
    2. Créer une skill et coller le contenu de `SKILL.md` (ou téléverser un dossier ou un zip nommé `kaido`).
    3. Enregistrer. La skill s'active quand votre demande correspond à sa description, ou sur appel par son nom.

## L'installer dans ChatGPT

ChatGPT n'a pas de format de skill natif : utilisez le **corps** du fichier comme instructions.

=== "GPT personnalisé (réutilisable)"

    1. **Explorer les GPT → Créer**, puis l'onglet **Configurer**.
    2. Coller le corps de `SKILL.md` (sans l'en-tête YAML) dans **Instructions**.
    3. Le nommer "KaiDO", et reprendre la ligne `description` comme description si vous voulez.
    4. Enregistrer, puis discuter avec ce GPT.

=== "Projet"

    1. Créer un **Projet**.
    2. Ouvrir ses **Instructions** et y coller le corps de `SKILL.md`.
    3. Toutes les conversations du projet suivent l'approche KaiDO.

=== "Conversation unique"

    Coller le corps de `SKILL.md` en premier message, précédé de "Suis ces instructions pour toute la conversation :". Suffisant pour une séance ponctuelle.

## L'installer dans Gemini

=== "Gem (réutilisable)"

    1. Dans l'application Gemini, ouvrir **Gems → Nouveau Gem**.
    2. Coller le corps de `SKILL.md` dans le champ d'instructions.
    3. Le nommer "KaiDO", enregistrer, le sélectionner quand vous travaillez.

=== "Google AI Studio"

    1. Créer un nouveau prompt.
    2. Coller le corps de `SKILL.md` dans **System instructions**.
    3. Discuter dans le panneau d'exécution, ou récupérer le code d'appel API.

## À quoi reconnaître qu'elle est active

- L'assistant pose une question de diagnostic avant d'enseigner, au lieu de déverser une réponse complète.
- Il donne le plus petit indice qui débloque, puis vous demande de retrouver ou de prédire la suite.
- Il termine en vous faisant restituer ou en planifiant une révision espacée.
- Quand il affirme un fait, il indique la fiabilité de la source (🟢 🟠 🔴) et admet son incertitude plutôt que d'inventer une référence.

Si l'assistant se contente de livrer des réponses sans récupération ni réflexion, il ne suit pas la skill : vérifiez que les instructions ont été collées en entier.
