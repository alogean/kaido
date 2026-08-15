# Forfaits d'abonnement IA , OpenAI et Anthropic

> Instantané : 9 août 2026. Prix en USD, hors taxes, pour les abonnements grand public et équipe aux produits de conversation (ChatGPT et Claude). La facturation des tokens de l'API n'est pas couverte ici.
> Clé de fiabilité : 🟢 recherche primaire / autoritatif , 🟠 journalisme sérieux ou institutionnel , 🔴 blog / éditeur de logiciel / revue de faible qualité.
> Note sur la qualité des sources : les chiffres Anthropic viennent de la page de tarifs officielle (🟢). OpenAI bloque l'accès automatisé à sa page de tarifs, donc les chiffres ChatGPT viennent de la presse tech (🟠) et d'agrégateurs de prix (🔴). À vérifier avant de citer dans un support.

## Pourquoi cette page existe

Les étudiants demandent quel forfait ils devraient payer. La réponse honnête dépend du travail d'apprentissage qu'ils font réellement, pas du palier qui affiche le plus gros chiffre. Cette page donne d'abord la grille brute, puis la partie qui compte pédagogiquement : un palier supérieur achète du volume et de la vitesse, pas une meilleure pensée chez l'étudiant. Voir la [théorie de la charge cognitive](../methode/charge-cognitive.md) pour comprendre pourquoi une réponse plus rapide et plus complète peut être l'option coûteuse.

## La grille

