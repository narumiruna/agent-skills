---
name: python-typer
description: Use when building or structuring Python CLI commands with Typer, including commands, options, and multi-command apps.
---

# Python CLI with Typer

## Overview

Use Typer for ergonomic CLI construction. Core principle: keep command wiring thin, explicit, and testable while moving business logic into regular Python functions.

## Use When

- Building a Python CLI with Typer.
- Adding commands, arguments, options, prompts, or confirmations.
- Wiring a module entry point or console script.
- Testing CLI behavior separately from business logic.

## Install

```bash
uv add typer
```

## Quick Reference

| Task | Pattern |
| --- | --- |
| Single command | `@app.command()` |
| Options | function args with defaults |
| Multiple commands | multiple `@app.command()` |
| Module run | `uv run python -m <package>.cli --help` |
| Script run | `uv run python cli.py --help` |
| CLI tests | `CliRunner().invoke(app, [...])` |

## Workflow

- Define a `typer.Typer()` app in `cli.py`.
- Keep command functions small; move business logic into separate modules.
- Wire either `if __name__ == "__main__": app()` for script/module execution or a project console script in `pyproject.toml`.
- Run CLI via `uv run python -m <module>` or `uv run python cli.py`.
- Test command parsing and exit behavior with `typer.testing.CliRunner`.
- Test business logic directly with normal function tests.

## Example

```python
import typer

app = typer.Typer()

@app.command()
def greet(name: str, count: int = 1) -> None:
    for _ in range(count):
        typer.echo(f"Hello, {name}!")

if __name__ == "__main__":
    app()
```

Usage:
```bash
uv run python cli.py --help
uv run python cli.py Alice
uv run python cli.py Alice --count 3
```

Module entry point:

```bash
uv run python -m my_package.cli --help
```

Multiple commands:
```python
import typer

app = typer.Typer()


@app.command()
def create(name: str) -> None:
    """Create a new item."""
    typer.echo(f"Creating {name}...")


@app.command()
def delete(name: str, force: bool = False) -> None:
    """Delete an item."""
    if not force:
        if not typer.confirm(f"Delete {name}?"):
            raise typer.Abort()
    typer.echo(f"Deleted {name}")


if __name__ == "__main__":
    app()
```

CLI test:

```python
from typer.testing import CliRunner

from my_package.cli import app

runner = CliRunner()


def test_greet() -> None:
    result = runner.invoke(app, ["Alice", "--count", "2"])

    assert result.exit_code == 0
    assert "Hello, Alice!" in result.stdout
```

## Common Mistakes

- Putting heavy business logic inside CLI functions.
- Forgetting to wire `if __name__ == "__main__"` for script entry.
- Testing only the underlying functions and missing CLI parsing or exit-code behavior.
- Adding shell parsing manually instead of using Typer arguments and options.

## Red Flags

- CLI guidance that ignores Typer when Typer is the chosen framework.
- CLI commands that cannot be run through `uv run`.
