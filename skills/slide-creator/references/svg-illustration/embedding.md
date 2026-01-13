# Embedding SVG in Marpit Slides

## Table of Contents

- [Embedding Methods](#embedding-methods)
  - [Method 0: Background Syntax (Preferred)](#method-0-background-syntax-preferred)
  - [Method 1: External File (Legacy - for small inline images only)](#method-1-external-file-legacy-for-small-inline-images-only)
  - [Method 2: Inline Base64 (Recommended for production)](#method-2-inline-base64-recommended-for-production)
  - [Method 3: Inline SVG XML (Not recommended)](#method-3-inline-svg-xml-not-recommended)
- [Placement Patterns](#placement-patterns)
  - [Pattern 1: Full-Page Background (Most Common)](#pattern-1-full-page-background-most-common)
  - [Pattern 2: Split Layout - Text and Image](#pattern-2-split-layout-text-and-image)
  - [Pattern 3: Multiple Images Comparison](#pattern-3-multiple-images-comparison)
  - [Pattern 4: Legacy Centered on Slide (Avoid)](#pattern-4-legacy-centered-on-slide-avoid)
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
  - [1. Use bg syntax by default](#1-use-bg-syntax-by-default)
  - [2. Consistent Sizing Within Presentation](#2-consistent-sizing-within-presentation)
  - [3. Use Alt Text](#3-use-alt-text)
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

**RECOMMENDED: Use `bg` (background) syntax for most images to avoid manual sizing.**

### Method 0: Background Syntax (Preferred)

**Use `bg` syntax with `fit` modifier for automatic sizing:**

```markdown
# Full-page background
![bg fit](diagram.svg)

# Split layout - image on right
![bg right fit](architecture.svg)

# Split layout - image on left
![bg left fit](workflow.svg)

# Custom split ratio
![bg right:40% fit](detail.svg)
```

**Pros**:
- `fit` modifier auto-scales images perfectly
- No manual width/height adjustments needed
- Consistent sizing across slides
- Better for split layouts with text

**Cons**:
- Less control over exact positioning (but rarely needed)

**This should be your default choice for diagrams and illustrations.**

---

### Method 1: External File (Legacy - for small inline images only)

Save SVG as separate file and reference:

```markdown
![width:800px](diagram.svg)
```

**Pros**:
- Easy to edit SVG separately
- Clean Markdown
- Faster iteration during development

**Cons**:
- **Manual sizing required** - must specify width/height
- Inconsistent across slides if not careful
- Requires managing separate files

**Use only for**: Small inline icons (e.g., `![width:40px](icon.svg)`)

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

**Prefer `bg` syntax for all these patterns.**

### Pattern 1: Full-Page Background (Most Common)

```markdown
![bg fit](architecture.svg)

# Optional Overlay Title

Optional text overlays on the image.
```

**Result**: SVG fills entire slide, auto-sized with `fit`.

**When to use**: Showing a complete diagram without much text.

---

### Pattern 2: Split Layout - Text and Image

**Image on right, text on left:**

```markdown
![bg right fit](process-flow.svg)

## Process Flow

1. Initialize system
2. Load configuration
3. Start services
4. Monitor health
```

**Image on left, text on right:**

```markdown
![bg left fit](architecture.svg)

# System Architecture

Explanation of the architecture appears on the right side.
```

**Custom split ratio:**

```markdown
![bg left:60% fit](main-diagram.svg)

# Details

Diagram takes 60%, text takes 40%.
```

**Result**: Side-by-side layout with automatic image sizing.

**When to use**: Explaining a diagram with text.

---

### Pattern 3: Multiple Images Comparison

```markdown
![bg left:50% fit](before.svg)
![bg right:50% fit](after.svg)

# Before → After
```

**Result**: Two images side-by-side.

**When to use**: Comparisons, before/after.

---

### Pattern 4: Legacy Centered on Slide (Avoid)

**Only use for small inline images:**

```markdown
## Architecture Overview

![width:60px](icon.svg) Component A
![width:60px](icon.svg) Component B
```

**Use bg syntax instead for diagrams:**

```markdown
![bg fit](architecture.svg)
```

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

### 1. Use bg syntax by default

**ALWAYS prefer `bg` syntax for diagrams and illustrations:**

```markdown
<!-- DO THIS -->
![bg fit](diagram.svg)
![bg right fit](architecture.svg)

<!-- NOT THIS (unless it's a tiny icon) -->
![width:800px](diagram.svg)
```

**Exceptions**: Only use regular syntax for very small inline icons:
```markdown
![width:40px](check-icon.svg) Feature enabled
```

### 2. Consistent Sizing Within Presentation

When using `bg fit`, sizing is automatic and consistent. No manual adjustments needed!

### 3. Use Alt Text

```markdown
![bg fit Microservices architecture diagram](architecture.svg)
```

**Benefits**:
- Accessibility
- Fallback description if SVG doesn't load

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
<!-- PREFERRED: bg syntax with fit -->
![bg fit](full-page.svg)
![bg right fit](side-image.svg)
![bg left fit](main-diagram.svg)
![bg right:40% fit](detail.svg)

<!-- Comparison -->
![bg left:50% fit](before.svg)
![bg right:50% fit](after.svg)

<!-- LEGACY: Only for small inline icons -->
![width:40px](icon.svg)

<!-- External file (for development) -->
![bg fit](diagram.svg)

<!-- Base64 inline (for distribution) -->
![bg fit](data:image/svg+xml;base64,PHN2Zy4uLg==)
```

### Sizing Guidelines

| Use Case | Recommended Syntax | Notes |
|----------|-------------------|-------|
| Full-page diagram | `![bg fit]` | Auto-sized, fills slide |
| Split layout | `![bg right/left fit]` | Auto-sized, 50/50 split |
| Custom split | `![bg right:40% fit]` | Image takes specified % |
| Small inline icon | `![width:40px]` | Only for tiny images |
| Comparison | `![bg left:50% fit]` + `![bg right:50% fit]` | Side-by-side |

**Rule of thumb**: If it's a diagram or illustration, use `bg fit` syntax.

---

## See Also

- [core-rules.md](core-rules.md) - SVG creation basics
- [pattern-examples.md](pattern-examples.md) - Common diagram patterns
- [troubleshooting.md](troubleshooting.md) - Solving embedding issues
- [../marpit-authoring/syntax-guide.md](../marpit-authoring/syntax-guide.md) - Marpit image syntax
