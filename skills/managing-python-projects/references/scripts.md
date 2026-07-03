# Standalone Scripts with uv

## Table of Contents

- [Basic Invocations](#basic-invocations)
- [No-Project Mode](#no-project-mode)
- [One-Off Dependencies with `--with`](#one-off-dependencies-with---with)
- [Inline Script Metadata](#inline-script-metadata)
- [Shebang Executable Scripts](#shebang-executable-scripts)
- [Locking and Reproducibility](#locking-and-reproducibility)
- [Alternative Package Indexes](#alternative-package-indexes)
- [Python Version Selection](#python-version-selection)
- [Windows GUI Scripts](#windows-gui-scripts)

Use these patterns when the work is a standalone Python script rather than a shared project. Prefer inline metadata when the script should be reused or shared; prefer `uv run --with ...` for disposable one-off dependencies.

## Basic Invocations

Run a script without extra dependencies:

```bash
uv run example.py
uv run example.py arg1 arg2
```

Run a module:

```bash
uv run -m http.server 8000
uv run -m pytest
```

Read from stdin:

```bash
echo 'print("hello")' | uv run -
```

Here-doc:

```bash
uv run - <<EOF
print("hello")
EOF
```

## No-Project Mode

- In a project directory, `uv run` installs the project first.
- Use `--no-project` only when the script must ignore the surrounding project and does not import local package code.
- Put `--no-project` before the script name.

```bash
uv run --no-project example.py
```

If a script uses inline metadata, project dependencies are ignored automatically and `--no-project` is not required.

## One-Off Dependencies with `--with`

Use `--with` for disposable, per-invocation dependencies:

```bash
uv run --with rich example.py
uv run --with 'rich>12,<13' example.py
uv run --with rich --with requests example.py
```

In a project, these dependencies are added on top of project dependencies. Use `--no-project` when the script should not see the project environment.

## Inline Script Metadata

Initialize inline metadata:

```bash
uv init --script example.py --python 3.12
```

Add dependencies:

```bash
uv add --script example.py 'requests<3' 'rich'
```

Example script:

```python
# /// script
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
```

Use inline metadata when the script should be reproducible, executable by other users, or kept outside a full project.

Notes:
- The `dependencies` field must be provided even if empty.
- Inline metadata ignores project dependencies.

Specify a Python requirement in metadata:

```python
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
```

`uv run` will locate, and if needed download, the required Python version.

## Shebang Executable Scripts

```python
#!/usr/bin/env -S uv run --script

print("Hello, world!")
```

Make executable and run:

```bash
chmod +x greet
./greet
```

Dependencies are supported in this mode via inline metadata.

## Locking and Reproducibility

Lock dependencies for a script:

```bash
uv lock --script example.py
```

This creates `example.py.lock` next to the script. Subsequent `uv run --script`, `uv add --script`, and `uv export --script` reuse the lock.

To improve reproducibility across time, add `exclude-newer`:

```python
# /// script
# dependencies = ["requests"]
# [tool.uv]
# exclude-newer = "2023-10-16T00:00:00Z"
# ///
```

## Alternative Package Indexes

```bash
uv add --index "https://example.com/simple" --script example.py 'requests<3' 'rich'
```

This adds `tool.uv.index` metadata to the script.

## Python Version Selection

```bash
uv run --python 3.10 example.py
```

Use `uv run --python` for ad hoc selection, or `requires-python` in script metadata when the script should carry its own version requirement.

## Windows GUI Scripts

On Windows, `.pyw` scripts run with `pythonw`:

```bash
uv run example.pyw
```

Dependencies still work, for example `uv run --with PyQt5 example.pyw`.
