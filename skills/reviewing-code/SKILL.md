---
name: reviewing-code
description: Use when reviewing code changes for correctness, maintainability, readability, security, performance, test coverage, and integration risk; especially when the user asks to inspect a diff, pull request, merge request, commit, patch, or source files.
---

# Reviewing Code

## Purpose

Review code changes from a senior engineer's perspective. Prioritize issues that affect correctness, maintainability, security, performance, testability, and production stability.

Do not focus only on surface style or formatting unless the user explicitly asks for that.

## Review Workflow

1. Understand the intended change.
   - Infer the intended behavior from the user request, diff, issue, PR/MR description, tests, and surrounding code.
   - If the intent is unclear, state your reasonable assumption.
   - Clearly separate confirmed problems, inferred risks, and things you cannot verify.

2. Check correctness first.
   - Look for logic errors, missing branches, boundary mistakes, off-by-one errors, state pollution, error-handling gaps, and unintended side effects.
   - Check whether the code handles empty inputs, single items, very large inputs, null, undefined, NaN, missing fields, and malformed data when relevant.
   - Verify changed interfaces remain compatible with existing callers.

3. Run an edge-case pass.
   - Every review must include a separate edge-case check; do not review only the happy path.
   - Consider only edge cases relevant to this change, such as:
     - empty input, single item, very large input
     - null, undefined, NaN, missing keys, malformed records
     - boundary values, inclusive/exclusive ranges, off-by-one behavior
     - duplicate values, unsorted input, hidden ordering assumptions
     - time zones, daylight saving time, date boundaries, clock skew
     - floating-point error, integer overflow, divide by zero
     - concurrent access, retries, idempotency, race conditions
     - partial failure, timeout, cancellation, rollback
     - backward compatibility, existing data formats, existing API contracts
     - permissions, ownership, tenant isolation, unauthorized access
     - resource cleanup, file handles, DB connections, locks, memory growth
   - Do not mechanically list every category. Report only edge cases that are plausible for the change.

4. Check integration risk.
   - Review API contracts, database schemas, migrations, background jobs, queues, caches, feature flags, permissions, and configuration when relevant.
   - Identify behavior that could affect existing users, downstream systems, or production operations.

5. Check security and privacy.
   - Review authentication, authorization, input validation, secret handling, logging, injection, unsafe deserialization, and sensitive-data exposure.
   - Flag high-risk dependencies, permission settings, and network behavior.

6. Check performance.
   - Look for unnecessary repeated work, excessive I/O, N+1 queries, unsuitable data structures, memory growth, blocking calls, and scalability issues.
   - Raise performance findings only when they are plausible for the expected workload.

7. Check tests.
   - Confirm tests cover the main behavior, edge cases, error paths, and regression cases.
   - If coverage is insufficient, name the exact test cases to add.
   - Do not demand excessive tests for trivial changes.

8. Check readability and maintainability.
   - Comment on naming, structure, duplication, abstraction level, or complexity only when it creates real maintenance cost or risk.
   - Avoid personal-preference comments. Tie each suggestion to a concrete risk or cost.

## Output Format

Unless the user asks for another format, use this structure.

### Summary

Briefly describe what the change appears to do and the overall risk level.

### Findings

List findings by severity:

- Critical: must fix before merge; can cause production failure, security issues, data loss, or severe correctness bugs.
- Major: should fix before merge; important correctness, reliability, or maintainability issue.
- Minor: useful but low-risk improvement.
- Nit: optional style or clarity suggestion.

Each finding should include:

- severity
- file and line number, when available
- problem description
- why it matters
- suggested fix

### Edge Cases

List relevant edge cases and mark each as one of:

- handled by the code
- covered by tests
- risky but acceptable
- missing; should be fixed

If you find no important edge-case gap, say so directly and list anything you still could not verify.

### Tests

State whether the existing tests are sufficient. If not, list the specific tests to add.

### Merge Recommendation

Use one conclusion:

- Approve
- Approve with minor comments
- Request changes
- Needs more context

## Review Standards

Feedback must be specific and actionable.

Prefer this style:

> Major — `src/foo.py:42`: This returns early when parsing fails, so `close()` is skipped. Use a context manager or `try/finally` so the resource is always released.

Avoid this style:

> This is bad.

Do not invent line numbers, behavior, or context. If required context is missing, say what cannot be verified.

If you find no blocking issues, say that directly and summarize the remaining risk.
