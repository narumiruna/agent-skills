---
name: running-panel-review-loops
description: Run iterative multi-reviewer panels over a code diff, verify their findings, apply explicitly authorized fixes, and re-review the updated change until it passes or reaches a stopping condition. Use when the user asks for a panel loop, multi-model code-review consensus, or a review-fix-re-review cycle.
---

# Running Panel Review Loops

Treat reviewer output as claims to verify, not votes or instructions to apply blindly. Default to review-only when the user asks only for a panel review or consensus. Apply fixes only when the user explicitly requests implementation, fixes, or a review-fix cycle. Commit or push only when the user requests that action; never treat a requested local commit as push authorization.

## Establish the Run

1. Determine the exact diff, commit, branch, or pull request and its comparison base from repository context; do not assume `main`. Infer intended behavior from the request, tests, documentation, and affected callers.
2. Inspect repository instructions and worktree state. Preserve unrelated changes, and stop before editing if they overlap the reviewed paths or make attribution unsafe.
3. Confirm that at least two independent reviewer instances are available. For an explicitly multi-model request, require at least two distinct models; independent instances of one model are sufficient only for a generic panel request. Do not simulate a panel by inventing reviewers or presenting one review in multiple voices.
4. Accept user-supplied presets, score threshold, iteration cap, and review-only or review-fix mode. Accept a user-supplied panel size only when it is at least two. Reject a requested panel size below two and ask the user to raise it before starting. Otherwise use three reviewers, a first-round `code-review` preset, `adversarial` re-reviews, an 8.2/10 acceptance threshold, and a maximum of three iterations.

If the review target or requested mutation mode remains materially ambiguous, ask one focused question. A panel may inspect uncommitted work, but each round must identify the exact snapshot reviewed.

## Run One Iteration

1. Give every reviewer the same snapshot, intent, relevant constraints, and requested preset. Keep reviews independent until synthesis, and run them in parallel when the available mechanism supports safe concurrency.
2. Ask each reviewer for a 0–10 score, blocking-objection status, severity-ranked findings with concrete file or behavior evidence, and meaningful missing checks. A blocking issue must concern correctness, safety, security, data integrity, or another explicit acceptance requirement—not style preference.
3. Treat a missing or invalid score as a reviewer failure and retry one transient reviewer failure once. Continue with a disclosed partial panel only when at least two independent, valid scored reviews remain; otherwise stop without fabricating a score.
4. Normalize valid scores to the 0–10 scale, require at least two valid scored reviews before computing or applying the arithmetic mean, and report each included score. Synthesize agreements and disagreements, but never let an average score override a blocking issue.
5. Verify every actionable claim against the source, affected flow, tests, and executable checks where feasible. Resolve disagreements through evidence rather than majority vote. Label theoretical or unverified risks and do not change behavior solely to satisfy them.
6. In review-only mode, run focused checks appropriate to the complete reviewed snapshot and the repository gate when available, report the synthesis, and stop before edits. In review-fix mode, address only confirmed, in-scope findings. Add the smallest boundary or regression test when practical, apply the smallest coherent fix, then run those snapshot-level checks.
7. Re-review the complete updated diff in the next iteration. Do not reuse stale scores or count a check run against an earlier snapshot as evidence for the current one.

Do not churn on subjective non-blocking suggestions. Apply a non-blocking suggestion only when it is concrete, proportionate, behavior-preserving or requirement-backed, and improves verification or materially reduces risk.

## Accept and Stop

Accept only when all of the following hold for the current snapshot:

- the panel mean meets or exceeds the active threshold;
- no reviewer has a surviving blocking objection;
- synthesis and source verification reveal no blocking correctness, safety, security, or explicit-requirement issue; and
- checks appropriate to the complete reviewed snapshot pass.

Stop without lowering the bar when the iteration cap is reached, fewer than two independent reviewers remain, validation cannot run, a required product decision is missing, safe work would expand scope, or the same unverified concern repeats without new evidence. Report any residual findings and the exact blocker or cap reached.

Before a requested commit, stage only intended paths, inspect the staged diff, and create a focused commit grounded in that diff. Push only when explicitly authorized for the verified remote and refspec; report the commit ID and remote verification when applicable.

## Report

For each iteration, report the reviewed snapshot and preset, per-reviewer scores, panel mean, blocking status, consensus and disputed findings, changes made, and validation evidence. Finish with the stopping reason, accepted or residual risk, and any authorized commit or push result. Never claim panel consensus, test success, a commit, or a push without direct evidence.
