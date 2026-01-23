# narumi

A working example of a Claude Code plugin marketplace with development tools and comprehensive documentation.

## About This Repository

This repository serves two purposes:

1. **Working Marketplace**: Install plugins for Python development (code quality hooks, project workflow standards, and ORM patterns)
2. **Documentation & Examples**: Learn how to create your own plugin marketplace (see [GUIDE.md](GUIDE.md))

## Available Plugins

### python-code-quality

Python code quality hooks that automatically run before Edit/Write operations:
- `uv run ruff format` - Auto-format code
- `uv run ruff check --fix` - Lint and auto-fix issues
- `uv run ty check` - Type checking

**Type**: Hooks plugin (PreToolUse)

### python-skills

Comprehensive Python development toolkit combining project workflow standards and ORM patterns:

**Python Modern Tooling** (`python-modern-tooling` umbrella):
- Routes requests to focused skills for setup, quality, CLI, logging, packaging

**uv Project Setup** (`python-uv-project-setup`):
- Project and script setup with uv
- Dependency management and `uv run` rules

**Quality Tooling** (`python-quality-tooling`):
- ruff, ty, pytest, coverage, CI gate patterns

**CLI with Typer** (`python-cli-typer`):
- Typer command patterns and structure

**Logging** (`python-logging`):
- stdlib logging vs loguru guidance

**Packaging with uv** (`python-packaging-uv`):
- Build and publish workflows

**Peewee ORM Patterns** (`python-peewee` skill):
- DatabaseProxy setup patterns
- Connection context and atomic transaction examples
- Testing patterns with SQLite

**Type**: Skill plugin (provides Claude with Python development expertise)

### slide-skills

Complete Marp/Marpit presentation toolkit for creating professional slides with unified workflow from color design to final slides with diagrams.

**Unified slide-creator skill** with three integrated modules:

**Module 1: Color Design**
- Design slide color systems (background, text, accents)
- Three strategies: Dark Technical, Light Professional, Accent-Driven
- 10 ready-to-use color palettes
- Step-by-step workflow with validation checklist

**Module 2: Marpit Authoring**
- Write valid Marpit/Marp Markdown slides
- Theme support (default/gaia/uncover)
- Slide patterns (title, content, two-column, code)
- Directives, frontmatter, and best practices
- Visual consistency guidelines

**Module 3: SVG Illustration**
- Create slide-ready SVG diagrams and illustrations
- Smart sizing logic for different contexts
- Pattern examples (flowcharts, timelines, architecture)
- Optimized for Marp HTML export
- Embedding methods and troubleshooting

**Architecture**: Progressive disclosure design - loads only needed modules/references based on task complexity.

**Type**: Skill plugin (provides Claude with end-to-end presentation creation expertise)

## Installation

### Claude Code (marketplace)

Add this marketplace:
```shell
/plugin marketplace add narumi/agent-skills
```

Or for local testing:
```shell
/plugin marketplace add ./path/to/agent-skills
```

Install plugins:
```shell
# Install code quality hooks
/plugin install python-code-quality@narumi

# Install Python development skills (includes project workflow + Peewee ORM)
/plugin install python-skills@narumi

# Install presentation slide creation skills
/plugin install slide-skills@narumi
```

## Testing & Validation

Validate the marketplace structure:
```shell
/plugin validate .
```

### Codex (local skills)

Install `stow` (required):
```shell
# Linux (Debian/Ubuntu)
sudo apt update
sudo apt install -y stow

# macOS (using Homebrew)
brew install stow
```

Sync skills into `~/.codex/skills/` using the Makefile:

```shell
make sync
```

Remove the synced skills when finished:

```shell
make clean
```

Test locally before publishing:
```shell
/plugin marketplace add .
/plugin list
/plugin install python-skills@narumi
```

## Documentation

- **[GUIDE.md](GUIDE.md)** - Complete guide for creating and distributing Claude Code plugin marketplaces
- **[CLAUDE.md](CLAUDE.md)** - Developer guidance for working with this repository

## Learn More

This marketplace demonstrates:
- Hooks-based plugins (python-code-quality)
- Multi-skill plugins (python-skills, slide-skills with multiple skills)
- Using `strict: false` for inline plugin definitions
- Organizing skills in `skills/` directory
- Marketplace validation and testing
