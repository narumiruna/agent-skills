---
name: maintaining-memory-md
description: Read and maintain concise repository-root MEMORY.md notes for verified gotchas and durable user preferences. Use at repository-conversation start, when MEMORY.md is mentioned or may be stale, or when a qualifying memory emerges.
---

# Maintaining MEMORY.md

Resolve the repository root and inspect `MEMORY.md` at the start of repository work and before non-trivial debugging, design, workflow, or skill maintenance. Missing memory is normal. Current repository evidence always overrides it.

## Qualifying Entries

- **GOTCHA:** repository evidence proves a reusable trap or failure mode and its cause, recovery, or avoidance is known.
- **TASTE:** the user expresses a durable preference that will change future repository work.

Do not record transient status, task history, broad summaries, speculation, or secrets. Sanitize any reusable lesson involving credentials, tokens, private endpoints, proprietary data, or personal information.

## Create or Update

- Do not create `MEMORY.md` merely because it is absent.
- When the first qualifying entry emerges and repository writes are authorized, create the root file without asking solely about its absence. In read-only or plan-only work, carry the entry into the next authorized write step.
- Keep exactly these top-level sections:

```markdown
## GOTCHA

## TASTE
```

- Add one concise bullet under the matching section. Revise a similar, stale, wrong, or contradicted entry instead of appending a duplicate.
- Keep entries grounded in reusable repository behavior:

```markdown
- Symptom: <failure>. Cause: <reason>. Fix: <future action>.
- Prefer <choice> when <context>; avoid <alternative> because <reason>.
```

After editing, reread the file to verify both headings, placement, deduplication, and absence of sensitive or task-log content. Report the entry created or revised; do not claim memory was updated when writes were unavailable.
