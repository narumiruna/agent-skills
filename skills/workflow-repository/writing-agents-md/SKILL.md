---
name: writing-agents-md
description: Create, review, audit, migrate, or update scoped AGENTS.md repository guidance with evidence-backed commands, concise constraints, explicit authority, instruction precedence, and verifiable completion criteria.
---

# Writing AGENTS.md

Write the smallest repository guidance that gives an agent the context, constraints, authority, and evidence needed to finish work safely.

## Workflow

1. Resolve the target directory and applicable `AGENTS.md` chain. Explicit user instructions outrank repository guidance; the closest scoped file outranks ancestors. Default to one root file and add nested files only for genuinely different subproject rules.
2. Inspect current guidance, human docs, manifests, task files, CI, and relevant package docs. Verify commands and paths from executable configuration where possible, and identify generated, vendored, migration-sensitive, destructive, external, large-data, or ownership boundaries that change agent behavior.
3. Keep only correct project-specific rules. Remove stale, repeated, speculative, generic, or misplaced content; keep shared rules in parents and local differences in children.
4. Check the instruction chain for conflicts, run proportionate checks, and inspect the diff for duplication or scope growth. Label facts that remain unresolved.
5. For reviews, prioritize wrong commands, stale paths, conflicting scope, unsafe authority, and missing verification. Give each finding a severity, location, evidence, and replacement; if none remain, state that and note material evidence gaps.

## Writing Rules

- State the outcome, relevant context, hard constraints, approval boundaries, and success criteria. Prescribe sequence only when order matters.
- State each rule once at the narrowest scope. Use direct imperatives and concrete paths, commands, conditions, evidence, and stopping points.
- Include only agent-needed scope, commands, code/test conventions, security or data constraints, and collaboration or release rules. Keep product positioning and human walkthroughs in human docs.
- Keep examples or response-style rules only when they encode a project requirement or prevent a demonstrated mistake.
- Name ambiguities that require a question; do not require blanket approval for safe local work.

When action policy is needed, keep one compact block:

```text
For answer, explanation, review, diagnosis, or planning requests, inspect and report; do not implement unless asked.
For change, build, or fix requests, make bounded local changes and run relevant non-destructive checks.
Require confirmation for external writes, destructive or costly actions, and material scope expansion.
```

Adapt the policy to repository evidence, naming safe local actions and domain-specific exceptions without repeating it elsewhere.

Add orchestration rules only for workflows the repository uses. For bounded automation, define the stage, allowed tools, evidence, limits, stopping condition, and handoff to judgment or approval.
