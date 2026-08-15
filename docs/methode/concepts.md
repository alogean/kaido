# Concepts des sciences de l'apprentissage , référence de la carte des domaines

> Une référence autonome qui explique les concepts fondamentaux de psychologie de l'éducation sous-jacents au parcours d'apprentissage, et qui associe chaque concept à la partie du parcours qu'il gouverne.
> Public : toute personne qui conçoit des expériences d'apprentissage ou des outils d'apprentissage assistés par l'IA, et les équipes qui animent des ateliers de pédagogie.

---

## 1. Comment lire ce fichier

Le parcours d'apprentissage peut être décomposé en 14 domaines : 7 du côté étudiant (S1:S7) et 7 du côté enseignant (T1:T7). Chaque domaine est "ancré" par un ou deux concepts des sciences de l'apprentissage : la théorie qui explique *pourquoi* ce domaine compte et *à quoi ressemble la qualité* à cet endroit.

Ce fichier fait la correspondance inverse : il prend chaque concept, l'explique en profondeur, et indique quel(s) domaine(s) il ancre et ce qu'il implique quand vous construisez un assistant d'apprentissage IA. Utilisez-le pour maintenir tout le monde sur la même longueur d'onde lors de la génération ou du filtrage de cas d'usage.

**Légende de lecture :** S = domaine étudiant, T = domaine enseignant. "Ancre" = le ou les domaines où ce concept constitue le fondement théorique nommé.

---

## 2. La carte des domaines

<figure class="kaido-figure">
<object class="kaido-map-object" type="image/svg+xml" data="../../assets/domain-map.svg"><img src="../../assets/domain-map.svg" alt="Carte des domaines des sciences de l'apprentissage : les 14 domaines du parcours d'apprentissage et le concept qui ancre chacun d'eux"></object>
<figcaption>Les 14 domaines du parcours d'apprentissage (S1:S7 étudiants, T1:T7 enseignants) et le concept qui ancre chacun d'eux. Cliquez sur un domaine pour ouvrir son concept ; S2 et T2 renvoient à la page commune sur la théorie de la charge cognitive.</figcaption>
</figure>

### Parcours étudiant (S1:S7)

| Domaine | Titre | Ce qu'il couvre |
|---|---|---|
| S1 | Orientation et planification | Comprendre ce qu'il faut apprendre et planifier le chemin avant que l'apprentissage ne commence |
| S2 | Acquisition de connaissances | Assimiler du contenu nouveau et le structurer dans son propre esprit |
| S3 | Pratique active et construction de compétences | Appliquer les connaissances par des projets, des problèmes, du travail de terrain |
| S4 | Collaboration et apprentissage entre pairs | Apprendre avec et par les autres étudiants |
| S5 | Évaluation et autodiagnostic | Vérifier ce que l'on sait avant l'examen officiel |
| S6 | Réflexion et métacognition | Réfléchir à son propre apprentissage et l'ajuster |
| S7 | Bien-être et motivation | Gérer la motivation, l'anxiété, l'accessibilité, l'engagement |

### Parcours enseignant (T1:T7)

| Domaine | Titre | Ce qu'il couvre |
|---|---|---|
| T1 | Conception de cours | Façonner un cours depuis les objectifs jusqu'au plan de cours et à l'évaluation |
| T2 | Création et curation de contenu | Produire ou sélectionner des diapositives, vidéos, lectures, exercices |
| T3 | Animation en classe | Mener des séances engageantes, en présentiel, en hybride ou en ligne |
| T4 | Conception de l'évaluation | Concevoir des examens qui mesurent équitablement les objectifs d'apprentissage |
| T5 | Notation et rétroaction | Noter les travaux et retourner une rétroaction actionnable |
| T6 | Évaluation et amélioration du cours | Recueillir de la rétroaction sur son enseignement et itérer |
| T7 | Développement professionnel | Faire progresser sa propre pratique d'enseignement dans la durée |

---

## 3. Index domaine → concept (vue directe)

