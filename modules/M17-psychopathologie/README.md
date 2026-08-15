# M17 , psychopathologie

Agent de révision pour le module M17 du bachelor en psychologie. Gabarit de référence pour les autres modules.

Documentation complète : <https://alogean.github.io/kaido/psycho/m17/>

## Arborescence

```text
M17-psychopathologie/
├── CLAUDE.md              ← configuration de l'agent (versionné)
├── README.md              ← ce fichier (versionné)
├── .gitignore             ← exclut sources et productions (versionné)
├── data-source/           ← supports de cours (jamais versionné)
├── generated-artifacts/   ← fiches, quiz, plans (jamais versionné)
└── memory/                ← progression, erreurs (jamais versionné)
```

## Démarrer

1. Ouvrir ce répertoire dans VS Code.
2. Verser les supports de cours dans `data-source/`.
3. Lancer une session Claude Code : la configuration de `CLAUDE.md` se charge toute seule.
4. Passer les trois tests d'acceptation ci-dessous avant de lui faire confiance.

## Les trois tests d'acceptation

| Test | Ce que vous faites | Réponse attendue |
|---|---|---|
| Le vide | Poser une question du cours avec `data-source` vide | Il signale l'absence de sources, il n'improvise pas |
| Le hors-champ | Poser une question du domaine absente du cours | Il dit que ce n'est pas dans les sources |
| La traçabilité | "D'où vient cette affirmation ?" | Il nomme un fichier, pas ses connaissances générales |

Un agent qui échoue au premier test échouera partout ailleurs, en silence.

## Ce qui ne monte jamais ici

Polycopiés, diapositives, articles sous licence, énoncés d'examen, notes numérisées. Le `.gitignore` les exclut, mais vérifiez avant de pousser : un `.gitignore` protège moins bien qu'une habitude.

Ce qui se partage utilement entre étudiants, c'est le `CLAUDE.md`, pas le PDF du cours.
