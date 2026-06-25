# Learning Science Concepts , Domain Map Reference

> A standalone reference that explains the core educational-psychology concepts behind the learning journey, and maps each concept to the part of the journey it governs.
> Audience: anyone designing learning experiences or AI-assisted learning tools, and teams running pedagogy workshops.

---

## 1. How to read this file

The learning journey can be decomposed into 14 domains: 7 on the student side (S1:S7) and 7 on the lecturer side (T1:T7). Each domain is "anchored" by one or two learning-science concepts: the theory that explains *why* that domain matters and *what good looks like* there.

This file does the inverse mapping: it takes each concept, explains it in depth, and tells you which domain(s) it anchors and what it implies when you build an AI learning assistant. Use it to keep everyone on the same page when generating or filtering use cases.

**Reading legend:** S = student domain, T = lecturer domain. "Anchors" = the domain(s) where this concept is the named theoretical foundation.

---

## 2. The Domain Map

### Student journey (S1:S7)

| Domain | Title | What it covers |
|---|---|---|
| S1 | Orientation & Planning | Understanding what to learn and planning the path before learning starts |
| S2 | Knowledge Acquisition | Taking in new content and structuring it in one's own mind |
| S3 | Active Practice & Skill Building | Applying knowledge through projects, problems, fieldwork |
| S4 | Collaboration & Peer Learning | Learning with and from other students |
| S5 | Assessment & Self-Diagnosis | Checking what one knows before the official exam |
| S6 | Reflection & Metacognition | Thinking about one's own learning and adjusting |
| S7 | Wellbeing & Motivation | Managing motivation, anxiety, accessibility, engagement |

### Lecturer journey (T1:T7)

| Domain | Title | What it covers |
|---|---|---|
| T1 | Course Design | Shaping a course from outcomes to syllabus and assessment |
| T2 | Content Creation & Curation | Producing or curating slides, videos, readings, exercises |
| T3 | In-Class Facilitation | Running engaging sessions, in person, hybrid or online |
| T4 | Assessment Design | Designing exams that fairly measure learning outcomes |
| T5 | Grading & Feedback | Grading work and returning actionable feedback |
| T6 | Course Evaluation & Improvement | Gathering feedback on teaching and iterating |
| T7 | Professional Development | Growing one's own teaching practice over time |

---

## 3. Domain → Concept index (forward view)

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
| T4 | Assessment Design | Five Phases of Assessment |
| T5 | Grading & Feedback | Effective Feedback (Hattie & Timperley) |
| T6 | Course Evaluation & Improvement | Reflective Practice (Schön) |
| T7 | Professional Development | Communities of Practice (Wenger) |

---

## 4. Concept catalog (reverse view)

Each concept below follows the same structure: **origin → what it says → what it looks like in practice → anchors → relevance for an AI learning assistant.**

### 4.1 Self-Regulation / Goal-Setting , Zimmerman (2000)

- **What it says:** Learners who set specific goals, monitor their own progress, and adjust their strategies achieve more than those who do not. Self-regulation is a cycle (forethought → performance → self-reflection) and a *teachable* skill, not a fixed trait.
- **In practice:** Help learners translate a vague intention ("pass the exam") into concrete, monitored sub-goals ("finish module 3 readings by week 5, self-test on week 6").
- **Anchors:** S1 (Orientation & Planning).
- **Relevance for an AI learning assistant:** A natural entry point. An assistant that knows the curriculum, deadlines and course structure can scaffold goal-setting at the semester and study-path level, turning planning from a one-off into a monitored cycle.

### 4.2 Cognitive Load Theory , Sweller (1988)

- **What it says:** Learning is bounded by working memory. Three load types: **intrinsic** (inherent task difficulty), **extraneous** (friction added by poor design), **germane** (effort that actually builds long-term knowledge). Good design minimises extraneous load and protects germane load.
- **In practice:** Don't make learners hunt across many systems to assemble what they need ; don't overload a slide ; sequence content so prerequisites come first.
- **Anchors:** S2 (Knowledge Acquisition, learner side) and T2 (Content Creation & Curation, lecturer side).
- **Relevance for an AI learning assistant:** Scattered information *is* extraneous cognitive load. A single point of entry that retrieves the right validated content reduces exactly this load. Cross-persona: it helps learners absorb (S2) and lecturers curate (T2).

### 4.3 Dual Coding , Paivio (1971)

- **What it says:** Humans process information through two partly independent channels, verbal and visual. Well-chosen text *and* imagery together produce better recall and comprehension than text alone.
- **In practice:** Pair explanations with diagrams, concept maps, annotated figures rather than walls of prose.
- **Anchors:** S2 (Knowledge Acquisition).
- **Relevance for an AI learning assistant:** A lever whenever the assistant surfaces or generates learning material: pairing a textual explanation with a generated concept map or diagram improves retention over text alone.