| Domaine | Titre | Concept(s) d'ancrage |
|---|---|---|
| S1 | Orientation et planification | Autorégulation / fixation d'objectifs (Zimmerman) |
| S2 | Acquisition de connaissances | Théorie de la charge cognitive (Sweller) ; double codage (Paivio) |
| S3 | Pratique active et construction de compétences | ICAP niveau "C" Constructif (Chi) ; apprentissage cognitif (Collins et al.) |
| S4 | Collaboration et apprentissage entre pairs | ICAP niveau "I" Interactif (Chi) ; constructivisme social / ZPD (Vygotsky) |
| S5 | Évaluation et autodiagnostic | Évaluation formative (Black & Wiliam) |
| S6 | Réflexion et métacognition | Contrôle métacognitif (Flavell) |
| S7 | Bien-être et motivation | Théorie de l'autodétermination (Deci & Ryan) |
| T1 | Conception de cours | Alignement constructif (Biggs) |
| T2 | Création et curation de contenu | Théorie de la charge cognitive (Sweller) |
| T3 | Animation en classe | Apprentissage actif (Freeman et al.) |
| T4 | Conception de l'évaluation | Les cinq phases de l'évaluation |
| T5 | Notation et rétroaction | Rétroaction efficace (Hattie & Timperley) |
| T6 | Évaluation et amélioration du cours | Pratique réflexive (Schön) |
| T7 | Développement professionnel | Communautés de pratique (Wenger) |

---

## 4. Catalogue des concepts (vue inverse)

Chaque concept ci-dessous suit la même structure : **origine → ce qu'il dit → à quoi il ressemble en pratique → ce qu'il ancre → pertinence pour un assistant d'apprentissage IA.**

### 4.1 Autorégulation / fixation d'objectifs , Zimmerman (2000)

- **Ce qu'il dit :** les étudiants qui fixent des objectifs précis, suivent leur propre progression et ajustent leurs stratégies réussissent mieux que ceux qui ne le font pas. L'autorégulation est un cycle (anticipation → performance → autoréflexion) et une compétence *enseignable*, pas un trait figé.
- **En pratique :** aider les étudiants à traduire une intention vague ("réussir l'examen") en sous-objectifs concrets et suivis ("terminer les lectures du module 3 pour la semaine 5, auto-évaluation en semaine 6").
- **Ancre :** S1 (Orientation et planification).
- **Pertinence pour un assistant d'apprentissage IA :** un point d'entrée naturel. Un assistant qui connaît le programme, les échéances et la structure du cours peut étayer la fixation d'objectifs au niveau du semestre et du parcours d'étude, transformant la planification d'un acte ponctuel en un cycle suivi.

### 4.2 Théorie de la charge cognitive , Sweller (1988)

- **Ce qu'il dit :** l'apprentissage est borné par la mémoire de travail. Trois types de charge : **intrinsèque** (difficulté inhérente à la tâche), **superflue** (friction ajoutée par une mauvaise conception), **utile** (effort qui construit réellement des connaissances durables). Une bonne conception minimise la charge superflue et protège la charge utile.
- **En pratique :** ne pas obliger les étudiants à chercher dans de multiples systèmes pour rassembler ce dont ils ont besoin ; ne pas surcharger une diapositive ; séquencer le contenu pour que les prérequis viennent d'abord.
- **Ancre :** S2 (Acquisition de connaissances, côté étudiant) et T2 (Création et curation de contenu, côté enseignant).
- **Pertinence pour un assistant d'apprentissage IA :** une information dispersée *est* une charge cognitive superflue. Un point d'entrée unique qui retrouve le bon contenu validé réduit exactement cette charge. Transversal aux deux personas : il aide les étudiants à assimiler (S2) et les enseignants à sélectionner (T2).

### 4.3 Double codage , Paivio (1971)

- **Ce qu'il dit :** l'être humain traite l'information par deux canaux partiellement indépendants, verbal et visuel. Un texte *et* une image bien choisis produisent ensemble un meilleur rappel et une meilleure compréhension que le texte seul.
- **En pratique :** associer les explications à des schémas, des cartes conceptuelles, des figures annotées plutôt qu'à des murs de prose.
- **Ancre :** S2 (Acquisition de connaissances).
- **Pertinence pour un assistant d'apprentissage IA :** un levier chaque fois que l'assistant présente ou génère du matériel d'apprentissage : associer une explication textuelle à une carte conceptuelle ou un schéma généré améliore la rétention par rapport au texte seul.

### 4.4 Cadre ICAP , Chi (2014)

