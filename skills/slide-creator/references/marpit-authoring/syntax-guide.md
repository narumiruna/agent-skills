# Marpit Markdown Syntax Guide

## Table of Contents

- [Core Rule](#core-rule)
- [Basic Structure](#basic-structure)
  - [Minimal Slide Deck](#minimal-slide-deck)
- [Content Slide](#content-slide)
  - [Frontmatter (Required)](#frontmatter-required)
- [Slide Separation](#slide-separation)
- [Directives](#directives)
  - [Global Directives (in frontmatter)](#global-directives-in-frontmatter)
  - [Local Directives (per slide)](#local-directives-per-slide)
- [Headers and Text](#headers-and-text)
  - [Header Hierarchy](#header-hierarchy)
- [H2 - Section Heading](#h2-section-heading)
  - [H3 - Subsection](#h3-subsection)
    - [H4 - Minor heading (rarely used)](#h4-minor-heading-rarely-used)
  - [Text Formatting](#text-formatting)
  - [Lists](#lists)
- [Code Blocks](#code-blocks)
  - [Basic Code Block](#basic-code-block)
  - [Code with Language Highlighting](#code-with-language-highlighting)
- [Images](#images)
  - [Basic Image](#basic-image)
  - [Image with Size](#image-with-size)
  - [Image Positioning](#image-positioning)
  - [SVG Images](#svg-images)
- [Custom Styling](#custom-styling)
  - [Scoped Style Tags](#scoped-style-tags)
  - [Inline HTML](#inline-html)
- [Left Column](#left-column)
- [Right Column](#right-column)
- [Two-Column Layouts](#two-column-layouts)
  - [Method 1: HTML Grid](#method-1-html-grid)
- [Left](#left)
- [Right](#right)
  - [Method 2: Flexbox](#method-2-flexbox)
- [Special Features](#special-features)
  - [Presenter Notes](#presenter-notes)
  - [Fragments (Incremental Reveal)](#fragments-incremental-reveal)
- [Point 2](#point-2)
- [Point 2](#point-2)
  - [Point 3](#point-3)
- [Theme Selection](#theme-selection)
  - [Available Themes](#available-themes)
  - [Setting Theme](#setting-theme)
- [Common Patterns](#common-patterns)
  - [Title Slide](#title-slide)
  - [Section Divider](#section-divider)
  - [Content Slide](#content-slide)
- [Slide Title](#slide-title)
  - [Code Example Slide](#code-example-slide)
- [Code Example](#code-example)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
  - [Slide not rendering](#slide-not-rendering)
  - [Images not showing](#images-not-showing)
  - [Styling not applying](#styling-not-applying)
- [Quick Reference Card](#quick-reference-card)
- [Content](#content)
- [See Also](#see-also)

Complete reference for writing valid Marpit/Marp Markdown slides.

---

## Core Rule

**ALWAYS output valid Marpit-compatible Markdown** that can be directly rendered.

- Do NOT explain Marpit syntax unless explicitly asked
- Do NOT output non-Markdown prose
- Do NOT mix presentation content with commentary
- Output must be directly renderable by Marpit/Marp

---

## Basic Structure

### Minimal Slide Deck

```markdown
---
marp: true
---

# Title Slide
Subtitle or description

---

## Content Slide
- Point 1
- Point 2
- Point 3
```

### Frontmatter (Required)

Every Marpit file must start with frontmatter:

```yaml
---
marp: true
theme: default
paginate: true
---
```

**Common frontmatter fields**:
- `marp: true` - Enable Marp rendering (required)
- `theme: default` - Theme choice (default, gaia, uncover)
- `paginate: true` - Show page numbers
- `_paginate: false` - Hide pagination on specific slides
- `backgroundColor: #f8fafc` - Global background color
- `color: #1e293b` - Global text color

---

## Slide Separation

Use `---` (three hyphens) to separate slides:

```markdown
# Slide 1

---

# Slide 2

---

# Slide 3
```

**Important**:
- Blank line before and after `---` is optional but recommended
- Use exactly three hyphens (not more, not less)

---

## Directives

Directives control slide-specific styling. They must be placed **at the top of a slide** (after `---`).

### Global Directives (in frontmatter)

```yaml
---
marp: true
theme: default
paginate: true
backgroundColor: #f8fafc
---
```

### Local Directives (per slide)

```markdown
---

<!-- _class: lead -->
<!-- _backgroundColor: #0891b2 -->
<!-- _color: #ffffff -->

# Section Title
```

**Common directives**:
- `<!-- _class: lead -->` - Center-aligned, large text (title slides)
- `<!-- _class: invert -->` - Invert colors (dark background)
- `<!-- _backgroundColor: #HEX -->` - Custom background color
- `<!-- _color: #HEX -->` - Custom text color
- `<!-- _paginate: false -->` - Hide page number on this slide

**Directive syntax**:
- Must start with `<!--` and end with `-->`
- Underscore `_` means "apply to this slide only"
- Without underscore applies to all following slides

---

## Headers and Text

### Header Hierarchy

```markdown
# H1 - Main Title (slide title)
## H2 - Section Heading
### H3 - Subsection
#### H4 - Minor heading (rarely used)
```

**Best practices**:
- Use `#` for slide titles only
- Use `##` for main content headings
- Maintain consistent hierarchy throughout presentation

### Text Formatting

```markdown
**Bold text**
*Italic text*
~~Strikethrough~~
`inline code`
```

### Lists

```markdown
- Unordered list
- Item 2
  - Nested item
  - Another nested

1. Ordered list
2. Item 2
   1. Nested ordered
```

---

## Code Blocks

### Basic Code Block

````markdown
```python
def hello():
    print("Hello, World!")
```
````

### Code with Language Highlighting

````markdown
```javascript
const greet = () => {
  console.log("Hello!");
};
```
````

**Supported languages**: Most common languages (Python, JavaScript, TypeScript, Go, Rust, Java, C++, etc.)

---

## Images

**IMPORTANT: Prefer `bg` (background) syntax for all images to avoid manual size adjustments.**

### Background Images (Recommended)

Use background syntax to automatically size and position images:

```markdown
# Full-page background (entire slide)
![bg fit](diagrams/architecture.svg)

# Right-side image (split layout)
![bg right fit](diagrams/workflow.svg)

# Left-side image (split layout)
![bg left fit](diagrams/concept.svg)

# Custom width split
![bg right:40% fit](diagrams/detail.svg)  # Image takes 40% on right
![bg left:60% fit](diagrams/main.svg)     # Image takes 60% on left
```

**Key benefits of `bg` syntax:**
- `fit` modifier auto-scales images to fill available space
- No manual width/height adjustments needed
- Consistent sizing across slides
- Better for responsive layouts

### Split Layout Patterns

**Text on left, image on right:**
```markdown
![bg right fit](diagrams/city-venice.svg)

# Feature Description

- Point 1
- Point 2
- Point 3
```

**Image on left, text on right:**
```markdown
![bg left fit](diagrams/concept.svg)

# Explanation

Content appears on the right side.
```

**Full-page image with optional overlay text:**
```markdown
![bg fit](diagrams/pretrip-checklist.svg)

# Optional Title
Text will overlay on the image
```

### Regular Images (Avoid if possible)

Only use for small inline images (icons, logos):

```markdown
![width:60px](icon.svg)  # Small icon only
```

**Do NOT use regular syntax for diagrams or large images** - use `bg` instead.

---

## Custom Styling

### Scoped Style Tags

```markdown
<style scoped>
section {
  background: linear-gradient(to bottom, #f0f9ff, #e0f2fe);
}
h1 {
  color: #0891b2;
  font-weight: 700;
}
</style>

# Styled Slide
```

### Inline HTML

Marpit supports limited HTML:

```markdown
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px;">
  <div>

## Left Column
Content here

  </div>
  <div>

## Right Column
More content

  </div>
</div>
```

**Limitations**:
- Not all HTML elements supported
- Keep it simple—prefer Markdown when possible

---

## Two-Column Layouts

### Method 1: HTML Grid

```markdown
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px;">

<div>

## Left
- Point 1
- Point 2

</div>

<div>

## Right
- Point A
- Point B

</div>

</div>
```

### Method 2: Flexbox

```markdown
<div style="display: flex; gap: 32px;">

<div style="flex: 1;">

Content left

</div>

<div style="flex: 1;">

Content right

</div>

</div>
```

See [patterns.md](patterns.md) for more layout examples.

---

## Special Features

### Presenter Notes

```markdown
# Slide Title

Content visible to audience.

<!--
These are presenter notes.
Only visible in presenter mode.
-->
```

### Fragments (Incremental Reveal)

Not supported in Marpit by default. Use separate slides instead:

```markdown
---
# Point 1
---
# Point 1
## Point 2
---
# Point 1
## Point 2
### Point 3
```

---

## Theme Selection

### Available Themes

1. **default** - Clean, minimal, professional
2. **gaia** - Modern, colorful, tech-focused
3. **uncover** - Bold, high-contrast, presentation-style

### Setting Theme

In frontmatter:
```yaml
---
marp: true
theme: gaia
---
```

Or per-slide:
```markdown
<!-- theme: uncover -->
```

See [themes.md](themes.md) for detailed theme documentation.

---

## Common Patterns

### Title Slide

```markdown
---
marp: true
theme: default
---

<!-- _class: lead -->

# Presentation Title
Subtitle or Tagline

Your Name · Date

---
```

### Section Divider

```markdown
<!-- _class: lead -->
<!-- _backgroundColor: #0891b2 -->
<!-- _color: #ffffff -->

# Section Name

---
```

### Content Slide

```markdown
## Slide Title

- Key point 1
- Key point 2
- Key point 3

---
```

### Code Example Slide

````markdown
## Code Example

```python
def calculate(x, y):
    return x + y

result = calculate(5, 3)
print(result)  # Output: 8
```

---
````

See [patterns.md](patterns.md) for comprehensive pattern library.

---

## Best Practices

1. **Start with frontmatter** - Always include `marp: true`
2. **One idea per slide** - Don't overcrowd slides
3. **Use consistent directives** - Apply same styles to similar slides
4. **Test rendering** - Preview slides before finalizing
5. **Keep it simple** - Prefer Markdown over complex HTML

See [best-practices.md](best-practices.md) for detailed guidelines.

---

## Troubleshooting

### Slide not rendering

- Check frontmatter has `marp: true`
- Verify `---` separator is correct (exactly 3 hyphens)
- Ensure no syntax errors in directives

### Images not showing

- Check file path is correct
- Use relative paths from .md file location
- Verify image format is supported (PNG, JPG, SVG)

### Styling not applying

- Verify `<style scoped>` tag is properly closed
- Check CSS syntax is valid
- Ensure directives are at top of slide

---

## Quick Reference Card

```markdown
# Slide structure
---
marp: true
---
<!-- _class: lead -->
# Title
---
## Content
---

# Formatting
**bold** *italic* `code`

# Lists
- Item
  - Nested

# Code
```language
code here
```

# Images (prefer bg syntax)
![bg fit](full-page.svg)
![bg right fit](side-image.svg)
![bg left:60% fit](main-image.svg)

# Directives
<!-- _class: lead -->
<!-- _backgroundColor: #HEX -->
<!-- _color: #HEX -->
```

---

## See Also

- [patterns.md](patterns.md) - Common slide patterns and layouts
- [themes.md](themes.md) - Theme-specific features
- [advanced-layouts.md](advanced-layouts.md) - Complex layout techniques
- [best-practices.md](best-practices.md) - Design and consistency guidelines
