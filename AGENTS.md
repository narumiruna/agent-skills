# Repository Guidelines

Follow global defaults; this file defines only repo-specific additions and overrides.

## Documentation Boundaries

- `README.md` owns external positioning, installation flows, and skill discovery.
- This file owns maintainer workflow. Do not duplicate README product messaging or step-by-step install instructions here.
- When install recipes or supported paths change, update `README.md`, `AGENTS.md`, and `justfile` together.

## Repository Layout

- Active skills live in `skills/<skill-name>/SKILL.md`.
- Deprecated skills live in `skills/deprecated/<skill-name>/SKILL.md` and are excluded from default install and clean flows.
- Optional supporting material stays inside the skill directory under `references/`, `scripts/`, `assets/`, or `agents/`.
- Slides and visual examples live under `examples/`.

## Commands

- `just` is non-mutating by default and only lists available recipes.
- Local Codex copy/rm flows use `just install-all`, `just install <skill>`, `just clean-all`, and `just clean <skill>`.
- `prek run -a` is the default repository-wide verification gate before a PR.
- Rebuild slide outputs after changing content under `examples/slides/`.

## Editing Rules

- Use lowercase kebab-case for skill directories.
- Name the required entry file exactly `SKILL.md`.
- Keep examples repository-relative and executable when practical.
- Do not reintroduce root-level marketplace or plugin metadata assumptions unless the corresponding files actually exist in the repo.

## Pull Requests

- Summarize what changed and why.
- List affected paths.
- Include verification steps with command output summary.
- Add screenshots or rendered output links for slide visual changes.