- **Ce qu'il dit :** classe les activités d'apprentissage par profondeur cognitive : **I**nteractif > **C**onstructif > **A**ctif > **P**assif. Plus l'engagement est profond, plus l'apprentissage est important. Interactif (co-construire avec un partenaire) l'emporte sur Constructif (produire soi-même quelque chose), qui l'emporte sur Actif (manipuler un matériel donné), qui l'emporte sur Passif (se contenter de recevoir).
- **En pratique :** un levier de diagnostic pour l'IA : il indique *quand l'assistance de l'IA amplifie l'apprentissage et quand elle le court-circuite.* Si l'IA fait le travail constructif à la place de l'étudiant, vous l'avez fait redescendre au niveau Passif.
- **Ancre :** S3 (Pratique active, niveau "C" / Constructif) et S4 (Collaboration, niveau "I" / Interactif).
- **Pertinence pour un assistant d'apprentissage IA :** le concept de conception pivot. C'est la raison de principe de donner des indices et des contre-questions plutôt que des réponses finies. Utilisez ICAP comme filtre : un cas d'usage qui fait retomber les étudiants au niveau Passif doit être rejeté, même s'il est techniquement facile à construire.

### 4.5 Apprentissage cognitif , Collins, Brown & Newman (1989)

- **Ce qu'il dit :** enseigner des compétences cognitives complexes en rendant la pensée experte *visible* : modelage, accompagnement, étayage, articulation, réflexion, estompage. L'expert externalise un raisonnement normalement invisible.
- **En pratique :** montrer le raisonnement déroulé, puis retirer progressivement le soutien à mesure que l'étudiant prend le relais (l'étape d'"estompage").
- **Ancre :** S3 (Pratique active et construction de compétences).
- **Pertinence pour un assistant d'apprentissage IA :** correspond à une conception "tuteur ou explicateur" et à des limites de requêtes par séance (étayage puis estompage). L'assistant modélise le raisonnement, accompagne, et s'efface à mesure que la compétence grandit.

### 4.6 Constructivisme social / zone proximale de développement , Vygotsky (1978)

