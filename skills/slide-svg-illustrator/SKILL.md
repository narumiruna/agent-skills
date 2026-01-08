# Marp Slide SVG Illustrator

## Intent

Create clean, editable SVG illustrations that embed reliably in **Marp/Marpit Markdown** and look good in **HTML exports**. Optimize for common slide placement: **centered** or **left/right** aligned blocks, sometimes full-slide backgrounds.

---

## Core Defaults

### Canvas Specifications

- Slide baseline: **16:9, 1920×1080**
- SVG canvas: `viewBox="0 0 1920 1080"` with explicit `width="1920"` `height="1080"`
- Safe margins: **120px on each side** (keep key content inside)
- Grid alignment: **8px**

### Visual Style

- Stroke width: **4px @ 1920×1080**, rounded caps/joins
- Default palette:
  - Dark: `#111827`
  - Mid: `#6B7280`
  - Light: `#E5E7EB`
  - Accent: `#2563EB`

### Technical Constraints

- No external dependencies: no remote images, no external CSS, no external font loading
- HTML-first: optimize for Marp HTML export (GitHub Actions workflow)
- Self-contained: all styles and assets inline

---

## Output Contract

Every response MUST include:

1. **1–3 bullets**: intent + layout + recommended embed style
2. **One SVG** in a single code block
3. **One Marp embedding snippet** (choose the best option from below)

---

## Smart Sizing Logic

**IMPORTANT**: Analyze the current slide's configuration to determine optimal SVG size automatically.

### Decision Flow

#### 1. Detect Slide Context

Look for these indicators in the conversation:

- **Theme mentioned**: `theme: default`, `theme: gaia`, `theme: uncover`
- **Layout hints**: "centered", "two-column", "left/right split", "full-screen"
- **Content type**: diagram, icon, background, illustration
- **Existing slides**: If user shows their slides, match their conventions

#### 2. Choose Size Based on Context

| Context | Recommended Size | Embed Method |
|---------|------------------|--------------|
| **Centered diagram** (default) | `w:1200` (1200px) | `![w:1200](assets/...)` |
| **Centered, compact** | `w:1000` (1000px) | `![w:1000](assets/...)` |
| **Centered, large emphasis** | `w:1400` (1400px) | `![w:1400](assets/...)` |
| **Two-column layout** | `width="720"` or `width="760"` | `<img ... width="720">` |
| **Small icon/badge** | `w:200` to `w:400` | `![w:300](assets/...)` |
| **Full-slide background** | Native 1920×1080 | `backgroundImage: url(...)` |
| **Icon set (multiple)** | Individual icons 120×120 | Arrange in grid |

#### 3. Theme-Specific Adjustments

**Default theme**:
- Clean, technical → prefer `w:1200` for main diagrams
- Works well with two-column at `width="720"`

**Gaia theme**:
- Larger, bolder → prefer `w:1400` for impact
- Two-column at `width="760"` for better balance

**Uncover theme**:
- Dramatic, full-screen → prefer `w:1400` or background images
- High contrast, larger strokes (consider 5-6px)

#### 4. Layout-Specific Decisions

**Centered on slide**:
```markdown
![w:1200](assets/diagram.svg)
```

**Left text + right diagram**:
```markdown
<div style="display:grid; grid-template-columns: 1fr 720px; gap:48px;">
  <div>Content...</div>
  <div><img src="assets/diagram.svg" width="720" /></div>
</div>
```

**Right text + left diagram**:
```markdown
<div style="display:grid; grid-template-columns: 720px 1fr; gap:48px;">
  <div><img src="assets/diagram.svg" width="720" /></div>
  <div>Content...</div>
</div>
```

**Full-slide background**:
```markdown
---
backgroundImage: url("assets/bg.svg")
backgroundSize: cover
---
```

### Inference Examples

**User says**: "Create a process flow diagram for my slide"
→ **Infer**: Centered, main content → use `w:1200`

**User says**: "Make an SVG to go next to my bullet points on the right"
→ **Infer**: Two-column layout → use `width="720"` with grid layout

