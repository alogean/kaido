# Learning Science Concepts , Domain Map Reference

> Companion to the Learning & Teaching Domain Map (memory/learning_teaching.md, section 11).
> Purpose: explain each educational-psychology concept used to anchor the Domain Map, and map it back to the student (S1:S7) and lecturer (T1:T7) domains it governs.
> Audience: workshop participants, lecturers being scouted, the AI Buddy / KlickerUZH / OLAT / Lehrentwicklung pilot teams.
> Created: 25 June 2026.

---

## 1. How to read this file

The Domain Map decomposes the learning journey into 14 domains: 7 for students (S1:S7) and 7 for lecturers (T1:T7). Each domain is "anchored" by one or two learning-science concepts: the theory that explains *why* that domain matters and *what good looks like* there.

This file does the inverse mapping: it takes each concept, explains it in depth, and tells you which domain(s) it anchors and what it implies for AI Buddy. Use it to keep everyone on the same page when generating or filtering use cases.

**Reading legend:** S = student domain, T = lecturer domain. "Anchors" = the domain(s) where this concept is the named theoretical foundation.

---

## 2. Domain → Concept index (forward view)

| Domain | Title | Anchoring concept(s) |
|---|---|---|
| S1 | Orientation & Planning | Self-Regulation / Goal-Setting (Zimmerman) |
| S2 | Knowledge Acquisition | Cognitive Load Theory (Sweller) ; Dual Coding (Paivio) |
| S3 | Active Practice & Skill Building | ICAP "C" Constructive (Chi) ; Cognitive Apprenticeship (Collins et al.) |
| S4 | Collaboration & Peer Learning | ICAP "I" Interactive (Chi) ; Social Constructivism / ZPD (Vygotsky) |
| S5 | Assessment & Self-Diagnosis | Formative Assessment (Black & Wiliam) |
| S6 | Reflection & Metacognition | Metacognitive Monitoring (Flavell) |
| S7 | Wellbeing & Motivation | Self-Determination Theory (Deci & Ryan) |
| T1 | Course Design | Constructive Alignment (Biggs) |
| T2 | Content Creation & Curation | Cognitive Load Theory (Sweller) |
| T3 | In-Class Facilitation | Active Learning (Freeman et al.) |
| T4 | Assessment Design | Five Phases of Assessment (Teaching Tools framework) |
| T5 | Grading & Feedback | Effective Feedback (Hattie & Timperley) |
| T6 | Course Evaluation & Improvement | Reflective Practice (Schön) |
| T7 | Professional Development | Communities of Practice (Wenger) |

---

## 3. Concept catalog (reverse view)

Each concept below follows the same structure: **origin → what it says → what it looks like in practice → anchors → AI Buddy relevance.**

### 3.1 Self-Regulation / Goal-Setting , Zimmerman (2000)

- **What it says:** Learners who set specific goals, monitor their own progress, and adjust their strategies achieve more than those who do not. Self-regulation is a cycle (forethought → performance → self-reflection) and a *teachable* skill, not a fixed trait.
- **In practice:** Help students translate a vague intention ("pass the exam") into concrete, monitored sub-goals ("finish module 3 readings by week 5, self-test on week 6").
- **Anchors:** S1 (Orientation & Planning).
- **AI Buddy relevance:** This is the most natural student-side entry point. AI Buddy already holds the UZH-specific data (regulations, VVZ course structure, deadlines) needed to scaffold goal-setting at the *semester and study-path* level: something ChatGPT cannot do because it has no UZH context. Strong fit with the F1 (UZH knowledge) differentiator filter.

### 3.2 Cognitive Load Theory , Sweller (1988)

- **What it says:** Learning is bounded by working memory. Three load types: **intrinsic** (inherent task difficulty), **extraneous** (friction added by poor design), **germane** (effort that actually builds long-term knowledge). Good design minimises extraneous load and protects germane load.
- **In practice:** Don't make students hunt across OLAT, VVZ and slides to assemble what they need ; don't overload a slide ; sequence content so prerequisites come first.
- **Anchors:** S2 (Knowledge Acquisition, student side) and T2 (Content Creation & Curation, lecturer side).
- **AI Buddy relevance:** The "scattered information" business problem *is* extraneous cognitive load. A single point of entry that retrieves the right validated content reduces exactly this load. Cross-persona: it helps students absorb (S2) and lecturers curate (T2).

### 3.3 Dual Coding , Paivio (1971)

- **What it says:** Humans process information through two partly independent channels, verbal and visual. Well-chosen text *and* imagery together produce better recall and comprehension than text alone.
- **In practice:** Pair explanations with diagrams, concept maps, annotated figures rather than walls of prose.
- **Anchors:** S2 (Knowledge Acquisition).
- **AI Buddy relevance:** Secondary anchor of S2, more relevant to content presentation than to retrieval. A lever if AI Buddy ever surfaces course material (e.g. generating a concept map from validated content via the Klicker MCP), less central to the current admin/retrieval core.

### 3.4 ICAP Framework , Chi (2014)

