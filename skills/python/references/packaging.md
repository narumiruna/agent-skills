# Packaging with uv

Use `uv build` and `uv publish` to produce artifacts and publish packages. Build first, verify the result, then publish.

## Commands

| Task | Command |
| --- | --- |
| Build wheel and sdist | `uv build` |
| Build wheel only | `uv build --wheel` |
| Build release artifacts | `uv build --no-sources` |
| Build with a specific Python | `uv build --python <version>` |
| Publish to PyPI | `uv publish --token $PYPI_TOKEN` |
| Publish to Test PyPI | `uv publish --publish-url https://test.pypi.org/legacy/ --token $TEST_PYPI_TOKEN` |

## Artifacts

Build output lands in `dist/`:

- `*.whl` for wheel distributions
- `*.tar.gz` for source distributions

## Pre-Publish Checks

Run these before release:

```bash
uv build --no-sources
uv pip install dist/my_package-1.0.0-py3-none-any.whl
unzip -l dist/my_package-1.0.0-py3-none-any.whl
```

For a first release, validate on Test PyPI before publishing to PyPI:

```bash
uv publish --publish-url https://test.pypi.org/legacy/ --token $TEST_PYPI_TOKEN
uv pip install --index-url https://test.pypi.org/simple/ my-package
```

## Common Issues

- Missing files in the wheel: verify package layout and included files.
- Import errors after install: check the `[project]` name, package directory, and import path.
- Publishing too early: do not skip local wheel verification.
