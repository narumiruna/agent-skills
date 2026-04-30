# Agent Skills

This repo hosts my personal agent skills.

## Available Plugins

- `python-skills` - Skill bundle for modern Python workflows and Peewee ORM patterns
- `slide-skills` - Umbrella + focused skills for Marp/Marpit slides (color, authoring, SVG) with fast routing
- `writing-skills` - IMRaD toolkit centered on a single `imrad` skill that auto-routes between applicability detection, drafting, recomposition, and review
- `gourmet-research` - Evidence-based gourmet research workflow for city dining recommendations

## Installation

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
just

# or
just sync
```

Remove the synced skills when finished:

```shell
just clean
```

## Learn More

This marketplace demonstrates:
- Multi-skill plugins (python-skills, slide-skills with multiple skills)
- Using `strict: false` for inline plugin definitions
- Organizing skills in `skills/` directory
- Marketplace validation and testing
- Entry skills for faster routing in multi-skill bundles
