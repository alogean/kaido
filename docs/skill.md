# The Kaido Skill

Kaido is also packaged as a **portable skill**: a single instruction file that turns any capable AI assistant into a sound learning companion, grounded in the learning science on this site. It favors guided discovery over giving away answers, places each request on the Domain Map (S1:S7 / T1:T7), and reasons from mechanisms (cognitive load, retrieval, ICAP, metacognition) instead of opinion.

**The skill file:** [`skill/kaido/SKILL.md`](https://github.com/alogean/kaido/blob/main/skill/kaido/SKILL.md)
([raw / copy](https://raw.githubusercontent.com/alogean/kaido/main/skill/kaido/SKILL.md))

The file has two parts: a small YAML front matter (`name`, `description`) used by platforms that support native skills, and a Markdown body that works as a system prompt on any assistant. To install it, you either drop the file in a skills folder (Claude) or paste the **body** (everything after the second `---`) into a custom assistant (ChatGPT, Gemini).

---

## Add it to Claude

Claude supports skills natively, so you can use the file as-is.

=== "Claude Code (CLI / IDE)"

    Save the file to a skills directory and Claude loads it automatically:

    - Personal, all projects: `~/.claude/skills/kaido/SKILL.md`
    - One project only: `<project>/.claude/skills/kaido/SKILL.md`

    ```bash
    mkdir -p ~/.claude/skills/kaido
    curl -sL https://raw.githubusercontent.com/alogean/kaido/main/skill/kaido/SKILL.md \
      -o ~/.claude/skills/kaido/SKILL.md
    ```

    Start a new session, then ask Claude to "use the kaido skill" or just ask a learning question: it triggers from the `description`.

=== "Claude apps (claude.ai / Desktop)"

    1. Open **Settings , Capabilities , Skills**.
    2. Create a new skill and paste the contents of `SKILL.md` (or upload it as a folder / zip named `kaido`).
    3. Save. The skill activates automatically when your request matches its description, or you can invoke it by name.

---

## Add it to ChatGPT

ChatGPT has no native skill format, so use the skill **body** as instructions for a Custom GPT or a Project.

=== "Custom GPT (reusable)"

    1. Go to **Explore GPTs , Create**, then open the **Configure** tab.
    2. Paste the body of `SKILL.md` (skip the YAML front matter) into **Instructions**.
    3. Name it "Kaido" and, optionally, give it the one-line `description` as the GPT description.
    4. Save. Start a chat with that GPT to learn with it.

=== "Project (your account)"

    1. Create a **Project**.
    2. Open the project's **Instructions** and paste the body of `SKILL.md`.
    3. Every chat inside that project now follows the Kaido approach.

=== "Single chat"

    Paste the body of `SKILL.md` as your first message, prefixed with "Follow these instructions for the rest of this chat:". Good for a one-off session.

---

## Add it to Gemini

Use the skill body as a **Gem** or as system instructions.

=== "Gemini Gem (reusable)"

    1. In the Gemini app, open **Gems , New Gem** (Gem manager).
    2. Paste the body of `SKILL.md` into the instructions field.
    3. Name it "Kaido", save, and select it whenever you want to learn with it.

=== "Google AI Studio"

    1. Create a new prompt.
    2. Paste the body of `SKILL.md` into **System instructions**.
    3. Chat in the run panel, or grab the API snippet to use it in code.

---

## What "good" looks like once installed

- The assistant asks a quick diagnostic question before teaching, instead of dumping a full answer.
- It gives the smallest hint that unblocks you, then asks you to retrieve or predict.
- It ends by having you summarize or plan a spaced review.
- When it makes a factual claim, it flags how reliable the source is (🟢 / 🟠 / 🔴) and admits uncertainty rather than inventing references.

If the assistant just hands over answers with no retrieval or reflection, it is not following the skill: re-check that the full instructions were pasted.
