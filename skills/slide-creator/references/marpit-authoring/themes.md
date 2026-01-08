# Themes and Directives Reference

## Table of Contents

- [Built-in Themes](#built-in-themes)
  - [1. Default Theme](#1-default-theme)
  - [2. Gaia Theme](#2-gaia-theme)
  - [3. Uncover Theme](#3-uncover-theme)
- [Global Directives (Frontmatter)](#global-directives-frontmatter)
- [Local Directives (Per-Slide)](#local-directives-per-slide)
  - [Background Color](#background-color)
  - [Text Color](#text-color)
  - [Hide Pagination](#hide-pagination)
  - [Custom Class](#custom-class)
- [Common Classes](#common-classes)
  - [`lead`](#lead)
  - [`invert`](#invert)
  - [Combining Classes](#combining-classes)
- [Image Sizing and Positioning](#image-sizing-and-positioning)
  - [Background Image](#background-image)
  - [Background Image with Styling](#background-image-with-styling)
  - [Image Filters](#image-filters)
- [Image as Background](#image-as-background)
- [Color Keywords](#color-keywords)
- [Custom Styling (Advanced)](#custom-styling-advanced)
  - [Inline Custom CSS](#inline-custom-css)
  - [Scoped Styles](#scoped-styles)
- [Fragmentation (Build Animations)](#fragmentation-build-animations)
- [Headers and Footers](#headers-and-footers)
- [Common Directive Combinations](#common-directive-combinations)
  - [Dark Title Slide](#dark-title-slide)
  - [Image Split Layout](#image-split-layout)
  - [Subtle Background](#subtle-background)
- [Quick Reference Table](#quick-reference-table)
- [Theme Selection Guide](#theme-selection-guide)

Marpit styling options and customization techniques.

---

## Built-in Themes

### 1. Default Theme
```markdown
---
marp: true
theme: default
---
```

**Characteristics:**
- Clean, minimal design
- Blue accent colors
- Good for technical content
- Standard font sizing

---

### 2. Gaia Theme
```markdown
---
marp: true
theme: gaia
---
```

**Characteristics:**
- Modern, colorful
- Larger headings
- Better for creative/business presentations
- Supports lead class well

---

### 3. Uncover Theme
```markdown
---
marp: true
theme: uncover
---
```

**Characteristics:**
- Bold, high-contrast
- Large typography
- Dramatic section dividers
- Great for keynotes

---

## Global Directives (Frontmatter)

Applied to entire presentation:

```markdown
---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff
color: #333333
class: invert
style: |
  section {
    font-size: 28px;
  }
---
```

**Common options:**
- `paginate: true` - Show page numbers
- `backgroundColor` - Default background color
- `color` - Default text color
- `class` - Default class for all slides
- `style` - Custom CSS for entire deck

---

## Local Directives (Per-Slide)

Applied with HTML comments using `_` prefix:

### Background Color
```markdown
<!-- _backgroundColor: #1a1a1a -->
# Dark Background Slide
```

### Text Color
```markdown
<!-- _color: #ffffff -->
# White Text
```

### Hide Pagination
```markdown
<!-- _paginate: false -->
# No Page Number Here
```

### Custom Class
```markdown
<!-- _class: lead -->
# Centered Large Text
```

---

## Common Classes

### `lead`
```markdown
<!-- _class: lead -->
# Centered Content
Subtitle text
```

**Effect:** Centers content, enlarges text, good for section dividers

---

### `invert`
```markdown
<!-- _class: invert -->
# Inverted Colors
```

**Effect:** Swaps foreground/background (dark mode)

---

### Combining Classes
```markdown
<!-- _class: lead invert -->
# Dark Centered Slide
```

**Effect:** Applies both lead and invert styles

---

## Image Sizing and Positioning

### Background Image
```markdown
<!-- _backgroundImage: url('path/to/image.jpg') -->
# Text Over Image
```

### Background Image with Styling
```markdown
<!-- _backgroundImage: "linear-gradient(to bottom, rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('image.jpg')" -->
# Darkened Background
```

### Image Filters
```markdown
![bg](image.jpg)
![bg brightness:0.5](darker-image.jpg)
![bg blur:5px](blurred-bg.jpg)
```

**Available filters:**
- `brightness` - Adjust brightness (0-1)
- `contrast` - Adjust contrast
- `blur` - Apply blur effect
- `grayscale` - Convert to grayscale
- `sepia` - Apply sepia tone

---

## Image as Background

```markdown
![bg](background.jpg)

# Content Over Background
```

**Modifiers:**
- `![bg](image.jpg)` - Full background
- `![bg left](image.jpg)` - Left half
- `![bg right](image.jpg)` - Right half
- `![bg vertical](image.jpg)` - Split vertically
- `![bg fit](image.jpg)` - Fit without cropping

---

## Color Keywords

Use standard CSS colors or hex codes:

```markdown
<!-- _backgroundColor: aqua -->
<!-- _backgroundColor: #00FFFF -->
<!-- _backgroundColor: rgb(0, 255, 255) -->
```

**Common colors:**
- `black`, `white`
- `red`, `green`, `blue`
- `aqua`, `navy`, `teal`
- `orange`, `purple`, `pink`

---

## Custom Styling (Advanced)

### Inline Custom CSS
```markdown
---
marp: true
style: |
  section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
  h1 {
    border-bottom: 3px solid white;
  }
---
```

### Scoped Styles
```markdown
<style scoped>
h1 {
  color: #ff6b6b;
  font-size: 72px;
}
</style>

# Custom Styled Title
```

**Note:** Scoped styles only affect the current slide.

---

## Fragmentation (Build Animations)

**Not natively supported in Marpit**, but some renderers support:

```markdown
* First item
* <!-- .element: class="fragment" --> Second item (appears on click)
* <!-- .element: class="fragment" --> Third item (appears on click)
```

**Alternative:** Use multiple slides with incremental reveals.

---

## Headers and Footers

```markdown
---
marp: true
header: 'Company Name'
footer: 'Confidential - Internal Use Only'
---
```

**Note:** Availability depends on theme support.

---

## Common Directive Combinations

### Dark Title Slide
```markdown
<!-- _class: lead invert -->
<!-- _paginate: false -->

# Presentation Title
```

### Image Split Layout
```markdown
![bg left:40%](diagram.png)

# Content
- Point about the diagram
- Another observation
```

### Subtle Background
```markdown
<!-- _backgroundImage: url('watermark.png') -->
<!-- _backgroundSize: 20% -->
<!-- _backgroundPosition: bottom right -->

# Content With Watermark
```

---

## Quick Reference Table

| Directive | Scope | Example |
|-----------|-------|---------|
| `paginate` | Global/Local | `paginate: true` |
| `backgroundColor` | Global/Local | `#1a1a1a` |
| `color` | Global/Local | `#ffffff` |
| `class` | Global/Local | `lead invert` |
| `backgroundImage` | Local | `url('img.jpg')` |
| `header` | Global | `'Text'` |
| `footer` | Global | `'Text'` |

**Local directives use `_` prefix:** `<!-- _paginate: false -->`

---

## Theme Selection Guide

**Use `default`** for:
- Technical documentation
- Code-heavy presentations
- Professional reports

**Use `gaia`** for:
- Business presentations
- Marketing content
- Creative pitches

**Use `uncover`** for:
- Keynote speeches
- High-impact messages
- Conference talks
