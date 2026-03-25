# Repository Guidelines

## Project Structure & Module Organization
This repository hosts reusable agent skills and plugin metadata.

- `.claude-plugin/marketplace.json`: plugin catalog and marketplace metadata.
- `skills/<skill-name>/SKILL.md`: required entry file for each skill.
- `skills/<skill-name>/references/`: optional supporting documentation.
- `examples/slides/<project>/`: Marp slide examples and assets.
- `.github/`: CI and automation configuration.

Keep each skill focused on a single responsibility and self-contained.

## Build, Test, and Development Commands
Use repository commands from the root directory:

- `just sync`: symlink local skills into `~/.agents/skills` for fast local testing.
- `just clean`: remove synced skill symlinks.
- `prek run -a`: run the full required pre-commit suite.
- `docker run --rm -v $PWD:/home/marp/app/ -e MARP_USER="$(id -u):$(id -g)" marpteam/marp-cli:latest -I examples/slides -o build/`: build slide HTML output.

For marketplace changes, also run `/plugin validate .` and test local install/uninstall flows.

## Coding Style & Naming Conventions
Write clear, standard English. Keep instructions concise and enforceable.

- Use lowercase kebab-case for skill directories (example: `python-quality-tooling`).
- Name the required skill entry file exactly `SKILL.md`.
- Keep examples executable and repository-relative.
- Avoid adding dependencies unless there is a current, concrete need.

Formatting and linting are enforced via pre-commit (`check-yaml`, `check-json`, LF normalization, trailing-whitespace cleanup, `svglint`, `ruff --fix`, `ruff-format`, `ty-check`).

## Testing Guidelines
Treat all generated outputs as untrusted until verified.

- Run `prek run -a` before opening a PR.
- Rebuild slides when slide content changes and verify rendered output.
- Validate marketplace changes with `/plugin validate .` and installation checks.

## Commit & Pull Request Guidelines
Follow the repository’s commit style: short, imperative, and specific (<= 72 chars), for example `fix filename`.

PRs should include:

- what changed and why;
- affected paths (example: `skills/python-logging/SKILL.md`);
- verification steps with command output summary;
- screenshots or rendered output links for slide visual changes.
