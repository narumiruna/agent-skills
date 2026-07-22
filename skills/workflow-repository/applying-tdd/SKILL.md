---
name: applying-tdd
description: "Use when implementing a non-trivial behavior change with Test-Driven Development (TDD) when practical: prove a focused failure, make the smallest passing change, then refactor safely."
---

# Applying TDD

Use tests as executable behavior specifications, not as a coverage ritual.

## Cycle

1. Identify the smallest observable behavior that should change.
2. Add or update the lowest-level meaningful test. Control time, randomness, network, storage, and other external inputs so the test is deterministic and isolated.
3. Run it and confirm it fails for the intended reason. If it passes, correct the test or establish why another check is the valid red state.
4. Implement the smallest change that makes the test pass. Do not weaken or delete a correct test to accommodate the implementation.
5. Run the focused test, then relevant integration or end-to-end coverage and the repository gate.
6. Refactor only while tests are green and without changing behavior.

For a bug, add a regression test when feasible. For a multi-path change, repeat the cycle in small observable increments rather than writing the entire implementation first.

## Exceptions

Pure formatting, comments, behavior-preserving renames, exploratory spikes, and visual-only styling may not benefit from a red-first cycle. Requirements may also be too uncertain to encode safely.

When a non-trivial behavior change cannot start with a failing test, state:

- why the red state was impractical or unavailable
- how behavior was verified instead
- what risk remains

Finish with the behavior proved, the initial failure evidence when available, and the passing checks. Do not claim TDD merely because tests were added after implementation.
