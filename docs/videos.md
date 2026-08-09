# Videos

Whiteboard explainers on what generative AI actually is, filmed in one take. **Spoken in French, with French subtitles** (enable them in the player controls).

They sit upstream of the rest of this knowledge base. Before you can judge whether an AI tool is helping your learning or doing it for you, you need a working model of what the tool does. A learner who believes a chatbot "knows" things will misread every answer it gives, which makes S2 (Knowledge Acquisition) and S6 (Reflection & Metacognition) impossible to exercise honestly. See the [Domain Map](learning_science_concepts.md).

## Apprendre avec l'IA générative, mes méthodes

<video class="kaido-video" controls preload="none" poster="assets/video/apprendre-avec-lia-generative.jpg">
  <source src="assets/video/apprendre-avec-lia-generative.mp4" type="video/mp4">
  <track kind="subtitles" src="assets/video/apprendre-avec-lia-generative.fr.vtt" srclang="fr" label="Français" default>
  Your browser does not support the video tag.
  <a href="assets/video/apprendre-avec-lia-generative.mp4">Download the video</a>.
</video>

*23 min, French.*

A ground-up tour, from AI to LLM to agent:

- **A first-hand account of the crutch effect.** Four years of a bachelor's degree with ChatGPT available, and the honest verdict on one habit: routinely having the model summarise scientific papers instead of reading them. The conclusion is not "AI is bad" but "the papers that matter have to be read, even when it hurts, because otherwise nothing remains." That is germane load being spent or skipped, described from the inside. See [Cognitive Load Theory](cognitive_load_theory.md).
- **Where generative AI sits** inside AI, machine learning and data science, and why October 2022 was the break: not the model, but the natural-language interface that made it usable by anyone who can string words together.
- **What an LLM does mechanically:** next-token prediction, walked through on "I'm in London and the sky is ...", with the probability distribution written out on the board. This is the part that dissolves the "it knows the answer" intuition, and it sets up the real lesson: what you put into the context determines what you get out.
- **Who builds what:** OpenAI / ChatGPT, Anthropic / Claude (Opus, Sonnet, Haiku), Google / Gemini and NotebookLM, xAI / Grok, plus the open-source and open-weight family. The distinction between open source and open weight is made properly, which is rarer than it should be.
- **Chatbot versus agent,** and the first sketch of the harness: a model at the centre, tooling around it.

**Where AI would steal the learning here:** having a chatbot summarise this video gives you a vocabulary you can recite and cannot use. The mechanism only sticks if you try to predict the distribution yourself, before the board reveals it.

## Différence entre agent IA et harnais

<video class="kaido-video" controls preload="none" poster="assets/video/agent-ia-et-harnais.jpg">
  <source src="assets/video/agent-ia-et-harnais.mp4" type="video/mp4">
  <track kind="subtitles" src="assets/video/agent-ia-et-harnais.fr.vtt" srclang="fr" label="Français" default>
  Your browser does not support the video tag.
  <a href="assets/video/agent-ia-et-harnais.mp4">Download the video</a>.
</video>

*5 min, French.*

One distinction, done properly: **the agent is a behaviour, the harness is the infrastructure.**

- The agentic loop: a goal goes in, the model reasons, draws up a task list, calls tools (web search, a shell, producing a file), reads the result, revises the list, and loops until the goal is met.
- The harness is the software layer that wraps the model and makes that possible. Same model, different harness, different behaviour.
- Concretely: Codex at OpenAI, Claude Code at Anthropic, Gemini CLI and Antigravity at Google, plus a growing set of open-source harnesses.

**Why this matters for a course on learning:** "the AI got it wrong" is usually a harness question, not a model question. A learner who cannot tell the two apart cannot debug their own tool use, and will generalise one bad experience into a rule about AI.

---

Subtitles were produced with a local speech-to-text model and lightly corrected for proper nouns. They are faithful to what was said, hesitations included.

Model names and version numbers on the whiteboard reflect the state of things when the videos were filmed. That part ages in weeks. The mechanisms do not.
