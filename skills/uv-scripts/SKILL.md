---
name: uv-scripts
description: Use when running or authoring standalone Python scripts with uv, especially when choosing Python versions, adding one-off dependencies, using no-project mode, or embedding inline script metadata.
---

# UV Scripts

## Overview
Use `uv run` to execute standalone scripts with automatic dependency management. Keep detailed examples in `references/uv-scripts.md` and load it when you need full patterns.

## Quick Reference

| Need | Command |
| --- | --- |
| Run a script | `uv run script.py` |
| Run module | `uv run -m http.server 8000` |
| Skip project install | `uv run --no-project script.py` |
| One-off deps | `uv run --with requests --with rich script.py` |
| Pick Python | `uv run --python <version> script.py` |

## Core Pattern

```bash
uv run --with rich --with requests script.py arg1 arg2
```

For inline metadata and script initialization, read `references/uv-scripts.md`.

## Common Mistakes

- Using `python script.py` after installing deps manually instead of `uv run`.
- Forgetting `--no-project` in project directories when you do not need project code.
- Omitting the `# /// script` metadata block when you want self-contained scripts.
