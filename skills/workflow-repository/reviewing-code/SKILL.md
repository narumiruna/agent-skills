---
name: reviewing-code
description: Review code changes for correctness, maintainability, readability, security, performance, test coverage, and integration risk. Use when asked to inspect a diff, pull request, merge request, commit, patch, or source files; when fixes are also requested, hand confirmed edge-case and failure-mode findings to hardening-code-paths when available.
---

# Reviewing Code

Review the requested change, not the entire codebase. Prioritize correctness and production risk over surface style. Treat the review as read-only unless the user asks you to address findings.

## Scope and Evidence

1. Determine the review target and comparison base from the request and repository context.
   - For a branch or pull request, compare against the merge base of its target branch; do not assume the target is `main`.
   - For a commit, patch, staged change, or working tree, inspect the exact requested change.
   - When asked to audit whole source files rather than a change, state that broader scope explicitly.
2. Infer intended behavior from the request, issue or PR description, tests, documentation, and surrounding code. State a reasonable assumption when intent remains unclear.
3. Inspect the diff and enough related code to trace changed behavior through callers, downstream consumers, tests, and contracts.
4. Run focused tests or static checks when feasible. Passing checks are supporting evidence, not proof that the behavior is correct.
5. Keep the investigation proportional to the change. Stop when the relevant diff, directly affected callers and contracts, and focused checks provide enough evidence; report remaining uncertainty instead of expanding the scope indefinitely.
6. Clearly separate confirmed problems, inferred risks, and anything you could not verify.

Report findings introduced by the reviewed change or made materially worse or newly reachable by it. Keep unrelated pre-existing problems out of the main findings unless the user requested a broader audit; mention a directly relevant pre-existing problem separately and label it clearly.

## Hardening Handoff

Keep the review read-only unless the user explicitly asks to fix findings, harden the implementation, or review and improve the code.

When changes are authorized:

1. Follow this review workflow until the triggering edge-case or failure-mode finding is confirmed.
2. For each confirmed finding that needs bounded code-path hardening, load and follow the available `hardening-code-paths` skill for the affected flow.
3. Do not hand off speculative risks, preference-only comments, or unrelated findings.
4. Return to this workflow after hardening, inspect the resulting change, and report what was fixed, how it was verified, and any residual risk.

If `hardening-code-paths` is unavailable, keep the review read-only, report the confirmed finding and missing companion skill, and do not recreate its workflow here.

## Review Workflow

1. Check correctness and relevant edge cases first.
   - Trace logic, state changes, error handling, side effects, and boundary behavior.
   - Consider only plausible cases such as empty or malformed input, ordering assumptions, time or numeric boundaries, concurrency, retries, partial failure, authorization, and resource cleanup.
2. Check compatibility and integration.
   - Verify changed interfaces against existing callers and data formats.
   - Inspect relevant schemas, migrations, jobs, queues, caches, feature flags, permissions, configuration, and downstream behavior.
3. Check security and privacy.
   - Review trust boundaries, authentication, authorization, validation, secret handling, logging, injection, unsafe deserialization, dependencies, and sensitive-data exposure when relevant.
4. Check performance and resources.
   - Look for plausible repeated work, excessive I/O, N+1 queries, unsuitable data structures, blocking calls, leaks, and scalability regressions for the expected workload.
5. Check tests and maintainability.
   - Confirm tests cover the changed behavior, important error paths, and concrete regressions. Name exact missing cases without demanding excessive tests for trivial changes.
   - Raise naming, structure, duplication, abstraction, or complexity concerns only when they create a concrete maintenance cost or risk.

## Findings

Lead with findings, ordered by severity:

- Critical: must fix; enables severe security impact, data loss, or widespread production failure.
- Major: should fix before merge; causes important correctness, reliability, security, or maintainability risk.
- Minor: a real but low-risk problem worth correcting.

Each finding must include the file and line when available, the concrete triggering scenario, its impact, and an actionable fix. Do not invent context or report speculative risks without a plausible path to failure. Omit preference-only comments and nits unless the user explicitly asks for style or clarity feedback.

If there are no findings, say so directly and note any meaningful residual risk or verification gap. Add a short summary only when it helps explain a complex change. Discuss tests separately only when there is a specific coverage gap.

Give a merge recommendation only for a pull request, merge request, or explicit mergeability question. Use one conclusion: `Approve`, `Approve with minor comments`, `Request changes`, or `Needs more context`.
