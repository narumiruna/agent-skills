# Color Design Workflow

## Table of Contents

- [Core Goal](#core-goal)
- [5-Step Workflow](#5-step-workflow)
  - [Step 1 — Identify Context](#step-1-identify-context)
  - [Step 2 — Choose Color Strategy](#step-2-choose-color-strategy)
  - [Step 3 — Define Color Roles (Mandatory)](#step-3-define-color-roles-mandatory)
  - [Step 4 — Specify Colors](#step-4-specify-colors)
  - [Step 5 — Slide Usage Guidance](#step-5-slide-usage-guidance)
- [Design Constraints](#design-constraints)
- [Validation Checklist](#validation-checklist)
- [What This Does NOT Do](#what-this-does-not-do)
- [See Also](#see-also)

Design clear, consistent, and presentation-safe color systems for slides.

## Core Goal

Produce a **slide-ready color system** that:
- Works on projectors and recordings
- Supports technical content (code, diagrams, charts)
- Maintains visual hierarchy and readability
- Can be directly applied to Marp, CSS, PowerPoint, or Keynote

---

## 5-Step Workflow

Always follow this sequence when designing slide colors.

### Step 1 — Identify Context

Determine:
- **Audience**: engineers, managers, mixed
- **Tone**: technical / neutral / persuasive
- **Usage density**: text-heavy, diagram-heavy, code-heavy
- **Environment**: projector, screen share, dark room, light room

If information is missing, make **explicit assumptions** and state them.

**Example assumptions**:
- "Assuming technical audience since the topic is Kubernetes architecture"
- "Assuming projector environment for conference presentation"
- "Assuming diagram-heavy content for system design review"

---

### Step 2 — Choose Color Strategy

Select ONE primary strategy based on context.

**Decision guide:**
- Code/diagrams dominant + technical audience → **Dark Technical**
- Documentation-style + formal setting → **Light Professional**
- Storytelling + emphasis needed → **Accent-Driven**

See [strategies.md](strategies.md) for detailed descriptions of each strategy.

**Quick reference**:

| Strategy | Background | Best For | Avoid If |
|----------|-----------|----------|----------|
| Dark Technical | #1E1E1E - #2D2D2D | Code, terminals, diagrams | Printing, bright room |
| Light Professional | #FAFAFA - #FFFFFF | Business, docs, formal | Dark room, code-heavy |
| Accent-Driven | White/light gray | Storytelling, keynotes | Complex data |

Explain why this strategy fits the context in your output.

---

### Step 3 — Define Color Roles (Mandatory)

Always define these roles:

| Role | Purpose | Typical Usage |
|------|---------|---------------|
| **Background** | Main slide background | Full slide fill |
| **Surface** | Cards, panels, diagrams | Content containers |
| **Primary** | Titles, key highlights | H1, H2 headings |
| **Secondary** | Supporting emphasis | H3, icons, dividers |
| **Accent** | Callouts, focus points | Important keywords, highlights |
| **Text Primary** | Main text | Body paragraphs, lists |
| **Text Secondary** | Metadata, captions | Small text, timestamps |
| **Semantic (optional)** | Success / Warning / Error | Status indicators |

**Rules**:
- All 7 roles (excluding Semantic) are mandatory
- Each role must have exactly one hex color
- Colors must be distinct enough to serve their purposes
- Total palette: 5-7 colors (excluding semantic)

---

### Step 4 — Specify Colors

For each role, provide:
1. **HEX value** (e.g., `#1E1E1E`)
2. **Short rationale** (1 line max, e.g., "VS Code blue, familiar to developers")
3. **Contrast consideration** (light/dark, readability)

**Guidelines**:
- Avoid overly saturated colors unless explicitly requested
- Ensure text colors have sufficient contrast with backgrounds
- Use established palettes from [../color-palettes.md](../color-palettes.md) when appropriate
- Dark backgrounds: #1E1E1E to #2D2D2D (not pure black #000000)
- Light backgrounds: #FAFAFA to #FFFFFF (not pure white for readability)

**Contrast requirements**:
- Text Primary / Background: ≥ 4.5:1 (AA standard)
- For AAA accessibility: ≥ 7:1
- Use online contrast checkers if unsure

---

### Step 5 — Slide Usage Guidance

Explain how to apply the colors to:
- **Title slides**: Which colors for title, subtitle, background
- **Content slides**: Body text, headings, background
- **Code blocks**: Background color, text color, syntax highlighting hints
- **Diagrams / flow arrows**: Box fills, strokes, connectors
- **Charts** (if applicable): Primary data, secondary data, gridlines

**Focus on consistency, not decoration.**

**Creating Visual Hierarchy with Color Depth**

Use different background shades to establish slide hierarchy:

1. **Lead/Title slides (highest impact)** - Use the **darkest** background shade
   - Creates strong opening/transition moments
   - Demands attention and signals section changes
   - Example: `#0f1f2e` (darkest) for Dark Technical strategy

2. **Content slides (main body)** - Use **medium** background shade
   - Balances readability with visual interest
   - Easier on the eyes for prolonged viewing
   - Example: `#1e3a5f` (medium) for Dark Technical strategy

3. **Special emphasis slides** - Use **lightest** or accent backgrounds sparingly
   - Reserve for critical messages or calls-to-action
   - Example: `#2a5f8f` (lighter) for highlighted content

**Why this works:**
- Creates natural "rhythm" in presentation flow
- Deepest backgrounds signal "pause and listen"
- Medium backgrounds allow focus on content
- Consistent application reinforces structure

**Example application**:
```
* Lead slides: Background = Darkest shade (#0f1f2e)
* Content slides: Background = Medium shade (#1e3a5f)
* Titles: Primary (#569CD6) on respective backgrounds
* Body text: Text Primary (#D4D4D4) with high contrast
* Code blocks: Surface background with syntax highlighting
* Diagrams: Surface for boxes, Primary for arrows
```

---

## Design Constraints

- **Prioritize readability over aesthetics**
- Avoid pure white (#FFFFFF) and pure black (#000000) unless justified
- Ensure sufficient contrast for projectors (colors may wash out)
- Assume slides are read at a distance (3-5 meters)
- Keep palette limited to 5-7 colors maximum

---

## Validation Checklist

Before finalizing your color palette, verify:

- [ ] Text contrast ratio ≥ 4.5:1 for body text (≥ 7:1 for AAA)
- [ ] Accent color stands out clearly from primary
- [ ] Palette limited to 5-7 colors maximum
- [ ] Colors work on projector (avoid pure black/white)
- [ ] Consistent color usage across all slide types
- [ ] All 7 mandatory roles defined
- [ ] Each color has a clear purpose

---

## What This Does NOT Do

- Does not design UI components
- Does not generate illustrations or icons
- Does not enforce brand guidelines unless provided

If brand colors exist, adapt them into the system rather than replacing them.

---

## See Also

- [strategies.md](strategies.md) - Detailed strategy explanations
- [../color-palettes.md](../color-palettes.md) - Comprehensive color reference
- [output-template.md](output-template.md) - Complete output example
