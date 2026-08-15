---
title: Ligne de commande et markdown
---

# Ligne de commande et markdown

Version écrite de la [vidéo 3](parcours-video.md). Deux outils que beaucoup d'étudiants n'ont jamais touchés, et qui conditionnent tout le reste.

## Pourquoi une fenêtre noire

L'argument n'est pas nostalgique. Il est de contrôle.

| | Interface graphique | Ligne de commande |
|---|---|---|
| Ce que vous envoyez | Ce que l'interface veut bien transmettre | Exactement ce que vous tapez |
| Ce qui est ajouté à votre insu | Inconnu | Rien |
| Reproductible | Difficilement | Une commande se copie, se partage, s'archive |
| Découvrabilité | Bonne : on clique et on voit | Mauvaise : il faut savoir quoi taper |

La ligne de commande gagne sur la seule dimension qui compte ici : **savoir ce qui entre dans le contexte**. Dès qu'une interface s'interpose, une partie de ce qui est envoyé au modèle vous échappe, et vous perdez la capacité de diagnostiquer.

Le coût est réel : deux heures d'inconfort. Le rendement l'est aussi.

## Le markdown, en six signes

Le markdown est du texte brut où le formatage est écrit avec des caractères ordinaires. Deux propriétés en font le bon format pour configurer un agent : **un humain le lit sans le rendre**, et **une machine sait exactement où sont les titres**.

| Vous écrivez | Vous obtenez |
|---|---|
| `# Titre` | Un titre de premier niveau |
| `## Sous-titre` | Un titre de deuxième niveau |
| `**gras**` | **gras** |
| `*italique*` | *italique* |
| `- élément` | Une puce dans une liste |
| `` `code` `` | Du `code` |

C'est tout ce qu'il faut pour écrire un `CLAUDE.md`.

## Pourquoi pas Word

Dans un document Word, le formatage est stocké dans des couches invisibles. Vous voyez le résultat, pas la cause. Quand quelque chose se comporte mal, il n'y a rien à inspecter.

En markdown, **tout ce qui existe est visible**. Rien n'est caché, donc rien ne surprend. La comparaison avec HTML éclaire l'intérêt :

```html
<h1>Mon titre</h1>
```

```markdown
# Mon titre
```

Même sémantique, un tiers des caractères, et lisible sans effort. Les balises ouvrantes et fermantes de HTML ou XML sont faites pour les machines ; le markdown est fait pour les deux.

## L'extension compte

`CLAUDE.md`, pas `CLAUDE.txt`. Le suffixe indique le type de fichier : c'est ce qui permet à VS Code d'afficher les titres correctement et à Claude Code de reconnaître sa configuration.

Dans VS Code, un fichier markdown s'affiche en deux modes : la **source** (les dièses et les étoiles) et le **rendu** (le résultat mis en forme). Le bouton d'aperçu bascule de l'un à l'autre. Éditez la source, relisez le rendu.

## Vérifiez que ça tient

1. Pourquoi préférer une commande tapée à un bouton cliqué, dans ce contexte précis ?
2. Écrivez de tête le markdown pour un titre de deuxième niveau contenant un mot en gras.
3. Qu'est-ce qui, dans un fichier Word, empêche de diagnostiquer un problème de configuration ?

Ensuite : [Créer son agent](creer-son-agent.md).
