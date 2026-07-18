---
name: writing-plans
description: Draft, execute, and track lean, verifiable plans for non-trivial work. Use when the user asks for a plan, implementation plan, roadmap, design plan, migration plan, refactor plan, PR split, plan checklist, completion checklist, or execution of an existing plan; or when the task needs sequencing, tradeoffs, assumptions, unknowns, risk control, or completion criteria. Do not use for small, obvious tasks that can be completed directly.
---

# Writing Plans

## Purpose

Write plans that help an agent or engineer act, verify progress, and expose uncertainty. Keep the plan as small as the task allows.

## First Steps

1. Retrieve missing context before asking the user when local files, command output, or existing documentation can answer the question.
2. State assumptions and unknowns only when they affect execution or validation.
3. Ask at most one clarifying question if the plan would otherwise depend on a risky guess.
4. Prefer a short plan over a complete-looking template.

## File Output

When drafting a plan, save it to the repository unless the user explicitly requests chat-only output. When executing an existing saved plan, update that file in place.

Use `./docs/plans/` by default unless the user specifies another path. Name new plan files `YYYY-MM-DD_<topic>-plan.md`, where `<topic>` is a concise lowercase kebab-case stem, for example `2026-05-10_auth-migration-plan.md`.

Create `./docs/plans/` when needed. If the user does not specify a topic, derive it from the plan goal and report the resulting file path.

## Output Shape

Use this default structure, deleting optional sections that do not add value.

```markdown
## Goal
## Context (optional)
## Architecture (optional)
## Tech Stack (optional)
## Non-Goals (optional)
## Assumptions (optional)
## Unknowns (optional)
## Plan
## Risks (optional)
## Rollback / Recovery (optional)
## Completion Checklist
```

Always include `Goal`, `Plan`, and `Completion Checklist`.

## Section Rules

- `Goal`: Describe the intended outcome and success condition.
- `Context` (optional): Include only task-local background needed to understand the plan.
- `Architecture` (optional): Include when the work affects module boundaries, data flow, APIs, state management, deployment, permissions, storage, or ownership.
- `Tech Stack` (optional): Include when the work adds, removes, upgrades, or chooses tools, frameworks, packages, runtimes, databases, CI/CD, or cloud services.
- `Non-Goals` (optional): Name related work that is explicitly out of scope.
- `Assumptions` (optional): Name premises the plan depends on but can reasonably proceed with for now.
- `Unknowns` (optional): Name unanswered questions that could change the plan; convert each important unknown into an early discovery task or completion-check item.
- `Plan`: Use Markdown task list items (`- [ ]`) for actionable steps. Each task must be independently executable by an agent or engineer, with a clear object, expected result, and an executable acceptance method in the same task item, such as a command, file/path evidence, test result, review status, deployment state, or explicit user acceptance. Example: `- [ ] Update \`src/auth.ts\` to reject expired tokens; verify with \`npm test -- auth\`.` Prefer tasks that can map to a commit, PR slice, command, file change, investigation, or review step. Include dependencies between steps when order matters.
- `Risks` (optional): List risks that could break correctness, schedule, data integrity, UX, security, or maintainability.
- `Rollback / Recovery` (optional): Include when the work touches production data, releases, migrations, infrastructure, public APIs, or user-visible behavior.
- `Completion Checklist`: End every plan with finite Markdown task list items (`- [ ]`) that prove the whole work outcome is complete. Each item must be objectively checkable by code, docs, command output, test result, deployment state, review status, or explicit user acceptance. Each checklist item must include the verification method or evidence in the same item.

### Plan Task Item Template

Use this shape for `Plan` task list items when it helps keep acceptance explicit:

```markdown
- [ ] <action> <object> to produce <expected result>; verify with <command/evidence/user acceptance>.
```

### Completion Checklist Item Template

Use this shape for `Completion Checklist` items to prove the whole work outcome is complete:

```markdown
- [ ] <completed outcome> is verified by <command/evidence/user acceptance>.
```

## Planning Standards

- Keep task list items implementation-level when the user needs execution guidance.
- Keep task list items design-level when the user is choosing direction or scope.
- Split tasks that combine unrelated outcomes.
- Avoid vague verbs such as "handle", "improve", or "refactor" unless the object and expected result are concrete.
- Do not hide uncertainty inside plan steps.
- Do not add optional sections just to satisfy the template.
- Mention tradeoffs only when they affect a decision the user or implementer must make.
- Do not include open-ended completion checks such as "monitor forever", "keep improving", "ensure quality", or "handle edge cases"; convert them into bounded checks.
- End with `Completion Checklist`, not with open-ended commentary. If execution should begin immediately, put the next concrete action in the `Plan` task list.

## Execution Tracking

Use the plan as the live progress tracker during execution. Whenever a `Plan` task completes—sequentially or in parallel—confirm its stated acceptance method, then immediately change that item from `- [ ]` to `- [x]`. Update saved plans in place; for a chat-only plan, show the updated item in the next progress response.

Record supporting evidence in the item when it is not obvious from repository state. If verification fails or is unavailable, leave the item unchecked and report the blocker or missing evidence. Do not defer or batch checkbox updates.

Apply the same rule to each `Completion Checklist` item as soon as its required evidence is available. If later work invalidates that evidence, immediately change the item back to `- [ ]` and reverify it after the relevant work. For an inapplicable item, use `- [x] Not applicable: <reason>` rather than silently skipping it.

## Completion Review

Treat a plan as complete only when all of these are true:

1. Every required `Plan` task list item is checked or explicitly marked as not applicable using `- [x] Not applicable: <reason>`.
2. Every `Completion Checklist` item is checked, reverified after any work that could invalidate it, and has supporting evidence when the evidence is not obvious from repository state. Put evidence in the checklist item or in the completion review response, using commands, file paths, PR or review status, deployment state, or explicit user acceptance.
3. Any `Unknowns` that affected execution are resolved, converted into follow-up work, or explicitly accepted by the user.
4. Any unresolved `Risks` are documented as accepted, mitigated, or moved to follow-up work.
5. Required handoff, documentation, or release notes are completed when the plan calls for them.

Do not infer completion from implementation work alone. If evidence is missing, report which checks remain open instead of calling the plan complete.

At the end of a task that executes a saved plan, run the Completion Review only for the current plan. Do not inspect, update, or archive unrelated plan files merely because this skill was active.

When the current plan is complete, create `./docs/plans/archived/` if needed, archive that plan there immediately, and report the archived path. Do not archive if completion evidence is missing. If an archived file with the same name already exists, stop and report the conflict instead of overwriting.

## Useful Distinctions

Use these distinctions when deciding whether a section is needed:

```markdown
Non-Goal: Do not migrate historical records in this phase.
Assumption: Historical records can remain readable through the old schema.
Unknown: Do any reports require historical records in the new schema?
```
