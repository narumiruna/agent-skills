# Troubleshooting

## Table of Contents

- [Issue: Emoji Not Rendering in SVG](#issue-emoji-not-rendering-in-svg)
- [Issue: SVG Not Rendering](#issue-svg-not-rendering)
  - [1. Incorrect File Path](#1-incorrect-file-path)
  - [2. Missing `xmlns` Attribute](#2-missing-xmlns-attribute)
  - [3. External Dependencies](#3-external-dependencies)
- [Issue: SVG Clipped or Cropped](#issue-svg-clipped-or-cropped)
  - [1. Content Outside ViewBox](#1-content-outside-viewbox)
  - [2. Missing ViewBox](#2-missing-viewbox)
  - [3. Transform Issues](#3-transform-issues)
- [Issue: Text Not Displaying](#issue-text-not-displaying)
  - [1. External Font References](#1-external-font-references)
  - [2. Missing Font Size](#2-missing-font-size)
  - [3. Text Color Matches Background](#3-text-color-matches-background)
- [Issue: SVG Too Small or Too Large](#issue-svg-too-small-or-too-large)
  - [1. Wrong Width Specification](#1-wrong-width-specification)
  - [2. Missing Width/Height Attributes](#2-missing-widthheight-attributes)
- [Issue: Inconsistent Rendering Across Browsers](#issue-inconsistent-rendering-across-browsers)
  - [1. Missing Explicit Sizes](#1-missing-explicit-sizes)
  - [2. Using `foreignObject`](#2-using-foreignobject)
- [Issue: Blurry or Pixelated SVG](#issue-blurry-or-pixelated-svg)
  - [1. Rasterized Elements](#1-rasterized-elements)
  - [2. Browser Scaling Issues](#2-browser-scaling-issues)
- [Issue: Colors Not Matching Expectation](#issue-colors-not-matching-expectation)
  - [1. Missing Color Definitions](#1-missing-color-definitions)
  - [2. Invalid Gradient References](#2-invalid-gradient-references)
- [Issue: Performance Problems](#issue-performance-problems)
  - [1. Overly Complex Paths](#1-overly-complex-paths)
  - [2. Too Many Elements](#2-too-many-elements)
- [Issue: Alignment Issues](#issue-alignment-issues)
  - [1. Not Using Grid](#1-not-using-grid)
  - [2. Inconsistent Spacing](#2-inconsistent-spacing)
- [Issue: Arrows Not Appearing](#issue-arrows-not-appearing)
  - [1. Missing Marker Definition](#1-missing-marker-definition)
  - [2. Incorrect Marker Reference](#2-incorrect-marker-reference)
- [Issue: GitHub Actions Build Fails](#issue-github-actions-build-fails)
  - [1. File Not Committed](#1-file-not-committed)
  - [2. Incorrect Path in CI](#2-incorrect-path-in-ci)
- [SVG Validation Tools](#svg-validation-tools)
  - [svglint - Command-Line SVG Linter](#svglint-command-line-svg-linter)
- [Debugging Workflow](#debugging-workflow)
- [Quick Fixes Checklist](#quick-fixes-checklist)
- [Still Having Issues?](#still-having-issues)

Common issues and solutions when embedding SVG in Marp slides.

---

## Issue: Emoji Not Rendering in SVG

**Symptoms:**
- Emoji characters appear as boxes or blank spaces
- Icons show correctly in editor but break in exports
- Inconsistent rendering across different platforms

**Cause:**
Emoji in `<text>` elements are not reliably supported across SVG renderers. Different browsers, PDF exporters, and SVG viewers handle emoji differently or not at all.

**Solution:**
**NEVER use emoji in SVG `<text>` elements.** Use pure SVG paths and shapes instead.

**Wrong:**
```xml
<text x="100" y="100" font-size="48">🛡️</text>
<text x="200" y="100" font-size="48">🎓</text>
<text x="300" y="100" font-size="48">🎨</text>
```

**Correct:**
```xml
<!-- Shield icon using SVG paths -->
<path d="M 100 70 L 120 80 L 120 110 Q 120 120 100 130 Q 80 120 80 110 L 80 80 Z"
      fill="none" stroke="#e8d7b0" stroke-width="3"/>

<!-- Graduation cap using SVG shapes -->
<rect x="90" y="95" width="40" height="8" rx="2" fill="#e8d7b0"/>
<path d="M 110 95 L 80 85 L 110 75 L 140 85 Z" fill="#e8d7b0"/>

<!-- Palette using circles and paths -->
<circle cx="300" cy="85" r="4" fill="#e8d7b0"/>
<circle cx="315" cy="85" r="4" fill="#e8d7b0"/>
```

**Best Practices:**
- Create simple geometric icons from circles, rects, and paths
- Use Unicode characters only for standard Latin text
- Test SVG rendering in target export format (HTML, PDF)
- Keep icon designs simple and recognizable at small sizes

---

## Issue: SVG Not Rendering

**Symptoms:**
- Blank space where SVG should appear
- Broken image icon
- SVG works locally but not in HTML export

**Causes & Solutions:**

### 1. Incorrect File Path

**Problem:** Path doesn't match actual file location

**Fix:**
```markdown
<!-- Wrong -->
![w:1200](diagram.svg)

<!-- Correct -->
![w:1200](assets/diagram.svg)
```

Verify file structure:
```
presentation/
├── slides.md
└── assets/
    └── diagram.svg
```

### 2. Missing `xmlns` Attribute

**Problem:** SVG missing XML namespace declaration

**Fix:**
```xml
<!-- Wrong -->
<svg viewBox="0 0 1920 1080">

<!-- Correct -->
<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
```

### 3. External Dependencies

**Problem:** SVG references external resources

**Fix:** Embed all resources inline
```xml
<!-- Wrong: external image -->
<image href="http://example.com/image.png" />

<!-- Correct: data URI or remove -->
<image href="data:image/png;base64,..." />
```

---

## Issue: SVG Clipped or Cropped

**Symptoms:**
- Parts of SVG cut off at edges
- Content extends beyond visible area

**Causes & Solutions:**

### 1. Content Outside ViewBox

**Problem:** Elements positioned outside viewBox bounds

**Fix:** Ensure all content within 120-1800 range (horizontal) and 120-960 range (vertical)

```xml
<!-- Check bounds -->
<rect x="120" y="120" width="1680" height="840" fill="none" stroke="red"/>
```

### 2. Missing ViewBox

**Problem:** ViewBox not defined or incorrect

**Fix:**
```xml
<!-- Wrong -->
<svg width="1920" height="1080">

<!-- Correct -->
<svg viewBox="0 0 1920 1080" width="1920" height="1080">
```

### 3. Transform Issues

**Problem:** Elements transformed outside visible area

**Fix:** Review all `transform` attributes
```xml
<!-- Check: does this push content out? -->
<g transform="translate(2000, 0)">
```

---

## Issue: Text Not Displaying

**Symptoms:**
- Missing labels or annotations
- Font rendering issues

**Causes & Solutions:**

### 1. External Font References

**Problem:** Font not available in export environment

**Fix:** Use system font stack
```xml
<!-- Wrong -->
<text font-family="CustomFont">

<!-- Correct -->
<text font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial">
```

### 2. Missing Font Size

**Problem:** Font size not specified, defaults to tiny

**Fix:**
```xml
<!-- Add explicit font-size -->
<text font-size="24" fill="#111827">Label</text>
```

### 3. Text Color Matches Background

**Problem:** Text invisible due to same color as background

**Fix:** Verify contrast
```xml
<rect fill="#FFFFFF"/>
<text fill="#000000">Visible text</text>
```

---

## Issue: SVG Too Small or Too Large

**Symptoms:**
- SVG appears tiny on slide
- SVG overflows slide bounds

**Causes & Solutions:**

### 1. Wrong Width Specification

**Problem:** Width not appropriate for layout

**Fix:** Adjust based on placement

**Centered:**
```markdown
![w:1200](assets/diagram.svg)
```

**Side-by-side:**
```markdown
<img src="assets/diagram.svg" width="720" />
```

### 2. Missing Width/Height Attributes

**Problem:** Browser can't determine size

**Fix:**
```xml
<!-- Wrong -->
<svg viewBox="0 0 1920 1080">

<!-- Correct -->
<svg viewBox="0 0 1920 1080" width="1920" height="1080">
```

---

## Issue: Inconsistent Rendering Across Browsers

**Symptoms:**
- SVG looks different in Chrome vs Firefox
- Elements misaligned in HTML export

**Causes & Solutions:**

### 1. Missing Explicit Sizes

**Problem:** Relying on browser defaults

**Fix:** Specify all dimensions explicitly
```xml
<rect x="100" y="100" width="200" height="100" />
<!-- Not: <rect /> with CSS -->
```

### 2. Using `foreignObject`

**Problem:** `foreignObject` has inconsistent support

**Fix:** Avoid entirely, use native SVG elements
```xml
<!-- Avoid -->
<foreignObject>
  <div>HTML content</div>
</foreignObject>

<!-- Use instead -->
<text>SVG text</text>
```

---

## Issue: Blurry or Pixelated SVG

**Symptoms:**
- SVG appears low quality
- Jagged edges

**Causes & Solutions:**

### 1. Rasterized Elements

**Problem:** SVG contains embedded raster images

**Fix:** Use vector shapes only
```xml
<!-- Avoid -->
<image href="bitmap.png" />

<!-- Prefer -->
<path d="M..." />
```

### 2. Browser Scaling Issues

**Problem:** SVG scaled improperly by browser

**Fix:** Ensure viewBox and dimensions match
```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080">
```

---

## Issue: Colors Not Matching Expectation

**Symptoms:**
- Colors appear different in export
- Gradients not rendering

**Causes & Solutions:**

### 1. Missing Color Definitions

**Problem:** Colors not explicitly defined

**Fix:**
```xml
<!-- Wrong: relies on defaults -->
<rect />

<!-- Correct: explicit colors -->
<rect fill="#E5E7EB" stroke="#111827" />
```

### 2. Invalid Gradient References

**Problem:** Gradient ID doesn't match

**Fix:**
```xml
<defs>
  <linearGradient id="grad1">...</linearGradient>
</defs>
<rect fill="url(#grad1)" />
<!-- Ensure ID matches -->
```

---

## Issue: Performance Problems

**Symptoms:**
- Slide deck loads slowly
- Browser lags when navigating

**Causes & Solutions:**

### 1. Overly Complex Paths

**Problem:** Too many path points

**Fix:** Simplify paths using tools or manual reduction
```xml
<!-- Complex -->
<path d="M0,0 L1,1 L2,1.5 L3,2 ..." />

<!-- Simplified -->
<path d="M0,0 L10,10" />
```

### 2. Too Many Elements

**Problem:** Thousands of individual elements

**Fix:** Group and simplify
```xml
<!-- Instead of 100 circles -->
<circle ... />
<circle ... />

<!-- Use patterns or combine -->
<pattern id="dots">...</pattern>
```

---

## Issue: Alignment Issues

**Symptoms:**
- Elements not aligned as expected
- Spacing inconsistent

**Causes & Solutions:**

### 1. Not Using Grid

**Problem:** Arbitrary positioning

**Fix:** Align to 8px grid
```xml
<!-- Wrong -->
<rect x="123" y="456" />

<!-- Correct -->
<rect x="120" y="456" />
```

### 2. Inconsistent Spacing

**Problem:** Different gaps between elements

**Fix:** Use consistent spacing units (40px, 80px, 160px)

---

## Issue: Arrows Not Appearing

**Symptoms:**
- Arrow markers missing from lines
- Arrowheads not visible

**Causes & Solutions:**

### 1. Missing Marker Definition

**Problem:** Marker not defined in `<defs>`

**Fix:**
```xml
<defs>
  <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
    <polygon points="0 0, 10 3, 0 6" fill="#111827" />
  </marker>
</defs>
<line x1="100" y1="100" x2="200" y2="100" marker-end="url(#arrowhead)" />
```

### 2. Incorrect Marker Reference

**Problem:** ID mismatch

**Fix:** Ensure `marker-end="url(#arrowhead)"` matches `id="arrowhead"`

---

## Issue: GitHub Actions Build Fails

**Symptoms:**
- Marp CLI fails to process SVG
- Build errors related to assets

**Causes & Solutions:**

### 1. File Not Committed

**Problem:** SVG file not in repository

**Fix:**
```bash
git add assets/diagram.svg
git commit -m "Add SVG diagram"
git push
```

### 2. Incorrect Path in CI

**Problem:** Path works locally but not in CI

**Fix:** Use relative paths from markdown file
```markdown
![w:1200](./assets/diagram.svg)
```

---

## SVG Validation Tools

### svglint - Command-Line SVG Linter

**Purpose:** Validate SVG syntax, check for common issues, and enforce best practices.

**Installation:**
```bash
npm install -g svglint
```

**Usage:**
```bash
# Validate a single SVG file
svglint path/to/your/file.svg

# Validate with custom config
svglint -C path/to/your/file.svg

# Validate multiple files
svglint path/to/diagrams/*.svg
```

**Common Issues Detected:**
- Invalid XML characters (e.g., unescaped `&` must be `&amp;`)
- Missing required attributes (`xmlns`, `viewBox`)
- Malformed paths or shapes
- Invalid color values
- Incorrect attribute syntax

**Example Error:**
```
x slides/assets/diagrams/three-plugins.svg
  x valid char '&' is not expected.
```

**Fix:** Replace `&` with `&amp;` in text content:
```xml
<!-- Wrong -->
<text>Auto lint & fix</text>

<!-- Correct -->
<text>Auto lint &amp; fix</text>
```

**Other XML Entities to Escape:**
- `<` → `&lt;`
- `>` → `&gt;`
- `"` → `&quot;`
- `'` → `&apos;`
- `&` → `&amp;`

**Best Practice:** Always run `svglint` before committing SVG files to catch syntax errors early.

---

## Debugging Workflow

1. **Open SVG directly in browser**
   - Check if SVG renders correctly standalone
   - Verify viewBox and dimensions

2. **Inspect in Marp preview (VS Code)**
   - Use Marp extension to preview
   - Check console for errors

3. **Test in HTML export**
   ```bash
   marp slides.md -o output.html
   ```
   - Open output.html in browser
   - Check network tab for failed loads

4. **Validate SVG syntax**
   - Use `svglint` for command-line validation: `svglint file.svg`
   - Use online validators (https://validator.w3.org/)
   - Check XML well-formedness and escape special characters

5. **Simplify progressively**
   - Remove complex features one by one
   - Identify problematic element

---

## Quick Fixes Checklist

When SVG isn't working, try:

- [ ] **Validate syntax**: Run `svglint file.svg` to catch XML errors
- [ ] Verify file path is correct
- [ ] Add `xmlns="http://www.w3.org/2000/svg"`
- [ ] Ensure viewBox and width/height are set
- [ ] Remove external dependencies (fonts, images)
- [ ] Check all content within safe margins (120px from edges)
- [ ] Use system font stack for text
- [ ] **Escape special characters**: `&` → `&amp;`, `<` → `&lt;`, etc.
- [ ] Test SVG file standalone in browser
- [ ] Check browser console for errors
- [ ] Simplify complex filters or effects

---

## Still Having Issues?

1. **Validate SVG**:
   - Command-line: `svglint file.svg`
   - Online: https://validator.w3.org/
2. **Check Marp docs**: https://marpit.marp.app/
3. **Simplify**: Start with basic shapes, add complexity gradually
4. **Test standalone**: Open SVG directly in browser
5. **Compare working example**: Use pattern examples from this skill
