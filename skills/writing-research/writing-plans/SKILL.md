---
name: writing-plans
description: Draft, execute, and track lean, verifiable implementation plans for non-trivial work involving sequencing, tradeoffs, assumptions, unknowns, risks, or completion criteria. Use for migrations, refactors, PR splits, task checklists, or execution of an existing plan; use writing-roadmap for strategic product or system direction and phased outcomes; skip small obvious tasks.
---

# Writing Plans

A plan request authorizes creating or revising the plan artifact, not implementing it. Execute only when the user requests execution or an active workflow already authorizes the planned work.

## Start

Inspect local evidence before asking a question. State only assumptions or unknowns that affect execution or validation, and ask at most one question when proceeding would otherwise require a risky guess.

Save a drafted plan to the repository unless the user requests chat-only output. Default to `docs/plans/YYYY-MM-DD_<topic>-plan.md`; derive a concise lowercase kebab-case topic and create the directory when needed. Update an existing plan in place during execution.

## Shape

Always include `Goal`, `Plan`, and `Completion Checklist`. Add only useful sections from:

```markdown
## Context
## Architecture
## Tech Stack
## Non-Goals
## Assumptions
## Unknowns
## Risks
## Rollback / Recovery
```

Use Architecture for boundaries, ownership, data flow, APIs, state, permissions, storage, or deployment. Use Tech Stack for tool/runtime/package choices. Include rollback/recovery for production data, migrations, infrastructure, releases, or public APIs.

## Plan Items

Use Markdown tasks. Each item must name one executable action, object, expected result, and acceptance evidence in the same item:

```markdown
- [ ] Update `src/auth.ts` to reject expired tokens; verify with `npm test -- auth`.
```

Order dependencies explicitly. Convert important unknowns into early discovery tasks. Avoid vague, combined, or open-ended items such as “improve quality,” “handle edge cases,” or “monitor forever.” End with finite completion checks proving the whole outcome through files, commands, tests, review/deployment state, or explicit user acceptance.

## Execution and Completion

- After each task's acceptance method passes, immediately change `- [ ]` to `- [x]` and add evidence when repository state does not make it obvious.
- Leave failed or unavailable checks open. Mark an inapplicable item `- [x] Not applicable: <reason>`.
- If later work invalidates evidence, reopen the item and reverify it.
- Track the current saved plan only; do not inspect or alter unrelated plans. For a chat-only plan, show each updated checkbox and its evidence in chat.

Complete only when every task and completion check is checked, important unknowns are resolved or explicitly accepted, risks are mitigated/accepted/moved to follow-up, and required handoff or release work is done. Do not infer completion from implementation alone.

After a complete execution of a saved plan, archive that plan under `docs/plans/archived/` and report the path. Do not create an archive file for a chat-only plan. Do not archive with missing evidence or overwrite an existing archived filename; stop and report that conflict.
