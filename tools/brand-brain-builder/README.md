# Brand Brain Builder

A copy-paste prompt that turns any business owner into a working brand Skill file.
They paste it into a fresh Claude chat, answer questions for 20-30 minutes, and walk
away with a `SKILL.md` that keeps every future chat sounding and looking like them.

## Files

| File | Use |
| --- | --- |
| `PROMPT.md` | The prompt. Hand this out as-is — select all, copy, paste into a new chat. |
| `SKILL-TEMPLATE.md` | The output shape the interview produces. Reference, not required by the prompt. |

## How to hand it out

1. Send them `PROMPT.md` (or the text of it).
2. They paste it into a new chat on claude.ai. Nothing else needs setting up first.
3. Claude runs the twelve-section interview, one section at a time, pushing back on
   anything generic.
4. Claude summarises what it captured, they correct it, Claude writes and zips the skill.

## Installing the finished skill on claude.ai

1. Turn on file creation once, in `Settings -> Capabilities`.
2. Go to `Customize -> Skills`, click `+`, then `Create skill -> Upload a skill`.
3. Upload the zip. Claude checks it for the `SKILL.md` file automatically.

## Using it in Claude Code

Drop the unzipped folder into `.claude/skills/` in a project, or into
`~/.claude/skills/` to have it available everywhere.

## What the prompt enforces

- One section at a time, three or four questions, then it waits.
- The competitor test: if a rival could publish the same sentence unchanged, it
  isn't an answer yet and the owner gets asked again.
- No invention. Anything the owner didn't say stays out of the file.
- Every "Avoid" in the tone of voice section carries an example sentence, so the
  rule is checkable rather than decorative.
- A review step before the file is written.
