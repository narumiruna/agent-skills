## Goal

Merge the naming and rename-selection behavior from `naming-agent-skills` into `creating-agent-skills`, retire the standalone skill from active discovery, and preserve it as a deprecated compatibility reference on a dedicated branch.

## Plan

- [x] Create and verify branch `refactor/merge-naming-agent-skills`; verified by `git switch -c` and `git status --short --branch` showing that branch with a clean starting worktree.
- [x] Add focused repository regression assertions for the merged naming trigger, naming/rename constraints, active/deprecated inventories, and catalog placement; verified the three focused tests failed against the pre-merge layout because the active/deprecated counts and naming directory had not changed.
- [x] Expand `creating-agent-skills` with the standalone skill's discriminating naming, candidate-selection, collision, user-intent, and authorized-rename behavior; verified by the focused merged-skill assertions.
- [x] Move `naming-agent-skills` to `deprecated/` as an internal compatibility reference and align the README active/deprecated catalog entries and durable repository memory; verified 28 active, 5 deprecated, and 33 total skills, with exact-name references limited to the deprecated catalog, regression test, replacement UI label, and historical archived plan.
- [x] Run all repository validation gates, inspect the final diff and branch state, and archive this completed plan with command evidence; verified 33/33 skill directories passed `quick_validate.py`, 87/87 tests passed, every `prek run -a` hook passed after its one formatting fix, `git diff --check` passed, `just` listed non-mutating recipes, and final review's only minor test-coverage finding was addressed.

## Risks

- Naming guidance could be shortened enough to lose the user's preference for preserving original intent; retain that rule explicitly and add a regression assertion.
- A directory move without aligned metadata/catalog changes could keep the old skill discoverable or break inventory tests; assert both active absence and deprecated internal metadata.
- Historical archived plans legitimately mention the old active skill; leave those records unchanged rather than rewriting past evidence.

## Completion Checklist

- [x] `creating-agent-skills` handles creating, naming, reviewing, and authorized renaming with aligned frontmatter and README wording; verified by focused regression assertions and manual surface review.
- [x] `naming-agent-skills` is absent from active discovery and retained under `deprecated/` with `metadata.internal: true` and deprecated UI labeling; verified by inventory tests and 28-active/5-deprecated counts.
- [x] The user's durable shortcut preference is recorded without changing the decision to keep `explaining-step-by-step` active; verified in `MEMORY.md` and the unchanged active skill inventory.
- [x] The full pytest suite, `prek run -a`, skill metadata validation, and `git diff --check` pass on `refactor/merge-naming-agent-skills`; verified by 87 passing tests, all hooks passing, 33 valid skill directories, and a clean diff check.
