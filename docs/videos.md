---
title: Videos
---

# Videos

Whiteboard explainers on what generative AI actually is, filmed in one take. **Spoken in French, no subtitles yet.**

They sit upstream of the rest of this knowledge base. Before you can judge whether an AI tool is helping your learning or doing it for you, you need a working model of what the tool does. A student who believes a chatbot "knows" things will misread every answer it gives, which makes S2 (Knowledge Acquisition) and S6 (Reflection & Metacognition) impossible to exercise honestly. See the [Domain Map](learning_science_concepts.md).

## Apprendre avec l'IA générative, mes méthodes

<video class="kaido-video" controls preload="none" poster="assets/video/apprendre-avec-lia-generative.jpg">
  <source src="assets/video/apprendre-avec-lia-generative.mp4" type="video/mp4">
  Your browser does not support the video tag.
  <a href="assets/video/apprendre-avec-lia-generative.mp4">Download the video</a>.
</video>

*23 min, French.*

A ground-up tour of the landscape:

- Where generative AI sits inside AI and machine learning, and what changed in October 2022.
- What an LLM does mechanically: next-token prediction, walked through on a sentence with the probability distribution written out. This is the part that dissolves the "it knows the answer" intuition.
- Who builds what: OpenAI / ChatGPT, Anthropic / Claude, Google / Gemini and NotebookLM, xAI / Grok, and the open-weight family (DeepSeek, Kimi, Mistral).
- Chatbot versus agent, tested on a question with a false premise. The chatbot answers from the distribution; the agent goes and checks, through web access and MCP.

**Where AI would steal the learning here:** asking a chatbot to summarise this video gives you a list of terms you can recite and cannot use. The mechanism only sticks if you predict the next token yourself before the video reveals the distribution.

## Différence entre agent IA et harnais

<video class="kaido-video" controls preload="none" poster="assets/video/agent-ia-et-harnais.jpg">
  <source src="assets/video/agent-ia-et-harnais.mp4" type="video/mp4">
  Your browser does not support the video tag.
  <a href="assets/video/agent-ia-et-harnais.mp4">Download the video</a>.
</video>

*5 min, French.*

One distinction, done properly: **the agent is a behaviour, the harness is the infrastructure.**

- The agentic loop: a goal goes in, the model reasons, calls tools (search, a shell in a container, producing a file), reads the result, and loops until the goal is met.
- The harness is what wraps the model and gives it those tools. Same model, different harness, different behaviour.
- Concretely: OpenAI ships Codex, Anthropic ships Claude Code, Google ships Gemini CLI and Antigravity.

**Why this matters for a course on learning:** "the AI got it wrong" is usually a harness question, not a model question. A student who cannot tell the two apart cannot debug their own tool use, and will generalise one bad experience into a rule about AI.

---

Model names and version numbers on the whiteboard reflect the state of things when the videos were filmed. That part ages in weeks. The mechanisms do not.
