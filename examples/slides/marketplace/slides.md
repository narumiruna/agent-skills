---
marp: true
theme: default
paginate: true
backgroundColor: #1e3a5f
color: #e8d7b0
---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# 🔌 Narumi's Claude Marketplace

**Claude Code Plugin Marketplace**
Developer tools + complete documentation examples

---

<!-- _class: lead -->

## Two goals for this repository

**1. Working Marketplace**
Install-and-go developer tool plugins

**2. Documentation & Examples**
Learn how to build your own plugin marketplace

---

<style scoped>
table {
  background-color: #0d2438;
  color: #e8d7b0;
}
table th {
  background-color: #0a1520;
  color: #e8d7b0;
}
table td {
  background-color: #0d2438;
}
</style>

## 🎯 Core value

| ⚡ **Ready to use** | 📚 **Learning templates** | 🔧 **Extensible** |
|:---:|:---:|:---:|
| Three practical plugins | End-to-end examples | Customizable marketplace |
| Python + slide creation | Hooks + skills demos | Best-practice patterns |

---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# Three available plugins

**Code Quality + Development Skills + Slide Creation**

---

## 📦 Plugin overview

![w:1400](diagrams/three-plugins.svg)

---

## 🛡️ python-code-quality

**Automated code-quality checks**

Automatically runs before Edit/Write actions:
- `uv run ruff format` - Auto-format
- `uv run ruff check --fix` - Lint + auto-fix
- `uv run ty check` - Type checking

**Plugin type**: Hooks Plugin (PreToolUse)

**Highlights**: Zero config; works immediately after install

---

## 🎓 python-skills

**Comprehensive Python development toolkit**

Combines project workflow standards with ORM patterns

**Plugin type**: Skill Plugin (gives Claude Python development expertise)

---

## 🎓 python-skills (1/2)

**Python Project Workflow** (`python-project` skill)

- Modern toolchain: uv, ruff, pytest, ty, typer, loguru
- Project setup and dependency management
- Testing, type checking, linting patterns
- CLI development best practices

---

## 🎓 python-skills (2/2)

**Peewee ORM Patterns** (`python-peewee` skill)

- DatabaseProxy setup patterns
- Connection context + atomic transaction examples
- SQLite testing patterns

---

## 🎨 slide-skills (1/2)

**Complete Marp/Marpit slide toolkit**

One workflow: from color design to a final deck with diagrams

**Color Design module**
- Design a slide color system (background, text, accents)
- Three strategies: dark technical, light professional, accent-driven
- 10 ready-to-use palettes

**Marpit Authoring module**
- Write valid Marpit/Marp Markdown decks
- Theme support (default/gaia/uncover)
- Slide patterns (title, content, two-column, code)

---

## 🎨 slide-skills (2/2)

**SVG Illustration module**
- Create slide-ready SVG diagrams and illustrations
- Smart sizing optimized for Marp HTML export
- Pattern examples (flows, timelines, architecture)

**Architecture highlights**
- Progressive disclosure by design
- Load only the modules needed for the task
- End-to-end slide creation support

**Plugin type**: Skill Plugin

---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# Quick install

**Three simple steps**

---

## 🚀 Installation workflow

![w:1320](diagrams/workflow-overview.svg)

---

## Step 1: Add the marketplace

**Add from GitHub**

```bash
/plugin marketplace add narumi/claude-marketplace
```

**Local testing**

```bash
/plugin marketplace add ./path/to/claude-marketplace
```

---

## Step 2: Install plugins

Pick the plugins you need:

```bash
# Code-quality hook
/plugin install python-code-quality@narumi

# Python dev skills (project workflow + Peewee ORM)
/plugin install python-skills@narumi

# Slide creation skills
/plugin install slide-skills@narumi
```

---

## Step 3: Start using

Plugins activate immediately after installation

**Python automation**
- Auto-format while editing Python files
- Auto lint and fix issues
- Instant type-check feedback

---

## Step 3: Start using (continued)

**Slide creation guidance**
- Color system design suggestions
- Marpit syntax best practices
- Help creating SVG diagrams

**Claude gains expertise**
- Python project workflow standards
- Peewee ORM patterns and examples
- End-to-end slide creation workflow

---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# Learn and extend

**What this marketplace demonstrates**

---

## 📚 Example: Hooks plugin

**python-code-quality demonstrates PreToolUse hooks**

- Automatically intercepts file operations to run tools
- Runs quality checks before Edit/Write
- Shows how to build an automated workflow

---

## 📚 Example: Multi-skill plugin

**Integrating related skills**

- `python-skills` combines project workflow + Peewee ORM
- `slide-skills` uses progressive module loading
- Uses `strict: false` for inline plugin definitions

---

## 📚 Example: Directory structure

**A standardized marketplace layout**

- Plugins live in `plugins/`
- Shared skills live in `skills/`
- Each plugin is configured independently

---

## 🧪 Testing and validation

**Ensure the marketplace structure is valid**

```bash
/plugin validate .
```

**Local testing before publishing**

```bash
# 1. Add local marketplace
/plugin marketplace add .

# 2. List available plugins
/plugin list

# 3. Test install
/plugin install python-skills@narumi
```

---

## 📂 Marketplace structure

**Standard directory layout**

```
claude-marketplace/
├── plugins/
│   ├── python-code-quality/
│   ├── python-skills/
│   └── slide-skills/
└── skills/
    ├── python-project/
    ├── python-peewee/
    └── slide-creator/
```

---

## 📖 Full documentation

**Learn how to build your own marketplace**

**Core docs**
- **[GUIDE.md](GUIDE.md)** - Full guide to creating and publishing a Claude Code plugin marketplace
- **[CLAUDE.md](CLAUDE.md)** - Developer guidelines
- **[README.md](README.md)** - Quick start and installation instructions

**Implementation showcases**
- Hooks plugin (PreToolUse)
- Multi-skill plugin organization strategy
- Marketplace validation and testing workflow
- Progressive skill loading architecture

---

<!-- _class: lead -->
<!-- _backgroundColor: #0a1520 -->

# Get started

**Working Marketplace + Learning Resource**

🔗 **github.com/narumiruna/claude-marketplace**

Install useful plugins | Learn to build your own marketplace
