# Repository Guidelines

Follow global defaults; this file defines only repo-specific additions and overrides.

## Scope and Documentation

- Use `docs/guides/gpt-5.6.md` as the primary model guide when creating or revising skills and other agent-facing prompts. Use another versioned guide only when the task targets that model version.
- `README.md` owns external positioning, installation flows, and skill discovery; this file owns maintainer workflow. Do not duplicate product messaging or installation walkthroughs here.
- Update the README catalog when a skill is added, deprecated, renamed, recategorized, or materially changes its trigger. Update install documentation and executable recipes only in the files that own the affected flow.

## Repository Layout

- Active skills live in `skills/<category>/<skill-name>/SKILL.md`; category directories are organizational only.
- Deprecated skills live in `deprecated/<skill-name>/SKILL.md`, outside the active `skills/` tree, and are excluded from standard discovery.
- Optional supporting material stays inside the skill directory under `references/`, `scripts/`, `assets/`, or `agents/`.
- Source slides and visual examples live under `examples/`. Treat ignored `build/` content as generated output; do not hand-edit or commit it.
- Treat `skills/` as the active source of truth. `.agents/skills` is an ignored local discovery symlink, not a second copy to edit.

## Editing Rules

- Use lowercase kebab-case for skill directories and name every required entry file exactly `SKILL.md`.
- Keep a skill's frontmatter description and README catalog entry aligned when its trigger or purpose changes.
- Keep examples repository-relative and executable when practical.
- Do not introduce root-level marketplace or plugin metadata unless corresponding repository files and workflows actually exist.

## Verification

- This repository does not use automated tests. Do not add or maintain repository tests, and do not apply TDD to repository changes.
- `just` is non-mutating by default and lists available recipes.
- Run changed bundled scripts through a representative path.
- Run `prek run -a` as the repository-wide formatting and lint gate. Before a PR, this gate must pass or the failure must be reported.
- Changes under `examples/slides/` are rendered by `.github/workflows/marp-to-pages.yml`; verify source assets and include the generated preview or screenshots in the PR.

## Pull Requests

- Summarize what changed and why.
- List affected paths.
- Include verification commands with an outcome summary and disclose any skipped or failing check.
- Add screenshots or rendered output links for slide visual changes.
