---
name: creating-slide-decks
description: Use when creating slide decks with Marp/Marpit Markdown (marp), including authoring slide content, designing slide color schemes, and building SVG diagrams or illustrations for the deck.
---

# Slide Creation Toolkit

Create professional Marp/Marpit presentations, diagrams, and color systems with a consistent design language.

## Core rules

- Use `bg` syntax for full-slide or split-layout visuals; keep logos, icons, and other small images inline.
- Define one 7-role color palette and reuse it in slides and SVGs.
- Define one spacing unit (e.g., 8px or 16px) and reuse it across layouts.
- Define text hierarchy tiers (title/section/body) with sizes and weights; use them consistently.
- For SVGs, use one stroke width and one corner radius across shapes.

## Design guidance (non-enforceable)

- Aim for clear visual hierarchy with size, weight, and saturation.
- Prefer one visual language (fill vs outline, emphasis rules).
- Minimize visual noise; keep one primary visual anchor per section.

## Working directory

This umbrella skill does not own module assets or scripts.
Use the focused skills (`authoring-marp-slides`, `designing-slide-colors`, `creating-svg-illustrations`) for paths and commands.

## Start here (task entry)

**Entry skills (fast routing)**:
- `authoring-marp-slides` → Marp/Marpit authoring rules, layouts, themes
- `designing-slide-colors` → palette workflow and color roles
- `creating-svg-illustrations` → SVG diagram rules, patterns, embedding

Pick one task and follow the exact reading path:

- **Color palette only** → `designing-slide-colors`
- **Slides only (no diagrams)** → `authoring-marp-slides`
- **Diagram only** → `creating-svg-illustrations`
- **Slides + diagrams** → `authoring-marp-slides` → `creating-svg-illustrations`
- **Full deck (colors + slides + diagrams)** → `designing-slide-colors` → `authoring-marp-slides` → `creating-svg-illustrations`

## One-page quick reference

**Minimal steps (fast path)**:
1. Pick a palette → `designing-slide-colors`.
2. Draft slides → `authoring-marp-slides`.
3. Add SVG diagrams → `creating-svg-illustrations`.
4. Validate via the module skills.

**Common commands**:
- `designing-slide-colors` → palette scripts
- `authoring-marp-slides` → Marp validation/preview
- `creating-svg-illustrations` → SVG linting

**Output summary**: Use module-specific output examples via the entry skills.

## Quick Start

### Two Ways to Start

**Option 1: Use scripts** (automated):
Load `authoring-marp-slides`, resolve `scripts/init_presentation.py` against that skill directory, and run it by absolute path:

```bash
AUTHORING_MARP_SLIDES_SKILL_DIR="/absolute/path/to/authoring-marp-slides"
uv run "$AUTHORING_MARP_SLIDES_SKILL_DIR/scripts/init_presentation.py" technical-dark my-deck.md "My Title" "Author"
```

**Option 2: Work manually** (full control):
- Copy a template from `authoring-marp-slides` → `assets/templates/` → customize
- Design colors via `designing-slide-colors`
- Write slides via `authoring-marp-slides`
- Add diagrams via `creating-svg-illustrations`

**Study examples first**: Read `authoring-marp-slides` → `assets/examples/` to see working presentations before starting.

### Script Commands

Use `designing-slide-colors` for palette scripts and outputs.

**Templates** (starting points - copy and fill in your content):
- Use `authoring-marp-slides` → `assets/templates/`.

**Examples** (learning references - study patterns and copy techniques):
- `authoring-marp-slides` → `assets/examples/` for slide patterns.
- `creating-svg-illustrations` → `assets/examples/` for diagram examples.
- `designing-slide-colors` → `assets/examples/` for palette examples.

**Common icons** (ready to use in slides):
- `authoring-marp-slides` → `assets/icons/`.

## Quick index (where to look)

- **Reference hub**: `references/index.md`
- **Color design**: `designing-slide-colors`
- **Marpit authoring**: `authoring-marp-slides`
- **SVG illustration**: `creating-svg-illustrations`
- **Decision guide**: `references/decision-guide.md`

## Modules

Use the focused skills for module-specific rules and references:

- **Color design** → `designing-slide-colors`
- **Marpit authoring** → `authoring-marp-slides`
- **SVG illustration** → `creating-svg-illustrations`

## Workflow

### Single tasks

Draw a diagram:
1. Use `creating-svg-illustrations` for core rules and patterns.
2. Choose colors via `designing-slide-colors` or existing palette.

Design slide colors:
1. Use `designing-slide-colors` for workflow and templates.

Write slides:
1. Use `authoring-marp-slides` for syntax and layout patterns.
2. Apply a palette from `designing-slide-colors`.

### Full presentation

1. Establish a palette with the color module.
2. Outline slides and author via `authoring-marp-slides`.
3. Add diagrams via `creating-svg-illustrations`.
4. Keep palette, spacing, and hierarchy consistent.

## Decision guide

See [references/decision-guide.md](references/decision-guide.md) for a flowchart and loading strategy.

Quick rules:
```
Slides or deck -> authoring-marp-slides
Slides + colors -> designing-slide-colors -> authoring-marp-slides
Slides + diagrams -> authoring-marp-slides + creating-svg-illustrations
Diagram only -> creating-svg-illustrations
```

Scale reference loading:
```
Simple request -> core rules only
Complex request -> add patterns and best-practices
```

## Output formats

Use the focused skills for module-specific output formats:
- `designing-slide-colors` → `references/output-examples.md`
- `authoring-marp-slides` → `references/output-examples.md`
- `creating-svg-illustrations` → `references/output-examples.md`

## Integration rules

- Use palette hex values in SVG `fill` and `stroke`.
- Keep border radius and stroke widths consistent between Marpit and SVG.
- Embed SVGs with Markdown images or file references.

## Troubleshooting

Common cross-cutting issues:
- [references/troubleshooting-common.md](references/troubleshooting-common.md)
- [creating-svg-illustrations](../creating-svg-illustrations/SKILL.md) → `references/troubleshooting.md`

## Common mistakes

- Using absolute paths instead of relative paths for assets.
- Using multiple palettes across one deck or between slides and SVGs.
- Skipping validation checks (Marp, SVG lint, contrast).

See `authoring-marp-slides`, `designing-slide-colors`, and `creating-svg-illustrations` for module-specific mistakes.

## Quick check (minimal)

Use module-specific quick checks:
- `authoring-marp-slides` → validation/preview workflow
- `creating-svg-illustrations` → SVG lint checks
- `designing-slide-colors` → contrast checks

## Validation

Use the module-specific validation guides:
- `authoring-marp-slides` → `references/preview-workflow.md`
- `creating-svg-illustrations` → `references/troubleshooting.md`
- `designing-slide-colors` → `references/color-design/workflow.md` (validation checklist)

Always validate before committing files using the focused skills.

## Constraints

- Output Marpit Markdown only; do not generate PowerPoint/Keynote files.
- Output SVG only; do not generate raster images.
- Avoid interactive animations; keep slides static.
- Preserve provided brand colors; adapt them into the palette.
