---
name: writing-agents-md
description: Create, review, audit, migrate, or update AGENTS.md files for repositories, packages, subprojects, and monorepos. Use when agent-facing repository guidance must be scoped, evidence-backed, concise, and explicit about commands, constraints, approval boundaries, verification, or instruction precedence.
---

# Writing AGENTS.md

Write lean, evidence-backed repository instructions that give agents the context, constraints, authority, and completion criteria they need.

## Workflow

1. Determine the request mode and authority.
   - For requests to answer, explain, review, diagnose, or plan, inspect relevant materials and report the result without editing files.
   - For requests to create, update, fix, or migrate guidance, make the requested in-scope local edits and run relevant non-destructive checks.
   - Require confirmation before external writes, destructive or costly actions, or a material expansion of scope.
   - Ask one focused question only when an unresolved ambiguity would materially change the result or authorization.

2. Resolve scope and precedence.
   - Identify the target directory and every `AGENTS.md` that applies to it.
   - Treat explicit user instructions as higher priority than repository guidance and the closest scoped `AGENTS.md` as higher priority than ancestor files.
   - Default to a root `AGENTS.md`. Add nested files only where subprojects need genuinely different rules.

3. Gather repository evidence.
   - Read current agent guidance, `README.md`, `CONTRIBUTING.md`, relevant package documentation, build manifests, task files, and CI configuration.
   - Inspect the tree for subprojects, generated or vendored content, large data, and directories with distinct workflows.
   - Verify commands from executable configuration or CI. Prefer those sources over prose when they conflict.
   - Label unresolved uncertainty briefly; do not turn ecosystem conventions into repository facts.

4. Draft or revise the smallest useful guidance.
   - Preserve correct project-specific rules and remove stale, repeated, speculative, or misplaced guidance.
   - Include only sections supported by the repository or an explicit user requirement.
   - Keep parent guidance global and child guidance local; do not repeat inherited rules.

5. Verify the result.
   - Confirm every path and command exists, or clearly label illustrative examples.
   - Check the applicable instruction chain for contradictions and missing precedence.
   - Run the repository's documented Markdown, documentation, or full verification gate when proportionate to the change.
   - Review the diff for duplicated rules, accidental scope growth, and unrelated edits.

6. Report completion.
   - For edits, summarize changed paths, the reason for the change, verification performed, and any unresolved caveat.
   - For reviews, lead with findings and include the evidence needed to act on them.

## Instruction Design

- State the desired outcome, relevant context, hard constraints, approval boundaries, and success criteria. Let the agent infer routine steps unless sequencing is operationally important.
- State each rule once. Consolidate repeated warnings and remove generic reminders that do not change behavior.
- Use direct imperatives with concrete paths, commands, conditions, and stopping points.
- When brevity matters, specify what the response must preserve and what it may omit instead of relying on vague instructions such as "be concise."
- Define tone through observable writing choices, such as leading with the conclusion or omitting generic sign-offs, rather than broad personality labels.
- Name the ambiguities that require a question; avoid blanket "ask first" rules for safe, expected local work.
- Keep examples only when they encode a project requirement or prevent a demonstrated mistake.

## Durable Autonomy Rules

When the repository needs an action policy, keep it in one compact section:

- Distinguish read-only work from authorized in-scope local changes.
- Name safe local actions that do not require confirmation, such as reading files, inspecting logs, editing requested paths, and running non-destructive checks.
- Require explicit approval for external writes, destructive actions, purchases or material cost, and scope expansion.
- Do not scatter overlapping approval rules across sections; repetition can cause unnecessary pauses or contradictory behavior.

## File and Scope Rules

- Name the file exactly `AGENTS.md` and use plain Markdown without YAML frontmatter.
- Use a clear repository-appropriate title and a scannable heading structure.
- Keep all required facts, decisions, caveats, and verification steps. Trim repetition, generic background, and optional examples first.
- Keep product positioning and human installation walkthroughs in human-facing documentation unless agents need a specific command to work or validate changes.
- Do not include secrets, credentials, private URLs, speculative claims, or instructions to bypass security checks.
- Mark generated, vendored, migration-sensitive, destructive, or externally managed areas that agents must not edit casually.

## Content Selection

Include only the categories the repository needs:

- **Structure and scope:** important directories, ownership boundaries, generated artifacts, and nested guidance.
- **Commands:** the smallest reliable setup, build, format, lint, typecheck, test, and CI-equivalent commands, including required working directories.
- **Code and tests:** enforceable naming, formatting, architecture, fixture, coverage, and targeted-test conventions.
- **Security and data:** secret handling, configuration examples, migrations, external services, large datasets, and safe dry-run or mock paths.
- **Collaboration:** evidence-backed commit conventions, pull-request requirements, screenshots, migration notes, deployments, and release constraints.

## Tool and Workflow Rules

- Add tool-routing instructions only for workflows the repository actually uses; omit generic directions such as "use tools efficiently."
- For bounded automation, identify the exact stage, allowed tools, required output or evidence, retry limit, and stopping condition.
- Keep semantic judgment, approval decisions, and final validation explicit when automation cannot safely decide them.

## Review Mode

Report concrete findings with severity, affected section or path, repository evidence, and a specific replacement. Prioritize incorrect commands, stale paths, unsafe instructions, conflicting scope, ambiguous authority, and missing verification. Use this order when useful: `Findings`, `Suggested edits`, `Verified evidence`, `Open questions`. If no findings remain, say so and identify any material area that could not be verified.

## Final Checks

- Every instruction is grounded in repository evidence or an explicit user requirement.
- Each rule appears once at the narrowest correct scope.
- Authorization boundaries distinguish safe local work from actions requiring confirmation.
- Commands, paths, precedence, validation, and completion criteria are concrete.
- The final file is concise because low-value content was removed, not because required detail was omitted.
