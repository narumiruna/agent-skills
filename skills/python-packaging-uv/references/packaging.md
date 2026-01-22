# Packaging with uv

## Table of Contents

- [Building Packages](#building-packages)
- [Build Artifacts](#build-artifacts)
- [Pre-publish Checklist](#pre-publish-checklist)
- [Publishing](#publishing)
- [Common Issues](#common-issues)

Build and distribute Python packages using uv's built-in build tools.

## Building Packages

**Build both wheel and source distribution:**

```bash
uv build
```

**Build wheel only (faster, recommended for most cases):**

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

**1. Build succeeds:**
```bash
uv build --no-sources
```

**2. Test installation from wheel:**
```bash
uv pip install dist/my_package-1.0.0-py3-none-any.whl
```

**3. Verify package contents:**
```bash
unzip -l dist/my_package-1.0.0-py3-none-any.whl
```

## Publishing

**To PyPI:**
```bash
uv publish --token $PYPI_TOKEN
```

**To Test PyPI (recommended first):**
```bash
uv publish --publish-url https://test.pypi.org/legacy/ --token $TEST_PYPI_TOKEN
```

**Test installation from Test PyPI:**
```bash
uv pip install --index-url https://test.pypi.org/simple/ my-package
```

## Common Issues

**Missing files in wheel:**
- Ensure `src/` layout is used

**Import errors after installation:**
- Verify package name matches import name
- Check `[project]` name and `src/` directory structure

**Large package size:**
- Add `.pyc` and `__pycache__` to `.gitignore`
- Exclude test files and docs from wheel
