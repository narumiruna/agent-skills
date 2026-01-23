# narumi

A working example of a Claude Code plugin marketplace with development tools and comprehensive documentation.

## About This Repository

This repository serves two purposes:

1. **Working Marketplace**: Install plugins for Python development (code quality hooks, project workflow standards, and ORM patterns)
2. **Documentation & Examples**: Learn how to create your own plugin marketplace (see [GUIDE.md](GUIDE.md))

## Available Plugins

- `python-skills` - Skill bundle for modern Python workflows and Peewee ORM patterns
- `slide-skills` - Skill bundle for Marp/Marpit slide creation (color, authoring, SVG) with entry skills for faster routing

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
# Install Python development skills (includes project workflow + Peewee ORM)
/plugin install python-skills@narumi

# Install presentation slide creation skills
/plugin install slide-skills@narumi
```

### Codex (local skills)

Codex does not support marketplaces. Use one of the following:

Option A: Copy skills directly into `~/.codex/skills/`:
```shell
cp -R ./skills/* ~/.codex/skills/
```

Option B: Use `stow` to create symlinks (recommended for development).
Install `stow`:
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

## Documentation

- **[GUIDE.md](GUIDE.md)** - Complete guide for creating and distributing Claude Code plugin marketplaces
- **[CLAUDE.md](CLAUDE.md)** - Developer guidance for working with this repository

## Learn More

This marketplace demonstrates:
- Multi-skill plugins (python-skills, slide-skills with multiple skills)
- Using `strict: false` for inline plugin definitions
- Organizing skills in `skills/` directory
- Marketplace validation and testing
- Entry skills for faster routing in multi-skill bundles
