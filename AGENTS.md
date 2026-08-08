# Repository Guidelines

Follow global defaults; this file contains only repository-specific additions and overrides.

## Documentation

- Use `docs/guides/gpt-5.6.md` as the primary model guide when creating or revising skills and other agent-facing prompts.
- Use another versioned model guide only when the task targets that model version.
- Keep external positioning, installation flows, and skill discovery in `README.md`, and keep maintainer workflow in this file.
- Update the README catalog when a skill is added, deprecated, renamed, recategorized, or materially changes its trigger.
- Update installation documentation and executable recipes only in the files that own the affected flow.

## Code style

- Use lowercase kebab-case for skill directories and name every required entry file exactly `SKILL.md`.
- Keep a skill's frontmatter description and README catalog entry aligned when its trigger or purpose changes.
- Keep examples repository-relative and executable when practical.

## Commands

- Run `just` to list available recipes without mutating repository state.

## Boundaries

- For answer, explanation, review, diagnosis, or planning requests, inspect the relevant materials and report without making changes.
- For change, build, or fix requests, make the requested in-scope local changes and run relevant safe checks without asking first.
- Ask before writing to external systems, taking destructive or costly actions, or materially expanding the scope.
- Run `just bump-version <major|minor|patch>` only when explicitly requested because it fetches tags and creates a local lightweight tag.
- Ask before running `scripts/download_human_interface_guidelines.py` because its default mode downloads a large external corpus.
- Treat ignored `build/` content as generated output; do not hand-edit or commit it.
- Treat `skills/` as the active source of truth; `.agents/skills` is an ignored local discovery symlink, not a second copy to edit.
- Do not introduce root-level marketplace or plugin metadata unless corresponding repository files and workflows exist.

## Testing

- This repository has no maintained automated test suite; do not add or maintain repository tests or apply TDD to repository changes.
- Run changed bundled scripts through a representative path.
- Run `prek run -a` as the repository-wide formatting and lint gate, and report any failure before a pull request.
- Run `git diff --check` and inspect the final diff for unintended scope or repeated guidance.
- For changes under `examples/slides/`, verify source assets and include the generated preview or screenshots in the pull request.

## Repository structure

- Keep active skills in `skills/<category>/<skill-name>/SKILL.md`; category directories are organizational only.
- Keep deprecated skills in `deprecated/<skill-name>/SKILL.md`, outside standard discovery.
- Keep optional supporting material inside its skill directory under `references/`, `scripts/`, `assets/`, or `agents/`.
- Keep source slides and visual examples under `examples/`.

## Git and commits

- In pull requests, summarize what changed and why, list affected paths, and report verification outcomes with any skipped or failing check.
- Add screenshots or rendered output links for slide visual changes.
