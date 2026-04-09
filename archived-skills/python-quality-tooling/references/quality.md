# Quality Tools (ruff, ty, pytest)

## Table of Contents

- [prek (pre-commit runner)](#prek-pre-commit-runner)
- [Type Checking with ty](#type-checking-with-ty)
- [Linting and Formatting with ruff](#linting-and-formatting-with-ruff)
- [Testing and Coverage with pytest](#testing-and-coverage-with-pytest)
- [Pre-merge Quality Gate](#pre-merge-quality-gate)
- [CI Configuration Example](#ci-configuration-example)

Keep quality tools in dev dependencies and run via `uv run` for consistency.

## prek (pre-commit runner)

**Install (preferred):**

```bash
uv tool install prek
```

**Usage:**

```bash
prek run -a        # Run all hooks on the repo
prek run <hook>    # Run a specific hook
prek install       # Install git hooks
```

## Type Checking with ty

**Installation:**

```bash
uv add --dev ty
```

**Usage:**

```bash
uv run ty check              # Check all files
uv run ty check src/         # Check specific directory
uv run ty check --watch      # Watch mode for development
```

## Linting and Formatting with ruff

**Installation:**

```bash
uv add --dev ruff
```

**Commands:**

```bash
uv run ruff check           # Check for issues
uv run ruff check --fix     # Auto-fix safe issues
uv run ruff format          # Format code
```

## Testing and Coverage with pytest

**Installation:**

```bash
uv add --dev pytest pytest-cov
```

**Commands:**

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=term-missing

# Run specific tests
uv run pytest tests/test_specific.py
uv run pytest tests/test_specific.py::test_function

# Verbose output
uv run pytest -v

# Stop on first failure
uv run pytest -x

# Run tests matching pattern
uv run pytest -k "test_user"
```

## Pre-merge Quality Gate

Run before committing or in CI:

```bash
#!/bin/bash
set -e

echo "Running quality checks..."

# Format and lint
uv run ruff check --fix
uv run ruff format

# Type check
uv run ty check

# Run tests with coverage
uv run pytest --cov=src --cov-report=term-missing --cov-fail-under=80

echo "All checks passed!"
```

## CI Configuration Example

**.github/workflows/test.yml:**

```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v3

      - name: Set up Python
        run: uv python install <version>

      - name: Install dependencies
        run: uv sync --all-extras --dev

      - name: Lint
        run: uv run ruff check

      - name: Format check
        run: uv run ruff format --check

      - name: Type check
        run: uv run ty check

      - name: Test
        run: uv run pytest --cov=src --cov-report=xml
```