- **What it says:** Classifies learning activities by cognitive depth: **I**nteractive > **C**onstructive > **A**ctive > **P**assive. The deeper the engagement, the more learning. Interactive (co-constructing with a partner) beats Constructive (generating something yourself) beats Active (manipulating given material) beats Passive (just receiving).
- **In practice:** A diagnostic lever for AI: it tells you *when AI assistance amplifies learning versus short-circuits it.* If AI does the constructive work for the student, you have pushed them down to Passive.
- **Anchors:** S3 (Active Practice, the "C" / Constructive level) and S4 (Collaboration, the "I" / Interactive level).
- **AI Buddy relevance:** This is the pivotal concept for the whole learning pivot. It is the principled reason the project triages didactics to OLAT/Klicker (guided discovery, hints not answers, D13) rather than answering for the student. Use ICAP as the test in the differentiation filter: a use case that drops students to Passive should be rejected even if technically easy.

### 3.5 Cognitive Apprenticeship , Collins, Brown & Newman (1989)

- **What it says:** Teach complex cognitive skills by making expert thinking *visible*: modelling, coaching, scaffolding, articulation, reflection, fading. The expert externalises reasoning that is normally invisible.
- **In practice:** Show worked reasoning, then progressively withdraw support as the learner takes over (the "fading" step).
- **Anchors:** S3 (Active Practice & Skill Building).
- **AI Buddy relevance:** Maps directly onto the KlickerUZH "Tutor vs Explainer" modes and the per-session query limits (scaffolding then fading). Reinforces that the tutoring layer belongs in Klicker/OLAT, with AI Buddy as the entry/triage point.

### 3.6 Social Constructivism / Zone of Proximal Development , Vygotsky (1978)

- **What it says:** Knowledge is built through social interaction. The Zone of Proximal Development (ZPD) is the gap between what a learner can do alone and what they can do with help from a more capable peer or teacher: the band where the most productive learning happens.
- **In practice:** Peer teaching, structured group work, and well-calibrated hints (operating inside the ZPD, not above or below it).
- **Anchors:** S4 (Collaboration & Peer Learning).
- **AI Buddy relevance:** Frames the AI as a "more capable peer" operating in the ZPD: useful framing, but also a caution. An over-helpful bot collapses the ZPD. Pairs with ICAP to justify hint-based tutoring over answer-giving.

### 3.7 Formative Assessment , Black & Wiliam (1998)

- **What it says:** Assessment used *during* learning to diagnose and adjust, not to judge. Tight teacher-learner feedback loops produce some of the largest measurable gains in learning outcomes in the whole education literature.
- **In practice:** Low-stakes quizzes, retrieval practice, live polling: each generating signal that changes what happens next.
- **Anchors:** S5 (Assessment & Self-Diagnosis).
- **AI Buddy relevance:** KlickerUZH is purpose-built here (live polling, question pools). For AI Buddy, the student-facing value is self-diagnosis ("test me on this module") grounded in validated, course-specific content. Strong fit if/when course content is reachable via the Klicker MCP for HS26.

### 3.8 Metacognitive Monitoring , Flavell (1979)

- **What it says:** Awareness of one's own thinking and learning ("do I actually understand this?"). Students who monitor their comprehension learn more, because they catch their own misunderstandings before the exam does.
- **In practice:** Prompting students to self-explain, predict their exam readiness, and identify what they *don't* know.
- **Anchors:** S6 (Reflection & Metacognition).
- **AI Buddy relevance:** S6 is a white-space domain (only 4 tools): high differentiation opportunity. A conversational agent is naturally suited to metacognitive prompting ("explain this back to me", "where are you least confident?"). Worth flagging as an underserved area in the workshop.

### 3.9 Self-Determination Theory , Deci & Ryan (1985)

- **What it says:** Sustained motivation rests on three basic psychological needs: **autonomy** (sense of choice), **competence** (feeling capable), and **relatedness** (connection to others). Support the three and you get engagement ; undermine them and you get dropout.
- **In practice:** Give students meaningful choices, calibrate challenge to keep them feeling capable, and preserve human/social connection.
- **Anchors:** S7 (Wellbeing & Motivation). Also one of the three educational-psychology pillars of the workshop (section 11.2).
- **AI Buddy relevance:** The retention lens (R13). D+7 / D+30 retention is downstream of whether the product satisfies autonomy/competence/relatedness. Also the value frame: "supportive, not prescriptive" is SDT-autonomy in plain words. Note the tension flagged in the persona map: too much AI undermines competence (students stop building the skill themselves).

### 3.10 Constructive Alignment , Biggs (1996)

- **What it says:** A course is well designed when intended learning outcomes, teaching activities, and assessment all target the same competencies. "State what they should learn, teach exactly that, then assess exactly that."
- **In practice:** Backward design from outcomes ; no activity or exam item that isn't tied to a stated outcome.
- **Anchors:** T1 (Course Design). Also a workshop pillar (section 11.2) and the backbone running through S1, T1, T4.
- **AI Buddy relevance:** The shared vocabulary for talking to lecturers. When scouting, framing AI Buddy's role inside their constructive-alignment chain (helping students reach the stated outcomes, not bypass the assessment) is the credible pitch. Connects S1 (student planning toward outcomes) to T4 (assessment of those outcomes).

