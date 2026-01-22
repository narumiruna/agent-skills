---
name: python-quality-tooling
description: Use when configuring or running Python quality tools (ruff, ty, pytest, coverage, CI gates) and when enforcing a pre-merge quality checklist.
---

# Python Quality Tooling

## Overview

Use ruff, ty, and pytest consistently through uv. Core principle: one repeatable quality gate across local and CI.

## Quick Reference

| Task | Command |
| --- | --- |
| Lint | `uv run ruff check` |
| Auto-fix | `uv run ruff check --fix` |
| Format | `uv run ruff format` |
| Type check | `uv run ty check` |
| Test | `uv run pytest` |
| Coverage | `uv run pytest --cov=src --cov-report=term-missing` |

## Workflow

- Install tools as dev deps (see `python-uv-project-setup`).
- Run all checks before commit.
- Keep CI aligned with local commands.

## Example

Pre-merge gate:
```bash
uv run ruff check --fix
uv run ruff format
uv run ty check
uv run pytest --cov=src --cov-report=term-missing
```

## Common Mistakes

- Running tools outside uv (drifts from project env).
- Running only one tool and calling it done.

## Red Flags

- Direct `ruff`/`pytest` invocations without `uv run`.

## References

- `references/quality.md` - Full command set and CI example
