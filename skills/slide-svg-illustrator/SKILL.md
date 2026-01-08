# Marp Slide SVG Illustrator

## Intent

Create clean, editable SVG illustrations that embed reliably in **Marp/Marpit Markdown** and look good in **HTML exports**. Optimize for common slide placement: **centered** or **left/right** aligned blocks, sometimes full-slide backgrounds.

---

## Core Principle: Visual Consistency

**CRITICAL: All SVG assets in a presentation must follow a unified design system.**

When creating multiple SVGs for the same presentation:

1. **Use the SAME color palette** across all assets
2. **Maintain consistent stroke widths** (e.g., 3px or 4px everywhere)
3. **Apply uniform border radius** (e.g., 12px or 16px for all cards)
4. **Use consistent shadow/depth system** (same filter definitions)
5. **Keep icon style uniform** (all outlined OR all filled, not mixed)

**Example: Consistent Design System**

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

**Common Inconsistency Mistakes:**

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

- Stroke width: **3-4px** (use 3px for modern, clean look), rounded caps/joins
- **Default palette: Van Gogh Starry Night (Recommended)**
  - Night Sky: `#1e3a5f` (deep prussian blue)
  - Swirling Blue: `#2a5f8f` (cobalt blue)
  - Bright Star: `#f4e5a0` (pale gold)
  - Moon Glow: `#fef7cd` (creamy yellow)
  - Dark Stroke: `#0f1f2e` (midnight blue-black)
  - Village Light: `#d4a574` (warm ochre)

**Why Van Gogh Starry Night?**
- Artistic yet professional
- Distinctive color harmony
- Evokes emotion and creativity
- Works well for technical and creative content
- Blues convey trust and depth
- Golds add warmth and highlight important elements

---

## Design System

### Color Palette & Psychology

**Recommended Default: Van Gogh Starry Night**

Inspired by Vincent van Gogh's masterpiece, this palette combines emotional depth with professional credibility.

```
Primary Colors:
  - Night Sky: #1e3a5f (deep prussian blue)
    → Use for: Main backgrounds, primary containers, trust elements

  - Swirling Blue: #2a5f8f (cobalt blue)
    → Use for: Section dividers, headers, active states

  - Bright Star: #f4e5a0 (pale gold)
    → Use for: Highlights, icons, call-to-action elements

  - Moon Glow: #fef7cd (creamy yellow)
    → Use for: Light backgrounds, subtle highlights, success states

Supporting Colors:
  - Dark Stroke: #0f1f2e (midnight blue-black)
    → Use for: Text, borders, strong contrast

  - Village Light: #d4a574 (warm ochre)
    → Use for: Secondary highlights, warm accents

  - Cypress Green: #1a4d2e (dark forest green)
    → Use for: Alternative accents, nature/growth themes

  - Sky Accent: #4a7ba7 (cerulean)
    → Use for: Links, interactive elements
```

**Color Application Examples:**

```xml
<!-- Card with Starry Night palette -->
<defs>
  <linearGradient id="starry-card" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" style="stop-color:#2a5f8f;stop-opacity:0.1" />
    <stop offset="100%" style="stop-color:#1e3a5f;stop-opacity:0.15" />
  </linearGradient>
</defs>

<rect fill="url(#starry-card)" stroke="#2a5f8f" stroke-width="3" rx="16"/>
<circle fill="#f4e5a0"/>  <!-- Star/icon -->
<text fill="#0f1f2e">Text</text>  <!-- Dark readable text -->
```

**Alternative: Modern Tech Palette (Secondary Option)**

Use this for purely technical, corporate presentations:

```
Primary (Trust, Stability):
  - Deep Blue: #1e40af
  - Cyan Blue: #0891b2

Accent Colors (Context-specific):
  - Amber (Attention, Quality): #f59e0b
  - Emerald (Success, Skills): #10b981
  - Rose (Error, Critical): #e11d48

Neutral Palette:
  - Text Dark: #1e293b
  - Background Light: #f8fafc
  - Border: #cbd5e1
```

