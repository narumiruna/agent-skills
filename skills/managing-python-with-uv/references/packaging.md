# Packaging with uv

## Table of Contents

- [Building Packages](#building-packages)
- [Build Artifacts](#build-artifacts)
- [Pre-publish Checklist](#pre-publish-checklist)
- [Publishing](#publishing)
- [Common Issues](#common-issues)

Build and distribute Python packages using uv's built-in build tools. Release flow is: run the quality gate, build from release-ready sources, inspect artifacts, test wheel installation, publish to Test PyPI when appropriate, then publish to PyPI.

## Building Packages

**Build both wheel and source distribution:**

```bash
uv build
```

**Build wheel only:**

```bash
uv build --wheel
```

**Build for release (ignore `[tool.uv.sources]` local path overrides):**

```bash
uv build --no-sources
```

**Build with a specific Python version:**

```bash
uv build --python <version>
```

## Build Artifacts

Output is placed in the `dist/` directory:

- `*.whl` - Wheel package (binary distribution)
- `*.tar.gz` - Source distribution (sdist)

**Wheel format:**
```
my_package-1.0.0-py3-none-any.whl
```

**Source distribution format:**
```
my_package-1.0.0.tar.gz
```

## Pre-publish Checklist

Before publishing, verify:

**1. Quality gate passes:**
```bash
prek run -a
```

**2. Build succeeds:**
```bash
uv build --no-sources
```

**3. Verify package contents:**
```bash
unzip -l dist/my_package-1.0.0-py3-none-any.whl
tar -tzf dist/my_package-1.0.0.tar.gz
```

**4. Test installation from wheel and import from the artifact:**
```bash
uv run --with dist/my_package-1.0.0-py3-none-any.whl python -c "import my_package"
```

## Publishing

Keep upload tokens out of command arguments. Set `UV_PUBLISH_TOKEN` through the shell's secure environment or CI secret store, then publish without a token flag.

**To PyPI:**
```bash
UV_PUBLISH_TOKEN="$PYPI_TOKEN" uv publish
```

**To Test PyPI (recommended first):**
```bash
UV_PUBLISH_TOKEN="$TEST_PYPI_TOKEN" \
UV_PUBLISH_URL="https://test.pypi.org/legacy/" \
uv publish
```

Prefer trusted publishing in supported CI environments so no long-lived upload token is required.

**Test installation from Test PyPI:**
```bash
uv run --with my-package --index-url https://test.pypi.org/simple/ python -c "import my_package"
```

## Common Issues

**Missing files in wheel:**
- Ensure `src/` layout is used

**Import errors after installation:**
- Verify package name matches import name
- Check `[project]` name and `src/` directory structure
- Test import from the built wheel, not from the source checkout

**Large package size:**
- Add `.pyc` and `__pycache__` to `.gitignore`
- Exclude test files and docs from wheel
