---
name: slide-color-design
description: Design consistent, presentation-ready color systems for slides. Use when creating or improving slide color palettes, choosing presentation colors, designing slide themes, selecting background/text/accent colors, or establishing visual hierarchy for technical presentations, Marp/Marpit slides, PowerPoint, Keynote, architecture diagrams, or developer-focused decks. Provides guidance on color strategy, contrast, accessibility, and semantic color usage.
---

# Slide Color Design

Design clear, consistent, and presentation-safe color systems for slides.
This skill focuses on **decision-making and system design**, not illustration or UI component styling.

## Core Goal

Produce a **slide-ready color system** that:
- Works on projectors and recordings
- Supports technical content (code, diagrams, charts)
- Maintains visual hierarchy and readability
- Can be directly applied to Marp, CSS, PowerPoint, or Keynote

---

## Workflow

Always follow this sequence.

### Step 1 — Identify Context

Determine:
- **Audience**: engineers, managers, mixed
- **Tone**: technical / neutral / persuasive
- **Usage density**: text-heavy, diagram-heavy, code-heavy
- **Environment**: projector, screen share, dark room, light room

If information is missing, make **explicit assumptions** and state them.

---

### Step 2 — Choose Color Strategy

Select ONE primary strategy based on context.

**Decision guide:**
- Code/diagrams dominant + technical audience → **Dark Technical**
- Documentation-style + formal setting → **Light Professional**
- Storytelling + emphasis needed → **Accent-Driven**

**Strategies:**

