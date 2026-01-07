# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This repository serves two purposes:

1. **Example Marketplace**: A working Claude Code plugin marketplace (`narumi-marketplace`) that demonstrates best practices
2. **Documentation**: GUIDE.md provides comprehensive instructions for creating and distributing Claude Code plugin marketplaces

## Repository Structure

```
.
├── .claude-plugin/
│   └── marketplace.json       # Marketplace catalog (defines available plugins)
├── skills/
│   └── python-peewee/         # Skill plugin source directories
│       └── SKILLS.md          # Skill content in markdown format
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

This repository contains two example plugins:

### 1. python-code-quality (hooks-based)
- **Type**: Hooks plugin (no skill content, only PreToolUse hooks)
- **Source**: `./plugins/python-code-quality` (currently not created - defined inline with `strict: false`)
- **Purpose**: Automatically runs code quality tools before Edit/Write operations
- **Hooks**:
  - `uv run ruff format` - Code formatting
  - `uv run ruff check --fix` - Linting with auto-fixes
  - `uv run ty check` - Type checking
- **Note**: Uses `strict: false` so all configuration is in marketplace.json

### 2. python-peewee (skill-based)
- **Type**: Skill plugin
- **Source**: `./skills/python-peewee/SKILLS.md`
- **Purpose**: Provides patterns for using Peewee ORM with DatabaseProxy
- **Content**: Markdown-based skill with setup patterns, connection/transaction examples, and testing templates
- **Note**: Uses `strict: false` so plugin.json is not required

## Adding New Plugins

When adding plugins to this marketplace:

1. **For skills**: Create a directory in `skills/<plugin-name>/` with `SKILLS.md`
2. **For hooks-only**: Define inline in marketplace.json with `strict: false`
3. **Update marketplace.json**: Add plugin entry with name, source, description, version, keywords
4. **Update README.md**: Document the new plugin in the "Available Plugins" section
5. **Test locally**: Use `/plugin marketplace add .` then `/plugin install <name>@narumi-marketplace`

## Validating Changes

After editing marketplace.json or adding plugins:

```shell
/plugin validate .
```

After editing GUIDE.md, verify:
- All JSON examples are syntactically valid
- Code block attributes are consistent (```json, ```bash, ```shell with theme={null})
- Internal links work correctly
- Schema tables match the examples
- Step-by-step walkthroughs use `<Steps>` and `<Step>` blocks
- Notes use `<Note>` blocks for important callouts
