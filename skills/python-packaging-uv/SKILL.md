---
name: python-packaging-uv
description: Use when building or publishing Python packages with uv, including dist artifacts and pre-publish checks.
---

# Python Packaging with uv

## Overview

Use uv build and publish commands to produce wheels/sdists and ship to package indexes. Core principle: build from release-ready sources, verify artifacts, test installation, then publish.

## Use When

- Building wheels or source distributions.
- Preparing release artifacts with uv.
- Publishing to Test PyPI or PyPI.
- Verifying package contents or installation behavior before release.

## Quick Reference

| Task | Command |
| --- | --- |
| Build wheel+sdist | `uv build` |
| Build wheel only | `uv build --wheel` |
| Build for release (ignore local path overrides) | `uv build --no-sources` |
| Publish to PyPI | `uv publish --token $PYPI_TOKEN` |
| Publish to Test PyPI | `uv publish --publish-url https://test.pypi.org/legacy/ --token $TEST_PYPI_TOKEN` |
| Inspect wheel contents | `unzip -l dist/<wheel>.whl` |
| Test wheel install | `uv run --with dist/<wheel>.whl python -c "import <module>"` |

## Workflow

1. Run the repository quality gate before release.
2. Build artifacts in `dist/` with `uv build --no-sources`.
3. Inspect wheel and sdist contents.
4. Test install from the built wheel in a fresh uv-managed invocation.
5. Publish to Test PyPI for first or risky releases, validate install/import, then publish to PyPI.

## Example

```bash
prek run -a
uv build --no-sources
unzip -l dist/my_package-1.0.0-py3-none-any.whl
uv run --with dist/my_package-1.0.0-py3-none-any.whl python -c "import my_package"
uv publish --publish-url https://test.pypi.org/legacy/ --token $TEST_PYPI_TOKEN
```

## Common Mistakes

- Publishing before verifying wheel contents.
- Skipping Test PyPI for first release.
- Building release artifacts while local `[tool.uv.sources]` overrides are active.
- Verifying only the source tree instead of importing from the built wheel.

## Red Flags

- Packaging guidance that ignores uv build/publish.
- Publishing commands shown before quality checks and artifact verification.

## References

- `references/packaging.md` - Build and publish details
