---
name: uv-scripts
description: Use when running or authoring standalone Python scripts with uv, especially when choosing Python versions, adding one-off dependencies, using no-project mode, or embedding inline script metadata.
---

# UV Scripts

## Overview
Use `uv run` to execute standalone scripts with automatic dependency management. Prefer inline metadata for self-contained scripts and `--no-project` when you are inside a project but do not need project code.

## Quick Reference

| Need | Command |
| --- | --- |
| Run a script | `uv run script.py` |
| Run module | `uv run -m http.server 8000` |
| Skip project install | `uv run --no-project script.py` |
| One-off deps | `uv run --with requests --with rich script.py` |
| Pick Python | `uv run --python <version> script.py` |
| Init script metadata | `uv init --script script.py --python <version>` |
| Add script deps | `uv add --script script.py requests rich` |

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
- When a project is present, `uv run` installs the current project first
- Use for scripts that depend on your project code

```bash
cd my-project/
uv run scripts/process_data.py
```

**Outside Project Context:**
- Use `--no-project` if the script does not depend on the project
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
uv init --script example.py --python <version>
```

**Add dependencies to script:**

```bash
uv add --script example.py requests rich
```

**Example script with inline metadata:**

```python
# /// script
# requires-python = ">=<min-version>"
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
uv run --python <version> example.py
```

**In inline metadata:**

```python
# /// script
# requires-python = ">=<min-version>"
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
# requires-python = ">=<min-version>"
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

## Common Mistakes

- Using `python script.py` after installing deps manually instead of `uv run`.
- Forgetting `--no-project` in project directories when you do not need project code.
- Omitting the `# /// script` metadata block when you want self-contained scripts.
