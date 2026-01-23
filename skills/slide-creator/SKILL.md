---
name: slide-creator
description: Use when creating slide decks with Marp/Marpit Markdown (marp), including authoring slide content, designing slide color schemes, and building SVG diagrams or illustrations for the deck.
---

# Slide Creation Toolkit

Create professional Marp/Marpit presentations, diagrams, and color systems with a consistent design language.

## Core rules

- **Use `bg` (background) syntax for all images** - Reduces manual resizing with `fit` modifier
- Define one 7-role color palette and reuse it in slides and SVGs.
- Define one spacing unit (e.g., 8px or 16px) and reuse it across layouts.
- Define text hierarchy tiers (title/section/body) with sizes and weights; use them consistently.
- For SVGs, use one stroke width and one corner radius across shapes.

## Design guidance (non-enforceable)

- Aim for clear visual hierarchy with size, weight, and saturation.
- Prefer one visual language (fill vs outline, emphasis rules).
- Minimize visual noise; keep one primary visual anchor per section.

## Working directory

All paths and commands in this skill assume you are running from `skills/slide-creator/`.
If running from the repo root, prefix paths with `skills/slide-creator/`.

Example (from repo root):
```bash
bash skills/slide-creator/scripts/validate_marpit.sh slides.md
```

## Start here (task entry)

**Entry skills (fast routing)**:
- `marp-authoring` → Marp/Marpit authoring rules, layouts, themes
- `slide-color-design` → palette workflow and color roles
- `svg-illustration` → SVG diagram rules, patterns, embedding

Pick one task and follow the exact reading path:

- **Color palette only** → `slide-color-design`
- **Slides only (no diagrams)** → `marp-authoring`
- **Diagram only** → `svg-illustration`
- **Slides + diagrams** → `marp-authoring` → `svg-illustration`
- **Full deck (colors + slides + diagrams)** → `slide-color-design` → `marp-authoring` → `svg-illustration`

## One-page quick reference

**Minimal steps (fast path)**:
1. Pick a palette (or generate from brand).
2. Draft slides in Marp (via `marp-authoring`).
3. Add SVG diagrams if needed (via `svg-illustration`).
4. Validate output.

**Common commands**:
```bash
uv run scripts/init_presentation.py technical-dark my-deck.md "My Title" "Author"
uv run scripts/generate_palette.py list
uv run scripts/generate_palette.py show code-blue
uv run scripts/generate_palette.py brand "#FF6B35" light
uv run scripts/generate_palette.py svg-show default
svglint diagram.svg
bash scripts/validate_marpit.sh slides.md
```

**Output summary**: See **Output formats** and `references/output-examples.md` for full templates.

## Quick Start

### Two Ways to Start

**Option 1: Use scripts** (automated):
```bash
uv run scripts/init_presentation.py technical-dark my-deck.md "My Title" "Author"
```

**Option 2: Work manually** (full control):
- Copy a template from `assets/templates/` → customize
- Design colors via `slide-color-design`
- Write slides via `marp-authoring`
- Add diagrams via `svg-illustration`

**Study examples first**: Read `assets/examples/` to see working presentations before starting.

### Script Commands

**Browse and generate color palettes**:
See **Common commands** (above) for palette and SVG helpers.

**Templates** (starting points - copy and fill in your content):
- `assets/templates/minimal.md` - Bare minimum structure (5 slides)
- `assets/templates/technical-dark.md` - Dark theme for code/technical content
- `assets/templates/professional-light.md` - Light theme for business presentations
- `assets/templates/minimal-keynote.md` - Minimal design for story-driven talks
- `assets/templates/with-bg-images.md` - Template showcasing bg syntax for images

**Examples** (learning references - study patterns and copy techniques):
- `assets/examples/with-bg-syntax.md` - Shows all bg syntax patterns (full-page, split, comparison)
- `assets/examples/with-diagrams.md` - Shows inline SVG diagram integration
- `assets/examples/with-palette.md` - Shows custom palette application
- `assets/examples/full-presentation.md` - Shows all features combined (architecture + charts + code)

