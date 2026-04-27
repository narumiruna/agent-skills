---
name: python-quality-tooling
description: Use when configuring or running Python quality tools (ruff, ty, pytest, coverage, CI gates) and when enforcing a pre-merge quality checklist.
---

# Python Quality Tooling

## Overview

Use ruff, ty, pytest, coverage, and prek consistently. Core principle: prefer the repository's single quality gate; otherwise run each tool through `uv run`.

## Use When

- Configuring or running lint, format, type checking, tests, coverage, hooks, or CI checks.
- Deciding between `prek run -a` and individual `uv run` commands.
- Adding quality tools as development dependencies.

## Workflow

1. Check the repo's existing quality gate first.
2. If the repo uses prek, run `prek run -a` as the primary pre-merge gate.
3. If no aggregate gate exists, run focused commands with `uv run`.
4. Add missing quality tools with `uv add --dev`, not as runtime dependencies.
5. Keep CI and local commands aligned.

## Quick Reference

| Task | Command |
| --- | --- |
| Lint | `uv run ruff check` |
| Auto-fix | `uv run ruff check --fix` |
| Format | `uv run ruff format` |
| Type check | `uv run ty check` |
| Test | `uv run pytest` |
| Coverage | `uv run pytest --cov=src --cov-report=term-missing` |
| Full repo gate (prek) | `prek run -a` |
| Install git hooks (prek) | `prek install` |

## Command Priority

Use this order:

1. Existing project command documented in the repo.
2. `prek run -a` when the repo uses prek.
3. Individual `uv run ruff ...`, `uv run ty check`, and `uv run pytest ...` commands.

Pytest tests MUST be function-based (no class-based tests or `unittest.TestCase`).

## Example

Pre-merge gate:
```bash
prek run -a
```

Fallback when no aggregate gate exists:
```bash
uv run ruff check --fix
uv run ruff format
uv run ty check
uv run pytest --cov=src --cov-report=term-missing
```

## Common Mistakes

- Running tools outside uv (drifts from project env).
- Skipping `prek run -a` when a repo standardizes on prek.
- Running only one tool and calling it done.

## Red Flags

- Direct `ruff`/`pytest` invocations without `uv run`.
- Mixing `pre-commit` and `prek` commands in the same repo.
- Class-based pytest tests (`class Test*`) or `unittest.TestCase` usage.

## References

- `references/quality.md` - Full command set, CI example, and prek install/usage notes (prefer `uv tool install prek`)
