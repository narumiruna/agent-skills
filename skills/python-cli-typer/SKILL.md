---
name: python-cli-typer
description: Use when building or structuring Python CLI commands with Typer, including commands, options, and multi-command apps.
---

# Python CLI with Typer

## Overview

Use Typer for ergonomic CLI construction. Core principle: keep CLI entry points explicit and testable.

## Quick Reference

| Task | Pattern |
| --- | --- |
| Single command | `@app.command()` |
| Options | function args with defaults |
| Multiple commands | multiple `@app.command()` |

## Workflow

- Define a `typer.Typer()` app in `cli.py`.
- Keep command functions small; move logic into separate modules.
- Run CLI via `uv run python -m <module>` or `uv run python cli.py`.

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

## Common Mistakes

- Putting heavy business logic inside CLI functions.
- Forgetting to wire `if __name__ == "__main__"` for script entry.

## Red Flags

- CLI guidance that ignores Typer when Typer is the chosen framework.

## References

- `references/cli.md` - Full Typer examples and usage
