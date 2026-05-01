---
name: python
description: Use when a task involves Python project setup or standalone scripts with uv, including dependency management, `uv run`, `uv run --with`, `--no-project`, inline script metadata, quality gates (ruff, ty, pytest, coverage, prek), or building and publishing packages with uv, and when routing specialized Typer CLI, logging, or Peewee work.
---

# Python

## Overview

Use this skill as the default entry point for Python and uv work. Own project setup, standalone script workflow, dependency management, quality checks, and package release here. For brand-new projects, bootstrap a default quality baseline with `ruff`, `ty`, `pytest`, and `pytest-cov`. Route only Typer CLI structure, logging design, and Peewee ORM patterns to focused skills.

## Quick Reference

| Need | Use this skill |
| --- | --- |
| Init project, add or remove deps, sync, run commands | `python` |
| Init a new project with the default quality baseline | `python` |
| Standalone scripts, inline metadata, one-off deps, or `--no-project` | `python` |
| Lint, format, type-check, test, coverage, CI gates | `python` |
| Build or publish wheel/sdist with uv | `python` |
| Build a CLI with Typer | `python-typer` |
| Choose/configure logging or loguru | `python-logging` |
| Peewee ORM, DatabaseProxy, SQLite tests | `python-peewee` |

## Routing Rules

- Stay in `python` for project-scoped work involving `pyproject.toml`, shared dependencies, `uv run`, quality tools, or package release.
- Stay in `python` for standalone Python files when deciding among plain `uv run`, `uv run --with`, inline metadata, `--no-project`, or script-specific Python version handling.
- Route to `python-typer`, `python-logging`, or `python-peewee` only for those domain-specific concerns. Keep dependency, quality, and release expectations from this skill.
- For mixed tasks, select project mode or standalone-script mode here first, then apply the focused skill if needed.

Use these trigger rules:

- Install, dependency, project initialization, missing package, running project commands, lint, type-checking, tests, coverage, CI gates, or packaging: stay in `python`.
- Standalone script, inline script metadata, one-off dependencies, `--with`, `--no-project`, `uv init --script`, `uv add --script`, `uv lock --script`, or script Python version selection: stay in `python`.
- CLI commands, Typer, options, arguments, shell entry points, or command tests: `python-typer`.
- Logging, loguru, handlers, formatters, structured context, or library logging: `python-logging`.
- Peewee, ORM models, `DatabaseProxy`, transactions, or SQLite model tests: `python-peewee`.

## Mode Selection

- Choose project mode when the work has a `pyproject.toml`, shared codebase, or lockfile.
- Treat a brand-new repository created with `uv init` as project mode.
- Choose standalone-script mode when the work is a single file, stdin snippet, or ad hoc invocation that should not become a full project.
- Treat a script inside a project as project mode when it imports local package code, for example `uv run python script.py`.
- Treat a script inside a project as standalone-script mode only when it should ignore project code via `--no-project`.

## New Project Baseline

When creating a brand-new Python project, do this immediately after `uv init <name>`:

1. Install the default dev toolchain with `uv add --dev ruff ty pytest pytest-cov`.
2. Make `pytest` the default test framework for the project.
3. Write new tests as function-based `tests/test_*.py` files that use plain `assert`.
4. Prefer pytest fixtures for setup and teardown, and use `@pytest.mark.parametrize` for matrix-style cases.
5. Do not introduce `unittest`, `unittest.TestCase`, or class-based `Test*` suites unless the repository already requires them.
6. In an existing repository, follow the established test stack unless the user explicitly asks to migrate frameworks.

## Project Workflow

1. Inspect `pyproject.toml` and the repository's documented commands before changing anything.
2. For a brand-new project, install the default dev toolchain with `uv add --dev ruff ty pytest pytest-cov`; otherwise install the missing lint, test, type, and build tools with `uv add --dev`.
3. Remove dependencies with `uv remove` and reconcile the environment with `uv sync` when dependencies changed elsewhere.
4. Run project commands through `uv run`.
5. Run the repository quality gate after dependency or code changes.
6. For package release, build, inspect, test-install, then publish.

## Standalone-Script Workflow

1. Decide whether the script should use project dependencies, one-off `--with` dependencies, or inline metadata.
2. Use plain `uv run script.py` when no extra dependencies are needed.
3. Use `uv run --with ... script.py` for disposable per-invocation dependencies.
4. Use `uv init --script` and `uv add --script` when the dependency list should live with the script.
5. Use `--no-project` only when running inside a project and the script must ignore project code.
6. Use `uv run --python <version>` or `requires-python` in metadata when the script needs a specific Python version.
7. Use `uv lock --script` when reproducibility matters.
8. See `references/scripts.md` for stdin, heredoc, shebang, alternate indexes, Windows `.pyw`, and lock details.

