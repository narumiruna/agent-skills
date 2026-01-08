# Running Scripts with uv

## Table of Contents

- [Basic Usage](#basic-usage)
- [Project vs. No-Project Mode](#project-vs-no-project-mode)
- [One-off Dependencies](#one-off-dependencies)
- [Inline Script Metadata (Recommended)](#inline-script-metadata-recommended)
- [Python Version Selection](#python-version-selection)
- [Common Patterns](#common-patterns)

Use `uv run` for standalone scripts to automatically manage dependencies without manual venv setup.

## Basic Usage

**Run a Python script:**

```bash
uv run example.py
uv run example.py arg1 arg2
```

**Run a module:**

```bash
uv run -m http.server 8000
uv run -m pytest
```

## Project vs. No-Project Mode

**In Project Context:**
- When `pyproject.toml` exists, `uv run` installs the current project first
- Use for scripts that depend on your project code

```bash
cd my-project/
uv run scripts/process_data.py
```

**Outside Project Context:**
- Use `--no-project` if script doesn't depend on the project
- Faster execution, skips project installation

```bash
uv run --no-project example.py
```

## One-off Dependencies

Add ephemeral dependencies for a single invocation with `--with`:

**Single dependency:**
```bash
uv run --with rich example.py
```

**Version constraints:**
```bash
uv run --with 'rich>12,<13' example.py
```

**Multiple dependencies:**
```bash
uv run --with rich --with requests example.py
```

## Inline Script Metadata (Recommended)

Embed dependencies directly in the script for self-contained execution.

**Initialize script with metadata:**

```bash
uv init --script example.py --python 3.12
```

**Add dependencies to script:**

```bash
uv add --script example.py requests rich
```

**Example script with inline metadata:**

```python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
from rich.pretty import pprint


def fetch_peps():
    """Fetch and display Python PEPs."""
    resp = requests.get("https://peps.python.org/api/peps.json")
    resp.raise_for_status()
    data = resp.json()

    # Display first 10 PEPs
    peps = [(k, v["title"]) for k, v in data.items()][:10]
    pprint(peps)


if __name__ == "__main__":
    fetch_peps()
```

**Run the script:**

```bash
uv run example.py  # Dependencies auto-resolved from metadata
```

## Python Version Selection

**Specify Python version:**

```bash
uv run --python 3.12 example.py
uv run --python 3.11 example.py
```

**In inline metadata:**

```python
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
```

## Common Patterns

**Data processing script:**

```bash
uv run --with pandas --with matplotlib analyze.py data.csv
```

**Web scraping:**

```bash
uv run --with requests --with beautifulsoup4 scrape.py
```

**Quick testing tool:**

```bash
uv run --with pytest --no-project test_utils.py
```

**One-off utility in project:**

```python
#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.12"
# dependencies = ["typer", "rich"]
# ///

import typer
from rich.console import Console

console = Console()

def main(name: str) -> None:
    console.print(f"[bold green]Hello {name}![/bold green]")

if __name__ == "__main__":
    typer.run(main)
```

Make executable and run:
```bash
chmod +x example.py
./example.py Alice
```
