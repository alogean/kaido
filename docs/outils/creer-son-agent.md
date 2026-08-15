---
title: Créer son agent
---

# Créer son agent

Version écrite de la [vidéo 5](parcours-video.md). C'est le moment où l'outillage devient votre agent.

## Un agent, c'est un répertoire

La démystification la plus utile de la série :

> **Un agent = un répertoire + un fichier `CLAUDE.md`.**

Pas de compte à créer, pas d'interface à configurer, pas de plateforme à apprendre. Un dossier sur votre disque, et dedans un fichier texte qui décrit qui il est et comment il travaille.

## L'arborescence

```text
M17-psychopathologie/
├── CLAUDE.md              ← la configuration : qui il est, comment il travaille
├── data-source/           ← vos supports de cours (entrée)
├── generated-artifacts/   ← ce qu'il produit (sortie)
└── memory/                ← ce qu'il retient d'une séance à l'autre
```

| Répertoire | Contenu | Qui écrit |
|---|---|---|
| `data-source` | Polycopiés, articles, notes de cours, diapositives | Vous |
| `generated-artifacts` | Fiches, plans de révision, quiz, synthèses | L'agent |
| `memory` | Progression, erreurs récurrentes, profil de révision | L'agent |

La séparation entrée / sortie n'est pas cosmétique. Sans elle, au bout de deux semaines vous ne savez plus ce qui vient du cours et ce que l'agent a produit. Or c'est **exactement** la distinction qui compte quand vous réviser : une fiche générée n'a pas l'autorité d'un polycopié.

Les noms sont à vous. `sources` et `sorties` marchent aussi bien, tant que vous vous y tenez.

## Écrire la configuration en parlant

Le geste central de la vidéo 5 : vous ne rédigez pas `CLAUDE.md` à la main. Vous décrivez ce que vous voulez en langage naturel, et l'agent écrit sa propre configuration.

Créez le répertoire, ses sous-répertoires, un `CLAUDE.md` vide. Ouvrez le répertoire dans VS Code, lancez une session, et dictez :

> Tu es mon agent de révision pour le module M17. Je veux que tu m'aides à réussir l'examen. Tu t'appelles El Professor. Mets toute ta configuration dans le fichier `CLAUDE.md`. Je veux une personnalité empreinte d'humour noir, un peu sarcastique : challenge-moi, ne me passe pas de pommade. Prends toutes tes sources dans le répertoire `data-source`, mets tout ce que tu génères dans `generated-artifacts`. Configuration et réponses en français.

Il écrit le fichier. Vous le relisez, vous corrigez ce qui ne va pas.

**Relisez vraiment.** C'est la seule partie de l'exercice qui ne se délègue pas : la configuration est le contrat, et un contrat qu'on ne lit pas n'engage que celui qui l'a écrit.

## Les six décisions à prendre

Quel que soit le module, une configuration utile tranche six points :

| Décision | Question | Exemple |
|---|---|---|
| **Identité** | Qui est-il, pour quel module | "Agent de révision pour M17, psychopathologie" |
| **Objectif** | Réussir quoi, précisément | "Réussir l'examen, pas me faire plaisir" |
| **Langue** | Dans quelle langue il répond et écrit | "Français, sans exception" |
| **Personnalité** | Complaisant ou exigeant | "Sarcastique. Zéro pommade. Moque-toi des réponses approximatives" |
| **Sources** | D'où viennent les faits | "Uniquement `data-source`" |
| **Productions** | Où vont les fichiers | "`generated-artifacts`" |

La ligne "personnalité" n'est pas décorative. Un agent qui valide tout ce que vous dites vous laisse croire que vous savez. Un agent qui vous contredit vous montre l'écart entre ce que vous croyez savoir et ce que vous savez, ce qui est exactement le travail de la métacognition. Voir [Concepts](../methode/concepts.md).

## L'instruction décisive

Sans elle, vous avez un chatbot dans un répertoire. Avec elle, vous avez un agent de révision :

> Très important : quand je te pose une question, va chercher l'information **uniquement** dans `data-source`. N'utilise ni tes connaissances préexistantes ni la recherche web. Uniquement les fichiers que je te donne.

Pourquoi c'est le pivot de tout le parcours :

- **Le modèle connaît le domaine, pas votre cours.** Il vous servira une psychopathologie générique, correcte et hors sujet, avec la même assurance.
- **L'examen porte sur le cours de votre enseignant**, avec ses définitions, ses limites, son découpage.
- **Une réponse qui contredit le polycopié devient repérable** au lieu de passer pour une nuance.

Quand vous posez une question et que `data-source` est vide, un agent bien configuré doit vous le dire plutôt que d'improviser. C'est le comportement à vérifier en premier.

## La mémoire

Deuxième itération de la vidéo : demander un répertoire `memory` et laisser l'agent découper ses connaissances en fichiers.

> Crée un sous-répertoire `memory` et subdivise tes connaissances en fichiers que tu y stockes.

Il propose en général une découpe raisonnable : progression, erreurs récurrentes, profil, journal. Vous ajustez.

Ce qu'il faut savoir : l'agent range parfois une instruction ailleurs que là où vous l'attendiez, par exemple dans `memory/profil.md` au lieu de `CLAUDE.md`. **Déplacez-la.** La configuration reste la vôtre, et savoir où se trouve chaque règle fait partie du contrôle que tout ce parcours cherche à vous donner.

## Ce qui se recharge à chaque fois

À l'ouverture du répertoire, Claude Code lit `CLAUDE.md` automatiquement. Vous n'avez rien à recoller, rien à réexpliquer. La configuration est persistante par construction, versionnable, partageable, et lisible en clair.

C'est la différence de fond avec un projet ChatGPT ou un dossier Claude : là-bas la configuration existe aussi, mais vous ne pouvez ni la relire ligne à ligne, ni la mettre sous git, ni l'envoyer à un camarade.

## Plusieurs sessions en parallèle

VS Code permet d'ouvrir plusieurs sessions Claude Code en même temps sur le même répertoire. Une pour réviser un chapitre, une autre pour une question de fond, sans mélanger les fils.

## Le raccourci qui coûte cher

Demander à l'agent de produire la fiche de révision **et** de vous la résumer, puis lire le résumé. Vous obtenez un document que vous n'avez ni construit ni interrogé, et la sensation d'avoir travaillé.

La fiche générée est un point de départ à contester, pas un livrable à archiver. Testez-vous dessus avant de la relire : se tester est plus efficace que relire, et c'est le seul moyen de voir ce qui manque. Voir [Charge cognitive](../methode/charge-cognitive.md).

## Ensuite

Le gabarit complet, avec un `CLAUDE.md` prêt à adapter : [Module M17](../psycho/m17.md). La convention générale : [Méthode par module](../psycho/methode-module.md).
