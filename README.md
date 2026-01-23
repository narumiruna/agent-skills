# Agent Skills

This repo hosts my personal agent skills, packaged so they can be used in Codex or Claude Code.

## Available Plugins

- `python-skills` - Skill bundle for modern Python workflows and Peewee ORM patterns
- `slide-skills` - Umbrella + focused skills for Marp/Marpit slides (color, authoring, SVG) with fast routing
- `gourmet-research` - Evidence-based gourmet research workflow for city dining recommendations

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

# Install gourmet research workflow skills
/plugin install gourmet-research@narumi
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

- **[CLAUDE.md](CLAUDE.md)** - Developer guidance for working with this repository

## Learn More

This marketplace demonstrates:
- Multi-skill plugins (python-skills, slide-skills with multiple skills)
- Using `strict: false` for inline plugin definitions
- Organizing skills in `skills/` directory
- Marketplace validation and testing
- Entry skills for faster routing in multi-skill bundles