**User says**: "Create a background pattern for the title slide"
→ **Infer**: Full-slide background → use native 1920×1080 + `backgroundImage`

**User says**: "I need 6 icons for feature highlights"
→ **Infer**: Icon set → create at 120×120 each, arrange in grid

**User mentions**: "I'm using the gaia theme"
→ **Adjust**: Increase recommended widths by ~15%, consider bolder strokes

### Default When Uncertain

If no context is provided, use these safe defaults:

- **Size**: `w:1200` (1200px wide)
- **Embed**: `![w:1200](assets/diagram.svg)`
- **Canvas**: 1920×1080 with safe margins
- **Theme**: Assume `default` theme

### Multi-Version Output (Optional)

When appropriate, offer both versions:

1. **Standard**: `diagram.svg` (1920×1080 canvas, centered at w:1200)
2. **Compact**: `diagram-compact.svg` (1200×675 canvas, use at w:1000)

This gives users flexibility without manual scaling.

---

## Embedding Options

### Option A (Default): External SVG File + Image Syntax

Use when the SVG is saved as `assets/<name>.svg`.

**Centered:**

```markdown
![w:1200](assets/diagram.svg)
```

**Left/right aligned (HTML-first, reliable):**

```markdown
<div style="display:flex; gap:40px; align-items:center;">
  <div style="flex:1;">
    <!-- your text -->
    - Point A
    - Point B
  </div>
  <div style="flex:0 0 auto;">
    <img src="assets/diagram.svg" width="720" />
  </div>
</div>
```

Swap columns to place SVG on the left.

---

### Option B: Two-Column Slide Layout with Consistent Sizing

Use when the slide is structurally "text + figure".

```markdown
<div style="display:grid; grid-template-columns: 1fr 760px; gap:48px; align-items:center;">
  <div>
    ## Title
    - Bullet 1
    - Bullet 2
  </div>
  <div style="justify-self:center;">
    <img src="assets/figure.svg" width="760" />
  </div>
</div>
```

---

### Option C: Full-Slide Background SVG

Use when the SVG is designed as a full canvas background.

```markdown
---
backgroundImage: url("assets/bg.svg")
backgroundSize: cover
---

# Title
```

---

## SVG Authoring Rules (HTML-First)

### Required Elements

Every SVG MUST include:

```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <title>Descriptive title</title>
  <desc>Brief description of the illustration</desc>

  <g id="bg"><!-- background elements --></g>
  <g id="main"><!-- primary content --></g>
  <g id="labels"><!-- text labels --></g>
  <g id="decor"><!-- decorative elements --></g>
</svg>
```

### Grouping Convention

Use meaningful IDs for layer organization:

- `id="bg"` - Background shapes, fills, base layer
- `id="main"` - Primary diagram elements, key content
- `id="labels"` - Text labels, annotations
- `id="decor"` - Decorative elements, accents, embellishments

### Styling Strategy

Choose one approach per SVG:

1. **Inline attributes** (preferred for simple diagrams):
   ```xml
   <rect fill="#111827" stroke="#2563EB" stroke-width="4" />
   ```

2. **Internal `<style>` block** (for consistent theming):
   ```xml
   <style>
     .primary { fill: #2563EB; }
     .stroke { stroke: #111827; stroke-width: 4; }
   </style>
   ```

### What to Avoid

- `<foreignObject>` - inconsistent rendering across browsers
- Heavy `filter` chains - especially blur effects
- External font references - use system font stack or paths
- Embedded raster images - unless explicitly requested

### Text Strategy

**Default behavior**: Keep text editable *only if asked*.

**If labels are required but editability is not important:**
- Prefer simple shapes + minimal `<text>` elements

**If exact typography is required:**
- Convert text to paths
- Warn user that text is not editable

**If using `<text>`, use system-safe font stack:**

```xml
<text font-family="ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial">
  Label
</text>
```

---

## Create Workflow

When generating new SVG illustrations:

### 1. Infer Constraints

Assume defaults if missing:

- **Placement**: center vs left/right block
- **Style**: outline / flat / mixed
- **Palette**: default neutral + 1 accent color

