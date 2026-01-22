# CLI with Typer

## Installation

```bash
uv add typer
```

## Basic Example

```python
import typer

app = typer.Typer()


@app.command()
def greet(name: str, count: int = 1) -> None:
    """Greet someone multiple times.

    Args:
        name: Person to greet
        count: Number of times to greet (default: 1)
    """
    for _ in range(count):
        typer.echo(f"Hello, {name}!")


if __name__ == "__main__":
    app()
```

## Usage

```bash
uv run python cli.py --help
uv run python cli.py Alice
uv run python cli.py Alice --count 3
```

## Multiple Commands

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
