---
name: python
description: Use when a task involves Python and you need routing to focused Python skills (uv setup, scripts, quality tooling, CLI, logging, packaging, or Peewee).
---

# Python

## Overview

Use this skill whenever the task involves Python, then route to the narrowest focused skill or skills. Core principle: keep this umbrella lean, make routing explicit, and let focused skills carry implementation details.

## Quick Reference

| Need | Use this skill |
| --- | --- |
| Init project, add deps, run commands | `python-uv-project-setup` |
| Standalone scripts with inline metadata | `uv-scripts` |
| Lint/format/type-check/test/CI | `python-quality-tooling` |
| Build a CLI with Typer | `python-cli-typer` |
| Choose/configure logging or loguru | `python-logging` |
| Build/publish packages with uv | `python-packaging-uv` |
| Peewee ORM, DatabaseProxy, SQLite tests | `python-peewee` |

## Routing Rules

- If the task only needs Python routing, stop here after naming the focused skill and why.
- If the task asks for implementation or commands, continue into the focused skill immediately.
- For multi-intent tasks, use every focused skill that owns part of the work, in this order:
  1. Environment and dependency setup: `python-uv-project-setup` or `uv-scripts`.
  2. Domain/framework implementation: `python-cli-typer`, `python-logging`, or `python-peewee`.
  3. Validation: `python-quality-tooling`.
  4. Release: `python-packaging-uv`.

Use these trigger rules:

- Install, dependency, project initialization, missing package, or running project commands: `python-uv-project-setup`.
- Standalone script, inline script metadata, one-off dependencies, `--with`, or `--no-project`: `uv-scripts`.
- Ruff, ty, pytest, coverage, CI, hooks, or pre-merge checks: `python-quality-tooling`.
- CLI commands, Typer, options, arguments, shell entry points, or command tests: `python-cli-typer`.
- Logging, loguru, handlers, formatters, structured context, or library logging: `python-logging`.
- Packaging, build, wheel, sdist, dist, Test PyPI, PyPI, or release verification: `python-packaging-uv`.
- Peewee, ORM models, `DatabaseProxy`, transactions, or SQLite model tests: `python-peewee`.

## Example

User: "Missing fastapi and tests fail. How should I install it?"

Route to: `python-uv-project-setup` (dependency management and run rules).

User: "Add a Typer command and tests for it."

Route to: `python-cli-typer` for the command structure and `python-quality-tooling` for the test/quality gate.

## Common Mistakes

- Providing detailed commands here instead of routing to the focused skill.
- Choosing only one focused skill when the task clearly has multiple independent Python concerns.
- Routing standalone script work to project setup when inline metadata or no-project mode is the better fit.

## Red Flags

- Suggesting `pip install` or direct `python`/`pytest` execution here.