- **Dark Technical**
  - Dark background (#1E1E1E - #2D2D2D), muted accents
  - Best for: Code blocks, terminal output, system diagrams
  - Avoid if: Printing required, bright room, non-technical audience

- **Light Professional**
  - Light background (#FAFAFA - #FFFFFF), restrained colors
  - Best for: Documentation-style slides, business presentations, formal settings
  - Avoid if: Dark room, code-heavy content, casual audience

- **Accent-Driven**
  - Neutral base (white/light gray) with strong highlight color
  - Best for: Emphasis and storytelling, keynotes, single-message slides
  - Avoid if: Complex data, many competing elements

Explain why this strategy fits the context.

---

### Step 3 — Define Color Roles (Mandatory)

Always define these roles:

| Role | Purpose |
|-----|--------|
| Background | Main slide background |
| Surface | Cards, panels, diagrams |
| Primary | Titles, key highlights |
| Secondary | Supporting emphasis |
| Accent | Callouts, focus points |
| Text Primary | Main text |
| Text Secondary | Metadata, captions |
| Semantic (optional) | Success / Warning / Error |

---

### Step 4 — Specify Colors

For each role, provide:
- HEX value
- Short rationale (1 line max)
- Contrast consideration (light/dark)

Avoid overly saturated colors unless explicitly requested.

---

### Step 5 — Slide Usage Guidance

Explain how to apply the colors to:
- Title slides
- Content slides
- Code blocks
- Diagrams / flow arrows
- Charts (if applicable)

Focus on **consistency**, not decoration.

---

## Output Format (Strict)

Always output using this structure:

```
## Color Strategy

[Chosen strategy + reasoning]

## Color Palette

* Background: #XXXXXX — [1-line purpose]
* Surface: #XXXXXX — [1-line purpose]
* Primary: #XXXXXX — [1-line purpose]
* Secondary: #XXXXXX — [1-line purpose]
* Accent: #XXXXXX — [1-line purpose]
* Text Primary: #XXXXXX — [1-line purpose]
* Text Secondary: #XXXXXX — [1-line purpose]
* Semantic (optional): ...

## Usage Guidelines

* Titles: [How to use colors for titles]
* Body text: [How to use colors for body text]
* Code blocks: [How to use colors for code]
* Diagrams: [How to use colors for diagrams]
* Charts (if any): [How to use colors for charts]

## Notes & Constraints

* Accessibility considerations
* Projector / recording notes

## Validation Checklist

- [ ] Text contrast ratio ≥ 4.5:1 for body text (≥ 7:1 for AAA)
- [ ] Accent color stands out clearly from primary
- [ ] Palette limited to 5-7 colors maximum
- [ ] Colors work on projector (avoid pure black #000000 / pure white #FFFFFF)
- [ ] Consistent color usage across all slide types
```

Do NOT include images unless explicitly requested.

---

## Example Output

**User request:** "Create a color palette for a technical architecture presentation"

**Response:**

## Color Strategy

Dark Technical — chosen because the presentation focuses on system architecture diagrams with code snippets. The technical audience and diagram-heavy content benefit from a dark background that reduces eye strain and makes colored elements pop.

## Color Palette

* Background: `#1E1E1E` — Main slide background (dark gray, not pure black)
* Surface: `#2D2D2D` — Diagram boxes and code blocks (slightly lighter than background)
* Primary: `#569CD6` — Titles and main headings (VS Code blue, familiar to developers)
* Secondary: `#4EC9B0` — Section dividers and icons (cyan accent for visual hierarchy)
* Accent: `#F4BF75` — Important callouts and highlights (amber, limited use)
* Text Primary: `#D4D4D4` — Body text (light gray for readability on dark)
* Text Secondary: `#858585` — Captions and metadata (muted gray, less prominent)

## Usage Guidelines

* **Titles:** Primary (#569CD6) on Background, bold weight
* **Body text:** Text Primary (#D4D4D4) on Background or Surface
* **Code blocks:** Surface background with syntax highlighting using Primary/Secondary/Accent
* **Diagrams:** Surface for boxes, Primary for connectors/arrows, Accent for highlights/warnings
* **Charts:** Primary and Secondary as main colors, Accent for emphasis points

## Notes & Constraints

* All text contrasts exceed 7:1 for WCAG AAA accessibility
* Tested on projector—colors remain distinct even in bright rooms
* Amber accent used sparingly (max 5-10% of visual space) to maintain focus
* Avoid pure white text to reduce eye strain in dark rooms

## Validation Checklist

- [x] Text contrast ratio ≥ 4.5:1 for body text (≥ 7:1 for AAA)
- [x] Accent color stands out clearly from primary
- [x] Palette limited to 5-7 colors maximum
- [x] Colors work on projector (avoid pure black #000000 / pure white #FFFFFF)
- [x] Consistent color usage across all slide types

---

## Design Principles

Follow these core principles when designing color systems for slides:

### Visual Coherence
- **Visually similar elements must share a coherent visual language**
  - Use the same color family across related components
  - Apply consistent fill logic (solid vs outlined)
  - Follow uniform emphasis rules throughout

### Hue Consistency
- **Do not differentiate similar components by changing hue**
  - Use brightness, saturation, or weight to express state differences
  - Keep the same base hue for related elements
  - Vary lightness/darkness instead of changing colors entirely

### Semantic States
- **Define clear semantic states and represent them consistently**
  - Examples: active, inactive, completed, optional, in-progress
  - Each state should have a distinct visual treatment
  - Apply the same state representation across all components

### Solid Over Outlined
- **Prefer solid-filled surfaces over outlines or transparency**
  - Use filled shapes as the default
  - Reserve outlines only when they convey clear meaning
  - Avoid semi-transparent overlays unless necessary

### Visual Hierarchy
- **Establish a clear visual hierarchy**
  - Primary focus elements must stand out clearly
  - Secondary and tertiary elements should visually recede
  - Use size, weight, and saturation to create hierarchy
  - Not all elements deserve equal visual weight

### Single Focus Point
- **Ensure there is a single primary visual anchor per section**
  - Guide user attention deliberately
  - Reduce scanning ambiguity
  - One main focal point per slide or section

### Minimize Visual Noise
- **Avoid visual noise caused by excessive decoration**
  - Limit unnecessary borders and strokes
  - Don't overuse icons or graphics
  - Avoid multiple competing emphasis cues
  - Every visual element should serve a purpose

---

## Design Constraints

- Prioritize readability over aesthetics
- Avoid pure white (#FFFFFF) and pure black (#000000) unless justified
- Ensure sufficient contrast for projectors
- Assume slides are read at a distance

---

## What This Skill Does NOT Do

- Does not design UI components
- Does not generate illustrations or icons
- Does not enforce brand guidelines unless provided

If brand colors exist, adapt them into the system rather than replacing them.

---

## References

- [marpit-markdown/SKILL.md](../marpit-markdown/SKILL.md) — Authoring and structuring Marpit slides
- [slide-svg-illustrator/SKILL.md](../slide-svg-illustrator/SKILL.md) — Creating and embedding SVG diagrams/icons
- [references/color-palettes.md](references/color-palettes.md) — Ready-to-use color palettes for different contexts
