---
name: managing-python-projects
description: "Use when a task involves Python project setup or standalone scripts with uv, including dependency management, `uv run`, `uv run --with`, `--no-project`, inline script metadata, quality gates (ruff, ty, pytest, coverage, prek/pre-commit), and package build or publishing workflows."
---

# Python

## Core Posture

Use uv as the default workflow for Python projects, standalone scripts, dependency management, quality checks, and package release. Prefer the repository's existing configuration and documented commands over introducing new tooling.

## Mode Selection

- Choose project mode when the work has a `pyproject.toml`, shared package code, or lockfile.
- Treat a brand-new repository created with `uv init` as project mode.
- Choose standalone-script mode when the work is a single file, stdin snippet, or ad hoc invocation that should not become a full project.
- Treat a script inside a project as project mode when it imports local package code.
- Use `--no-project` only when a script must ignore the surrounding project.

## Project Workflow

1. Inspect `pyproject.toml`, lockfiles, repository docs, and existing test/tooling choices before changing dependencies or commands.
2. For a brand-new project, run `uv init <name>`, then install the default dev toolchain with `uv add --dev ruff ty pytest pytest-cov`.
3. Use pytest as the default test framework for new projects: function-based `tests/test_*.py` files with plain `assert`.
4. Add dependencies with `uv add`; remove them with `uv remove`; reconcile external dependency changes with `uv sync`.
5. Run project Python, tests, and tools through `uv run` unless the repository provides a documented wrapper command; for pytest, default to an explicit `tests` target when the project does not document another test location.
6. Run the repository quality gate before finalizing dependency or code changes.

## Standalone Script Workflow

1. Decide whether the script should use project dependencies, one-off `--with` dependencies, or inline metadata.
2. Use plain `uv run script.py` when no extra dependencies are needed.
3. Use `uv run --with ... script.py` for disposable per-invocation dependencies.
4. Use `uv init --script` and `uv add --script` when dependencies should live with the script.
5. Put `--no-project` before the script name, and never use it for a script that imports local package code.
6. Use `uv run --python <version>` or `requires-python` in metadata when the script needs a specific Python version.
7. Read `references/scripts.md` for stdin, heredoc, shebang, alternate indexes, Windows `.pyw`, locking, and reproducibility details.

## Non-Negotiable Rules

- Manage dependencies with `uv add`, `uv remove`, and `uv sync`; do not use `pip install` to mutate a project environment.
- Run Python, pytest, scripts, and Python tools with `uv run` unless a repository command wraps them; when no project-specific pytest target is documented, include `tests` explicitly (for example, `uv run pytest tests`) rather than bare `uv run pytest`.
- Follow existing repository choices; do not migrate test frameworks, hook runners, or tool configuration unless asked.
- For a brand-new project, immediately add `ruff`, `ty`, `pytest`, and `pytest-cov`; do not start with `unittest`, `unittest.TestCase`, or class-based `Test*` suites.
- Do not create a `pyproject.toml` only to run a one-file script.
- Treat `uv run --with` as disposable; use inline metadata when the script should be shared or reused.
- Build release artifacts with `uv build --no-sources` so local `[tool.uv.sources]` overrides do not leak into release output.
- Test installs from the built wheel or published artifact, not only from the source checkout.

## Quality Gate Priority

Use this order before finalizing code, dependency, or packaging changes:

1. The repository's documented aggregate gate.
2. `prek run -a` when the repo uses prek.
3. The documented `pre-commit` command when the repo uses pre-commit and provides no prek path.
4. Individual `uv run ...` commands only when no aggregate gate exists or when narrowing failures.

Do not introduce or switch hook runners only for verification. Read `references/quality.md` for command details, coverage, CI examples, and fallback checks.

## Release Workflow

1. Run the repository quality gate.
2. Build artifacts in `dist/` with `uv build --no-sources`.
3. Inspect wheel and sdist contents.
4. Test install from the built wheel or published artifact in a fresh uv-managed invocation.
5. Read `references/packaging.md` for publish commands, Test PyPI flow, and artifact inspection details.

## Common Mistakes

- Treating a one-file script as project work when inline metadata or `--no-project` would be smaller and clearer.
- Using `--no-project` for a script that imports local package code.
- Keeping reusable script dependencies only in `uv run --with ...` shell history instead of the script metadata.
- Starting a brand-new project with `unittest` or without the default dev toolchain.
- Running tools outside uv.
- Publishing before verifying artifacts.

## References

- `references/quality.md` - Full commands, CI examples, coverage, prek, and pre-commit fallback usage.
- `references/packaging.md` - Build, inspect, and publish details.
- `references/scripts.md` - Standalone script patterns, inline metadata, locking, and special cases.
