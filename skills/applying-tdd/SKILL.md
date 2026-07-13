---
name: applying-tdd
description: "Use when implementing non-trivial product or library code changes with Test-Driven Development (TDD): write a failing test first, make the smallest passing change, then refactor safely. Do not apply TDD to files under a repository's scripts/ directory."
---

# Applying TDD

These rules apply only to in-scope product and library code; files under `scripts/` follow the separate validation boundary below.

- Non-trivial in-scope changes SHOULD begin with a test.
- A test SHOULD fail before implementation begins whenever practical (red → green → refactor).
- Implementation SHOULD follow the red → green → refactor cycle.
- Implement the smallest change required to make the test pass.
- Refactoring MUST happen only after tests pass and MUST NOT change behavior.
- Tests MUST act as executable specifications of behavior, not merely coverage.
- Tests MUST assert observable behavior, not implementation details.
- Bug fixes SHOULD include a regression test when feasible.
- In-scope code changes SHOULD include corresponding test updates when behavior changes.
- Tests MUST be deterministic and isolated from uncontrolled inputs (for example network, time, or randomness).
- Tests SHOULD avoid reliance on external systems unless explicitly intended.
- External dependencies SHOULD be controlled appropriately.
- Tests SHOULD target the lowest meaningful level.
- Integration and end-to-end tests SHOULD complement lower-level tests where needed.
- Tests MUST NOT be weakened or removed to satisfy incorrect implementations.
- Tests SHOULD fail for a single clear reason.
- When tests cannot be added, this MUST be rare and explicitly justified, including:
  - why testing is not feasible
  - what risk remains
  - how the change was validated
- Skipping TDD for non-trivial in-scope changes REQUIRES explicit justification.

## Script Boundary

- Files under a repository's `scripts/` directory are outside TDD scope and do not require a failing test or the red → green → refactor cycle.
- Script changes MUST still receive proportionate validation, such as representative execution, dry-run, lint, syntax, or smoke checks.
- Reusable product, library, business, or query logic SHOULD be extracted from `scripts/` into `src/` or the repository's equivalent source root; the extracted logic remains in TDD scope.

## Scope

- Non-trivial in-scope product or library changes include:
  - Bug fixes
  - New features
  - Behavior changes
  - Data transformations
  - Business logic or query changes

- Excluded:
  - Files under a repository's `scripts/` directory, including standalone scripts, repository automation, migrations, and one-off helpers
  - Pure formatting changes
  - Renames without behavior change
  - Comment or documentation updates

### Exceptions

- TDD MAY be relaxed for:
  - Rapid prototyping or spike solutions
  - Exploratory coding where requirements are unclear
  - Pure UI layout or styling changes
