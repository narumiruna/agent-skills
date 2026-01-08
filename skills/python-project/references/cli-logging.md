# CLI and Logging Patterns

## Table of Contents

- [CLI with Typer](#cli-with-typer)
- [Logging with Loguru](#logging-with-loguru)

## CLI with Typer

**Installation:**

```bash
uv add typer
```

**Basic Example:**

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

**Usage:**
```bash
uv run python cli.py --help
uv run python cli.py Alice
uv run python cli.py Alice --count 3
```

**Multiple Commands:**

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

## Logging with Loguru

**Installation:**

```bash
uv add loguru
```

**Basic Usage:**

```python
from loguru import logger

# Simple logging
logger.info("Application started")
logger.debug("Processing item {item_id}", item_id=42)
logger.warning("Low disk space: {free} MB", free=512)
err = "Connection refused"
logger.error("Failed to connect: {error}", error=err)
```

**Configure Output:**

```python
from loguru import logger
import sys

# Remove default handler
logger.remove()

# Add custom handler with format
logger.add(
    sys.stderr,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
    level="INFO"
)

# Add file handler with rotation
logger.add(
    "logs/app.log",
    rotation="500 MB",
    retention="10 days",
    level="DEBUG"
)
```

**Exception Logging:**

```python
from loguru import logger

@logger.catch
def risky_function(x: int) -> float:
    """Automatically log exceptions with full traceback."""
    return 1 / x  # Will log if x is 0
```

**Structured Logging:**

```python
from loguru import logger

logger.info(
    "User action",
    user_id=123,
    action="login",
    ip_address="192.168.1.1"
)
```