**Color Combinations (Pre-tested)**

Use these proven combinations for different contexts:

1. **Tech/Professional**: Deep Blue + Cyan + Slate gray
2. **Code Quality**: Amber + Orange + Yellow tints
3. **Growth/Learning**: Emerald + Teal + Green tints
4. **Process/Flow**: Blue → Cyan → Emerald (gradient progression)
5. **Comparison**: Deep Blue vs Emerald (contrast)

**Color Application Rules**

- **Background cards**: Use subtle gradients (see below) instead of flat colors
- **Icons**: Use solid accent colors with 80-100% opacity
- **Borders**: Use color at 60-80% opacity, 3-4px width (consistent)
- **Text on color**: Ensure WCAG AA contrast (4.5:1 minimum)
- **Gradients**: Subtle, 5-10% lightness difference for modern look

**Recommended Gradient Pattern (Modern, Professional)**

```xml
<!-- For card backgrounds - subtle and professional -->
<linearGradient id="card-bg" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" style="stop-color:#f0f9ff;stop-opacity:1" />
  <stop offset="100%" style="stop-color:#e0f2fe;stop-opacity:1" />
</linearGradient>

<!-- Apply to card -->
<rect fill="url(#card-bg)" stroke="#0891b2" stroke-width="3"/>
```

**Use gradients for:**
- Card/container backgrounds (vertical, subtle)
- Progress indicators
- Section dividers

**DON'T use gradients for:**
- Text (always solid color)
- Small icons (< 80px)
- Borders/strokes

### Shadow & Depth System

Create visual hierarchy through layering:

**Shadow Levels (Recommended for Presentations)**

```xml
<!-- Use THIS shadow consistently across ALL assets -->
<filter id="shadow-sm">
  <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
</filter>
```

**Usage Guidelines**

- **Background layer**: No shadow
- **Card/Container layer**: shadow-sm (ALWAYS use same filter ID)
- **Icon/Badge layer**: Optional shadow-sm if floating
- **Floating elements**: shadow-sm (keep consistent)
- **Avoid**: Multiple shadow levels in same presentation (causes inconsistency)

**⚠️ Consistency Rule:**
Define shadow filter ONCE per presentation, reuse the exact same `<filter>` definition in all SVG files.

**Practical Implementation:**

```xml
<!-- In SVG #1: icon.svg -->
<defs>
  <filter id="shadow-sm">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
  </filter>
</defs>

<!-- In SVG #2: diagram.svg -->
<defs>
  <filter id="shadow-sm">
    <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
  </filter>
</defs>

<!-- SAME definition = visual consistency -->
```

**Alternative to shadows (Marp-safe)**

If filters are problematic, use stroke-based depth:

```xml
<!-- Outer glow effect with layered strokes -->
<rect stroke="#1e40af" stroke-width="4" stroke-opacity="0.3" />
<rect stroke="#1e40af" stroke-width="2" stroke-opacity="0.6" />
<rect stroke="#1e40af" stroke-width="1" stroke-opacity="1" />
```

### Gradient Guidelines

Use gradients sparingly for modern, polished look:

**Linear Gradients (Subtle)**

```xml
<defs>
  <linearGradient id="bg-gradient" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" style="stop-color:#f8fafc;stop-opacity:1" />
    <stop offset="100%" style="stop-color:#e0f2fe;stop-opacity:1" />
  </linearGradient>
</defs>
```

**When to use:**
- Card backgrounds (very subtle, 5-10% lightness change)
- Progress indicators (showing direction)
- Accent highlights (small elements only)

