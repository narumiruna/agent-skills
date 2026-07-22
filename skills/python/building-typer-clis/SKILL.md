---
name: building-typer-clis
description: Build, extend, wire, or test Python CLIs with Typer, including commands, arguments, options, prompts, entry points, and multi-command apps. Use when Typer is the chosen framework or an existing Typer CLI needs changes.
---

# Python CLI with Typer

Keep Typer commands as thin adapters between parsed terminal input and ordinary Python functions.

## Workflow

1. Inspect `pyproject.toml`, the existing entry point, command conventions, and tests before changing the CLI.
2. Add Typer with `uv add typer` only when the project does not already provide it.
3. Define one `typer.Typer()` app and model input with typed arguments and options. Use Typer prompts or confirmations instead of custom shell parsing.
4. Validate CLI-specific input at the boundary, call business logic, render the result, and map expected failures to deliberate messages and exit codes.
5. Wire the supported entry point:
   - `if __name__ == "__main__": app()` for direct script or module execution.
   - A `[project.scripts]` entry for an installed command.
6. Run `--help` and representative success and failure paths through the repository's uv workflow.
7. Test parsing, output, and exit behavior with `typer.testing.CliRunner`; test business logic directly with normal unit tests.

## Minimal Pattern

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

```python
from typer.testing import CliRunner

from my_package.cli import app


def test_greet() -> None:
    result = CliRunner().invoke(app, ["Ada", "--count", "2"])
    assert result.exit_code == 0
    assert result.stdout.count("Hello, Ada!") == 2
```

Mock or inject external, destructive, or costly effects in CLI tests; do not exercise them merely to verify command wiring. Finish with the entry point exercised, CLI behavior covered, and the exact validation results reported.
