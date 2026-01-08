# Embedding SVG in Marpit Slides

## Table of Contents

- [Embedding Methods](#embedding-methods)
  - [Method 1: External File (Recommended for development)](#method-1-external-file-recommended-for-development)
  - [Method 2: Inline Base64 (Recommended for production)](#method-2-inline-base64-recommended-for-production)
  - [Method 3: Inline SVG XML (Not recommended)](#method-3-inline-svg-xml-not-recommended)
- [Sizing Methods](#sizing-methods)
  - [Fixed Width](#fixed-width)
  - [Fixed Height](#fixed-height)
  - [Both Width and Height](#both-width-and-height)
  - [Percentage Width (in layouts)](#percentage-width-in-layouts)
- [Placement Patterns](#placement-patterns)
  - [Pattern 1: Centered on Slide](#pattern-1-centered-on-slide)
- [Architecture Overview](#architecture-overview)
  - [Pattern 2: Two-Column with SVG](#pattern-2-two-column-with-svg)
- [Process Flow](#process-flow)
  - [Pattern 3: Full-Slide Background](#pattern-3-full-slide-background)
  - [Pattern 4: Background Positioning](#pattern-4-background-positioning)
  - [Pattern 5: Multiple SVGs](#pattern-5-multiple-svgs)
- [Component Comparison](#component-comparison)
- [Responsive Considerations](#responsive-considerations)
  - [Maintain Aspect Ratio](#maintain-aspect-ratio)
  - [Percentage Widths](#percentage-widths)
- [Theme-Specific Adjustments](#theme-specific-adjustments)
  - [Default Theme](#default-theme)
  - [Gaia Theme](#gaia-theme)
  - [Uncover Theme](#uncover-theme)
- [Common Embedding Issues](#common-embedding-issues)
  - [Issue 1: SVG Too Small on Slide](#issue-1-svg-too-small-on-slide)
  - [Issue 2: SVG Pixelated](#issue-2-svg-pixelated)
  - [Issue 3: Colors Look Different](#issue-3-colors-look-different)
  - [Issue 4: SVG Not Showing](#issue-4-svg-not-showing)
  - [Issue 5: Base64 Too Long](#issue-5-base64-too-long)
- [Best Practices](#best-practices)
  - [1. Size Appropriately](#1-size-appropriately)
  - [2. Consistent Sizing Within Presentation](#2-consistent-sizing-within-presentation)
  - [3. Use Alt Text](#3-use-alt-text)
  - [4. Group Related SVGs](#4-group-related-svgs)
- [System Components](#system-components)
  - [5. Center Large Graphics](#5-center-large-graphics)
- [Production Workflow](#production-workflow)
  - [Development Phase](#development-phase)
  - [Distribution Phase](#distribution-phase)
- [Advanced: Dynamic SVG with Variables](#advanced-dynamic-svg-with-variables)
- [Quick Reference](#quick-reference)
  - [Syntax Cheatsheet](#syntax-cheatsheet)
  - [Sizing Guidelines](#sizing-guidelines)
- [See Also](#see-also)

Complete guide for embedding SVG illustrations in Marp/Marpit Markdown presentations.

---

## Embedding Methods

### Method 1: External File (Recommended for development)

Save SVG as separate file and reference:

```markdown
![width:800px](diagram.svg)
```

**Pros**:
- Easy to edit SVG separately
- Clean Markdown
- Faster iteration during development

**Cons**:
- Requires managing separate files
- May need bundling for distribution

---

### Method 2: Inline Base64 (Recommended for production)

Convert SVG to base64 and embed directly:

```markdown
![width:800px](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNjAwIj4KICA8cmVjdCB3aWR0aD0iODAwIiBoZWlnaHQ9IjYwMCIgZmlsbD0iI2YwZjlmZiIvPgo8L3N2Zz4K)
```

**Pros**:
- Self-contained Markdown file
- No external dependencies
- Easy distribution (single .md file)

**Cons**:
- Harder to edit inline
- Larger file size

**How to convert**:
```bash
# On macOS/Linux
base64 -i diagram.svg

# Or use online tools
# https://www.base64encode.org/
```

---

### Method 3: Inline SVG XML (Not recommended)

Embed SVG XML directly in Markdown:

```markdown
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <rect width="800" height="600" fill="#f0f9ff"/>
</svg>
```

**Pros**:
- Editable inline
- No encoding needed

**Cons**:
- **May not work reliably** in all Marpit themes
- Breaks Markdown flow
- Not officially supported

**Verdict**: Use base64 or external file instead.

---

## Sizing Methods

### Fixed Width

```markdown
![width:800px](diagram.svg)
![w:800px](diagram.svg)  <!-- shorthand -->
```

**When to use**: Most common, ensures consistent size across slides.

### Fixed Height

```markdown
![height:600px](diagram.svg)
![h:600px](diagram.svg)  <!-- shorthand -->
```

**When to use**: When height constraint is more important (e.g., vertical flows).

### Both Width and Height

```markdown
![w:800px h:600px](diagram.svg)
```

**When to use**: Rarely—usually let aspect ratio determine one dimension.

### Percentage Width (in layouts)

```markdown
<div style="width: 50%;">

![width:100%](diagram.svg)

</div>
```

**When to use**: Inside columns or containers.

---

## Placement Patterns

### Pattern 1: Centered on Slide

```markdown
## Architecture Overview

![width:1000px](architecture.svg)

Key components and their interactions.
```

**Result**: SVG centered horizontally, text above and below.

**Typical widths**: 800-1200px

---

### Pattern 2: Two-Column with SVG

```markdown
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px;">

<div>

## Process Flow

1. Initialize system
2. Load configuration
3. Start services
4. Monitor health

</div>

<div>

![width:100%](process-flow.svg)

</div>

</div>
```

**Result**: Text on left, SVG on right (or vice versa).

**SVG sizing**: Use `width:100%` to fill column.

---

### Pattern 3: Full-Slide Background

```markdown
---

![bg](background-pattern.svg)

# Title on Background

Content appears over SVG background.

---
```

**Result**: SVG fills entire slide as background.

**SVG requirements**:
- ViewBox: `0 0 1920 1080` (full slide dimensions)
- Use subtle colors (don't overpower text)
- Ensure text remains readable

---

### Pattern 4: Background Positioning

```markdown
![bg right:40%](side-graphic.svg)

# Main Content

Text appears on left, SVG on right 40% of slide.
```

**Options**:
- `![bg right:40%](...)` - Right side, 40% width
- `![bg left:30%](...)` - Left side, 30% width
- `![bg vertical](...)` - Stacked vertically

---

### Pattern 5: Multiple SVGs

```markdown
## Component Comparison

<div style="display: flex; gap: 32px; justify-content: center;">

![width:350px](component-a.svg)
![width:350px](component-b.svg)
![width:350px](component-c.svg)

</div>
```

**Result**: Three SVGs side-by-side.

---

## Responsive Considerations

### Maintain Aspect Ratio

**Good**:
```markdown
![width:800px](diagram.svg)  <!-- Height auto-calculated -->
```

**Bad**:
```markdown
![w:800px h:400px](diagram.svg)  <!-- May distort if aspect ratio doesn't match -->
```

### Percentage Widths

Works inside containers:

```markdown
<div style="width: 80%; margin: 0 auto;">

![width:100%](diagram.svg)

</div>
```

**Result**: SVG fills 80% of slide width, centered.

---

## Theme-Specific Adjustments

### Default Theme

- Clean, minimal background
- Use any SVG colors
- Good contrast required

### Gaia Theme

- Modern, colorful slides
- Match SVG colors to theme (blues, teals)
- Consider theme's existing accent colors

### Uncover Theme

- Bold, high-contrast
- Use strong colors in SVGs
- Ensure visibility on theme's backgrounds

**Tip**: Test SVGs on all intended themes.

---

## Common Embedding Issues

### Issue 1: SVG Too Small on Slide

**Cause**: ViewBox too large (e.g., 1920×1080 for small content)

**Solution**: Adjust viewBox to match actual content bounds.

```xml
<!-- Before (wrong) -->
<svg viewBox="0 0 1920 1080">
  <rect x="800" y="400" width="320" height="280"/>  <!-- Small in huge canvas -->
</svg>

<!-- After (correct) -->
<svg viewBox="0 0 320 280">
  <rect x="0" y="0" width="320" height="280"/>
</svg>
```

### Issue 2: SVG Pixelated

**Cause**: Raster image embedded in SVG, or bitmap export

**Solution**: Use vector shapes only, export as SVG (not PNG).

### Issue 3: Colors Look Different

**Cause**: Color profile issues, display calibration

**Solution**: Use web-safe hex colors, test on target device.

### Issue 4: SVG Not Showing

**Causes**:
- Wrong file path
- Missing `xmlns` attribute
- Invalid SVG syntax

**Solutions**:
```xml
<!-- Ensure namespace -->
<svg xmlns="http://www.w3.org/2000/svg" ...>

<!-- Validate syntax (close all tags) -->
```

### Issue 5: Base64 Too Long

**Cause**: Complex SVG with many elements

**Solutions**:
- Simplify SVG (remove unnecessary details)
- Use external file instead of base64
- Optimize with SVGO tool

See [troubleshooting.md](troubleshooting.md) for more issues and solutions.

---

## Best Practices

### 1. Size Appropriately

```markdown
<!-- Small icon/badge -->
![width:200px](icon.svg)

<!-- Medium diagram -->
![width:800px](diagram.svg)

<!-- Large centerpiece -->
![width:1200px](architecture.svg)
```

### 2. Consistent Sizing Within Presentation

If one architecture diagram is 1000px wide, make all architecture diagrams 1000px wide.

### 3. Use Alt Text

```markdown
![width:800px Microservices architecture diagram](architecture.svg)
```

**Benefits**:
- Accessibility
- Fallback description if SVG doesn't load

### 4. Group Related SVGs

```markdown
## System Components

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px;">

![width:100%](api-gateway.svg)
![width:100%](service-mesh.svg)
![width:100%](database.svg)

</div>
```

### 5. Center Large Graphics

```markdown
<div style="text-align: center;">

![width:1000px](large-diagram.svg)

</div>
```

---

## Production Workflow

### Development Phase

1. Create SVG files separately (`diagram1.svg`, `diagram2.svg`, etc.)
2. Reference externally in Markdown:
   ```markdown
   ![width:800px](diagram1.svg)
   ```
3. Iterate quickly (edit SVG, reload Marpit preview)

### Distribution Phase

**Option A: Bundle Files**
- Keep SVGs as separate files
- Distribute folder with `.md` + SVG files
- Easy for others to edit

**Option B: Embed as Base64**
- Convert all SVGs to base64
- Inline in Markdown
- Self-contained single file

**Recommended**: Option A during collaboration, Option B for final export.

---

## Advanced: Dynamic SVG with Variables

Use CSS custom properties for theming:

```xml
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      :root {
        --primary-color: #0891b2;
        --bg-color: #f0f9ff;
      }
    </style>
  </defs>

  <rect fill="var(--bg-color)" stroke="var(--primary-color)" stroke-width="3"/>
</svg>
```

**Benefit**: Change colors globally by updating CSS variables.

---

## Quick Reference

### Syntax Cheatsheet

```markdown
<!-- External file -->
![width:800px](diagram.svg)

<!-- Base64 inline -->
![width:800px](data:image/svg+xml;base64,PHN2Zy4uLg==)

<!-- Background -->
![bg](background.svg)
![bg right:40%](side.svg)

<!-- In column -->
<div style="width: 50%;">
![width:100%](diagram.svg)
</div>

<!-- Multiple -->
![width:400px](a.svg) ![width:400px](b.svg)
```

### Sizing Guidelines

| SVG Type | Recommended Width | Notes |
|----------|------------------|-------|
| Icon/Badge | 150-300px | Small, simple |
| Diagram | 600-1000px | Medium complexity |
| Architecture | 1000-1400px | Large, detailed |
| Full-slide BG | 1920×1080 (viewBox) | Background only |
| Two-column | 100% (in column) | Responsive |

---

## See Also

- [core-rules.md](core-rules.md) - SVG creation basics
- [pattern-examples.md](pattern-examples.md) - Common diagram patterns
- [troubleshooting.md](troubleshooting.md) - Solving embedding issues
- [../marpit-authoring/syntax-guide.md](../marpit-authoring/syntax-guide.md) - Marpit image syntax
