## Goal

Deprecate the rarely used `researching-gourmet-venues` skill by removing it from active discovery while preserving its workflow, templates, and explicit local compatibility under `deprecated/`.

## Plan

- [x] Create branch `chore/deprecate-gourmet-research` from clean, synchronized `main`; verified by `git status --short --branch`.
- [x] Add focused regression expectations for 27 active and 6 deprecated skills, the gourmet skill's deprecated-only location and catalog entry, and continued archived-workflow invariants; verified five focused tests failed against the active layout because the counts, directory, and preserved-workflow test paths had not changed.
- [x] Move `researching-gourmet-venues` with its templates and metadata to `deprecated/`, mark it internal/deprecated, and update the README catalog; verified 27 active, 6 deprecated, and 33 total skills, all six templates present, and exact-name references limited to the deprecated workflow/catalog, tests, illustrative slide, and historical plan.
- [x] Run repository validation, inspect the final diff and branch state, and archive this completed plan with evidence; verified 33/33 skills passed `quick_validate.py`, 88/88 tests passed, all `prek run -a` hooks passed after one formatting correction, `git diff --check` passed, and independent review found no actionable issue.

## Risks

- Moving only `SKILL.md` could orphan the six templates; move the entire skill directory and validate relative links.
- Existing tests intentionally preserve evidence and ranking safeguards in deprecated workflows; retarget them instead of dropping coverage.
- Archived plans and the illustrative project slide may retain historical examples; do not rewrite historical evidence or expand this bounded deprecation into a slide redesign.

## Completion Checklist

- [x] `researching-gourmet-venues` is absent from `skills/` and present under `deprecated/` with `metadata.internal: true` and deprecated UI labeling; verified by focused regression tests and inventory inspection.
- [x] README active discovery omits the skill and the deprecated catalog explains its retained compatibility status; verified by catalog assertions and exact-name review.
- [x] All templates and behavior safeguards remain intact and tested from the deprecated location; verified all six expected templates and existing ranking/evidence assertions.
- [x] Skill validation, the full pytest suite, `prek run -a`, and `git diff --check` pass on `chore/deprecate-gourmet-research`; verified by 33 valid skills, 88 passing tests, all hooks passing, and a clean diff check.
