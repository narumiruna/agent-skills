---
name: python-project
description: Python project workflow and standards using Astral uv for environments/dependencies, ty for type checking, typer for CLI, ruff for lint/format, pytest and pytest-cov for tests/coverage, and loguru for logging. Use for Python project setup, dependency management, CLI/logging patterns, type checking, testing, linting/formatting, and packaging guidance.
---

# Python Project

## Use this workflow

Build and maintain Python 3.12+ projects with modern tooling and best practices. Follow the steps below for project setup, dependency management, quality tools, CLI patterns, and packaging workflows.

Key tools:
- **uv**: Fast Python package installer and environment manager
- **ruff**: Lightning-fast linter and formatter
- **pytest**: Testing framework with coverage support
- **ty**: Static type checker
- **typer**: Modern CLI framework
- **loguru**: Simplified logging

For Python coding conventions, see the `python-conventions` skill.

## Set up a new project

1. Initialize a project:

```bash
uv init my-project
cd my-project
```

2. Add runtime dependencies:

```bash
uv add loguru typer
```

3. Add development dependencies:

```bash
uv add --dev ruff pytest pytest-cov ty
```

4. Verify the setup:

```bash
uv run python -V
# Confirm the expected Python version
```

## Use a src/ layout

Use a `src/` layout for better import clarity and testing isolation:

```
my-project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── cli.py
│       └── core.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
└── README.md
```

Benefits of a `src/` layout:
- Prevent accidental imports from the project root
- Force installation for testing
- Keep source and tests separated

## Manage dependencies

Basic operations:
- Add runtime dependency: `uv add <package>`
- Add dev dependency: `uv add --dev <package>`
- Add to named group: `uv add --group <name> <package>`
- Run commands: `uv run <command>`
- Sync dependencies: `uv sync`

Key principles:
- Use `uv run <command>` instead of plain `python` or tool commands.
- Use `--dev` for tools that are not needed in production (ruff, pytest, ty).
- Pin versions in production and use ranges during development.

Use the `uv-scripts` skill for inline metadata, `--no-project`, and `--with` flags.

## Run quality tools

Lint and format with ruff:
```bash
uv run ruff check         # Check for issues
uv run ruff check --fix   # Auto-fix issues
uv run ruff format        # Format code
```

Type check with ty:
```bash
uv run ty check          # Type check all code
```

Test with pytest and coverage:
```bash
uv run pytest                                     # Run tests
uv run pytest --cov=src --cov-report=term-missing # With coverage
uv run pytest -v tests/test_specific.py           # Specific test file
```

Use this pre-commit quality gate:
```bash
uv run ruff check --fix
uv run ruff format
uv run ty check
uv run pytest
```

Read `references/quality.md` for tool configuration and recommended settings.

## Build CLIs and logging

Use typer for CLIs:
```python
import typer

app = typer.Typer()

@app.command()
def greet(name: str, count: int = 1) -> None:
    """Greet someone multiple times."""
    for _ in range(count):
        typer.echo(f"Hello, {name}!")

if __name__ == "__main__":
    app()
```

Use loguru for logging:
```python
from loguru import logger

logger.info("Application started")
logger.warning("Low disk space: {free} MB", free=512)

try:
    # Some operation that might fail
    connect_to_service()
except Exception as err:
    logger.error("Failed to connect: {error}", error=err)
```

Read `references/cli-logging.md` for complete examples and advanced patterns.

## Package distributions

Build distribution packages:
```bash
uv build                 # Build wheel and sdist
uv build --no-sources    # Build wheel only (for publish checks)
```

Check outputs in `dist/`:
- `*.whl` - Wheel package
- `*.tar.gz` - Source distribution

Read `references/packaging.md` for publish workflows and checks.

## Read references when needed

- Script execution patterns: `uv-scripts` skill
- Tool configuration: `references/quality.md`
- CLI and logging: `references/cli-logging.md`
- Packaging details: `references/packaging.md`
- Coding style: use the `python-conventions` skill

## References

- `uv-scripts` - Running scripts with uv
- `references/quality.md` - Ruff, pytest, and ty configuration
- `references/cli-logging.md` - Typer and loguru patterns
- `references/packaging.md` - Build and publish workflows
