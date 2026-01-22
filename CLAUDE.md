# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository serves two purposes:

1. **Example Marketplace**: A working Claude Code plugin marketplace (`narumi`) that demonstrates best practices
2. **Documentation**: GUIDE.md provides comprehensive instructions for creating and distributing Claude Code plugin marketplaces

## Repository Structure

```
.
├── .claude-plugin/
│   └── marketplace.json       # Marketplace catalog (defines available plugins)
├── .github/workflows/
│   └── marp-to-pages.yml     # CI workflow: builds slides → GitHub Pages
├── plugins/
│   └── python-code-quality/  # Hooks-based plugin (inline definition)
├── skills/
│   ├── python-peewee/         # Peewee ORM skill
│   │   └── SKILL.md
│   ├── python-modern-tooling/ # Umbrella routing skill
│   │   └── SKILL.md
│   ├── python-uv-project-setup/ # uv setup and run rules
│   │   └── SKILL.md
│   ├── python-quality-tooling/ # ruff/ty/pytest workflows
│   │   ├── SKILL.md
│   │   └── references/
│   ├── python-cli-typer/      # Typer CLI patterns
│   │   ├── SKILL.md
│   │   └── references/
│   ├── python-logging/        # stdlib logging and loguru guidance
│   │   ├── SKILL.md
│   │   └── references/
│   ├── python-packaging-uv/   # uv build/publish workflows
│   │   ├── SKILL.md
│   │   └── references/
│   └── slide-creator/        # Unified slide creation skill
│       ├── SKILL.md
│       └── references/
│           ├── color-design/       # Color system design
│           ├── marpit-authoring/   # Marpit Markdown slides
│           └── svg-illustration/   # SVG diagrams
├── scripts/
│   └── sync_skills.sh        # Development: sync skills to ~/.codex/skills/
├── examples/slides/          # Live slide examples (built by CI)
│   ├── marketplace/          # Marketplace demo presentation
│   └── meanflows/            # Meanflows methodology presentation
├── build/                    # Generated: Marp HTML output (gitignored)
├── GUIDE.md                  # Complete marketplace creation guide
├── README.md                 # Installation and usage instructions
├── CLAUDE.md                 # This file
└── LICENSE
```

## Key Concepts

### Marketplace Architecture

Plugin marketplaces enable centralized distribution of Claude Code extensions. The system follows this structure:

- **Marketplace file**: `.claude-plugin/marketplace.json` defines the catalog
- **Plugin entries**: Each entry specifies name, source, and metadata
- **Plugin sources**: Can be relative paths, GitHub repos, or Git URLs
- **Plugin manifest**: Individual plugins have their own `plugin.json` (unless `strict: false`)

### Important Variables

- `${CLAUDE_PLUGIN_ROOT}`: Used in plugin configs to reference files within the plugin's installation directory (since plugins are copied to cache)

### Reserved Marketplace Names

The following names are blocked for official Anthropic use:
- claude-code-marketplace
- claude-code-plugins
- claude-plugins-official
- anthropic-marketplace
- anthropic-plugins
- agent-skills
- life-sciences

## Documentation Guidelines

When editing GUIDE.md:

1. **Maintain the structure**: Steps, examples, schema tables, and troubleshooting sections follow a specific pattern
2. **Use theme={null}**: Code blocks use `theme={null}` attribute for documentation rendering
3. **Include working examples**: All JSON examples should be valid and complete
4. **Cross-reference related sections**: Use relative links to other sections
5. **Keep schema tables accurate**: Required/optional fields must match actual implementation
6. **Validation commands**: Reference both CLI (`claude plugin validate`) and in-app (`/plugin validate`) commands

## Technical Details

### Plugin Installation Flow

1. User adds marketplace: `/plugin marketplace add <source>`
2. Claude Code fetches `.claude-plugin/marketplace.json`
3. User installs plugin: `/plugin install <name>@<marketplace>`
4. Plugin files are **copied** to cache (not symlinked by default)
5. Files outside plugin directory won't be available unless using symlinks

This copying behavior is critical for understanding why `../` references don't work and why `${CLAUDE_PLUGIN_ROOT}` is necessary.

### Strict Mode

The `strict` field in plugin entries controls manifest requirements:
- `true` (default): Plugin must have its own `plugin.json`, marketplace entry merges with it
- `false`: Plugin doesn't need `plugin.json`, marketplace entry defines everything

This is key for simple plugin definitions vs. complex multi-component plugins.

## This Marketplace's Plugins

This repository contains three example plugins:

### 1. python-code-quality (hooks-based)

Location: `./plugins/python-code-quality`
- Uses PreToolUse hooks to run code quality tools automatically
- Runs before Edit/Write operations on Python files
- No skills, only hooks
- Inline definition with `strict: false`

Commands executed:
- `uv run ruff format` - Auto-format Python code
- `uv run ruff check --fix` - Lint and auto-fix issues
- `uv run ty check` - Type checking

### 2. python-skills (multi-skill)

Location: `./` (root)
Skills: `./skills/python-peewee`, `./skills/python-modern-tooling`, `./skills/python-uv-project-setup`, `./skills/python-quality-tooling`, `./skills/python-cli-typer`, `./skills/python-logging`, `./skills/python-packaging-uv`

**python-modern-tooling skill**:
- Umbrella routing to focused Python tooling skills
- Chooses the right workflow for setup, quality, CLI, logging, packaging

**python-uv-project-setup skill**:
- uv-based setup for projects and scripts
- Dependency management and `uv run` execution rules

**python-quality-tooling skill**:
- ruff/ty/pytest quality gates and CI patterns

**python-cli-typer skill**:
- Typer CLI patterns and structure

