---
title: Bachelor en psychologie
---

# 2. Bachelor en psychologie

**La question de cette section : qu'est-ce que je verse dans l'agent, et sous quelle forme ?**

Un agent bien installé mais vide répond à côté avec assurance. Ce qui fait la différence entre un chatbot et un agent de révision, ce n'est pas l'outillage : c'est la discipline sur les sources.

## La règle qui gouverne tout

> **Ce qui entre détermine ce qui sort.**

Le modèle connaît la psychologie académique en général. Il ne connaît pas le module de votre enseignant, ses définitions, son découpage, ni ce qu'il considère comme hors-programme. Un agent contraint à `data-source` répond sur votre cours. Un agent non contraint répond sur la moyenne de la littérature, avec le même aplomb, et vous ne verrez pas la différence à la lecture.

## Les pages

| Page | Ce qu'elle contient |
|---|---|
| [Méthode par module](methode-module.md) | La convention de répertoire, quelles ressources verser, lesquelles jamais, et comment vérifier que l'agent s'y tient |
| [Module M17, psychopathologie](m17.md) | Le gabarit complet, reproductible pour n'importe quel module |

## Sur GitHub

Chaque module est un sous-répertoire de [`modules/`](https://github.com/alogean/kaido/tree/main/modules) dans le dépôt. Ce qui est versionné : la configuration de l'agent, la méthode, l'inventaire des sources.

!!! danger "Ce qui n'est jamais poussé"
    **Les supports de cours ne montent pas sur GitHub.** Polycopiés, diapositives, articles sous licence, énoncés d'examen : ils appartiennent à leurs auteurs et le dépôt est public. Chaque module contient un `.gitignore` qui exclut `data-source/` et `generated-artifacts/`, mais un `.gitignore` protège moins bien qu'une habitude. Vérifiez avant de pousser.

Ce qui se partage utilement entre étudiants, ce n'est pas le PDF du cours : c'est le `CLAUDE.md` qui a bien marché.

## Le raccourci qui coûte cher

Verser le polycopié, demander un résumé, lire le résumé, cocher la case. C'est exactement l'usage décrit dans la [vidéo 1](../outils/parcours-video.md) comme celui qui n'a rien laissé après quatre ans de bachelor : le travail de compression, celui qui produit la mémorisation, a été fait par la machine.

L'agent est utile pour vous **interroger** sur le polycopié, pas pour le lire à votre place. La [section méthodologie](../methode/index.md) explique pourquoi cette distinction est la seule qui compte vraiment.
