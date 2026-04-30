---
name: python
description: Use when a task involves Python project setup, dependency management with uv, running project commands, quality gates (ruff, ty, pytest, coverage, prek), or building and publishing packages with uv, and when routing specialized work to uv-scripts, Typer CLI, logging, or Peewee.
---

# Python

## Overview

Use this skill as the default entry point for Python project work. Own project setup, dependency management, quality checks, and package release here. Route only standalone scripts, Typer CLI structure, logging design, and Peewee ORM patterns to focused skills.

## Quick Reference

| Need | Use this skill |
| --- | --- |
| Init project, add or remove deps, sync, run commands | `python` |
| Lint, format, type-check, test, coverage, CI gates | `python` |
| Build or publish wheel/sdist with uv | `python` |
| Standalone scripts with inline metadata | `uv-scripts` |
| Build a CLI with Typer | `python-cli-typer` |
| Choose/configure logging or loguru | `python-logging` |
| Peewee ORM, DatabaseProxy, SQLite tests | `python-peewee` |

## Routing Rules

- Stay in `python` for project-scoped work involving `pyproject.toml`, shared dependencies, `uv run`, quality tools, or package release.
- Route to `uv-scripts` when the task is a standalone Python file that should carry its own dependencies or ignore the surrounding project with `--no-project`.
- Route to `python-cli-typer`, `python-logging`, or `python-peewee` only for those domain-specific concerns. Keep dependency, quality, and release expectations from this skill.
- For mixed tasks, use `python` first for environment and validation, then apply the focused skill.

Use these trigger rules:

- Install, dependency, project initialization, missing package, running project commands, lint, type-checking, tests, coverage, CI gates, or packaging: stay in `python`.
- Standalone script, inline script metadata, one-off dependencies, `--with`, or `--no-project`: `uv-scripts`.
- CLI commands, Typer, options, arguments, shell entry points, or command tests: `python-cli-typer`.
- Logging, loguru, handlers, formatters, structured context, or library logging: `python-logging`.
- Peewee, ORM models, `DatabaseProxy`, transactions, or SQLite model tests: `python-peewee`.

## Project vs. Standalone Script

- Project work has a `pyproject.toml`, shared codebase, or lockfile. Use this skill.
- Standalone script work is a single file with inline metadata, one-off `--with` dependencies, or intentional `--no-project` execution. Use `uv-scripts`.
- A script inside a project still belongs here when it should use project dependencies, for example `uv run python script.py`.

## Core Workflow

1. Inspect `pyproject.toml` and the repository's documented commands before changing anything.
2. Install runtime dependencies with `uv add`; install lint, test, type, and build tools with `uv add --dev`.
3. Remove dependencies with `uv remove` and reconcile the environment with `uv sync` when dependencies changed elsewhere.
4. Run project commands through `uv run`.
5. Run the repository quality gate after dependency or code changes.
6. For package release, build, inspect, test-install, then publish.

## Non-Negotiable Rules

- Install dependencies with `uv add`, never `pip install`.
- Run Python, pytest, and other project commands with `uv run`, never direct `python` or `pytest`.
- Keep quality and release tooling in dev dependencies via `uv add --dev`.
- Prefer the repository's aggregate command first; if the repo standardizes on prek, use `prek run -a`.
- Build release artifacts with `uv build --no-sources` so local `[tool.uv.sources]` overrides do not leak into release output.
- Test installs from the built wheel or published artifact, not only from the source checkout.

## Quick Commands

| Task | Command |
| --- | --- |
| Initialize project | `uv init <name>` |
| Add dependency | `uv add <package>` |
| Add dev dependency | `uv add --dev <package>` |
| Remove dependency | `uv remove <package>` |
| Sync deps | `uv sync` |
| Run Python | `uv run python <file.py>` |
| Run module | `uv run python -m <module>` |
| Run tests | `uv run pytest` |
| Full repo gate (prek) | `prek run -a` |
| Build release artifacts | `uv build --no-sources` |
| Publish to PyPI | `uv publish --token $PYPI_TOKEN` |

## Quality Gate Priority

Use this order:

1. Existing project command documented in the repo.
2. `prek run -a` when the repo uses prek.
3. Individual `uv run` commands.

Fallback command set:

```bash
uv run ruff check --fix
uv run ruff format
uv run ty check
uv run pytest --cov=src --cov-report=term-missing
```

Pytest tests MUST be function-based unless the repository already requires another style.

## Release Workflow

1. Run the repository quality gate.
2. Build artifacts in `dist/` with `uv build --no-sources`.
3. Inspect wheel and sdist contents.
4. Test install from the built wheel in a fresh uv-managed invocation.
5. Publish to Test PyPI first for first or risky releases, then publish to PyPI.

## Examples

User: "Missing fastapi and tests fail."

Handle in `python`: add the dependency with `uv add fastapi`, then run the repo quality gate.

User: "Build and publish this package."

Handle in `python`: follow the release workflow from build through artifact verification and publish.

User: "Write a one-file script with inline deps."

Route to `uv-scripts`.

User: "Add a Typer command and tests for it."

Use `python-cli-typer` for CLI structure and keep dependency and quality rules from `python`.

## Common Mistakes

- Treating a one-file script as project work when `uv-scripts` would be smaller and clearer.
- Routing lint, test, or release work away from `python` even though this skill owns those workflows.
- Running tools outside uv.
- Publishing before verifying artifacts.

## Red Flags

- Suggesting `pip install` or direct `python` or `pytest` execution.
- Mixing `pre-commit` commands into a prek-standardized repo.
- Verifying only the source tree instead of the built artifact.

## References

- `references/quality.md` - Full commands, CI examples, coverage, and prek usage.
- `references/packaging.md` - Build, inspect, and publish details.
