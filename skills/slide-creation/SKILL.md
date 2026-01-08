---
name: slide-creation
description: Complete Marp/Marpit presentation creation combining color design, Markdown slide authoring, and SVG diagrams. Use when (1) creating presentations or slides, (2) designing slide color schemes/themes/palettes, (3) drawing diagrams (flowcharts, architecture, timelines), (4) writing Marpit Markdown, or any combination of these tasks.
---

# Slide Creation Toolkit

Complete solution for creating professional Marp/Marpit presentations, from color design to final slides with diagrams.

## Overview

This skill combines three modules for end-to-end slide creation:

1. **Color Design** - Design consistent color systems and palettes
2. **Marpit Authoring** - Write valid Marpit Markdown slides
3. **SVG Illustration** - Create diagrams and illustrations

Each module can be used independently or together for complete presentations.

---

## Unified Design Principles

**CRITICAL: All outputs (Markdown slides, SVG diagrams, color palettes) must follow consistent design principles.**

### Visual Consistency: The Golden Rule

Establish a design system before starting and apply it uniformly:

1. **Color Palette** - Choose ONE palette for all slides, SVGs, and elements
2. **Spacing System** - Use ONE gap size (e.g., 48px) and ONE margin (e.g., 32px) throughout
3. **Visual Hierarchy** - Size, weight, and saturation create hierarchy—not all elements deserve equal emphasis
4. **Coherent Visual Language** - Differentiate by brightness/saturation, not hue; consistent fill logic (solid vs outlined)
5. **Minimize Visual Noise** - Every element serves a purpose; prefer solid fills; one primary anchor per section

---

## Module Quick Reference

### Module 1: Color Design

**Purpose**: Design slide color systems (background, text, accents, semantic colors)

**Output**: Color palette specification with hex codes and usage guidelines

**Key references**:
- `references/color-design/workflow.md` - Step-by-step color design process
- `references/color-palettes.md` - Ready-to-use color palettes
- `references/color-design/strategies.md` - Dark Technical / Light Professional / Accent-Driven

---

### Module 2: Marpit Authoring

**Purpose**: Write valid Marpit/Marp Markdown slides

**Output**: Valid Marpit-compatible Markdown (.md file)

**Core rule**: ALWAYS output valid Marpit Markdown that can be directly rendered. Do NOT explain syntax unless asked.

**CRITICAL: Avoid HTML in Marpit slides**:
- Use pure Marpit directives and Markdown syntax only
- HTML requires manual enablement (security risk, breaks portability)
- Prefer: directives (`backgroundColor`, `backgroundImage`), tables, `![bg]()` syntax
- Only use HTML if absolutely no Marpit alternative exists

**Key references**:
- `references/marpit-authoring/syntax-guide.md` - Marpit syntax and directives
- `references/marpit-authoring/patterns.md` - Title, content, two-column, code slides
- `references/marpit-authoring/themes.md` - Default, Gaia, Uncover themes

---

### Module 3: SVG Illustration

**Purpose**: Create SVG diagrams and illustrations for slides

**Output**: SVG XML code optimized for Marp HTML export

**Core principle**: Create clean, editable SVGs that embed reliably in Marpit and look good in HTML exports.

**Key references**:
- `references/svg-illustration/core-rules.md` - SVG creation basics and sizing
- `references/svg-illustration/pattern-examples.md` - Flowcharts, timelines, architecture diagrams
- `references/svg-illustration/embedding.md` - How to embed in Marpit slides

---

## Workflow Guidance

### Single Task Workflows

#### Task: "Draw a diagram"

1. Read `references/svg-illustration/core-rules.md` for sizing and structure
2. If needs specific pattern: Read `references/svg-illustration/pattern-examples.md`
3. For colors: Reference `references/color-palettes.md` (use an existing palette)

#### Task: "Design slide colors"

1. Read `references/color-design/workflow.md` (5-step process)
2. Follow strategy selection (Dark Technical / Light Professional / Accent-Driven)
3. Reference `references/color-palettes.md` for examples

#### Task: "Write slides"

1. Read `references/marpit-authoring/syntax-guide.md` for Marpit basics
2. For specific layouts: Read `references/marpit-authoring/slide-patterns.md`
3. For colors: Use an established palette or reference `references/color-palettes.md`

---

### Complete Presentation Workflow

**When user requests a full presentation** (e.g., "Create a presentation about Kubernetes"):

**Recommended sequence**:

**Step 1: Establish Color Palette**
- Read `references/color-design/workflow.md`
- Determine context (audience, tone, usage density, environment)
- Choose strategy: Dark Technical / Light Professional / Accent-Driven
- Define colors: Background, Surface, Primary, Secondary, Accent, Text
- Document the palette for use in slides and diagrams

