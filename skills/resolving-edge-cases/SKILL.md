---
name: resolving-edge-cases
description: Use when asked to proactively find, fix, or harden edge-case bugs in a specific code flow, or when a concrete bug fix suggests nearby same-pattern regression risks that should be inspected.
---

# Resolving Edge Cases

Use this to actively inspect relevant code, find plausible edge-case bugs, and fix or harden them. Do not wait for the user to enumerate edge cases.

## Default Scope

When the user does not provide files, a commit, or a diff, inspect `git status --short` and start with relevant staged, unstaged, and untracked paths. For a branch or pull request, determine its target from repository or PR context and include paths from the merge-base diff, such as `git diff --name-only <target>...HEAD`; do not assume the target is `main` or `master`. If no changed path applies, inspect the files implied by the request; if no scope can be inferred, ask for one target.

## Loop

1. Infer intended behavior from the user request, code, tests, docs, and sibling flows; state assumptions, but only ask when the rule is ambiguous.
2. Trace the real flow end to end, including callers, sibling routes, cleanup paths, and stored state.
3. Proactively inspect plausible edge cases for that flow; skip generic checklists that cannot occur.
4. Establish that each candidate violates intended behavior, then add the smallest regression test or executable check that fails before the fix when practical. If the failure cannot be verified, report the risk as unverified instead of changing behavior.
5. Fix or harden each confirmed bug at the shared root path, not only the reported symptom.
6. Run the narrow check, then scan sibling callers/routes for the same pattern.
7. Repeat while each fix exposes a concrete adjacent edge case.
8. Run the repo's normal verification gate before final response.

## Edge-Case Families

Consider these only when relevant:

- empty, single, duplicate, huge, unsorted, missing, null, undefined, NaN, malformed, or wrong-type inputs
- inclusive/exclusive bounds, off-by-one behavior, overflow, divide-by-zero, and precision loss
- trust boundaries: HTTP, WebSocket, CLI args, files, environment, database rows, external APIs
- path containment, authz/authn, tenant ownership, unsafe deserialization, and sensitive logging
- stale state, reconnect/disconnect, cancellation, retries, idempotency, races, and partial failure
- timeout, cleanup, file handles, sockets, locks, transactions, subscriptions, and memory growth
- time zones, DST, clock skew, expiry windows, ordering assumptions, and eventual consistency
- response shape, schema migration, backward compatibility, packaging/runtime/config mismatches

## Fix Rules

- Prefer one guard or normalization in the shared boundary over repeated caller patches.
- Preserve existing contracts unless the task explicitly changes them.
- If retained state is introduced, add the minimal eviction or cleanup path.
- If a timeout or cancellation can fire, close or clear the resource too.
- If input crosses a trust boundary, validate type and shape before use.
- If a package/config points to code, prove the referenced file exists in the packaged/runtime form.
- Keep the sibling scan bounded to the same root cause and directly affected flow. Stop and report when the next candidate requires a new behavior decision or material scope expansion.
- Stop when checks pass and the sibling scan finds no same-pattern bug; report fixed cases, checks run, and any unverified risk plainly.
- Do not return only a checklist or plan unless the user explicitly asks for one.