### 3.11 Active Learning , Freeman et al. (2014)

- **What it says:** Meta-analytic evidence that students in active-learning conditions outperform those in passive lectures (lower fail rates, higher scores). "Active" means doing something during the session, not just listening.
- **In practice:** Replace stretches of lecturing with questions, problems, peer exchange, polling.
- **Anchors:** T3 (In-Class Facilitation).
- **AI Buddy relevance:** Largely the live-classroom domain owned by KlickerUZH (live polling is the canonical active-learning tool). T3 is a saturated domain (27 tools): AI Buddy should only enter where it adds a genuine system/data advantage, not compete on facilitation methods.

### 3.12 Five Phases of Assessment , Teaching Tools framework

- **What it says:** The full lifecycle of an assessment as an iterative process, not a one-off event: design → develop → deliver → grade → improve.
- **In practice:** Treat each exam as something to be quality-analysed and improved, with rubrics and item analysis feeding the next iteration.
- **Anchors:** T4 (Assessment Design).
- **AI Buddy relevance:** Mostly lecturer-facing and out of AI Buddy's student scope, but relevant to the academic-integrity conversation (AI-aware assessment formats, open-book design). T4 is saturated (24 tools) ; AI Buddy's angle here is narrow (e.g. helping students practise against authentic formats), not building assessment-design tooling.

### 3.13 Effective Feedback , Hattie & Timperley (2007)

- **What it says:** Feedback works best when it answers three questions: *Where am I going?* (goals), *How am I going?* (progress), *Where to next?* (next steps). Most powerful at the task and process levels ; least useful when aimed at the person ("you're smart").
- **In practice:** Specific, forward-looking, actionable feedback tied to the goal, delivered while it can still change behaviour.
- **Anchors:** T5 (Grading & Feedback).
- **AI Buddy relevance:** T5 is a white-space domain (only 5 tools): high opportunity. The three-question structure is a clean template for any AI-generated formative feedback. Closely tied to S6 (the student receiving and acting on feedback is doing metacognition).

### 3.14 Reflective Practice , Schön (1983)

- **What it says:** Professionals develop by reflecting both *during* action (reflection-in-action) and *after* (reflection-on-action). Improvement comes from making tacit knowledge explicit and questioning it.
- **In practice:** Structured post-course reflection, peer observation, quality dialogue feeding the next iteration.
- **Anchors:** T6 (Course Evaluation & Improvement).
- **AI Buddy relevance:** Lecturer-facing and largely outside AI Buddy's student scope. Mirror image of S6 (student metacognition): same reflective mechanism, different persona. Mostly a framing concept here, not a near-term use-case source.

### 3.15 Communities of Practice , Wenger (1998)

- **What it says:** People who share a craft learn by belonging to a group that practises it together. Professional growth happens through participation, not only formal instruction.
- **In practice:** Peer observation circles, teaching communities, shared portfolios.
- **Anchors:** T7 (Professional Development).
- **AI Buddy relevance:** The most distal concept from AI Buddy's product scope (lecturer professional growth). T7 is the sparsest domain (3 tools). Relevant chiefly as the collaboration model *between the pilot partners themselves* (AI Buddy, OLAT, KlickerUZH, Lehrentwicklung as a community of practice), not as a student-facing feature.

---

## 4. Cross-cutting reading for the pilot

A few patterns worth carrying into the workshop and lecturer scouting:

- **ICAP + SDT + ZPD are the guardrails of the whole learning pivot.** Together they justify the core design decision (D13): AI Buddy triages, didactics give hints not answers. Any use case that pushes students to "Passive" (ICAP), removes their sense of competence (SDT), or collapses the ZPD (Vygotsky) should be filtered out, however easy it is to build.
- **Cognitive Load Theory is the bridge concept.** It is the only anchor shared across personas (S2 + T2) and it is also the academic name for AI Buddy's founding business problem (scattered information = extraneous load). It is the cleanest line from "what we already do well" to learning science.
- **Concept density signals opportunity (cf. white-space, section 11.6).** The student-side white-space domains S6 (Metacognitive Monitoring) and S7 (SDT), plus lecturer-side T5 (Effective Feedback), are thinly covered by existing tools *and* well-matched to a conversational agent. These are the concepts to over-weight when generating use cases.
- **Saturated domains need a data/system advantage, not a method.** Active Learning (T3) and Five Phases of Assessment (T4) sit in crowded domains. AI Buddy should only enter through a genuine F1:F4 differentiator (UZH knowledge, system integration, validated content, privacy), never by competing on pedagogical method alone.

---

## 5. Provenance

All concept definitions are expanded from the glossary in memory/learning_teaching.md, section 11.7, which cites the primary sources above. Domain anchors are taken verbatim from the Domain Map (section 11.4 for S1:S7, section 11.5 for T1:T7). The differentiation filters (F1:F4) and white-space signals referenced here are defined in sections 11.3 and 11.6 of the same file.
