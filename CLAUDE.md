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
├── skills/
│   ├── python-peewee/         # Peewee ORM skill
│   │   └── SKILL.md
│   ├── python-project/        # Python project workflow skill
│   │   ├── SKILL.md
│   │   └── references/
│   └── slide-creator/        # Unified slide creation skill
│       ├── SKILL.md
│       └── references/
│           ├── color-design/       # Color system design
│           ├── marpit-authoring/   # Marpit Markdown slides
│           └── svg-illustration/   # SVG diagrams
├── GUIDE.md                   # Complete marketplace creation guide
├── README.md                  # Installation and usage instructions
├── CLAUDE.md                  # This file
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
Skills: `./skills/python-peewee`, `./skills/python-project`

**python-project skill**:
- Modern Python tooling patterns (uv, ruff, pytest, ty, typer, loguru)
- Project setup and dependency management
- Testing, type checking, and linting workflows
- CLI development with typer
- Logging best practices with loguru

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

## Validating Changes

After editing marketplace.json or adding plugins:

```shell
/plugin validate .
```

### Pre-commit Checks

This repository uses pre-commit hooks to ensure code quality. You can run checks manually using:

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

After editing GUIDE.md, verify:
- All JSON examples are syntactically valid
- Code block attributes are consistent (```json, ```bash, ```shell with theme={null})
- Internal links work correctly
- Schema tables match the examples
- Step-by-step walkthroughs use `<Steps>` and `<Step>` blocks
- Notes use `<Note>` blocks for important callouts
