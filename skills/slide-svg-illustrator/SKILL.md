# Marp Slide SVG Illustrator

## Intent

Create clean, editable SVG illustrations that embed reliably in **Marp/Marpit Markdown** and look good in **HTML exports**. Optimize for common slide placement: **centered** or **left/right** aligned blocks, sometimes full-slide backgrounds.

---

## Core Defaults

### Canvas Specifications

**CRITICAL: viewBox Must Match Content Bounds**

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

**Guidelines:**

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

## File Management and Organization

### Standard Directory Structure

All SVG files **MUST be saved to disk** using the Write tool. **NEVER embed SVG inline in Markdown.**

**Standard structure:**
```
presentation-root/
├── slides.md          # Main presentation file
└── assets/
    ├── diagrams/      # Process flows, architecture diagrams
    ├── icons/         # Icon sets, badges
    ├── charts/        # Data visualizations, graphs
    ├── backgrounds/   # Full-slide background images
    └── images/        # Other images (photos, screenshots)
```

**Key principle: On-demand creation** - Only create directories when needed (when saving the first file to that location).

### Asset Classification Logic

Use this decision tree to determine the correct subdirectory:

| SVG Type | Subdirectory | Examples |
|----------|--------------|----------|
| Process flow, architecture, system diagram | `assets/diagrams/` | workflow, data-flow, system-architecture |
| Icon, badge, logo, small graphic | `assets/icons/` | feature-icon, status-badge |
| Chart, graph, data visualization | `assets/charts/` | bar-chart, pie-chart, timeline |
| Full-slide background pattern/image | `assets/backgrounds/` | title-bg, section-bg |
| Other images (not SVG you created) | `assets/images/` | photo, screenshot |

**Default:** If uncertain, use `assets/diagrams/`

### Naming Conventions

Use descriptive, kebab-case names:
- ✅ `marketplace-architecture.svg`
- ✅ `python-workflow-diagram.svg`
- ✅ `feature-comparison-chart.svg`
- ✅ `plugin-icon.svg`
- ❌ `diagram1.svg`, `img.svg`, `untitled.svg`, `new.svg`

**Pattern:** `{descriptive-name}.svg` where the name clearly indicates what the SVG shows.

### File Creation Workflow

**CRITICAL:** Every SVG must be saved as a separate file:

1. **Determine category** using the classification logic above
2. **Infer meaningful filename** from context (or ask if unclear)
3. **Check if directory exists** (conceptually - Write/Bash will handle it)
4. **Create directory if needed** using `mkdir -p assets/{category}/`
5. **Use Write tool** to save SVG to `assets/{category}/{name}.svg`
6. **Provide embedding code** with correct relative path
7. **Inform user** of the file path created

**Example:**
```
User: "Create a marketplace architecture diagram"
→ Category: diagrams (it's an architecture diagram)
→ Filename: marketplace-architecture.svg
→ Path: assets/diagrams/marketplace-architecture.svg
→ Check: does assets/diagrams/ exist?
→ If no: mkdir -p assets/diagrams/
→ Write SVG to assets/diagrams/marketplace-architecture.svg
→ Return embedding: ![w:1200](assets/diagrams/marketplace-architecture.svg)
```

---

## Output Contract

Every response MUST include:

1. **1–3 bullets**: intent + layout + recommended embed style
2. **File creation**: Use Bash to create directory (if needed) and Write tool to save SVG
   - Report the file path to user
   - Ensure path is relative from presentation root
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

- [ ] **viewBox matches content bounds** (no excessive empty space)
- [ ] No clipping of content outside viewBox
- [ ] Legible at typical slide viewing size
- [ ] Consistent alignment and spacing
- [ ] All paths use 8px grid alignment
- [ ] Colors follow palette guidelines
- [ ] Test embedding: `![w:XXX](path)` displays content at intended size

---

## Normalize & Optimize Workflow (Existing SVG)

When fixing or optimizing existing SVG files:

### Goal

Ensure consistent embedding in Marp HTML exports.

### Checklist

- [ ] **Ensure `viewBox` exists and matches content bounds** (no excessive empty space)
- [ ] **Adjust viewBox to actual content size**, not arbitrary 1920×1080 unless truly full-slide
- [ ] Remove editor metadata (Inkscape/Illustrator) if safe
- [ ] Flatten styles if needed (avoid reliance on external CSS)
- [ ] Replace problematic features with simpler primitives
- [ ] Decide on text: editable `<text>` vs paths
- [ ] Verify rendering in Marp preview and check scaling behavior

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

**File Creation:**
```
Created: assets/diagrams/marketplace-architecture.svg
```

**Marp Embedding:**
```markdown
![w:1200](assets/diagrams/marketplace-architecture.svg)
```

**Note:** The SVG file is saved to disk using Write tool. Do NOT output the raw SVG code to the user unless explicitly requested for debugging purposes.

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