### 2. Pick Embedding Option

- Most cases: **Option A** (external file)
- Text + figure: **Option B** (grid layout)
- Full background: **Option C** (background image)

### 3. Layout Design

- Use 8px grid alignment
- Keep content inside safe margins (120px from edges)
- Maintain consistent spacing between elements

### 4. Build Layers

Organize content with consistent styling:

- `bg` - Background shapes, fills
- `main` - Primary diagram elements
- `labels` - Text annotations
- `decor` - Decorative accents

Use consistent stroke widths (4px) and border radius values.

### 5. Final Checks

- [ ] No clipping of content outside viewBox
- [ ] Legible at typical slide viewing size
- [ ] Consistent alignment and spacing
- [ ] All paths use 8px grid alignment
- [ ] Colors follow palette guidelines

---

## Normalize & Optimize Workflow (Existing SVG)

When fixing or optimizing existing SVG files:

### Goal

Ensure consistent embedding in Marp HTML exports.

### Checklist

- [ ] Ensure `viewBox` exists and matches content bounds
- [ ] Normalize to 1920×1080 canvas for slide illustrations (keep original for icons)
- [ ] Remove editor metadata (Inkscape/Illustrator) if safe
- [ ] Flatten styles if needed (avoid reliance on external CSS)
- [ ] Replace problematic features with simpler primitives
- [ ] Decide on text: editable `<text>` vs paths
- [ ] Verify rendering in Marp preview

---

## Pattern Library (Quick Templates)

### Process Flow (3–7 steps)

- Rounded rectangles for steps
- Arrows with proper spacing
- Step numbers in circles
- Consistent gap: 80px between steps

### Timeline

- Horizontal baseline
- Milestones as circles or markers
- Labels below timeline
- Date range above

### Architecture Diagram

- Containers as rounded rectangles
- Components as smaller boxes inside
- Connectors with arrow markers
- Layer separation: 160px

### Comparison (2–3 columns)

- Equal-width columns
- Consistent iconography at top
- Bullet points below
- Visual separators between columns

### KPI Callout

- Large number (72px font or path)
- Label below (24px)
- Simple sparkline path if showing trend
- Optional icon or indicator

---

## Common Widths Reference

Recommended widths for different placements:

- **Centered, full attention**: `w:1200` (1200px)
- **Centered, compact**: `w:1000` (1000px)
- **Side-by-side with text**: `width="720"` or `width="760"`
- **Small icon or badge**: `w:200` to `w:400`
- **Full-width background**: native 1920px

---

## Trigger Examples

This skill should activate when users request:

- "Make an SVG diagram for a Marp slide, centered at w:1200"
- "Create an SVG illustration to sit on the right side next to bullets"
- "Fix this SVG so it scales correctly in Marp HTML"
- "Generate 6 consistent outline icons for slides"
- "Create a process flow diagram with 5 steps"
- "Design an architecture diagram showing 3 layers"

---

## Output Format

Always structure responses like this:

**Intent & Layout:**
- Brief description of what the SVG shows
- Recommended placement (centered / left / right)
- Suggested embed method (Option A/B/C)

**SVG Code:**
```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <!-- complete SVG here -->
</svg>
```

**Marp Embedding:**
```markdown
<!-- chosen embedding snippet -->
```

---

## Quality Standards

All SVG output must meet these criteria:

1. **Accessibility**: Include meaningful `<title>` and `<desc>`
2. **Maintainability**: Use clear IDs and logical grouping
3. **Performance**: Minimize path complexity, avoid unnecessary elements
4. **Consistency**: Follow grid alignment and palette rules
5. **Compatibility**: Test rendering in Marp HTML output

---

## Advanced: Two-Version Output (Optional)

For maximum flexibility, consider generating two versions:

1. **Full canvas**: `diagram.svg` (1920×1080) - for background use
2. **Compact**: `diagram-compact.svg` (1200×675) - for centered embedding

This gives users options without manual scaling.

---

## References

See `references/` for:
- Common diagram patterns with code examples
- Color palette variations
- Icon design guidelines
- Troubleshooting embedding issues
