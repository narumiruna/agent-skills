---
name: python
description: Use when a task involves modern Python workflows with uv, including project setup, standalone scripts, quality tooling, packaging, or routing to focused Python skills.
---

# Python

## Overview

Use this skill whenever the task involves Python. Treat `uv` as the default tool for environment management, dependency installation, and command execution. Keep the main workflow here, and route only when the task is specifically about Typer CLI design, logging strategy, or Peewee ORM patterns.

## Non-Negotiable Rules

- Install dependencies with `uv add`; do not use `pip install`.
- Run Python commands with `uv run`; do not call `python` or `pytest` directly.
- If the repository uses `prek`, prefer `prek run -a` as the full pre-merge quality gate.
- Pytest tests must be function-based; do not use `unittest.TestCase` or class-based pytest tests.

## Quick Reference

| Need | Command / Direction |
| --- | --- |
| Initialize a project | `uv init <name>` |
| Add a dependency | `uv add <package>` |
| Add a dev dependency | `uv add --dev <package>` |
| Sync dependencies | `uv sync` |
| Run Python | `uv run python <file.py>` |
| Run tests | `uv run pytest` |
| Run lint | `uv run ruff check` |
| Run format | `uv run ruff format` |
| Run type checks | `uv run ty check` |
| Build package artifacts | `uv build --no-sources` |
| Publish package | `uv publish --token $PYPI_TOKEN` |
| Standalone script with one-off deps | `uv run --with requests script.py` |
| Script with inline metadata | `uv init --script script.py --python 3.12` |

## Core Workflows

### Project Setup and Daily Commands

Use `uv` for project initialization, dependency changes, and command execution.

```bash
uv init my-project
cd my-project
uv add fastapi
uv add --dev ruff pytest pytest-cov ty
uv run pytest
```

When a dependency is missing, fix the environment first, then rerun the failing command.

### Standalone Scripts

Use `uv run` for standalone scripts. Prefer inline metadata when the script should be self-contained and portable. If you are inside a project directory but the script does not need project code, use `uv run --no-project script.py`.

Common cases:

```bash
uv run script.py
uv run --with rich --with requests script.py
uv init --script script.py --python 3.12
uv add --script script.py requests rich
uv lock --script script.py
```

Full script guidance lives in `references/uv-scripts.md`.

### Quality Tooling

Run quality tools through `uv run` so local and CI behavior stay aligned.

Pre-merge baseline:

```bash
uv run ruff check --fix
uv run ruff format
uv run ty check
uv run pytest --cov=src --cov-report=term-missing
```

If the repo standardizes on `prek`, use:

```bash
prek run -a
```

Full quality tooling guidance lives in `references/quality.md`.

### Packaging and Publishing

Build artifacts with `uv build`, verify them, then publish.

Release baseline:

```bash
uv build --no-sources
uv pip install dist/my_package-1.0.0-py3-none-any.whl
uv publish --publish-url https://test.pypi.org/legacy/ --token $TEST_PYPI_TOKEN
```

Package build and publish details live in `references/packaging.md`.

## Focused Routing

Keep these workflows inside `python` unless the task clearly needs a narrower skill.

- Route to `python-cli-typer` for command tree design, Typer patterns, and CLI UX.
- Route to `python-logging` for logging architecture, handlers, formatting, or `loguru`.
- Route to `python-peewee` for Peewee ORM usage, `DatabaseProxy`, and SQLite test patterns.

## Common Mistakes

- Using `pip install` for a quick fix instead of `uv add`.
- Running `python` or `pytest` directly instead of `uv run`.
- Forgetting `--no-project` for standalone scripts inside a project checkout.
- Assuming inline script metadata uses project dependencies.
- Publishing packages before testing the built wheel.

## Red Flags

- Guidance that bypasses `uv` for install or execution.
- Mixing `pre-commit` and `prek` in a repo that already standardizes on `prek`.
- Class-based pytest tests or `unittest.TestCase` in new test guidance.

## References

- `references/uv-scripts.md` - Standalone scripts, inline metadata, locking, and Python selection
- `references/quality.md` - Ruff, ty, pytest, coverage, CI, and prek usage
- `references/packaging.md` - Build artifacts, pre-publish checks, and publish flow
