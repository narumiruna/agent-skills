# UV Scripts

Use `uv run` to execute standalone Python scripts with automatic dependency management. Prefer inline metadata when the script should carry its own Python requirement and dependencies.

## Quick Reference

| Need | Command |
| --- | --- |
| Run a script | `uv run script.py` |
| Run a module | `uv run -m http.server 8000` |
| Run from stdin | `uv run -` |
| Skip project install | `uv run --no-project script.py` |
| One-off dependencies | `uv run --with requests --with rich script.py` |
| Pick Python | `uv run --python 3.12 script.py` |
| Initialize script metadata | `uv init --script script.py --python 3.12` |
| Add script dependencies | `uv add --script script.py requests rich` |
| Lock script dependencies | `uv lock --script script.py` |

## Project vs. No-Project Mode

- In a directory with `pyproject.toml`, `uv run` installs the project before execution.
- If the script does not need project code, use `uv run --no-project script.py`.
- The `--no-project` flag must appear before the script name.
- If the script uses inline metadata, project dependencies are ignored automatically.

## Inline Script Metadata

Recommended setup:

```bash
uv init --script example.py --python 3.12
uv add --script example.py 'requests<3' rich
```

Example:

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

resp = requests.get("https://peps.python.org/api/peps.json")
pprint(resp.json())
```

Rules:

- The metadata block must use `# /// script`.
- Include `dependencies`, even when empty.
- Inline metadata ignores project dependencies; do not combine it with assumptions about the local project environment.

## Reproducibility

Lock script dependencies when the script should remain stable over time:

```bash
uv lock --script example.py
```

This creates `example.py.lock` next to the script.

## Common Mistakes

- Using `python script.py` after manually installing dependencies.
- Forgetting `--no-project` when inside a project checkout.
- Putting `--no-project` after the script name.
- Omitting inline metadata for scripts meant to be portable and self-contained.
