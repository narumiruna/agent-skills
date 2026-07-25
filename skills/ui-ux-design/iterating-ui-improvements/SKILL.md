---
name: iterating-ui-improvements
description: Iteratively audit and improve an existing web interface with Chrome DevTools by planning, implementing, validating, and locally committing one evidence-backed UI/UX improvement at a time. Use when the user wants an autonomous audit-fix-commit loop rather than a review or proposal alone.
---

# Iterating UI Improvements

Run a Chrome DevTools-driven audit-fix-commit loop against an existing web product. An explicit invocation authorizes in-scope local edits, validation, and local commits; it does not authorize remote or destructive actions.

## Establish the Run

Accept an optional URL, user flow, page scope, stopping mode, and iteration limit. Prefer invocation details. Otherwise inspect repository instructions, application documentation, configuration, existing start commands, tests, and design-system conventions to infer one local site and primary flow. Ask one question only when multiple targets remain plausible.

Require all of the following before changing files:

- a clean Git worktree, including no staged, unstaged, or untracked changes;
- an available Chrome DevTools capability and a reachable target that can be started through established non-interactive project commands;
- any required test, account, or authentication context already available without bypassing controls; and
- enough product evidence to preserve existing behavior, data meaning, permissions, recovery paths, and unrelated capability.

Stop and report the blocker when a prerequisite fails. Do not substitute another browser tool silently, guess credentials or product intent, or alter data to gain access.

## Choose the Stopping Mode

- **`substantial` (default):** continue while there is an evidence-backed, medium- or high-value problem affecting task completion, usability, or accessibility. Stop rather than pursue low-impact polish or subjective taste.
- **`exhaustive`:** also address low-impact UI problems when they are concrete, evidence-backed, and verifiable. Do not pursue unsupported subjective preferences.
- **`fixed N`:** run at most the specified positive number of successful iterations, stopping earlier when no substantial issue remains. Report known remaining findings when the limit is reached.

There is no iteration limit by default. A user may set a positive limit with any mode. Never interpret an omitted limit as five or another implicit cap.

## Run One Iteration

1. Use Chrome DevTools to reproduce the primary task and collect baseline evidence. As relevant to the target, inspect visual hierarchy, critical interactions, representative wide and narrow viewports, keyboard operation, semantic accessibility, and related console or network failures.
2. Rank findings by user impact, confidence, scope, and reversibility. Select one highest-value, coherent improvement theme that meets the active stopping mode. If none qualifies, stop without creating an empty commit.
3. Record the iteration plan in the execution log: observed evidence, user impact, exact change boundary, and acceptance checks. Do not add a plan file to the product repository.
4. Implement the smallest coherent improvement. Preserve unknown behavior, content and data semantics, permissions, cancellation and recovery, and unrelated features. Stop before a product decision or material scope expansion.
5. Run the repository's focused checks for the affected behavior. Re-verify the same flow and representative viewports in Chrome DevTools, confirming the improvement and checking for related interaction, responsive, accessibility, console, and network regressions.
6. Only after verification passes, stage only the paths changed for this iteration, inspect the staged diff, and create one focused Conventional Commit grounded in that diff. Verify the commit ID and a clean worktree before beginning another iteration.

Repeat from the observed post-commit interface rather than reusing stale findings.

## Handle Failure and Stop

If implementation cannot pass its checks within the current coherent scope, restore only the current iteration's uncommitted tracked changes and remove only files created during that iteration. Preserve every earlier successful commit. Do not reset, amend, rebase, or otherwise rewrite prior commits. If safe restoration cannot be proved or completed, stop and report the exact worktree state.

Stop when the active finding threshold is empty, a fixed or explicit limit is reached, Chrome DevTools or tests are blocked, a required product decision is missing, safe work would expand scope, or restoration fails. Do not push, open a pull request, deploy, mutate remote services, perform destructive data operations, or broaden the target without separate explicit authorization.

Report each iteration's plan, commit ID, and validation evidence, followed by the stopping reason and any known unaddressed findings. Distinguish verified outcomes from untested states or assumptions.
