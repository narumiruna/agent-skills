---
name: writing-agents-md
description: Create, review, audit, migrate, or update scoped AGENTS.md files with clear rules, verified commands, action limits, instruction order, and checks that prove the work is done.
---

# Writing AGENTS.md

Write the shortest useful repository guide.
Give the agent the context, limits, authority, and evidence needed to finish the work safely.

## Workflow

- Find the target directory and every `AGENTS.md` file that applies to it.
  - Follow explicit user instructions before repository instructions.
  - Follow the closest scoped file before its parent files.
  - Use one root file by default.
  - Add nested files only when a subproject needs different rules.
- Inspect the current guidance, human docs, configuration, task files, CI, and relevant package docs.
  - Verify commands and paths from files that tools can run or read.
  - Find files that are generated or copied from elsewhere.
  - Find risky migrations, destructive steps, external actions, large data, and ownership rules that change how the agent should work.
- Keep only correct, project-specific rules.
  - Remove stale, repeated, guessed, generic, or misplaced content.
  - Keep shared rules in parent files and local differences in child files.
- Check the instruction chain for conflicts.
  - Run checks that match the size and risk of the change.
  - Inspect the diff for repeated rules or extra scope.
  - Label facts that you could not verify.
- For reviews, check wrong commands, stale paths, conflicting scope, unsafe permissions, and missing checks first.
  - Give each finding a severity, location, evidence, and replacement.
  - If no findings remain, say so and name any important missing evidence.

## Default Sections

Use these sections as a checklist when creating or restructuring an `AGENTS.md` file.
Check every unmarked section and preserve this relative order among the sections that remain.
Include a section only when it has verified guidance that an agent needs.
Omit it after inspection when no such guidance exists instead of leaving it empty or inventing rules.
Consider sections marked `[Optional]` only when they are relevant to the repository.
The `[Optional]` marker is a template annotation; remove it from headings included in the final file.

```markdown
## [Optional] Communication
## Documentation
## Code style
## Commands
## Boundaries
## [Optional] Security
## Testing
## [Optional] Project overview
## [Optional] Repository structure
## [Optional] Git and commits
```

## Writing Rules

- Write `AGENTS.md` in concise plain language, with one enforceable sentence on each line.
- State the outcome, useful context, hard limits, actions that need approval, and success criteria.
- Describe a sequence only when its order matters.
- State each rule once in the smallest scope where it belongs.
- Use direct wording and exact paths, commands, conditions, evidence, and stopping points.
- Include only the scope, commands, code and test conventions, security or data limits, and collaboration or release rules that an agent needs.
- Keep product descriptions and human walkthroughs in human docs.
- Keep examples or writing-style rules only when they encode a project requirement or prevent a demonstrated mistake.
- Name unclear points that require a question.
- Do not require blanket approval for safe local work.

When action policy is needed, keep one compact block:

```text
For answer, explanation, review, diagnosis, or planning requests, inspect the relevant materials and report the result.
Do not make changes unless the request asks for them.
For change, build, or fix requests, make the requested local changes and run relevant safe checks.
Ask before writing to external systems, taking destructive or costly actions, or greatly expanding the scope.
```

Adapt the policy to evidence from the repository.
Name safe local actions and project-specific exceptions.
Do not repeat the policy elsewhere.

Add automation rules only for workflows the repository uses.
For small automation workflows, define the stage, allowed tools, required evidence, limits, and stopping point.
State when judgment or approval must take over.