- **Ce qu'il dit :** la connaissance se construit par l'interaction sociale. La zone proximale de développement (ZPD) est l'écart entre ce qu'un étudiant peut faire seul et ce qu'il peut faire avec l'aide d'un pair plus compétent ou d'un enseignant : la bande où l'apprentissage le plus productif se produit.
- **En pratique :** enseignement par les pairs, travail de groupe structuré, et indices bien calibrés (opérant à l'intérieur de la ZPD, ni au-dessus ni en dessous).
- **Ancre :** S4 (Collaboration et apprentissage entre pairs).
- **Pertinence pour un assistant d'apprentissage IA :** présente l'IA comme un "pair plus compétent" opérant dans la ZPD : un cadrage utile, mais aussi une mise en garde. Un robot trop serviable fait s'effondrer la ZPD. Se combine avec ICAP pour justifier un tutorat par indices plutôt qu'une distribution de réponses.

### 4.7 Évaluation formative , Black & Wiliam (1998)

- **Ce qu'il dit :** une évaluation utilisée *pendant* l'apprentissage pour diagnostiquer et ajuster, pas pour juger. Des boucles de rétroaction serrées entre enseignant et étudiant produisent certains des gains mesurables les plus importants de toute la littérature en éducation.
- **En pratique :** quiz à faible enjeu, pratique de récupération, sondages en direct : chacun générant un signal qui change ce qui se passe ensuite.
- **Ancre :** S5 (Évaluation et autodiagnostic).
- **Pertinence pour un assistant d'apprentissage IA :** la valeur côté étudiant est l'autodiagnostic ("teste-moi sur ce module") ancré dans un contenu validé et spécifique au cours, dont le résultat oriente ce qu'il faut étudier ensuite.

### 4.8 Contrôle métacognitif , Flavell (1979)

- **Ce qu'il dit :** la conscience de sa propre pensée et de son propre apprentissage ("est-ce que je comprends vraiment ceci ?"). Les étudiants qui surveillent leur compréhension apprennent davantage, parce qu'ils repèrent leurs propres incompréhensions avant que l'examen ne le fasse.
- **En pratique :** inciter les étudiants à s'auto-expliquer, à prédire leur niveau de préparation à l'examen, et à identifier ce qu'ils ne savent *pas*.
- **Ancre :** S6 (Réflexion et métacognition).
- **Pertinence pour un assistant d'apprentissage IA :** un domaine peu couvert et à fort potentiel. Un agent conversationnel est naturellement adapté au questionnement métacognitif ("réexplique-moi ça", "où es-tu le moins sûr ?").

### 4.9 Théorie de l'autodétermination , Deci & Ryan (1985)

- **Ce qu'il dit :** la motivation durable repose sur trois besoins psychologiques fondamentaux : l'**autonomie** (sentiment de choix), la **compétence** (se sentir capable) et l'**affiliation** (lien aux autres). Soutenez les trois et vous obtenez de l'engagement ; sapez-les et vous obtenez de l'abandon.
- **En pratique :** offrir aux étudiants des choix qui ont du sens, calibrer le défi pour qu'ils continuent à se sentir capables, et préserver le lien humain et social.
- **Ancre :** S7 (Bien-être et motivation).
- **Pertinence pour un assistant d'apprentissage IA :** la lentille de la fidélisation. La rétention à long terme découle de la capacité du produit à satisfaire l'autonomie, la compétence et l'affiliation. "Soutenant, pas prescriptif" est le soutien à l'autonomie en langage clair. Notez la tension : trop d'IA sape la compétence, parce que les étudiants cessent de construire eux-mêmes la compétence.

### 4.10 Alignement constructif , Biggs (1996)

- **Ce qu'il dit :** un cours est bien conçu quand les objectifs d'apprentissage visés, les activités d'enseignement et l'évaluation ciblent tous les mêmes compétences. "Énoncez ce qu'ils doivent apprendre, enseignez exactement cela, puis évaluez exactement cela."
- **En pratique :** conception à rebours à partir des objectifs ; aucune activité ni item d'examen qui ne soit rattaché à un objectif énoncé.
- **Ancre :** T1 (Conception de cours). L'épine dorsale qui traverse S1, T1 et T4.
- **Pertinence pour un assistant d'apprentissage IA :** le vocabulaire commun pour parler aux enseignants. Situer le rôle de l'assistant à l'intérieur de leur chaîne d'alignement constructif (aider les étudiants à atteindre les objectifs énoncés, pas à contourner l'évaluation) constitue l'argumentaire crédible. Relie S1 (planification de l'étudiant vers les objectifs) à T4 (évaluation de ces objectifs).

### 4.11 Apprentissage actif , Freeman et al. (2014)

- **Ce qu'il dit :** des données méta-analytiques montrent que les étudiants en conditions d'apprentissage actif obtiennent de meilleurs résultats que ceux placés en cours magistraux passifs (moins d'échecs, notes plus élevées). "Actif" signifie faire quelque chose pendant la séance, pas seulement écouter.
- **En pratique :** remplacer des plages de cours magistral par des questions, des problèmes, des échanges entre pairs, des sondages.
- **Ancre :** T3 (Animation en classe).
- **Pertinence pour un assistant d'apprentissage IA :** essentiellement le domaine de la salle de classe en direct, où le sondage en direct est l'outil canonique d'apprentissage actif. Un domaine encombré : un assistant ne devrait y entrer que là où il apporte un véritable avantage de système ou de données, pas pour concurrencer sur les méthodes d'animation.

### 4.12 Les cinq phases de l'évaluation

- **Ce qu'il dit :** le cycle de vie complet d'une évaluation comme processus itératif, pas comme événement ponctuel : concevoir → développer → administrer → noter → améliorer.
- **En pratique :** traiter chaque examen comme quelque chose dont la qualité doit être analysée et améliorée, avec des grilles et une analyse d'items qui alimentent l'itération suivante.
- **Ancre :** T4 (Conception de l'évaluation).
- **Pertinence pour un assistant d'apprentissage IA :** surtout tourné vers l'enseignant, mais pertinent pour la conversation sur l'intégrité académique (formats d'évaluation conscients de l'IA, conception en livre ouvert). Un domaine encombré ; l'angle étroit côté étudiant consiste à les aider à s'entraîner sur des formats authentiques.

### 4.13 Rétroaction efficace , Hattie & Timperley (2007)

- **Ce qu'il dit :** la rétroaction fonctionne le mieux quand elle répond à trois questions : *Où vais-je ?* (objectifs), *Comment est-ce que j'avance ?* (progression), *Et ensuite ?* (prochaines étapes). Elle est la plus puissante aux niveaux de la tâche et du processus ; la moins utile quand elle vise la personne ("tu es intelligent").
- **En pratique :** une rétroaction spécifique, tournée vers l'avant, actionnable, rattachée à l'objectif, délivrée tant qu'elle peut encore changer le comportement.
- **Ancre :** T5 (Notation et rétroaction).
- **Pertinence pour un assistant d'apprentissage IA :** un domaine peu couvert et à fort potentiel. La structure en trois questions est un gabarit net pour toute rétroaction formative générée par l'IA. Étroitement liée à S6 (l'étudiant qui reçoit une rétroaction et agit en conséquence fait de la métacognition).

### 4.14 Pratique réflexive , Schön (1983)

- **Ce qu'il dit :** les professionnels progressent en réfléchissant à la fois *pendant* l'action (réflexion en cours d'action) et *après* (réflexion sur l'action). L'amélioration vient du fait de rendre explicite le savoir tacite et de le questionner.
- **En pratique :** réflexion structurée en fin de cours, observation par les pairs, dialogue qualité alimentant l'itération suivante.
- **Ancre :** T6 (Évaluation et amélioration du cours).
- **Pertinence pour un assistant d'apprentissage IA :** l'image miroir de S6 (métacognition de l'étudiant) : même mécanisme réflexif, persona différent. Surtout un concept de cadrage, pas une source de fonctionnalités à court terme.

### 4.15 Communautés de pratique , Wenger (1998)

- **Ce qu'il dit :** les personnes qui partagent un métier apprennent en appartenant à un groupe qui le pratique ensemble. La croissance professionnelle passe par la participation, pas seulement par la formation formelle.
- **En pratique :** cercles d'observation entre pairs, communautés d'enseignants, portfolios partagés.
- **Ancre :** T7 (Développement professionnel).
- **Pertinence pour un assistant d'apprentissage IA :** le concept le plus éloigné du périmètre produit (croissance professionnelle de l'enseignant). Pertinent surtout comme modèle de collaboration entre les équipes qui construisent les outils, pas comme fonctionnalité destinée aux étudiants.

---

## 5. Lecture transversale

Quelques motifs à retenir pour la conception et les ateliers :

- **ICAP + théorie de l'autodétermination + ZPD sont les garde-fous.** Ensemble, ils justifient la décision de conception centrale : un assistant d'apprentissage IA doit donner des indices, pas des réponses finies. Tout cas d'usage qui pousse les étudiants vers le "Passif" (ICAP), leur retire le sentiment de compétence (autodétermination) ou fait s'effondrer la ZPD (Vygotsky) doit être écarté, si facile soit-il à construire.
- **La théorie de la charge cognitive est le concept-pont.** C'est le seul ancrage partagé par les deux personas (S2 + T2) et c'est le nom académique du problème fondateur de la plupart des outils d'apprentissage : une information dispersée équivaut à une charge superflue.
- **La densité conceptuelle signale l'opportunité.** Les domaines peu couverts par les outils existants et bien adaptés à un agent conversationnel, notamment S6 (contrôle métacognitif), S7 (autodétermination) et T5 (rétroaction efficace), sont les concepts à surpondérer lors de la génération de cas d'usage.
- **Les domaines saturés exigent un avantage de données ou de système, pas une méthode.** L'apprentissage actif (T3) et les cinq phases de l'évaluation (T4) occupent des domaines encombrés. Un assistant devrait y entrer par un avantage réel (connaissance du programme, intégration système, contenu validé, confidentialité), pas en concurrençant sur la seule méthode pédagogique.

---

## 6. Sources

Les définitions des concepts proviennent des sources primaires citées en ligne : Zimmerman (2000), Sweller (1988), Paivio (1971), Chi (2014), Collins, Brown & Newman (1989), Vygotsky (1978), Black & Wiliam (1998), Flavell (1979), Deci & Ryan (1985), Biggs (1996), Freeman et al. (2014), Hattie & Timperley (2007), Schön (1983), Wenger (1998).
