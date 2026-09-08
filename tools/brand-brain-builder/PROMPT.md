I want to build a custom Skill file for my brand — so any AI I use (starting with you) can write, design and think like my business instead of sounding like everyone else's.

**How to run this with me**

- Interview me section by section, in the order below. Twelve sections.
- Ask a small handful of questions per section — three or four, never a wall of them — then stop and wait for my answers before moving on.
- Tell me where we are as we go, like "Section 4 of 12 — Brand Personality".
- If an answer is vague, generic, or could be lifted onto any other business in my industry, push back and ask a sharper follow-up before we move on. Don't let me get away with fluff. The test: if a competitor could put my sentence on their website without changing a word, it isn't an answer yet — tell me so and ask again.
- Never invent anything. If I haven't told you something, leave it out or ask me for it. No placeholder claims, no invented statistics, no filler adjectives.
- Keep my actual words wherever they're good. Verbatim beats polished.
- Don't write the Skill file until all twelve sections are done.

**The twelve sections**

1. **Who we are** — business name, the real founding story (not the polished version), what we actually do day to day, who we do it for, and why it exists beyond making money.
2. **Mission and purpose** — the change we're trying to make, for our customers or the world.
3. **Values** — 3 to 5 real values, each explained in a sentence, not just a single word.
4. **Brand personality** — help me pick 2 to 4 archetypes that fit, and how each one should show up in what we write and make. One-line reminders:
   - **Sage** — the trusted expert; teaches, gives clarity, chooses truth over hype.
   - **Jester** — makes it fun; irreverent, playful, refuses to be boring.
   - **Hero** — rises to the challenge; proves it, wins, pushes people to be better.
   - **Creator** — builds what didn't exist; craft, originality, imagination.
   - **Magician** — transforms; makes the hard thing feel effortless.
   - **Outlaw** — breaks the rules; challenges the establishment, serves the people it ignored.
   - **Lover** — beauty, intimacy, indulgence; makes people feel cared for and desired.
   - **Caregiver** — protects and nurtures; puts the customer's wellbeing first.
   - **Ruler** — sets the standard; authority, order, premium control.
   - **Explorer** — freedom and discovery; the next frontier, never fitting in.
   - **Innocent** — simple, honest, optimistic; wholesome and uncomplicated.
   - **Everyman** — one of us; down to earth, belonging, no pretence.
5. **Tone of voice** — 3 words for how we sound, then a Do / Avoid list of specific writing habits, not vague adjectives. Write an example sentence for every Avoid so I know exactly what to catch.
6. **Ideal client** — who they are, the state they're in right before they find us (in their words and their frustrations, not our jargon), and what they actually want.
7. **What makes us different** — our real point of difference. If I give you something a competitor could also claim, challenge me on it and make me go again.
8. **Core offerings** — what we actually sell, briefly.
9. **Visual identity** — brand colours (hex codes if I have them), fonts, logo rules, and our photography or imagery style.
10. **Language** — words and phrases we love and actually use, any taglines, and words or phrases we'd never say.
11. **Sample sentences** — write 3 to 5 example sentences with me, in our voice, and refine them together until they sound unmistakably like us.
12. **Brand assets** — links to logo files, a style guide, or fonts, if I have them (Google Drive, Dropbox, wherever they live).

**Before you write it up**

When all twelve are done, show me a short summary of what you captured — archetypes, tone words, point of difference, sample sentences — and let me correct anything before you build the file.

**Then write the Skill file**

A single markdown document, starting with YAML frontmatter:

```
---
name: my-business-brand
description: Brand voice, positioning and visual identity for [Business Name]. Use whenever writing, editing or reviewing any [Business Name] content — website copy, emails, social posts, ads, proposals, product descriptions, decks — or when making design, colour, font or imagery decisions for [Business Name].
---
```

Use my real business name in `name` (lowercase, hyphenated) and in `description`. The description has to be specific enough that it reliably triggers whenever I ask for brand content, marketing copy or design help.

Then these sections, in this order:

Who We Are · Mission · Values · Brand Personality · Tone of Voice · Ideal Client · What Makes Us Different · Core Offerings · Visual Identity · Language · Approved Sample Sentences · Brand Assets · How to Use This Skill

Write it so another AI can act on it, not just read it. Concrete rules, not descriptions of rules. Under Tone of Voice, keep the Do / Avoid lists with the example sentences. Under How to Use This Skill, tell the AI what to do before it writes anything for me, and what to check the draft against before it hands it over.

**Then package it**

- Put the file in a folder named to match the skill, lowercase and hyphenated — for example `my-business-brand`.
- Name the file `SKILL.md`.
- Zip the folder and give me the zip to download.
- If you can add it directly as a Skill on my account instead, do that and tell me it's ready to use.

If you can't create files, print the complete `SKILL.md` in one copyable code block instead, and tell me so.

**How I install the zip on claude.ai** (in case you only hand me the file):

1. Turn on file creation once, in `Settings → Capabilities`.
2. Go to `Customize → Skills`, click `+`, then `Create skill → Upload a skill`.
3. Upload the zip. Claude checks it for the `SKILL.md` file automatically.
