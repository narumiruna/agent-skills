# Quality Tools

Keep Python quality tools in dev dependencies and run them through `uv run` so local and CI behavior match.

## Commands

| Task | Command |
| --- | --- |
| Lint | `uv run ruff check` |
| Auto-fix lint issues | `uv run ruff check --fix` |
| Format | `uv run ruff format` |
| Type check | `uv run ty check` |
| Test | `uv run pytest` |
| Coverage | `uv run pytest --cov=src --cov-report=term-missing` |
| Full repo hooks | `prek run -a` |
| Install hooks | `prek install` |

## Setup

Install quality tools as dev dependencies:

```bash
uv add --dev ruff pytest pytest-cov ty
```

If the repository uses `prek`, install it the repo-standard way. Preferred standalone install:

```bash
uv tool install prek
```

## Pre-Merge Gate

Baseline gate:

```bash
uv run ruff check --fix
uv run ruff format
uv run ty check
uv run pytest --cov=src --cov-report=term-missing
```

If the repo already uses `prek`, prefer:

```bash
prek run -a
```

## CI Baseline

```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
      - run: uv sync --all-extras --dev
      - run: uv run ruff check
      - run: uv run ruff format --check
      - run: uv run ty check
      - run: uv run pytest --cov=src --cov-report=xml
```

## Rules

- Do not run `ruff`, `ty`, or `pytest` outside `uv run`.
- Do not mix `pre-commit` and `prek` commands in a repo that already chose one.
- Write pytest tests as plain functions, not classes.
