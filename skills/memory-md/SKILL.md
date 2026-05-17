---
name: memory-md
description: Use when creating, reviewing, updating, or deciding whether to consult a repository MEMORY.md file. Use when the user mentions MEMORY.md, asks to record a durable gotcha or taste preference, or when non-trivial debugging/design work may depend on prior repo context.
---

# MEMORY.md

Use `MEMORY.md` as a concise repository-local memory file. It is not automatically loaded, so check for it explicitly when prior project context may matter.

## When To Read

- Check whether `MEMORY.md` exists before non-trivial debugging, design work, workflow changes, or skill maintenance where past project choices may affect the answer.
- Treat a missing `MEMORY.md` as normal. Do not invent entries or assume the file exists.
- Use current repository evidence as the source of truth when memory and files disagree.

## When To Update

- Add an entry after a non-trivial error, discovery, or user preference only when it will help future work.
- Keep entries short, reusable, and grounded in the current repo.
- Do not add task logs, transient status, broad summaries, or speculative plans.

## Required Shape

- Keep exactly these top-level sections: `## GOTCHA` and `## TASTE`.
- Use `## GOTCHA` for traps, failure modes, commands that behave unexpectedly, and verified recovery steps.
- Use `## TASTE` for durable project or user preferences that shape future edits.
- Prefer one concise bullet per entry. If a similar entry already exists, revise it instead of adding a duplicate.

## Entry Pattern

For gotchas, capture the failure and the fix:

```markdown
- Symptom: <what went wrong>. Cause: <why>. Fix: <specific future action>.
```

For taste, capture the preference and its practical effect:

```markdown
- Prefer <choice> when <context>; avoid <alternative> because <reason>.
```