### 4.4 ICAP Framework , Chi (2014)

- **What it says:** Classifies learning activities by cognitive depth: **I**nteractive > **C**onstructive > **A**ctive > **P**assive. The deeper the engagement, the more learning. Interactive (co-constructing with a partner) beats Constructive (generating something yourself) beats Active (manipulating given material) beats Passive (just receiving).
- **In practice:** A diagnostic lever for AI: it tells you *when AI assistance amplifies learning versus short-circuits it.* If AI does the constructive work for the learner, you have pushed them down to Passive.
- **Anchors:** S3 (Active Practice, the "C" / Constructive level) and S4 (Collaboration, the "I" / Interactive level).
- **Relevance for an AI learning assistant:** The pivotal design concept. It is the principled reason to give hints and counter-questions rather than finished answers. Use ICAP as a filter: a use case that drops learners to Passive should be rejected even if it is technically easy to build.

### 4.5 Cognitive Apprenticeship , Collins, Brown & Newman (1989)

- **What it says:** Teach complex cognitive skills by making expert thinking *visible*: modelling, coaching, scaffolding, articulation, reflection, fading. The expert externalises reasoning that is normally invisible.
- **In practice:** Show worked reasoning, then progressively withdraw support as the learner takes over (the "fading" step).
- **Anchors:** S3 (Active Practice & Skill Building).
- **Relevance for an AI learning assistant:** Maps onto a "tutor vs explainer" design and onto per-session query limits (scaffolding then fading). The assistant models reasoning, coaches, and steps back as competence grows.

### 4.6 Social Constructivism / Zone of Proximal Development , Vygotsky (1978)

- **What it says:** Knowledge is built through social interaction. The Zone of Proximal Development (ZPD) is the gap between what a learner can do alone and what they can do with help from a more capable peer or teacher: the band where the most productive learning happens.
- **In practice:** Peer teaching, structured group work, and well-calibrated hints (operating inside the ZPD, not above or below it).
- **Anchors:** S4 (Collaboration & Peer Learning).
- **Relevance for an AI learning assistant:** Frames the AI as a "more capable peer" operating in the ZPD: a useful framing, but also a caution. An over-helpful bot collapses the ZPD. Pairs with ICAP to justify hint-based tutoring over answer-giving.

### 4.7 Formative Assessment , Black & Wiliam (1998)

- **What it says:** Assessment used *during* learning to diagnose and adjust, not to judge. Tight teacher-learner feedback loops produce some of the largest measurable gains in learning outcomes in the whole education literature.
- **In practice:** Low-stakes quizzes, retrieval practice, live polling: each generating signal that changes what happens next.
- **Anchors:** S5 (Assessment & Self-Diagnosis).
- **Relevance for an AI learning assistant:** The learner-facing value is self-diagnosis ("test me on this module") grounded in validated, course-specific content, with the result steering what to study next.

### 4.8 Metacognitive Monitoring , Flavell (1979)

- **What it says:** Awareness of one's own thinking and learning ("do I actually understand this?"). Learners who monitor their comprehension learn more, because they catch their own misunderstandings before the exam does.
- **In practice:** Prompting learners to self-explain, predict their exam readiness, and identify what they *don't* know.
- **Anchors:** S6 (Reflection & Metacognition).
- **Relevance for an AI learning assistant:** A thinly served domain and a high-opportunity one. A conversational agent is naturally suited to metacognitive prompting ("explain this back to me", "where are you least confident?").

### 4.9 Self-Determination Theory , Deci & Ryan (1985)

- **What it says:** Sustained motivation rests on three basic psychological needs: **autonomy** (sense of choice), **competence** (feeling capable), and **relatedness** (connection to others). Support the three and you get engagement ; undermine them and you get dropout.
- **In practice:** Give learners meaningful choices, calibrate challenge to keep them feeling capable, and preserve human/social connection.
- **Anchors:** S7 (Wellbeing & Motivation).
- **Relevance for an AI learning assistant:** The retention lens. Long-term retention is downstream of whether the product satisfies autonomy, competence and relatedness. "Supportive, not prescriptive" is autonomy-support in plain words. Note the tension: too much AI undermines competence, because learners stop building the skill themselves.

### 4.10 Constructive Alignment , Biggs (1996)

- **What it says:** A course is well designed when intended learning outcomes, teaching activities, and assessment all target the same competencies. "State what they should learn, teach exactly that, then assess exactly that."
- **In practice:** Backward design from outcomes ; no activity or exam item that isn't tied to a stated outcome.
- **Anchors:** T1 (Course Design). The backbone running through S1, T1 and T4.
- **Relevance for an AI learning assistant:** The shared vocabulary for talking to lecturers. Framing the assistant's role inside their constructive-alignment chain (helping learners reach the stated outcomes, not bypass the assessment) is the credible pitch. Connects S1 (learner planning toward outcomes) to T4 (assessment of those outcomes).

