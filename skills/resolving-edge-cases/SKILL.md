---
name: resolving-edge-cases
description: Use when implementing or debugging code and the goal is to keep finding and fixing plausible edge cases, harden a flow, resolve repeated review comments, or prevent adjacent regressions revealed by each fix.
---

# Resolving Edge Cases

Use this before editing code when the task is to find, fix, or harden edge cases.

## Default Scope

When the user does not provide files, a commit, or a diff, run `git diff --name-only main...HEAD`; if the repo uses `master`, run `git diff --name-only master...HEAD` instead. Use those changed paths as the starting point for the loop below.

## Loop

1. State the intended behavior and the boundary being hardened.
2. Trace the real flow end to end, including callers, sibling routes, cleanup paths, and stored state.
3. List only plausible edge cases for that flow; skip generic checklists that cannot occur.
4. Fix the shared root path, not only the reported symptom.
5. Add the smallest regression test or executable check that fails without the fix.
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
- Stop when checks pass and the sibling scan finds no same-pattern bug; report any unverified risk plainly.