## Non-Negotiable Rules

- Install dependencies with `uv add`, never `pip install`.
- Run Python, pytest, and script invocations with `uv run`, never direct `python` or `pytest`.
- Keep quality and release tooling in dev dependencies via `uv add --dev`.
- For a brand-new project, immediately install `ruff`, `ty`, `pytest`, and `pytest-cov` with `uv add --dev ruff ty pytest pytest-cov` unless the repository already defines an equivalent toolchain.
- For a brand-new project, use `pytest` as the default test framework. Do not start with `unittest`, `unittest.TestCase`, or class-based `Test*` suites.
- Write pytest tests as function-based `tests/test_*.py` files with plain `assert`; prefer fixtures and `@pytest.mark.parametrize` over custom setup helpers or loop-driven assertions.
- In an existing repository, follow the current test stack unless the user explicitly asks to migrate frameworks.
- Do not create a `pyproject.toml` only to run a one-file script.
- Put `--no-project` before the script name, and never use it when the script imports local package code.
- Treat `uv run --with` as disposable; use inline metadata when the script should be shared or reused.
- Remember that inline script metadata ignores project dependencies.
- Prefer the repository's aggregate command first; if the repo standardizes on prek, use `prek run -a`.
- Build release artifacts with `uv build --no-sources` so local `[tool.uv.sources]` overrides do not leak into release output.
- Test installs from the built wheel or published artifact, not only from the source checkout.

## Quick Commands

| Task | Command |
| --- | --- |
| Initialize project | `uv init <name>` |
| Add the new-project quality baseline | `uv add --dev ruff ty pytest pytest-cov` |
| Add dependency | `uv add <package>` |
| Add dev dependency | `uv add --dev <package>` |
| Remove dependency | `uv remove <package>` |
| Sync deps | `uv sync` |
| Run Python | `uv run python <file.py>` |
| Run module | `uv run python -m <module>` |
| Run a standalone script | `uv run script.py` |
| Run a script with one-off deps | `uv run --with requests script.py` |
| Run a script outside the project | `uv run --no-project script.py` |
| Init script metadata | `uv init --script script.py --python 3.12` |
| Add script deps | `uv add --script script.py requests rich` |
| Lock script deps | `uv lock --script script.py` |
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
uv run pytest --cov=<package-or-src-path> --cov-report=term-missing
```

Pytest tests MUST be function-based unless the repository already requires another style. For new projects, keep tests in `tests/test_*.py`, use plain `assert`, prefer fixtures plus `@pytest.mark.parametrize`, and avoid `unittest.TestCase` or class-based `Test*` suites.

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

Handle in `python`: initialize script metadata, add script dependencies, and keep the file self-contained.

User: "Run this ad hoc script inside the repo but ignore project code."

Handle in `python`: use `uv run --no-project ...` and keep the script separate from project dependencies.

User: "Start a new Python project with a simple test."

Handle in `python`: initialize the project, run `uv add --dev ruff ty pytest pytest-cov`, and write a function-based pytest test under `tests/test_*.py`.

User: "Add a Typer command and tests for it."

Use `python-typer` for CLI structure and keep dependency and quality rules from `python`.

## Common Mistakes

- Treating a one-file script as project work when inline metadata or `--no-project` would be smaller and clearer.
- Using `--no-project` for a script that imports local package code.
- Keeping reusable script dependencies only in `uv run --with ...` shell history instead of the script metadata.
- Routing lint, test, or release work away from `python` even though this skill owns those workflows.
- Starting a brand-new project with `unittest` or without the default dev toolchain.
- Running tools outside uv.
- Publishing before verifying artifacts.

## Red Flags

- Suggesting `pip install` or direct `python` or `pytest` execution.
- Starting a brand-new project without `uv add --dev ruff ty pytest pytest-cov`.
- Defaulting to `unittest.TestCase` for a new project.
- Adding a `pyproject.toml` only to run a one-file script.
- Mixing `pre-commit` commands into a prek-standardized repo.
- Verifying only the source tree instead of the built artifact.

## References

- `references/quality.md` - Full commands, CI examples, coverage, and prek usage.
- `references/packaging.md` - Build, inspect, and publish details.
- `references/scripts.md` - Standalone script patterns, inline metadata, locking, and special cases.
