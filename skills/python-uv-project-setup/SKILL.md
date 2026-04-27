---
name: python-uv-project-setup
description: Use when initializing a Python project or script, adding dependencies, or running commands with uv, especially to avoid pip install and direct python/pytest usage.
---

# Python uv Project Setup

## Overview

Use uv for project environments, dependency management, and command execution. Core principle: install, sync, and run through uv so local work matches the project environment.

## Use When

- Initializing a Python project with `pyproject.toml`.
- Adding, removing, or syncing project dependencies.
- Running project commands, tests, CLIs, or modules in the managed environment.
- Fixing missing imports caused by unsynced or missing dependencies.

For standalone scripts with inline metadata or one-off dependencies, use `uv-scripts` instead.

## Workflow

1. Identify whether the file belongs to a project or is a standalone script.
2. For projects, inspect `pyproject.toml` and use the repo's existing uv layout.
3. Add runtime dependencies with `uv add`; add test, lint, type, and build tools with `uv add --dev`.
4. Run commands with `uv run` and sync with `uv sync` when dependencies changed elsewhere.
5. If the repo has an established quality gate, run it after dependency or command changes.

## Non-Negotiable Rules

- Install dependencies with `uv add` (never `pip install`).
- Run commands with `uv run` (never direct `python` or `pytest`).
- Use `uv add --dev` for development-only tools such as ruff, ty, pytest, pytest-cov, and build/release helpers.
- Do not introduce a new package manager unless the existing project explicitly requires it.

## Quick Reference

| Task | Command |
| --- | --- |
| Initialize project | `uv init <name>` |
| Add dependency | `uv add <package>` |
| Add dev dependency | `uv add --dev <package>` |
| Remove dependency | `uv remove <package>` |
| Run Python | `uv run python <file.py>` |
| Run module | `uv run python -m <module>` |
| Run pytest | `uv run pytest` |
| Sync deps | `uv sync` |

## Project vs. Script Boundary

- Project work has a `pyproject.toml`, project code, or shared lockfile. Use this skill.
- Standalone script work is a single file that should carry its own Python/dependency metadata. Use `uv-scripts`.
- Scripts inside a project may still use project dependencies; run them with `uv run python script.py`.

## Examples

### Project setup

```bash
uv init my-project
cd my-project
uv add loguru typer
uv add --dev ruff pytest pytest-cov ty
```

### Missing dependency

```bash
uv add fastapi
uv run pytest
```

### Run project commands

```bash
uv run python -m my_package
uv run pytest
```

## Common Mistakes

- Running `pip install` first and only switching to uv after it fails.
- Running `python` or `pytest` directly instead of `uv run`.
- Adding pytest, ruff, ty, or coverage tools as runtime dependencies instead of dev dependencies.
- Treating a self-contained script as a full project when `uv-scripts` would be smaller and clearer.

## Rationalizations to Reject

| Excuse | Reality |
| --- | --- |
| "pip install is faster for a quick fix" | It bypasses the project environment and drifts from uv-managed state. |
| "I can run python/pytest directly this once" | Direct runs skip uv's environment and can break reproducibility. |

## Red Flags

- Any instruction that uses `pip install`, `python`, or `pytest` directly.
