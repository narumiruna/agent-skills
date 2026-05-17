---
name: memory-md
description: Maintains concise repository MEMORY.md notes for gotchas, stale memory corrections, and durable user preferences. Use at the start of repository conversations, when the user mentions MEMORY.md, when an error should be remembered to avoid repeating it, or when MEMORY.md content may be wrong.
---

# MEMORY.md

Use `MEMORY.md` as a concise repository-local memory file. It is not automatically loaded, so check for it explicitly at the start of repository conversations and whenever prior project context may matter.

## When To Read

- At the start of a repository conversation, check whether `MEMORY.md` exists and skim it for relevant context before planning or editing.
- Check it again before non-trivial debugging, design work, workflow changes, or skill maintenance where past project choices may affect the answer.
- Treat a missing `MEMORY.md` as normal. Do not invent entries or assume the file exists.
- Use current repository evidence as the source of truth when memory and files disagree.

## When To Update

- Add or revise an entry after a mistake, discovery, or user preference when it will help avoid repeating the same issue.
- If an existing `MEMORY.md` entry is wrong, stale, or contradicted by current evidence, correct that entry instead of adding a conflicting note.
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

## Examples

- `GOTCHA`: command failed because a tool needed `UV_CACHE_DIR=/tmp/uv-cache`; record the symptom, cause, and future command pattern.
- `TASTE`: the user prefers thin skills with only `SKILL.md` unless supporting files solve a concrete problem.
- Do not record: "finished PR #12" or "ran tests today." Those are task logs, not reusable memory.
