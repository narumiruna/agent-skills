---
name: writing-agents-md
description: Create, review, audit, migrate, or update scoped AGENTS.md repository guidance with evidence-backed commands, concise constraints, explicit authority, instruction precedence, and verifiable completion criteria.
---

# Writing AGENTS.md

Write the smallest repository guidance that gives an agent the context, constraints, authority, and evidence needed to finish work safely.

## Workflow

1. Resolve the target directory and all applicable `AGENTS.md` files. Explicit user instructions outrank repository guidance; the closest scoped file outranks ancestors. Default to one root file and add nested files only for genuinely different subproject rules.
2. Inspect current guidance, README/CONTRIBUTING, manifests, task files, CI, and relevant package docs. Verify paths and commands from executable configuration where possible; label unresolved facts instead of importing ecosystem conventions.
3. Identify generated, vendored, migration-sensitive, destructive, external, large-data, and ownership boundaries that materially change agent behavior.
4. Preserve correct project-specific rules and remove stale, repeated, speculative, generic, or misplaced content. Keep global rules in parents and local differences in children.
5. Verify every command and path, check the instruction chain for conflicts, run proportionate documentation or repository checks, and inspect the diff for duplication and scope growth.
6. For edits, report changed paths, purpose, checks, and caveats. For review, lead with concrete findings and replacement guidance.

## Instruction Design

- State outcome, relevant context, hard constraints, approval boundaries, and success criteria. Prescribe sequence only when order is operationally important.
- State each rule once at the narrowest scope. Use direct imperatives and concrete paths, commands, conditions, evidence, and stopping points.
- Keep examples only when they encode a project requirement or prevent a demonstrated mistake.
- When response length matters, say which facts, evidence, caveats, and next action must remain; trim repetition and generic background first.
- Define tone through observable choices rather than personality labels.
- Name ambiguities that require a question; do not add blanket approval requests for safe local work.

When action policy is needed, keep one compact block:

```text
For answer, explanation, review, diagnosis, or planning requests, inspect and report; do not implement unless asked.
For change, build, or fix requests, make bounded local changes and run relevant non-destructive checks.
Require confirmation for external writes, destructive or costly actions, and material scope expansion.
```

Adapt that policy to repository evidence. Name safe local actions and any domain-specific exception; do not scatter duplicates.

## Content and Tool Rules

Include only needed structure/scope, commands, code/test conventions, security/data constraints, and collaboration/release rules. Keep product positioning and human installation walkthroughs in human docs unless an agent needs a specific command.

Add orchestration guidance only for workflows the repository actually uses. For bounded automation, specify the stage, allowed tools, output/evidence schema, concurrency or retry limits, stopping condition, and the handoff to semantic judgment or approval. Avoid generic “use tools efficiently” rules.

In review mode, prioritize wrong commands, stale paths, conflicting scope, unsafe authority, and missing verification. Each finding needs severity, location, evidence, and a specific replacement. If no findings remain, say so and identify material evidence gaps.