**Common icons** (ready to use in slides):
```markdown
![width:60px](assets/icons/check.svg)    <!-- ✓ checkmark -->
![width:60px](assets/icons/warning.svg)  <!-- ⚠ warning -->
![width:60px](assets/icons/error.svg)    <!-- ✗ error -->
![width:60px](assets/icons/info.svg)     <!-- ℹ info -->
```

## Quick index (where to look)

- **Reference hub**: `references/index.md`
- **Color design**: `slide-color-design`
- **Marpit authoring**: `marp-authoring`
- **SVG illustration**: `svg-illustration`
- **Decision guide**: `references/decision-guide.md`
- **Output examples**: `references/output-examples.md`
- **Preview workflow**: `marp-authoring` → `references/preview-workflow.md`

## Modules

Use the focused skills for module-specific rules and references:

- **Color design** → `slide-color-design`
- **Marpit authoring** → `marp-authoring`
- **SVG illustration** → `svg-illustration`

## Workflow

### Single tasks

Draw a diagram:
1. Use `svg-illustration` for core rules and patterns.
2. Choose colors via `slide-color-design` or existing palette.

Design slide colors:
1. Use `slide-color-design` for workflow and templates.

Write slides:
1. Use `marp-authoring` for syntax and layout patterns.
2. Apply a palette from `slide-color-design`.

### Full presentation

1. Establish a palette with the color module.
2. Outline slides and author via `marp-authoring`.
3. Add diagrams via `svg-illustration`.
4. Keep palette, spacing, and hierarchy consistent.

## Decision guide

See [references/decision-guide.md](references/decision-guide.md) for a flowchart and loading strategy.

Quick rules:
```
Slides or deck -> marp-authoring
Slides + colors -> slide-color-design -> marp-authoring
Slides + diagrams -> marp-authoring + svg-illustration
Diagram only -> svg-illustration
```

Scale reference loading:
```
Simple request -> core rules only
Complex request -> add patterns and best-practices
```

## Output formats

See [references/output-examples.md](references/output-examples.md) for entry points to module-specific examples.

**Quick reference**:
- **Color design**: `slide-color-design` → `references/output-examples.md`
- **Marpit**: `marp-authoring` → `references/output-examples.md`
- **SVG**: `svg-illustration` → `references/output-examples.md`

## Integration rules

- Use palette hex values in SVG `fill` and `stroke`.
- Keep border radius and stroke widths consistent between Marpit and SVG.
- Embed SVGs with Markdown images or file references.

## Troubleshooting

Common cross-cutting issues:
- [references/troubleshooting-common.md](references/troubleshooting-common.md)
- [svg-illustration](../svg-illustration/SKILL.md) → `references/troubleshooting.md`

## Common mistakes

- Using absolute paths instead of relative paths for assets.
- Using multiple palettes across one deck or between slides and SVGs.
- Skipping validation checks (Marp, SVG lint, contrast).

See `marp-authoring`, `slide-color-design`, and `svg-illustration` for module-specific mistakes.

## Quick check (minimal)

Run in this order:
```bash
bash scripts/validate_marpit.sh slides.md
svglint path/to/diagram.svg
uv run scripts/check_contrast.py '#D4D4D4' '#1E1E1E'
```

## Validation

Use the module-specific validation guides:
- `marp-authoring` → `references/preview-workflow.md`
- `svg-illustration` → `references/troubleshooting.md`
- `slide-color-design` → `references/color-design/workflow.md` (validation checklist)

**Verify color contrast (WCAG compliance)**:
```bash
uv run scripts/check_contrast.py '#D4D4D4' '#1E1E1E'
# Output: Contrast ratio: 11.25:1 ✅ WCAG AAA
```

**Validate Marpit syntax**:
```bash
bash scripts/validate_marpit.sh slides.md
```

Always validate before committing files.

## Constraints

- Output Marpit Markdown only; do not generate PowerPoint/Keynote files.
- Output SVG only; do not generate raster images.
- Avoid interactive animations; keep slides static.
- Preserve provided brand colors; adapt them into the palette.