**python-logging skill**:
- stdlib logging vs loguru guidance

**python-packaging-uv skill**:
- Build and publish workflows with uv

**python-peewee skill**:
- DatabaseProxy setup patterns
- Connection context management
- Atomic transaction examples
- Testing patterns with SQLite
- ORM best practices

### 3. slide-skills (unified skill, v0.0.4)

Location: `./` (root)
Skills: `./skills/slide-creator` (unified skill with modular references)

**Architecture**: Progressive disclosure design with a lean SKILL.md (~250 lines) that loads references on-demand.

**slide-creator skill**:
- Unified presentation creation workflow: color design → slides → diagrams
- Three integrated modules accessible via single entry point
- Shared design principles ensure visual consistency across all outputs

**Module 1: Color Design** (`references/color-design/`):
- 5-step workflow for designing slide color systems
- Three strategies: Dark Technical, Light Professional, Accent-Driven
- 10 ready-to-use palettes with contrast validation
- Output templates and examples
- References:
  - `workflow.md` - Complete color design process
  - `strategies.md` - Strategy selection guide
  - `palettes.md` - 10 tested color palettes
  - `output-template.md` - Example outputs

**Module 2: Marpit Authoring** (`references/marpit-authoring/`):
- Valid Marpit/Marp Markdown slide creation
- Theme support (default/gaia/uncover)
- Slide patterns, directives, frontmatter
- Visual consistency and best practices
- References:
  - `syntax-guide.md` - Marpit syntax fundamentals
  - `patterns.md` - Common slide patterns
  - `themes.md` - Theme-specific features
  - `best-practices.md` - Consistency guidelines
  - `advanced-layouts.md` - Complex layouts

**Module 3: SVG Illustration** (`references/svg-illustration/`):
- Create slide-ready SVG diagrams and illustrations
- Smart sizing logic for different contexts
- Optimized for Marp HTML export
- Pattern examples and troubleshooting
- References:
  - `core-rules.md` - SVG basics and sizing
  - `embedding.md` - Embedding methods
  - `pattern-examples.md` - Flowcharts, timelines, architecture
  - `color-palettes.md` - SVG-specific colors
  - `troubleshooting.md` - Common issues

**Benefits of unified architecture**:
- Progressive disclosure: Load only needed modules (saves ~30% context for complex tasks)
- Unified design principles: Visual consistency written once, applied everywhere
- Clear workflow: Guided sequence from color → slides → diagrams
- Modular yet cohesive: Each module can be used independently or together

## Adding New Plugins

When adding plugins to this marketplace:

1. **For skills**: Create a directory in `skills/<skill-name>/` with `SKILL.md`
2. **For multi-skill plugins**: Reference multiple skills in the `skills` array
3. **For hooks-only**: Define inline in marketplace.json with `strict: false`
4. **Update marketplace.json**: Add plugin entry with name, source, description, version, keywords
5. **Update README.md**: Document the new plugin in the "Available Plugins" section
6. **Test locally**: Use `/plugin marketplace add .` then `/plugin install <name>@narumi`

## Common Development Workflows

### Testing Marketplace Changes Locally

After modifying marketplace.json or plugins:

1. **Validate marketplace structure**:
   ```shell
   /plugin validate .
   ```

2. **Test installation locally**:
   ```shell
   /plugin marketplace add .
   /plugin install <plugin-name>@narumi
   ```

3. **Remove and reinstall** (after making changes):
   ```shell
   /plugin uninstall <plugin-name>
   /plugin install <plugin-name>@narumi
   ```

### Working with Skills During Development

Use the Makefile to sync skills to `~/.codex/skills/` for rapid testing without reinstalling plugins (requires `stow`):

```shell
make sync
```

Remove the synced skills when you are done:

```shell
make clean
```

This is useful when iterating on skill content (SKILL.md and references/) without going through the full plugin installation flow.

### Building and Previewing Slides

The `examples/slides/` directory contains live slide examples that are built and deployed via GitHub Actions.

**Build slides locally** (requires Docker):
```shell
docker run --rm -v $PWD:/home/marp/app/ -e MARP_USER="$(id -u):$(id -g)" marpteam/marp-cli:latest -I examples/slides -o build/
```

**Preview built slides**:
```shell
# After building, open in browser
open build/marketplace/slides.html
open build/meanflows/slides.html
```

**Slide project structure**:
```
examples/slides/<project>/
├── slides.md          # Marpit Markdown source
├── README.md          # Project description
└── diagrams/          # SVG illustrations (optional)
    └── *.svg
```

The CI workflow (`.github/workflows/marp-to-pages.yml`):
1. Copies all slide assets from `examples/slides/` to `build/`
2. Runs Marp CLI to convert `.md` → `.html`
3. Deploys to GitHub Pages (production on push to main, preview on PRs)

### Pre-commit Checks

This repository uses pre-commit hooks to ensure code quality. Run checks manually:

**Using prek** (recommended):
```shell
prek run --all-files
```

**Using pre-commit**:
```shell
pre-commit run --all-files
```

**Installation** (if not already installed):
```shell
# Install prek
uv tool install prek

# Or install pre-commit
uv tool install pre-commit
```

**Configured hooks**:
- YAML/JSON validation
- Line ending normalization (LF)
- Trailing whitespace removal
- SVG linting
- Python: ruff (format + lint), ty (type check)

### Documentation Editing Guidelines

After editing GUIDE.md, verify:
- All JSON examples are syntactically valid
- Code block attributes are consistent (```json, ```bash, ```shell with theme={null})
- Internal links work correctly
- Schema tables match the examples
- Step-by-step walkthroughs use `<Steps>` and `<Step>` blocks
- Notes use `<Note>` blocks for important callouts
