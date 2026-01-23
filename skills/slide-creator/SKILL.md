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

Pick one task and follow the exact reading path:

- **Color palette only** → `references/color-design/workflow.md` → `references/color-design/strategies.md` → `references/color-design/output-template.md`
- **Slides only (no diagrams)** → `references/marpit-authoring/syntax-guide.md` → `references/marpit-authoring/patterns.md`
- **Diagram only** → `references/svg-illustration/core-rules.md` → `references/svg-illustration/pattern-examples.md`
- **Slides + diagrams** → `references/marpit-authoring/syntax-guide.md` → `references/svg-illustration/core-rules.md`
- **Full deck (colors + slides + diagrams)** → Color workflow → Marpit authoring → SVG illustration

## One-page quick reference

**Minimal steps (fast path)**:
1. Pick a palette (or generate from brand).
2. Draft slides in Marpit.
3. Add SVG diagrams if needed.
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

**Outputs**:
- **Color design**: strategy + 7-role palette + usage guidelines + validation checklist
- **Marpit**: `marp: true` frontmatter + slides separated by `---`
- **SVG**: `<svg viewBox="..." xmlns="...">` with consistent sizing/colors

## Quick Start

### Two Ways to Start

**Option 1: Use scripts** (automated):
```bash
uv run scripts/init_presentation.py technical-dark my-deck.md "My Title" "Author"
```

**Option 2: Work manually** (full control):
- Copy a template from `assets/templates/` → customize
- Design colors following `references/color-design/workflow.md`
- Write slides following `references/marpit-authoring/syntax-guide.md`
- Add diagrams following `references/svg-illustration/core-rules.md`

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

- **Color design**: `references/color-design/workflow.md`, `references/color-design/strategies.md`, `references/color-design/output-template.md`
- **Marpit authoring**: `references/marpit-authoring/syntax-guide.md`, `references/marpit-authoring/patterns.md`, `references/marpit-authoring/advanced-layouts.md`
- **SVG illustration**: `references/svg-illustration/core-rules.md`, `references/svg-illustration/pattern-examples.md`, `references/svg-illustration/embedding.md`
- **Decision guide**: `references/decision-guide.md`
- **Output examples**: `references/output-examples.md`
- **Preview workflow**: `references/preview-workflow.md`

## Modules

### Module 1: Color design

Design slide color systems (background, text, accents, semantic colors).

Output: color palette specification with hex codes and usage guidelines.

Browse available palettes:
See **Common commands** (above) for palette and SVG helpers.

Read in order:
- `references/color-design/workflow.md`
- `references/color-design/strategies.md`
- `references/color-palettes.md` (index of palettes; use script to view details)
- `references/color-design/output-template.md` (match the format)

### Module 2: Marpit authoring

Write valid Marpit/Marp Markdown slides.

Output: valid Marpit-compatible Markdown (.md).

Rules:
- Output directly renderable Marpit Markdown.
- **Always use `bg` syntax for images** (e.g., `![bg right fit](image.svg)`)
- Avoid HTML; use Marpit directives and Markdown only.
- Use HTML only if no Marpit alternative exists.

Read in order:
- `references/marpit-authoring/syntax-guide.md`
- `references/marpit-authoring/patterns.md`
- Use `references/marpit-authoring/advanced-layouts.md` only for multi-column, split, or asymmetric layouts.
- `references/marpit-authoring/themes.md`
- `references/marpit-authoring/best-practices.md` (use for quality checks)

### Module 3: SVG illustration

Create SVG diagrams and illustrations for slides.

Output: SVG XML optimized for Marp HTML export.

Rules:
- Create clean, editable SVGs with predictable sizing.
- Match slide colors and spacing.

Read in order:
- `references/svg-illustration/core-rules.md`
- `references/svg-illustration/pattern-examples.md`
- `references/svg-illustration/embedding.md`
- `references/svg-illustration/troubleshooting.md`

Validate SVGs after creation:
```bash
svglint path/to/file.svg
```

## Workflow

### Single tasks

Draw a diagram:
1. Read `references/svg-illustration/core-rules.md`.
2. Use `references/svg-illustration/pattern-examples.md` for layouts.
3. Choose colors: see **Common commands** (above).

Design slide colors:
1. Browse palettes: see **Common commands** (above).
2. Or follow `references/color-design/workflow.md` for custom design.

Write slides:
1. Follow `references/marpit-authoring/syntax-guide.md`.
2. Use `references/marpit-authoring/patterns.md` for layouts.
3. Apply a palette from the color module.

### Full presentation

1. Establish a palette with the color module.
2. Outline slides and author in Marpit.
3. Add diagrams with the SVG module.
4. Keep palette, spacing, and hierarchy consistent.

## Decision guide

See [references/decision-guide.md](references/decision-guide.md) for a flowchart and loading strategy.

Quick rules:
```
Slides or deck -> Marpit authoring
Slides + colors -> Color design -> Marpit authoring
Slides + diagrams -> Marpit authoring + SVG illustration
Diagram only -> SVG illustration
```

Scale reference loading:
```
Simple request -> core rules only
Complex request -> add patterns and best-practices
```

## Output formats

See [references/output-examples.md](references/output-examples.md) for complete examples with detailed annotations.

**Quick reference**:
- **Color design**: Strategy + 7-role palette + usage guidelines + validation checklist
- **Marpit**: Frontmatter (`marp: true`) + slides separated by `---`
- **SVG**: `<svg viewBox="..." xmlns="...">` with proper sizing and consistent colors

## Integration rules

- Use palette hex values in SVG `fill` and `stroke`.
- Keep border radius and stroke widths consistent between Marpit and SVG.
- Embed SVGs with Markdown images or file references.

## Troubleshooting

Common cross-cutting issues:
- [references/troubleshooting-common.md](references/troubleshooting-common.md)
- [references/svg-illustration/troubleshooting.md](references/svg-illustration/troubleshooting.md)

## Common mistakes

- Mixing `bg` and non-`bg` image syntax in the same deck.
- Using absolute paths instead of relative paths for assets.
- Using multiple palettes across one deck or between slides and SVGs.
- Changing stroke width or corner radius between SVG shapes.
- Skipping `svglint` before embedding SVGs.
- Using advanced layouts for simple single-column slides.

## Quick check (minimal)

Run in this order:
```bash
bash scripts/validate_marpit.sh slides.md
svglint path/to/diagram.svg
uv run scripts/check_contrast.py '#D4D4D4' '#1E1E1E'
```

## Validation

**Check SVG syntax and best practices**:
```bash
svglint diagram.svg
```

**Visual verification (required after any SVG/image change)**:
1. Ensure prerequisites are installed:
   - `marp` CLI
   - `svglint` (install via `npm install -g svglint` if missing)
   - Playwright with Chromium
2. Identify which slide page includes the updated SVG (avoid screenshotting the wrong page).
3. Run Marp preview for the target deck (or the smallest deck that imports the SVG).
   - If preview fails or assets 404, follow `references/troubleshooting-common.md#svg-not-rendering-in-marpit`.
   - If you hit EPERM or bind errors, set `--host 127.0.0.1` and an explicit `--port`.
4. Render the exact slide page in a browser.
5. Capture a Playwright screenshot of that page.
6. Review the screenshot in slide context before stating visual impact or completion.
7. Stop the Marp server when done.

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