**When NOT to use:**
- Text (always solid color)
- Icons (keep simple)
- Small elements < 100px (won't be visible)

### Spacing & Grid System

**8px Grid Base**

All spacing, sizing, and positioning should align to 8px grid:

```
Spacing Scale:
  - xs: 8px   (tight spacing)
  - sm: 16px  (compact elements)
  - md: 24px  (default spacing)
  - lg: 32px  (section separation)
  - xl: 48px  (major sections)
  - 2xl: 64px (slide regions)
```

**Border Radius Scale**

```
Rounding:
  - sm: 4px   (buttons, badges)
  - md: 8px   (cards, small containers)
  - lg: 12px  (large cards, containers)
  - xl: 16px  (prominent containers)
  - full: 50% (circles, pills)
```

**Stroke Width Scale**

```
Strokes:
  - Hairline: 1px (subtle dividers)
  - Regular: 2px  (standard borders)
  - Medium: 3px   (emphasis borders)
  - Bold: 4px     (primary borders, icons)
  - Heavy: 6px    (call-to-action)
```

### Visual Hierarchy Principles

**Create clear information hierarchy:**

1. **Focal Point** (largest, highest contrast)
   - Main title or key metric
   - Size: 48-72px text or 120-200px icons
   - Color: Primary or accent

2. **Secondary Elements** (medium size, medium contrast)
   - Subtitles, supporting text
   - Size: 24-36px text or 60-100px icons
   - Color: Secondary or neutral dark

3. **Tertiary Elements** (smaller, lower contrast)
   - Labels, captions, metadata
   - Size: 16-20px text or 40-60px icons
   - Color: Neutral mid

4. **Background Elements** (largest, lowest contrast)
   - Decorative shapes, patterns
   - Color: Neutral light or tints

**Contrast Rules**

- Adjacent elements should differ by at least 2:1 in size OR color
- Don't use size + color + position all at once (pick 2)
- High contrast for important info, low contrast for supporting info

### Icon & Illustration Style

**Consistent Visual Language**

Choose ONE style and stick to it:

**Option A: Outline Style** (Recommended for technical content)
- 3-4px strokes
- Rounded caps and joins
- Minimal fills
- Clean, technical feel

**Option B: Filled Style** (Better for quick recognition)
- Solid fills with subtle borders (1-2px)
- More visual weight
- Friendly, approachable

**Icon Design Rules**

1. **Optical sizing**: Adjust visual weight, not just mathematical size
   - Circles appear smaller than squares of same dimensions
   - Thin elements need to be thicker for visibility

2. **Consistent metaphors**: Use established visual language
   - Code quality → magnifying glass, checkmark, shield
   - Skills/Tools → wrench, gear, toolkit
   - Flow/Process → arrows, connected nodes
   - Marketplace → shopping bag, grid, network

3. **Detail level matches scale**:
   - Small icons (< 60px): 3-5 key shapes max
   - Medium icons (60-120px): 5-8 shapes
   - Large illustrations (> 120px): Add detail as needed

4. **Alignment and balance**:
   - Optically center icons (not mathematically)
   - Balance visual weight across icon set

### Typography Integration

**When using text in SVG:**

**Font Stack (System-safe)**

```xml
font-family="ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"
```

**Text Hierarchy**

```xml
<!-- Title / Hero -->
<text font-size="48" font-weight="700" fill="#1e293b">

<!-- Heading -->
<text font-size="36" font-weight="600" fill="#1e293b">

<!-- Body -->
<text font-size="24" font-weight="400" fill="#475569">

<!-- Caption / Label -->
<text font-size="18" font-weight="400" fill="#64748b">
```

**Text Rendering**

- Always set `text-anchor="middle"` or `text-anchor="start"` explicitly
- Use `dominant-baseline="middle"` for vertical centering
- Avoid small text (< 16px) - won't be legible on slides
- Prefer concise labels over long sentences

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
- [pattern-examples.md](references/pattern-examples.md) — Complete SVG templates for common diagrams
- [color-palettes.md](references/color-palettes.md) — Curated color schemes for different contexts
- Icon design guidelines
- Troubleshooting embedding issues

**Related Skills:**
- [marpit-markdown/SKILL.md](../marpit-markdown/SKILL.md) — Authoring and structuring Marpit slides
- [slide-color-design/SKILL.md](../slide-color-design/SKILL.md) — Designing accessible, consistent color palettes for slides
