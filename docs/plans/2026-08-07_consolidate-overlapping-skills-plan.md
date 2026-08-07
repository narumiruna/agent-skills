## Goal

Consolidate two overlapping active-skill pairs while preserving their distinct operating modes and old names as deprecated compatibility references: merge `scoring-agent-skills` into `creating-agent-skills`, and merge `designing-user-interfaces` into `designing-user-experiences`.

## Plan

- [x] Create and verify branch `refactor/consolidate-overlapping-skills`; verified by `git switch -c` and `git status --short --branch` showing the new branch from a clean `main` worktree.
- [x] Expand `creating-agent-skills` with an explicitly requested scoring mode, move its rubric into the maintained skill, retire `scoring-agent-skills` to `deprecated/`, and align the README catalogs; verified both active and deprecated skills with `quick_validate.py`, the rubric at its new linked path, the removed active directory, and focused catalog/reference inspection.
- [x] Expand `designing-user-experiences` with bounded interface proposal, review, and implementation modes while retaining proposal approval for substantial end-to-end work; move the UI references into the maintained skill, retire `designing-user-interfaces` to `deprecated/`, and align the README catalogs; verified both skills with `quick_validate.py`, all three relocated references, explicit bounded/substantial routing, and focused preservation review.
- [ ] Run repository-wide skill validation and formatting checks, inspect the complete diff for trigger collisions and lost requirements, and verify the intended inventory of 32 active and 9 deprecated skills.
- [ ] Push the branch to `origin`, create a pull request against the verified default branch, and verify the remote branch and pull-request state.

## Risks

- A broad merged description could trigger scoring without an explicit numerical request; retain a hard explicit-request boundary for Score mode.
- Moving the scoring rubric or UI references could leave broken relative links; validate every Markdown resource link after each move.
- Combining UI and UX could either impose proposal approval on small interface edits or bypass it for major information-architecture work; route by scope and preserve the approval gate only for substantial end-to-end changes.
- Deprecated copies could drift into a second maintained implementation; keep each as a concise internal compatibility reference pointing to the active replacement.
- Historical archived plans legitimately mention the former active skills; leave those records unchanged.

## Completion Checklist

- [x] `creating-agent-skills` supports create, name, rename, unscored review, and explicitly requested numerical scoring with the six-dimension rubric available on demand; verified by frontmatter and mode-boundary review plus the relocated `references/rubric.md`.
- [x] `designing-user-experiences` supports bounded interface work and substantial end-to-end UX work with distinct implementation-approval behavior; verified by the scope router, proposal boundary, and implementation-authority sections.
- [x] `scoring-agent-skills` and `designing-user-interfaces` are absent from active discovery and retained under `deprecated/` as internal compatibility references; verified by directory checks and valid frontmatter with `metadata.internal: true`.
- [ ] README catalog text, frontmatter, resource links, and active/deprecated counts agree.
- [ ] `prek run -a`, skill validation, link/inventory checks, and `git diff --check` pass.
- [ ] The branch is pushed and an open pull request targets the repository's verified default branch.
