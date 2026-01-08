---
name: slide-creator
description: Complete slide creation toolkit for Marp/Marpit presentations. Use when creating presentations, authoring slides, writing slide content, drawing diagrams, creating illustrations, designing slide color schemes, choosing presentation colors, designing slide themes, selecting background/text/accent colors, or any combination of these tasks. Covers Markdown authoring (Marpit/Marp), SVG illustration, and color design for technical presentations, PowerPoint, Keynote, architecture diagrams, and developer-focused decks.
---

# Slide Creation Toolkit

Create professional Marp/Marpit presentations, diagrams, and color systems with a consistent design language.

## Core rules

- Define one color palette and reuse it in slides and SVGs.
- Define one spacing system and reuse it everywhere.
- Enforce visual hierarchy with size, weight, and saturation.
- Use consistent visual language (fill vs outline, emphasis rules).
- Minimize visual noise; keep one primary visual anchor per section.

## Modules

### Module 1: Color design

Design slide color systems (background, text, accents, semantic colors).

Output: color palette specification with hex codes and usage guidelines.

Read in order:
- `references/color-design/workflow.md`
- `references/color-design/strategies.md`
- `references/color-palettes.md` (use as a base or cross-check)
- `references/color-design/output-template.md` (match the format)

### Module 2: Marpit authoring

Write valid Marpit/Marp Markdown slides.

Output: valid Marpit-compatible Markdown (.md).

Rules:
- Output directly renderable Marpit Markdown.
- Avoid HTML; use Marpit directives and Markdown only.
- Use HTML only if no Marpit alternative exists.

Read in order:
- `references/marpit-authoring/syntax-guide.md`
- `references/marpit-authoring/patterns.md`
- `references/marpit-authoring/advanced-layouts.md` (use for complex layouts)
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

Validate SVGs with:
```bash
svglint path/to/file.svg
```

## Workflow

### Single tasks

Draw a diagram:
1. Read `references/svg-illustration/core-rules.md`.
2. Use `references/svg-illustration/pattern-examples.md` for layouts.
3. Reuse a palette from `references/color-palettes.md`.

Design slide colors:
1. Follow `references/color-design/workflow.md`.
2. Select a strategy from `references/color-design/strategies.md`.
3. Cross-check with `references/color-palettes.md`.

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

Pick modules based on user intent:
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

Color design:
```
## Color Strategy
[Chosen strategy + reasoning]

## Color Palette
* Background: #XXXXXX — [purpose]
* Surface: #XXXXXX — [purpose]
* Primary: #XXXXXX — [purpose]
* Secondary: #XXXXXX — [purpose]
* Accent: #XXXXXX — [purpose]
* Text Primary: #XXXXXX — [purpose]
* Text Secondary: #XXXXXX — [purpose]

## Usage Guidelines
[How to apply colors]

## Validation Checklist
- [ ] Contrast ratio >= 4.5:1
- [ ] Palette limited to 5-7 colors
- [ ] Colors work on projector
```

Marpit authoring:
```markdown
---
marp: true
theme: default
---

# Title Slide
Subtitle

---

## Content Slide
- Point 1
- Point 2
```

SVG illustration:
```xml
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <!-- SVG content -->
</svg>
```

## Integration rules

- Use palette hex values in SVG `fill` and `stroke`.
- Keep border radius and stroke widths consistent between Marpit and SVG.
- Embed SVGs with Markdown images or file references.

## Constraints

- Output Marpit Markdown only; do not generate PowerPoint/Keynote files.
- Output SVG only; do not generate raster images.
- Avoid interactive animations; keep slides static.
- Preserve provided brand colors; adapt them into the palette.
