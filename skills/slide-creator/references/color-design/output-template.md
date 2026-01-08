# Color Design Output Template

## Table of Contents

- [Output Structure (Strict)](#output-structure-strict)
- [Color Strategy](#color-strategy)
- [Color Palette](#color-palette)
- [Usage Guidelines](#usage-guidelines)
- [Notes & Constraints](#notes-constraints)
- [Validation Checklist](#validation-checklist)
- [Complete Example 1: Dark Technical](#complete-example-1-dark-technical)
- [Color Strategy](#color-strategy)
- [Color Palette](#color-palette)
- [Usage Guidelines](#usage-guidelines)
- [Notes & Constraints](#notes-constraints)
- [Validation Checklist](#validation-checklist)
- [Complete Example 2: Light Professional](#complete-example-2-light-professional)
- [Color Strategy](#color-strategy)
- [Color Palette](#color-palette)
- [Usage Guidelines](#usage-guidelines)
- [Notes & Constraints](#notes-constraints)
- [Validation Checklist](#validation-checklist)
- [Complete Example 3: Accent-Driven](#complete-example-3-accent-driven)
- [Color Strategy](#color-strategy)
- [Color Palette](#color-palette)
- [Usage Guidelines](#usage-guidelines)
- [Notes & Constraints](#notes-constraints)
- [Validation Checklist](#validation-checklist)
- [Key Elements of Good Output](#key-elements-of-good-output)
  - [1. Strategy Justification](#1-strategy-justification)
  - [2. Color Rationales](#2-color-rationales)
  - [3. Specific Usage](#3-specific-usage)
  - [4. Constraints Documentation](#4-constraints-documentation)
  - [5. Checked Validation](#5-checked-validation)
- [Anti-Patterns (Avoid These)](#anti-patterns-avoid-these)
  - [❌ Vague Strategy](#-vague-strategy)
- [Color Strategy](#color-strategy)
- [Color Strategy](#color-strategy)
  - [❌ Colors Without Purpose](#-colors-without-purpose)
- [Color Palette](#color-palette)
- [Color Palette](#color-palette)
  - [❌ Generic Usage](#-generic-usage)
- [Usage Guidelines](#usage-guidelines)
- [Usage Guidelines](#usage-guidelines)
- [See Also](#see-also)

This file shows the expected output format when designing slide color palettes.

---

## Output Structure (Strict)

Always use this exact structure:

```
## Color Strategy

[Chosen strategy name] — [Brief reasoning for why this strategy fits the context]

## Color Palette

* Background: #XXXXXX — [1-line purpose/rationale]
* Surface: #XXXXXX — [1-line purpose/rationale]
* Primary: #XXXXXX — [1-line purpose/rationale]
* Secondary: #XXXXXX — [1-line purpose/rationale]
* Accent: #XXXXXX — [1-line purpose/rationale]
* Text Primary: #XXXXXX — [1-line purpose/rationale]
* Text Secondary: #XXXXXX — [1-line purpose/rationale]
* Semantic (optional): Success #XXXXXX, Warning #XXXXXX, Error #XXXXXX

## Usage Guidelines

* **Titles:** [How to use colors for titles]
* **Body text:** [How to use colors for body text]
* **Code blocks:** [How to use colors for code]
* **Diagrams:** [How to use colors for diagrams]
* **Charts (if any):** [How to use colors for charts]

## Notes & Constraints

* [Accessibility considerations - contrast ratios]
* [Projector / recording notes - visibility]
* [Any special considerations]

## Validation Checklist

- [x] Text contrast ratio ≥ 4.5:1 for body text (≥ 7:1 for AAA)
- [x] Accent color stands out clearly from primary
- [x] Palette limited to 5-7 colors maximum
- [x] Colors work on projector (avoid pure black #000000 / pure white #FFFFFF)
- [x] Consistent color usage across all slide types
```

---

## Complete Example 1: Dark Technical

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

## Complete Example 2: Light Professional

**User request:** "Design colors for a business quarterly review presentation"

**Response:**

## Color Strategy

Light Professional — chosen for a formal business setting with mixed audience (executives + team members). Light background ensures readability in bright conference rooms and works well for printed handouts.

## Color Palette

* Background: `#FAFAFA` — Main slide background (off-white, reduces glare)
* Surface: `#FFFFFF` — Content panels and cards (pure white)
* Primary: `#2E75B6` — Titles and key metrics (corporate blue, authoritative)
* Secondary: `#5B9BD5` — Subheadings and secondary data (lighter blue for hierarchy)
* Accent: `#F39C12` — Growth indicators and positive highlights (orange for warmth)
* Text Primary: `#2C2C2C` — Body text (near-black for maximum readability)
* Text Secondary: `#666666` — Captions and footnotes (medium gray)

## Usage Guidelines

* **Titles:** Primary (#2E75B6) on Background, 700 weight
* **Body text:** Text Primary (#2C2C2C) on Background or Surface
* **Code blocks:** Not applicable (business presentation)
* **Diagrams:** Surface for cards, Primary for lines/borders, Accent for key data points
* **Charts:** Primary for main data series, Secondary for comparison, Accent for highlights

## Notes & Constraints

* Text Primary/Background contrast is 14.2:1 (exceeds AAA)
* All colors print well on standard office printers
* Accent color (orange) used only for positive metrics and emphasis (< 10% usage)
* Conservative palette appropriate for C-level audience

## Validation Checklist

- [x] Text contrast ratio ≥ 4.5:1 for body text (≥ 7:1 for AAA)
- [x] Accent color stands out clearly from primary
- [x] Palette limited to 5-7 colors maximum
- [x] Colors work on projector (avoid pure black #000000 / pure white #FFFFFF)
- [x] Consistent color usage across all slide types

---

## Complete Example 3: Accent-Driven

**User request:** "Create colors for a product launch keynote"

**Response:**

## Color Strategy

Accent-Driven — chosen for a high-impact product launch requiring strong visual focus. Minimal color palette with one vibrant accent draws attention to key messages. Storytelling approach emphasizes single ideas per slide.

## Color Palette

* Background: `#FFFFFF` — Pure white for maximum contrast and clarity
* Surface: `#F8F9FA` — Subtle gray for differentiation (minimal use)
* Primary: `#343A40` — Titles and headings (charcoal, professional)
* Secondary: `#6C757D` — Subheadings and supporting text (medium gray)
* Accent: `#20C997` — Product name, CTAs, key features (vibrant teal, high energy)
* Text Primary: `#212529` — Body text (near-black)
* Text Secondary: `#6C757D` — Captions (same as Secondary for simplicity)

## Usage Guidelines

* **Titles:** Primary (#343A40) on Background, except product name uses Accent
* **Body text:** Text Primary (#212529) on Background, ample line spacing
* **Code blocks:** Not applicable (product launch)
* **Diagrams:** Minimal—use only when necessary, Accent for product highlights
* **Charts:** Grayscale (Primary/Secondary) with Accent for product data only

## Notes & Constraints

* Accent color used sparingly—only for product name, CTAs, and critical stats (< 10%)
* High contrast (16.8:1 for text) ensures readability in large venues
* Minimal design philosophy: every element must serve a purpose
* Ample whitespace between elements

## Validation Checklist

- [x] Text contrast ratio ≥ 4.5:1 for body text (≥ 7:1 for AAA)
- [x] Accent color stands out clearly from primary
- [x] Palette limited to 5-7 colors maximum
- [x] Colors work on projector (avoid pure black #000000 / pure white #FFFFFF)
- [x] Consistent color usage across all slide types

---

## Key Elements of Good Output

### 1. Strategy Justification

Always explain **why** this strategy was chosen:
- ✅ "Dark Technical — chosen because code-heavy content..."
- ❌ "I chose Dark Technical"

### 2. Color Rationales

Every color needs a brief purpose:
- ✅ `#569CD6` — VS Code blue, familiar to developers
- ❌ `#569CD6` — blue color

### 3. Specific Usage

Don't be vague about application:
- ✅ "Titles: Primary (#569CD6) on Background, bold weight"
- ❌ "Use Primary for important things"

### 4. Constraints Documentation

Note accessibility and practical considerations:
- Contrast ratios (with actual numbers)
- Projector visibility
- Accent usage percentage
- Any special limitations

### 5. Checked Validation

Mark all checklist items as completed ([x]) to show validation was done.

---

## Anti-Patterns (Avoid These)

### ❌ Vague Strategy

```
## Color Strategy
I'm using a dark theme because it looks nice.
```

✅ **Better:**
```
## Color Strategy
Dark Technical — chosen because the presentation focuses on system
architecture diagrams with code snippets. The technical audience benefits
from reduced eye strain, and colored elements pop against dark backgrounds.
```

### ❌ Colors Without Purpose

```
## Color Palette
* Background: #1E1E1E
* Primary: #569CD6
* Accent: #F4BF75
```

✅ **Better:**
```
## Color Palette
* Background: #1E1E1E — Main slide background (dark gray, not pure black)
* Primary: #569CD6 — Titles and headings (VS Code blue, familiar to developers)
* Accent: #F4BF75 — Important callouts (amber, limited use)
```

### ❌ Generic Usage

```
## Usage Guidelines
* Use Primary for titles
* Use Text Primary for text
```

✅ **Better:**
```
## Usage Guidelines
* **Titles:** Primary (#569CD6) on Background, bold weight
* **Body text:** Text Primary (#D4D4D4) on Background or Surface, 400 weight
* **Code blocks:** Surface background (#2D2D2D) with syntax highlighting
```

---

## See Also

- [workflow.md](workflow.md) - Complete design process
- [strategies.md](strategies.md) - Strategy details
- [../color-palettes.md](../color-palettes.md) - Comprehensive color reference
