---
title: Installation et outils
---

# 1. Installation et outils

**La question de cette section : qu'est-ce que je mets en place ?**

L'objectif n'est pas d'avoir un chatbot de plus. C'est d'avoir un **agent** : un répertoire sur votre disque, une configuration que vous lisez et modifiez, et un contrôle total sur ce qui entre dans le contexte du modèle. Tout le reste de KaiDO suppose que cette infrastructure tourne.

## Le parcours

| Étape | Page | Ce que vous en sortez |
|---|---|---|
| 0 | [Les cinq vidéos](parcours-video.md) | La série complète de la chaîne, dans l'ordre, avec ce qu'il faut retenir de chacune |
| 1 | [Comprendre avant d'installer](comprendre-avant-installer.md) | Ce qu'est un LLM, ce qu'est un agent, ce qu'est un harnais. Sans ça, l'installation est un rituel |
| 2 | [Installer Claude Code et VS Code](installer-claude-code.md) | L'outillage qui tourne, sur Windows ou macOS |
| 3 | [Ligne de commande et markdown](ligne-de-commande-et-markdown.md) | Pourquoi du texte brut plutôt qu'une interface, et les six signes de markdown à connaître |
| 4 | [Créer son agent](creer-son-agent.md) | Un répertoire, un `CLAUDE.md`, une mémoire. Votre agent existe |
| 5 | [Le coût](abonnements.md) | Ce que les abonnements achètent vraiment, et ce qu'ils n'achètent pas |

Une fois l'étape 4 franchie, passez au [Bachelor en psychologie](../psycho/index.md) : c'est là que l'agent rencontre vos supports de cours.

## Ce qu'il vous faut

| Élément | Obligatoire | Remarque |
|---|---|---|
| Un abonnement Claude payant | Oui | Claude Code n'a pas de version gratuite. Environ 20 francs par mois pour l'entrée de gamme. Voir [Le coût](abonnements.md) |
| VS Code | Fortement recommandé | Gratuit, open source. Techniquement optionnel : Claude Code tourne dans un terminal seul |
| Un terminal | Oui | Fenêtre noire, commandes tapées. Deux heures d'inconfort, puis plus jamais de retour en arrière |
| Un compte GitHub | Non, pour l'instant | Utile pour versionner vos modules et récupérer ceux des autres |
| Une dictée vocale | Non | Confort réel quand on rédige beaucoup d'instructions en langage naturel |

## Le raccourci qui coûte cher

Faire installer et configurer l'agent par quelqu'un d'autre, ou copier une configuration toute faite sans la lire, produit exactement l'effet décrit dans la [théorie de la charge cognitive](../methode/charge-cognitive.md) : le travail est fait, le schéma mental n'est pas construit. Le jour où l'agent se comporte bizarrement, vous n'avez aucun modèle pour diagnostiquer.

Tapez les commandes. Ouvrez les fichiers de configuration. Cassez-en un, réparez-le.
