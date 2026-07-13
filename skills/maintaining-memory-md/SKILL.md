---
name: maintaining-memory-md
description: Creates and maintains concise repository MEMORY.md notes for gotchas, stale memory corrections, and durable user preferences. Use at the start of repository conversations, when the user mentions MEMORY.md, when an error or preference should be remembered for future work, when MEMORY.md content may be wrong, or when the first qualifying memory emerges in a repository that has no MEMORY.md yet.
---

# MEMORY.md

Use `MEMORY.md` as a concise repository-local memory file. It is not automatically loaded, so check for it explicitly at the start of repository conversations and whenever prior project context may matter.

## When To Read

- At the start of a repository conversation, resolve the repository root, then check whether its `MEMORY.md` exists and skim it for relevant context before planning or editing. Do not create a competing file from a nested working directory.
- Check it again before non-trivial debugging, design work, workflow changes, or skill maintenance where past project choices may affect the answer.
- Treat a missing `MEMORY.md` as normal. Its absence alone is not a reason to create it.
- Use current repository evidence as the source of truth when memory and files disagree.

## When To Create

- During repository work, proactively notice qualifying memories even when the user does not explicitly ask to save them.
- A `GOTCHA` qualifies when repository evidence verifies a reusable trap or failure mode and its cause, recovery, or future avoidance step is known.
- A `TASTE` qualifies when the user expresses a durable preference that will change how future repository work should be performed.
- If the repository root has no `MEMORY.md`, the first qualifying entry emerges, and neither the user nor repository instructions prohibit the file, create `MEMORY.md` without asking for confirmation solely because it is missing. Create both required sections and put the entry under the correct one:

```markdown
## GOTCHA

## TASTE
```

- Create the file only when repository writes are permitted. In read-only or plan-only work, explicitly include the creation and entry in the next writable step instead of silently dropping the memory.
- Do not create `MEMORY.md` for transient status, task history, speculation, or sensitive material when no reusable sanitized lesson remains.

## When To Update

- Add or revise an entry after a qualifying mistake, discovery, or user preference when it will help future work avoid the same issue or preserve the preference.
- If an existing `MEMORY.md` entry is wrong, stale, contradicted by current evidence, or similar to the new memory, revise that entry instead of adding a conflicting or duplicate note.
- Keep entries short, reusable, and grounded in the current repo.
- Never store secrets or sensitive data in `MEMORY.md`, including credentials, tokens, API keys, cookies, private endpoints, proprietary/internal-only details, or sensitive personal data.
- When a gotcha or preference involves sensitive material, record only the sanitized lesson, not the secret or identifying detail.
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
