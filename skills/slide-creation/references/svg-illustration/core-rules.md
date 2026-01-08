# SVG Illustration Core Rules

## Table of Contents

- [Intent](#intent)
- [Standard Workflow](#standard-workflow)
- [Core Principle: Visual Consistency](#core-principle-visual-consistency)
  - [Example: Consistent Design System](#example-consistent-design-system)
  - [Common Inconsistency Mistakes](#common-inconsistency-mistakes)
- [Canvas Specifications](#canvas-specifications)
  - [ViewBox Must Match Content Bounds (CRITICAL)](#viewbox-must-match-content-bounds-critical)
  - [Guidelines](#guidelines)
- [Visual Style](#visual-style)
  - [Stroke and Fill](#stroke-and-fill)
  - [Border Radius](#border-radius)
  - [Shadows](#shadows)
- [Color Selection](#color-selection)
  - [Use Established Palettes](#use-established-palettes)
- [Smart Sizing Logic](#smart-sizing-logic)
  - [Centered Illustrations](#centered-illustrations)
  - [Two-Column Layouts](#two-column-layouts)
- [Left Column](#left-column)
- [Right Column](#right-column)
  - [Full-Background Graphics](#full-background-graphics)
- [Text in SVG](#text-in-svg)
  - [Best Practices](#best-practices)
  - [Emoji and Special Characters: Don't Use Them](#emoji-and-special-characters-dont-use-them)
  - [Text Alignment](#text-alignment)
- [Basic Shapes](#basic-shapes)
  - [Rectangle (with rounded corners)](#rectangle-with-rounded-corners)
  - [Circle](#circle)
  - [Path (for custom shapes)](#path-for-custom-shapes)
  - [Line](#line)
  - [Arrow](#arrow)
- [Gradients](#gradients)
  - [Linear Gradient](#linear-gradient)
  - [Radial Gradient](#radial-gradient)
- [Grouping and Organization](#grouping-and-organization)
  - [Group Elements](#group-elements)
  - [Transform Groups](#transform-groups)
- [Performance Tips](#performance-tips)
  - [Optimize SVG Code](#optimize-svg-code)
  - [Keep File Size Small](#keep-file-size-small)
- [Common Mistakes](#common-mistakes)
  - [❌ Avoid These](#-avoid-these)
  - [✅ Do These](#-do-these)
- [Quick Template](#quick-template)
- [See Also](#see-also)

Essential rules for creating clean, editable SVG illustrations for Marp/Marpit slides.

---

## Intent

Create clean, editable SVG illustrations that:
- Embed reliably in **Marp/Marpit Markdown**
- Look good in **HTML exports**
- Optimize for common slide placement (centered, left/right aligned, backgrounds)
- **Pass svglint validation** - Always validate SVG syntax after creation

---

## Standard Workflow

**CRITICAL: Follow this workflow for every SVG you create:**

1. **Design**: Plan layout, colors, and content
2. **Create**: Write SVG code following these core rules
3. **Validate**: Run `svglint file.svg` to check syntax
4. **Fix**: Correct any errors (especially XML character escaping)
5. **Test**: Embed in slide and verify rendering
6. **Commit**: Only commit validated, working SVGs

**Never skip validation.** XML syntax errors will break SVG rendering.

---

## Core Principle: Visual Consistency

**CRITICAL: All SVG assets in a presentation must follow a unified design system.**

When creating multiple SVGs for the same presentation:

1. **Use the SAME color palette** across all assets
2. **Maintain consistent stroke widths** (e.g., 3px or 4px everywhere)
3. **Apply uniform border radius** (e.g., 12px or 16px for all cards)
4. **Use consistent shadow/depth system** (same filter definitions)
5. **Keep icon style uniform** (all outlined OR all filled, not mixed)

### Example: Consistent Design System

```xml
<!-- Define ONCE, reuse everywhere -->
<defs>
  <!-- Standard shadow (use in ALL diagrams) -->
  <filter id="shadow-sm">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
  </filter>

  <!-- Primary gradient (use for all primary elements) -->
  <linearGradient id="primary-bg" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" style="stop-color:#f0f9ff;stop-opacity:1" />
    <stop offset="100%" style="stop-color:#e0f2fe;stop-opacity:1" />
  </linearGradient>
</defs>

<!-- Consistent styling -->
<rect rx="16" fill="url(#primary-bg)" stroke="#0891b2" stroke-width="3" filter="url(#shadow-sm)"/>
```

### Common Inconsistency Mistakes

❌ **Don't do this:**
- `icon.svg` uses stroke-width="4" but `diagram.svg` uses stroke-width="2"
- `card-1.svg` has rx="12" but `card-2.svg` has rx="8"
- `flow.svg` uses #2563EB but `architecture.svg` uses #1e40af
- Some SVGs have shadows, others don't

✅ **Do this:**
- ALL assets use stroke-width="3" consistently
- ALL cards/containers use rx="16" consistently
- ALL assets use the SAME accent color (#0891b2)
- ALL assets use the SAME shadow filter

---

## Canvas Specifications

### ViewBox Must Match Content Bounds (CRITICAL)

The `viewBox` should tightly fit the actual content, not be arbitrarily sized. Empty space in the viewBox will scale proportionally, causing the actual content to appear tiny.

**Wrong approach:**
```xml
<!-- Content only uses 600×400 area in center, rest is empty -->
<svg viewBox="0 0 1920 1080" width="1920" height="1080">
  <rect x="660" y="340" width="600" height="400" />
</svg>
```
Result: Massive empty space around content when embedded.

**Correct approach:**
```xml
<!-- viewBox matches actual content bounds -->
<svg viewBox="0 0 600 400" width="600" height="400">
  <rect x="0" y="0" width="600" height="400" />
</svg>
```
Result: Content fills the available space when scaled with `![w:600](...)`.

### Guidelines

- **Determine content bounds first**: Calculate the bounding box of all visible elements
- **Set viewBox to match**: `viewBox="0 0 {width} {height}"` where width/height fit the content
- **Avoid 1920×1080 for small graphics**: Only use full canvas for actual full-slide backgrounds
- **Common sizes**:
  - Centered diagrams: 1200×675 or 1400×787 (maintains 16:9)
  - Icons/badges: 200×200 to 600×400
  - Two-column graphics: 720×405 to 800×450
  - Plugin cards: 1440×300 (wide, short)
  - Flow diagrams: 1320×200 (extra wide, short)

**Slide baseline reference:** 16:9 aspect ratio, conceptually 1920×1080, but adjust viewBox to content.

**Other specs:**
- Safe margins: **120px on each side** when using full 1920×1080 canvas
- Grid alignment: **8px**

---

## Visual Style

### Stroke and Fill

- Stroke width: **3-4px** (use 3px for modern, clean look)
- Stroke caps/joins: rounded (`stroke-linecap="round" stroke-linejoin="round"`)
- Fill: Use solid colors or subtle gradients
- Prefer solid fills over outlines for clarity

### Border Radius

- Cards/containers: **12-16px** (use one value consistently)
- Small elements: **8px**
- Buttons/badges: **8-12px**

### Shadows

Define shadow filters in `<defs>` and reuse:

```xml
<defs>
  <filter id="shadow-sm">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
  </filter>
</defs>

<rect filter="url(#shadow-sm)" ... />
```

Use sparingly—only for elements that need depth.

---

## Color Selection

### Use Established Palettes

Always use colors from the slide's color palette (see [../color-palettes.md](../color-palettes.md)).

**Common palettes for SVG**:

**Technical (Dark Background)**:
- Primary: `#569CD6` (blue)
- Secondary: `#4EC9B0` (cyan)
- Accent: `#F4BF75` (amber)
- Background: `#2D2D2D`
- Stroke: `#D4D4D4`

**Professional (Light Background)**:
- Primary: `#2E75B6` (blue)
- Secondary: `#5B9BD5` (lighter blue)
- Accent: `#F39C12` (orange)
- Background: `#FFFFFF`
- Stroke: `#2C2C2C`

See [../color-palettes.md](../color-palettes.md) for more options including Van Gogh Starry Night palette.

---

## Smart Sizing Logic

### Centered Illustrations

```markdown
![width:800px](diagram.svg)
```

**Rules**:
- Typical widths: 600px-1200px
- Maintain aspect ratio
- Leave breathing room on slides

### Two-Column Layouts

```markdown
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px;">
  <div>

## Left Column

![width:100%](left-diagram.svg)

  </div>
  <div>

## Right Column

![width:100%](right-diagram.svg)

  </div>
</div>
```

**SVG sizing**:
- ViewBox: ~720×450 or similar
- Width: 100% (fills column)

### Full-Background Graphics

```markdown
![bg](background.svg)
```

**Rules**:
- ViewBox: 1920×1080 (full slide)
- Safe margins: 120px on each side
- Don't place critical content near edges

See [embedding.md](embedding.md) for complete embedding guide.

---

## Text in SVG

### Best Practices

```xml
<text x="100" y="50"
      font-family="sans-serif"
      font-size="24"
      font-weight="600"
      fill="#1e293b">
  Label Text
</text>
```

**Guidelines**:
- Use web-safe fonts (sans-serif, Arial, Helvetica)
- Font size: 18-32px for readability
- Font weight: 400 (normal), 600 (semi-bold), 700 (bold)
- Keep text minimal—prefer Markdown text when possible
- **NEVER use emoji in `<text>` elements** - emoji rendering is unreliable across SVG renderers

### Emoji and Special Characters: Don't Use Them

**CRITICAL: Avoid emoji in SVG text.** Emoji support in SVG is inconsistent across browsers, PDF exporters, and SVG viewers.

**Wrong:**
```xml
<text x="100" y="100" font-size="48">🛡️</text>  <!-- May not render -->
<text x="200" y="100" font-size="48">✓</text>    <!-- May not render -->
```

**Correct:**
```xml
<!-- Use simple geometric shapes instead -->
<circle cx="100" cy="100" r="20" fill="#4ade80"/>
<path d="M 95 100 L 98 103 L 105 96" stroke="white" stroke-width="2" fill="none"/>

<!-- Or use standard ASCII characters -->
<text x="100" y="100" font-size="24">OK</text>
<text x="200" y="100" font-size="24">v</text>  <!-- lowercase v looks like checkmark -->
```

For icons, create them from SVG primitives (circles, rects, paths) rather than text characters. See [troubleshooting.md](troubleshooting.md#issue-emoji-not-rendering-in-svg) for detailed examples.

### Text Alignment

```xml
<!-- Center-aligned -->
<text x="400" y="50" text-anchor="middle" fill="#1e293b">
  Centered Text
</text>

<!-- Right-aligned -->
<text x="800" y="50" text-anchor="end" fill="#1e293b">
  Right Text
</text>
```

---

## Basic Shapes

### Rectangle (with rounded corners)

```xml
<rect x="100" y="100" width="200" height="150"
      rx="16"
      fill="#f0f9ff"
      stroke="#0891b2"
      stroke-width="3"/>
```

### Circle

```xml
<circle cx="200" cy="200" r="60"
        fill="#2563EB"
        stroke="#1e40af"
        stroke-width="3"/>
```

### Path (for custom shapes)

```xml
<path d="M 100 100 L 200 100 L 150 200 Z"
      fill="#10b981"
      stroke="#059669"
      stroke-width="3"/>
```

### Line

```xml
<line x1="100" y1="100" x2="400" y2="100"
      stroke="#64748b"
      stroke-width="2"
      stroke-linecap="round"/>
```

### Arrow

```xml
<defs>
  <marker id="arrowhead" markerWidth="10" markerHeight="10"
          refX="9" refY="3" orient="auto">
    <polygon points="0 0, 10 3, 0 6" fill="#0891b2"/>
  </marker>
</defs>

<line x1="100" y1="200" x2="400" y2="200"
      stroke="#0891b2"
      stroke-width="3"
      marker-end="url(#arrowhead)"/>
```

---

## Gradients

### Linear Gradient

```xml
<defs>
  <linearGradient id="grad1" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" style="stop-color:#f0f9ff;stop-opacity:1" />
    <stop offset="100%" style="stop-color:#e0f2fe;stop-opacity:1" />
  </linearGradient>
</defs>

<rect fill="url(#grad1)" ... />
```

### Radial Gradient

```xml
<defs>
  <radialGradient id="grad2" cx="50%" cy="50%" r="50%">
    <stop offset="0%" style="stop-color:#FFFFFF;stop-opacity:0.8" />
    <stop offset="100%" style="stop-color:#000000;stop-opacity:0.2" />
  </radialGradient>
</defs>

<circle fill="url(#grad2)" ... />
```

---

## Grouping and Organization

### Group Elements

```xml
<g id="card-group">
  <rect x="100" y="100" width="200" height="150" rx="16" fill="#f0f9ff"/>
  <text x="200" y="180" text-anchor="middle">Card Title</text>
</g>
```

### Transform Groups

```xml
<g transform="translate(100, 50)">
  <!-- All elements shifted by 100,50 -->
  <rect x="0" y="0" width="200" height="100"/>
</g>
```

---

## Performance Tips

### Optimize SVG Code

- Remove unnecessary attributes
- Minimize decimal places (e.g., `100.0` → `100`)
- Reuse `<defs>` (gradients, filters, markers)
- Avoid excessive nesting

### Keep File Size Small

- Don't embed raster images in SVG
- Use simple paths instead of complex curves when possible
- Limit filter effects (shadows, blurs)

---

## Common Mistakes

### ❌ Avoid These

1. **Wrong viewBox**: Using 1920×1080 for small graphics
2. **Inconsistent styling**: Different stroke widths across SVGs
3. **Too much detail**: Overly complex paths that don't render well
4. **Missing namespace**: Forgetting `xmlns="http://www.w3.org/2000/svg"`
5. **Hardcoded sizes**: Using `width="1920"` instead of responsive sizing

### ✅ Do These

1. **Tight viewBox**: Match content bounds
2. **Unified design system**: Same colors, stroke widths, shadows
3. **Simple, clear graphics**: Readable at slide scale
4. **Proper namespace**: Always include `xmlns`
5. **Responsive**: Let Marpit control sizing with `![width:XXX]`
6. **Validate syntax**: Run `svglint file.svg` after creating each SVG

---

## Quick Template

```xml
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Define reusable elements here -->
    <filter id="shadow-sm">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Your content here -->
  <rect x="100" y="100" width="200" height="150"
        rx="16"
        fill="#f0f9ff"
        stroke="#0891b2"
        stroke-width="3"
        filter="url(#shadow-sm)"/>

  <text x="200" y="180"
        font-family="sans-serif"
        font-size="24"
        font-weight="600"
        fill="#1e293b"
        text-anchor="middle">
    Label
  </text>
</svg>
```

---

## See Also

- [pattern-examples.md](pattern-examples.md) - Common diagram patterns
- [../color-palettes.md](../color-palettes.md) - Ready-to-use color schemes
- [embedding.md](embedding.md) - How to embed in Marpit slides
- [troubleshooting.md](troubleshooting.md) - Common issues and fixes