| Éditeur | Forfait | Prix mensuel | Prix annualisé | Utilisateur visé | Accès aux modèles / usage | Caractéristiques distinctives |
|---|---|---|---|---|---|---|
| OpenAI | Free | $0 | : | Grand public | Modèle de pointe plafonné (de l'ordre de 10 messages par 5 h), puis bascule automatique vers un modèle plus léger | Recherche web, analyse de fichiers et d'images, génération d'images limitée, voix limitée. Publicité contextuelle en test |
| OpenAI | Go | ~$8 | : | Marchés sensibles au prix (98 pays depuis janv. 2026, UE incluse) | Plafonds plus élevés que Free sur les messages, les téléversements, les images, la longueur de mémoire | Positionné face au palier gratuit ; peut comporter de la publicité selon le marché |
| OpenAI | Plus | $20 | : | Particulier standard | Accès au raisonnement avancé, quotas autour de 160 messages par 3 h | Deep Research (quelques dizaines d'exécutions par mois), GPT personnalisés, Projects, voix avancée, sans publicité |
| OpenAI | Pro (palier Codex) | $100 | : | Développeurs, usage agentique intensif | 5x l'usage Codex de Plus ; même catalogue de modèles que le palier à $200 | Introduit le 9 avril 2026 en réponse directe à Claude Max 5x. La différence avec $200 porte sur le volume, pas sur la capacité |
| OpenAI | Pro (palier supérieur) | $200 | : | Utilisateurs intensifs | ~20x Plus, modèle "Pro" exclusif, contexte étendu, quota élevé de Deep Research | Téléversements et génération d'images de fait illimités |
| OpenAI | Business | $25 /siège | $20 /siège | Équipes, 2 sièges minimum | Usage large sur les modèles courants | Espaces de travail partagés, console d'administration, SSO, pas d'entraînement sur les données d'entreprise. Baisse de prix le 2 avril 2026 (auparavant $30 / $25) |
| OpenAI | Enterprise | Sur devis | Sur devis | Grandes organisations | Volumes négociés | SCIM, EKM, analytique, contexte étendu, support dédié, conformité |
| OpenAI | Edu | Sur devis | Sur devis | Universités | Négocié | Déploiement institutionnel, pas de prix public |
| Anthropic | Free | $0 | : | Grand public | Usage réduit, sous-ensemble de modèles | Chat web, mobile et bureau, recherche web, mémoire, création de fichiers, connecteurs, réflexion étendue |
| Anthropic | Pro | $20 | $17 /mois | Particulier standard | Usage accru, fenêtres glissantes de 5 h plus un plafond hebdomadaire | Claude Code, Cowork, Design, Science, projets illimités, Research, intégration Microsoft 365. Crédit d'usage non interactif : $20/mois |
| Anthropic | Max 5x | $100 | : | Usage intensif | 5x l'usage de Pro, limites de sortie relevées | Accès anticipé aux nouvelles fonctionnalités, priorité aux heures de pointe. Crédit non interactif : $100/mois |
| Anthropic | Max 20x | $200 | : | Utilisateurs intensifs | 20x l'usage de Pro | Même ensemble de fonctionnalités que Max 5x, plafonds hebdomadaires distincts (tous modèles / Sonnet seul). Crédit non interactif : $200/mois |
| Anthropic | Team, siège standard | $25 /siège | $20 /siège | Équipes | Plus d'usage que Pro | Facturation centralisée, SSO, recherche entreprise, pas d'entraînement sur les contenus par défaut |
| Anthropic | Team, siège premium | $125 /siège | $100 /siège | Équipes à usage intensif | 5x l'usage du siège standard | Même socle de fonctionnalités, quota multiplié |
| Anthropic | Enterprise, en libre-service | $20 /siège plus la consommation aux tarifs API | : | Organisations | Siège plus consommation variable | Plafonds de dépense, RBAC, SCIM, journaux d'audit, API de conformité, contrôles de rétention des données, liste blanche d'IP, HIPAA |
| Anthropic | Enterprise, avec accompagnement commercial | Sur devis | Sur devis | Grands comptes | Engagements de volume | MSA sur mesure, prise en charge des bons de commande, offres groupées |
| Anthropic | Education | Sur devis | Sur devis | Universités | Négocié | Accès étudiants et enseignants, crédits de recherche, ressources de formation |

## Lire la grille

Les deux catalogues ont convergé vers la même échelle : gratuit, ~$20, $100, $200, puis un siège équipe autour de $20:25. Le palier à $100 d'OpenAI a été introduit le 9 avril 2026 et vise explicitement Claude Max 5x. La seule vraie asymétrie est en bas de l'échelle : OpenAI a un palier à $8 (Go), Anthropic n'a rien entre $0 et $20.

Ce qu'achètent les paliers payants, par ordre d'importance réelle pour un étudiant :

1. **Le volume.** Plus de messages avant le plafond. C'est la principale chose au-dessus de $20.
2. **La latence et la priorité.** L'accès aux heures de pointe.
3. **Le quota agentique et de code.** Les paliers à $100 et $200 des deux côtés se vendent largement là-dessus. Sans intérêt pour la plupart des étudiants non techniciens.
4. **La capacité du modèle.** Réelle mais plus faible que ce que suggère le marketing, et surtout concentrée dans les meilleurs modèles de raisonnement.

Rien dans cette échelle n'achète un meilleur apprentissage. Un étudiant qui colle l'énoncé d'un devoir dans un forfait à $200 obtient le même non-apprentissage que sur le palier gratuit, en plus rapide.

## Réserves

Deux points sur lesquels les sources divergent, et où rien ne devrait être affirmé sans la page officielle :

- **Les noms exacts des modèles par palier pour ChatGPT.** Les agrégateurs citent GPT-5.3, 5.4 et 5.5 selon la date de rédaction de l'article.
- **Les quotas de messages.** OpenAI les ajuste sans annonce. Les chiffres ci-dessus sont des ordres de grandeur observés, pas des engagements contractuels.

Non couvert, parce que ce n'est pas un abonnement : la facturation de l'API au token des deux côtés. Elle s'ajoute à l'abonnement ou le remplace selon le forfait, notamment pour l'offre Enterprise en libre-service d'Anthropic, où le siège à $20 ne couvre pas la consommation.

## Sources

| Source | Média | Fiabilité | Lien |
|---|---|---|---|
| Claude pricing page | Anthropic | 🟢 Tarifs officiels de l'éditeur | https://claude.com/pricing |
| OpenAI introduces ChatGPT Pro $100 tier with 5x Codex usage | VentureBeat, 9 avr. 2026 | 🟠 Journalisme tech, cite l'annonce d'OpenAI | https://venturebeat.com/orchestration/openai-introduces-chatgpt-pro-usd100-tier-with-5x-usage-limits-for-codex |
| OpenAI adds new $100/month ChatGPT subscription tier | MacRumors, 9 avr. 2026 | 🟠 Journalisme tech | https://www.macrumors.com/2026/04/09/openai-pro-subscription-tiers/ |
| ChatGPT pricing 2026: Free vs Go vs Plus vs Pro | CometAPI | 🔴 Agrégateur proche des éditeurs, utilisé uniquement pour la structure des paliers | https://www.cometapi.com/chatgpt-pricing-2026-free-vs-go-vs-plus-vs-pro/ |
| ChatGPT Business pricing 2026 | Azterion | 🔴 Blog commercial, utilisé uniquement pour la baisse de prix de Business d'avril 2026 | https://azterion.com/en-us/chatgpt-for-business-pricing/ |
| Anthropic usage limits explained | tokenkarma | 🔴 Blog, utilisé uniquement pour les multiplicateurs d'usage 5x / 20x | https://tokenkarma.app/blog/anthropic-usage-limits-explained-2026/ |

## Maintenance

Cette page vieillit vite. Les deux éditeurs ont changé leurs prix deux fois sur le premier semestre 2026. Revérifier les deux pages de tarifs officielles avant de réutiliser ces chiffres dans du matériel pédagogique, et mettre à jour la date de l'instantané en haut de page quand c'est fait.
