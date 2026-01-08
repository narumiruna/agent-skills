---
name: slide-color-design
description: Design consistent, presentation-ready color systems for slides. Use when creating or improving slide color palettes for technical presentations, Marp/Marpit slides, architecture diagrams, or developer-focused decks, including guidance on backgrounds, text, accents, and semantic color usage.
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

Select ONE primary strategy:

- **Dark Technical**
  - Dark background, muted accents
  - Best for code and diagrams

- **Light Professional**
  - Light background, restrained colors
  - Best for documentation-style slides

- **Accent-Driven**
  - Neutral base with strong highlight color
  - Best for emphasis and storytelling

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

* Background: #XXXXXX
* Surface: #XXXXXX
* Primary: #XXXXXX
* Secondary: #XXXXXX
* Accent: #XXXXXX
* Text Primary: #XXXXXX
* Text Secondary: #XXXXXX
* Semantic (optional): ...

## Usage Guidelines

* Titles:
* Body text:
* Code blocks:
* Diagrams:
* Charts (if any):

## Notes & Constraints

* Accessibility considerations
* Projector / recording notes
```

Do NOT include images unless explicitly requested.

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
