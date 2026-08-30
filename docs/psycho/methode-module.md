---
title: Méthode par module
---

# Méthode par module

La convention reproductible : un module, un répertoire, un agent. Elle vaut pour la psychopathologie comme pour les statistiques ou la neuroanatomie.

## L'arborescence

```text
modules/Bachelor/M17/
├── CLAUDE.md              ← la configuration de l'agent
├── README.md              ← ce que couvre le module, comment l'examen est évalué
├── data-source/           ← vos supports de cours
├── generated-artifacts/   ← fiches, quiz, plans
└── memory/                ← progression, erreurs récurrentes
```

!!! danger "Ce répertoire reste local"
    Un module ne se pousse pas sur un dépôt public, ni ses supports, ni sa configuration, ni sa mémoire. Si vous versionnez votre travail, ignorez `modules/` en entier plutôt que d'y trier fichier par fichier :

    ```gitignore
    modules/
    ```

    Une règle grossière se respecte. Une règle subtile s'oublie un soir de révision, et un polycopié sous droits se retrouve public.

## Quelles ressources verser

| Type de ressource | Verser ? | Pourquoi |
|---|---|---|
| Polycopié, notes de cours de l'enseignant | **Oui, en priorité** | C'est la source de vérité de l'examen |
| Diapositives du cours | Oui | Structure et vocabulaire attendus |
| Articles obligatoires de la bibliographie | Oui | Souvent évalués directement |
| Vos propres notes manuscrites | Oui, une fois numérisées | Elles portent ce que vous avez compris, donc les trous |
| Anciens examens, énoncés types | Oui | Alignent la révision sur la forme réelle de l'évaluation |
| Manuel entier de 600 pages | Non | Noie le signal : le cours n'en couvre qu'une fraction |
| Résumés trouvés en ligne | **Non** | Fiabilité inconnue, découpage étranger au cours |
| Fiches produites par l'agent lui-même | **Non** | Boucle de rétroaction : il révise ses propres approximations |

Cette dernière ligne est le piège le plus courant. Une fiche générée qui retourne dans `data-source` devient une source de vérité alors qu'elle n'en est pas une. Les productions restent dans `generated-artifacts` et n'en sortent pas.

## Sous quelle forme

| Format | Utilisable | Remarque |
|---|---|---|
| PDF texte | Très bien | Le cas normal |
| PDF scanné (image) | Médiocre | Sans couche texte, il n'y a rien à lire. Passer par un OCR d'abord |
| Markdown, texte brut | Idéal | Léger, propre, éditable |
| Word, PowerPoint | Correct | Lisible sans conversion |
| Photos de tableau | À éviter | Convertissez ce qui compte en texte |

Nommez les fichiers de façon parlante : `03-troubles-anxieux-polycopie.pdf` vaut mieux que `Cours3_v2_final.pdf`. L'agent utilise les noms pour se repérer, et vous aussi.

!!! tip "Récupérer les supports sans trente clics droits"
    La [skill Moodle](../outils/skill-moodle.md) télécharge les documents et les vidéos d'un cours UniDistance directement dans `data_sources/`, correctement nommés. Elle ne remplace pas le tri décrit ci-dessus : elle vous donne juste de quoi trier.

## Les quatre instructions non négociables

À faire figurer dans chaque `CLAUDE.md`, quel que soit le module :

1. **Contrainte de source.** Répondre uniquement depuis `data-source`, sans culture générale ni recherche web.
2. **Aveu d'absence.** Si l'information n'est pas dans les sources, le dire clairement au lieu de combler.
3. **Traçabilité.** Citer le fichier et si possible la section d'où vient chaque affirmation.
4. **Refus de complaisance.** Signaler une réponse fausse ou approximative sans l'adoucir.

Les trois premières sont des garde-fous factuels. La quatrième est pédagogique : un agent qui valide tout vous laisse dans l'illusion de savoir, ce qui est précisément l'échec que la [métacognition](../methode/concepts.md) cherche à éviter.

## Vérifier que l'agent s'y tient

Trois tests, à faire une fois par module, avant de lui faire confiance.

| Test | Ce que vous faites | Réponse attendue |
|---|---|---|
| **Le vide** | Poser une question du cours avec `data-source` encore vide | Il annonce que les sources sont absentes, il n'improvise pas |
| **Le hors-champ** | Poser une question du domaine mais absente du cours | Il dit que ce n'est pas dans les sources fournies |
| **La traçabilité** | Demander d'où vient une affirmation qu'il vient de faire | Il nomme le fichier, pas "mes connaissances générales" |

Un agent qui échoue au test du vide échouera partout ailleurs, en silence. C'est le test à faire en premier et à refaire après chaque modification de la configuration.

## Le cycle de révision

1. **Verser** les sources dans `data-source`.
2. **Demander un plan de bataille** : ce que couvre le module, dans quel ordre, où sont les points denses.
3. **Se faire interroger**, chapitre par chapitre. Répondre d'abord, vérifier ensuite. Jamais l'inverse.
4. **Consigner les erreurs** dans `memory` : ce sont elles qui pilotent les séances suivantes.
5. **Espacer.** Revenir sur un chapitre quelques jours plus tard, sans relire d'abord.

L'ordre de l'étape 3 est le cœur du dispositif. Tenter de répondre avant de voir la réponse, même en se trompant, produit un apprentissage nettement supérieur à la relecture, et l'échec lui-même prépare la mémorisation. Voir [Charge cognitive](../methode/charge-cognitive.md) et [Concepts](../methode/concepts.md).

## Où l'IA volerait l'apprentissage

| Usage | Effet réel |
|---|---|
| Faire résumer le chapitre et lire le résumé | Le travail de compression, celui qui produit la trace mémoire, a été fait par la machine |
| Faire produire des fiches et les relire | La relecture crée un sentiment de familiarité, pas une capacité de restitution |
| Demander la réponse avant d'avoir essayé | Supprime l'effort de récupération, c'est-à-dire l'apprentissage lui-même |
| Faire rédiger une dissertation d'entraînement | Vous évaluez un texte que vous n'avez pas produit : aucun diagnostic exploitable |

Le test simple : **si vous n'avez pas eu à récupérer quelque chose en mémoire, vous n'avez rien appris pendant cette heure.** Vous avez peut-être produit un document. Ce n'est pas la même chose.

## Démarrer un nouveau module

1. Copier l'arborescence de [M17](m17.md).
2. Adapter le `CLAUDE.md` : identité, objectif, spécificités du module.
3. Verser les sources.
4. Passer les trois tests ci-dessus.
5. Réviser.