**Step 2: Structure Slides**
- Read `references/marpit-authoring/syntax-guide.md` and `references/marpit-authoring/patterns.md`
- Create slide outline using the established color palette
- Apply consistent theme and directives
- Use the colors defined in Step 1

**Step 3: Add Diagrams (as needed)**
- Read `references/svg-illustration/core-rules.md`
- Create SVG diagrams using colors from Step 1 palette
- Match spacing and styling with slides
- Embed using patterns from `references/svg-illustration/embedding.md`

**Critical**: Always maintain consistency by:
- Using the same color palette across all modules
- Following the same spacing system
- Applying uniform visual hierarchy
- Keeping design language coherent

---

## Decision Trees

### "Which module do I need?"

```
User mentions "slides", "presentation", "deck"
  ├─ Also mentions "colors", "theme", "palette"
  │   └─> Start with Color Design module
  │
  ├─ Also mentions "diagram", "illustration", "flowchart"
  │   └─> Use Marpit + SVG modules
  │
  └─ Just slide content
      └─> Use Marpit Authoring module
```

### "How detailed should I go?"

```
Simple request (e.g., "basic flowchart")
  └─> Read only core-rules.md (minimal references)

Complex request (e.g., "complete architecture presentation")
  └─> Read workflow + patterns + examples (full references)

User says "follow best practices"
  └─> Read all relevant best-practices files
```

---

## Output Formats by Module

### Color Design Output

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
- [ ] Contrast ratio ≥ 4.5:1
- [ ] Palette limited to 5-7 colors
- [ ] Colors work on projector
```

### Marpit Authoring Output

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

(Must be valid Marpit Markdown)

### SVG Illustration Output

```xml
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <!-- SVG content -->
</svg>
```

**Validation Required:**
After creating SVG, ALWAYS validate with svglint:
```bash
svglint path/to/file.svg
```

Fix any errors before using in slides (especially XML character escaping).

(Optimized for Marpit embedding)

---

## Cross-Module Integration

### Colors in SVG

When creating SVG after establishing a color palette:
- Use `fill="#XXXXXX"` with hex codes from the palette
- Match stroke widths to the design system
- Apply consistent border radius

### SVG in Marpit

When embedding SVG in slides:
```markdown
![width:600px](data:image/svg+xml;base64,...)
```
Or save as separate file and reference.

### Consistent Styling

- Same border radius in both CSS (Marpit) and SVG `rx` attribute
- Same color values in both contexts
- Same spacing principles (gaps, margins, padding)

---

## Common Patterns

### Pattern 1: Technical Presentation

1. Color Design: Choose "Dark Technical" palette
2. Marpit: Use code-heavy slide patterns
3. SVG: Create system architecture diagrams with same colors

### Pattern 2: Business Presentation

1. Color Design: Choose "Light Professional" palette
2. Marpit: Use clean, minimal slide patterns
3. SVG: Create simple flowcharts with same colors

### Pattern 3: Quick Diagram Only

1. Skip color design (use default palette from `references/color-palettes.md`)
2. Skip Marpit (no slides needed)
3. SVG: Create diagram with selected palette

---

## References Structure

```
references/
├── color-palettes.md        - Comprehensive color reference (complete systems + SVG quick reference)
│
├── color-design/
│   ├── workflow.md          - 5-step color design process
│   ├── strategies.md        - Three strategy types explained
│   └── output-template.md   - Complete output example
│
├── marpit-authoring/
│   ├── syntax-guide.md      - Marpit/Marp syntax fundamentals
│   ├── patterns.md          - Title, content, two-column, code patterns
│   ├── themes.md            - Default, Gaia, Uncover theme usage
│   └── best-practices.md    - Consistency checklist and tips
│
└── svg-illustration/
    ├── core-rules.md        - SVG basics, sizing, embedding
    ├── pattern-examples.md  - Flowcharts, timelines, architecture
    └── troubleshooting.md   - Common SVG issues and fixes
```

**Load references progressively**: Start with core files, add detailed files only when needed.

---

## Key Constraints

1. **Marpit Output**: Must be valid, directly renderable Markdown
2. **Color Palettes**: Limited to 5-7 colors maximum
3. **SVG Sizing**: Smart sizing based on slide context (see core-rules.md)
4. **Consistency**: Same design system across all outputs
5. **Contrast**: Text contrast ratio ≥ 4.5:1 (≥ 7:1 for AAA)

---

## What This Skill Does NOT Do

- Does not create PowerPoint/Keynote files (only Marpit Markdown)
- Does not generate raster images (PNG/JPG) - only SVG
- Does not enforce specific brand guidelines unless provided
- Does not create interactive animations (static slides only)

If brand colors exist, adapt them into the system rather than replacing them.
