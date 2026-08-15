---
title: Installer Claude Code et VS Code
---

# Installer Claude Code et VS Code

Version écrite de la [vidéo 4](parcours-video.md). Compter vingt minutes la première fois.

!!! warning "Prérequis payant"
    Claude Code n'a pas de version gratuite. Il faut un **abonnement Claude payant**, le premier palier suffit. Voir [Le coût](abonnements.md) pour ce que chaque palier achète réellement.

## Vue d'ensemble

| Composant | Rôle | Analogie |
|---|---|---|
| Claude (le modèle) | Le cerveau : il raisonne, il décide | Le moteur |
| Claude Code | Le harnais : la boucle, les outils, l'accès aux fichiers | La transmission |
| VS Code | L'atelier : éditer et lire les fichiers de configuration | La carrosserie |
| Le terminal | Le canal direct vers le harnais | Le levier de vitesses |

VS Code est techniquement optionnel : Claude Code tourne dans un terminal seul. En pratique, éditer un `CLAUDE.md` de deux pages dans un terminal est une épreuve inutile.

## Windows

### 1. Installer VS Code

1. Aller sur <https://code.visualstudio.com>, cliquer **Download for Windows**.
2. Lancer l'exécutable téléchargé, accepter la licence.
3. Cocher **Create a desktop icon** si vous voulez l'icône, puis **Install**.
4. VS Code démarre à la fin de l'installation.

### 2. Installer l'extension Claude Code

1. Dans la barre latérale gauche, cliquer l'icône **Extensions** (les quatre carrés).
2. Chercher `Claude Code`, sélectionner l'extension officielle d'Anthropic.
3. Cliquer **Install**, puis accepter la demande de confiance.

### 3. Se connecter

1. Ouvrir Claude Code depuis l'icône ajoutée par l'extension.
2. Au choix du mode de connexion, **choisir "Claude AI subscription"**.

!!! danger "Ne prenez pas l'option API"
    L'option API se facture à l'usage, au token. Pour un usage quotidien d'étude, c'est nettement plus cher que l'abonnement, et la facture n'est pas plafonnée. C'est le seul écran de l'installation où une erreur coûte de l'argent.

3. Le navigateur s'ouvre sur la page de connexion Claude. Se connecter, autoriser VS Code.
4. Retour dans VS Code : taper `salut, qui es-tu ?`. S'il répond, c'est installé.

## macOS

Même parcours, deux différences :

1. Télécharger le `.zip` de VS Code depuis <https://code.visualstudio.com>, le décompresser, glisser **Visual Studio Code** dans **Applications**. Au premier lancement, macOS demande une confirmation d'ouverture.
2. Le reste est identique : extension Claude Code, connexion par abonnement, test.

Pour installer depuis le terminal plutôt que par l'extension, la commande est documentée sur <https://claude.com/product/claude-code>. La version en extension VS Code suffit pour tout ce que fait KaiDO.

## Choisir son modèle

Dans une session Claude Code, la commande `/model` liste les modèles disponibles. Au moment d'écrire :

| Modèle | Profil | Quand |
|---|---|---|
| **Opus 5** | Le défaut, très capable | Ne rien changer tant que rien ne coince |
| **Fable 5** | Le plus capable, le plus cher en jetons | Raisonnement long et vraiment difficile |
| **Sonnet 5** | Rapide, presque aussi bon | Volume, itérations rapides |
| **Haiku 4.5** | Petit et très rapide | Tâches mécaniques et répétitives |

L'analogie de la vidéo tient : Opus est la berline avec les airbags, Haiku la deux-chevaux. Aucune n'est "la bonne" dans l'absolu.

Utiliser Fable pour ranger trois fichiers de révision est du surdimensionnement conscient. Ce n'est pas grave, c'est juste à savoir.

!!! note "Cette section vieillit vite"
    Les noms de modèles et les versions changent en semaines. Si `/model` affiche autre chose que ce tableau, `/model` a raison.

## La commande slash

Dans une session, taper `/` ouvre la liste des commandes disponibles. Il y en a beaucoup. Trois suffisent pour commencer :

| Commande | Effet |
|---|---|
| `/model` | Changer de modèle en cours de session |
| `/clear` | Repartir d'un contexte vide, en gardant la configuration |
| `/help` | Voir le reste |

## Ça ne marche pas

| Symptôme | Cause la plus fréquente |
|---|---|
| "command not found" dans le terminal | L'installation en ligne de commande n'a pas abouti, ou le terminal doit être relancé |
| Demande de payer à l'usage | Vous avez choisi l'option API au lieu de "Claude AI subscription". Se déconnecter et recommencer |
| L'agent ne voit pas vos fichiers | Le répertoire ouvert dans VS Code n'est pas celui du module. Voir [Créer son agent](creer-son-agent.md) |
| Réponses génériques sur votre cours | Le contexte est vide : rien n'a été versé dans `data-source`. Voir [la méthode par module](../psycho/methode-module.md) |

## Ensuite

- [Ligne de commande et markdown](ligne-de-commande-et-markdown.md) : pourquoi ces outils, et les six signes de markdown à connaître.
- [Créer son agent](creer-son-agent.md) : le répertoire, le `CLAUDE.md`, la mémoire.
