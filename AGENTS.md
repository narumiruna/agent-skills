# Repository Guidelines

## Project Scope and Structure
This repository maintains reusable agent skills for Codex/Claude Code plugin marketplaces. Keep each skill self-contained and focused on one responsibility.

Key paths:
- `.claude-plugin/marketplace.json`: plugin catalog and metadata
- `skills/<skill-name>/SKILL.md`: primary skill contract
- `skills/<skill-name>/references/`: optional supporting docs
- `examples/slides/<project>/`: Marp example decks and assets

## Build, Test, and Development Commands
Use these commands during changes:
- `just sync`: symlink local skills for rapid testing
- `just clean`: remove synced links
- `prek run -a`: required full pre-commit checks
- `docker run --rm -v $PWD:/home/marp/app/ -e MARP_USER="$(id -u):$(id -g)" marpteam/marp-cli:latest -I examples/slides -o build/`: build slide HTML

Formatting and linting are enforced by pre-commit hooks: YAML/JSON checks, LF normalization, trailing whitespace cleanup, `svglint`, `ruff --fix`, `ruff-format`, and `ty-check`.

## Coding and Documentation Style
Write code and docs in clear, standard English. Keep instructions concise and enforceable.

Conventions:
- Use lowercase kebab-case for skill directory names (example: `python-quality-tooling`)
- Name required skill entry files as `SKILL.md`
- Keep examples executable and repository-relative
- Avoid adding dependencies unless justified by a current, concrete need

## Testing Guidelines
Treat all outputs as untrusted until verified.

Before opening a PR:
- Run `prek run -a` and ensure all hooks pass
- For marketplace changes, validate install flow with `/plugin validate .` and local install/uninstall checks
- For slide updates, rebuild `examples/slides` output and verify rendered HTML

## Commit and Pull Request Guidelines
Recent history favors short, imperative subjects (examples: `fix filename`, `Update README.md`, `Refactor ... for clarity`). Follow this pattern:
- Commit title: imperative, specific, <= 72 chars
- Group related changes only; avoid mixed-purpose commits

PRs should include:
- What changed and why
- Affected paths (for example, `skills/python-logging/SKILL.md`)
- Verification steps and command outputs summary
- Screenshots or rendered output links when slide visuals change