### 4.11 Active Learning , Freeman et al. (2014)

- **What it says:** Meta-analytic evidence that students in active-learning conditions outperform those in passive lectures (lower fail rates, higher scores). "Active" means doing something during the session, not just listening.
- **In practice:** Replace stretches of lecturing with questions, problems, peer exchange, polling.
- **Anchors:** T3 (In-Class Facilitation).
- **Relevance for an AI learning assistant:** Largely the live-classroom domain, where live polling is the canonical active-learning tool. A crowded domain: an assistant should only enter where it adds a genuine system or data advantage, not compete on facilitation methods.

### 4.12 Five Phases of Assessment

- **What it says:** The full lifecycle of an assessment as an iterative process, not a one-off event: design → develop → deliver → grade → improve.
- **In practice:** Treat each exam as something to be quality-analysed and improved, with rubrics and item analysis feeding the next iteration.
- **Anchors:** T4 (Assessment Design).
- **Relevance for an AI learning assistant:** Mostly lecturer-facing, but relevant to the academic-integrity conversation (AI-aware assessment formats, open-book design). A crowded domain ; the narrow learner-facing angle is helping students practise against authentic formats.

### 4.13 Effective Feedback , Hattie & Timperley (2007)

- **What it says:** Feedback works best when it answers three questions: *Where am I going?* (goals), *How am I going?* (progress), *Where to next?* (next steps). Most powerful at the task and process levels ; least useful when aimed at the person ("you're smart").
- **In practice:** Specific, forward-looking, actionable feedback tied to the goal, delivered while it can still change behaviour.
- **Anchors:** T5 (Grading & Feedback).
- **Relevance for an AI learning assistant:** A thinly served, high-opportunity domain. The three-question structure is a clean template for any AI-generated formative feedback. Closely tied to S6 (the learner receiving and acting on feedback is doing metacognition).

### 4.14 Reflective Practice , Schön (1983)

- **What it says:** Professionals develop by reflecting both *during* action (reflection-in-action) and *after* (reflection-on-action). Improvement comes from making tacit knowledge explicit and questioning it.
- **In practice:** Structured post-course reflection, peer observation, quality dialogue feeding the next iteration.
- **Anchors:** T6 (Course Evaluation & Improvement).
- **Relevance for an AI learning assistant:** The mirror image of S6 (learner metacognition): same reflective mechanism, different persona. Mostly a framing concept, not a near-term feature source.

### 4.15 Communities of Practice , Wenger (1998)

- **What it says:** People who share a craft learn by belonging to a group that practises it together. Professional growth happens through participation, not only formal instruction.
- **In practice:** Peer observation circles, teaching communities, shared portfolios.
- **Anchors:** T7 (Professional Development).
- **Relevance for an AI learning assistant:** The most distal concept from product scope (lecturer professional growth). Relevant chiefly as the collaboration model between the teams building the tools, not as a learner-facing feature.

---

## 5. Cross-cutting reading

A few patterns worth carrying into design and workshops:

- **ICAP + SDT + ZPD are the guardrails.** Together they justify the core design decision: an AI learning assistant should give hints, not finished answers. Any use case that pushes learners to "Passive" (ICAP), removes their sense of competence (SDT), or collapses the ZPD (Vygotsky) should be filtered out, however easy it is to build.
- **Cognitive Load Theory is the bridge concept.** It is the only anchor shared across both personas (S2 + T2) and it is the academic name for the founding problem of most learning tools: scattered information equals extraneous load.
- **Concept density signals opportunity.** Domains thinly covered by existing tools and well matched to a conversational agent, notably S6 (Metacognitive Monitoring), S7 (SDT) and T5 (Effective Feedback), are the concepts to over-weight when generating use cases.
- **Saturated domains need a data or system advantage, not a method.** Active Learning (T3) and the Five Phases of Assessment (T4) sit in crowded domains. An assistant should enter through a genuine advantage (curriculum knowledge, system integration, validated content, privacy), not by competing on pedagogical method alone.

---

## 6. Sources

Concept definitions are drawn from the primary sources cited inline: Zimmerman (2000), Sweller (1988), Paivio (1971), Chi (2014), Collins, Brown & Newman (1989), Vygotsky (1978), Black & Wiliam (1998), Flavell (1979), Deci & Ryan (1985), Biggs (1996), Freeman et al. (2014), Hattie & Timperley (2007), Schön (1983), Wenger (1998).
