# Color Design Output Examples

Complete examples of expected outputs for slide color design.

Format structure: see `color-design/output-template.md`.

## Example 1: Dark Technical Palette

```markdown
## Color Strategy

**Strategy**: Dark Technical
**Reasoning**: Code-heavy presentation for developer audience, projector environment, need high contrast for code readability

## Color Palette

* Background: #1E1E1E — Main slide background (VS Code dark)
* Surface: #252526 — Code blocks, diagram containers
* Primary: #569CD6 — Titles, headings (VS Code blue)
* Secondary: #4EC9B0 — Section dividers, icons (cyan)
* Accent: #F4BF75 — Important callouts, highlights (amber)
* Text Primary: #D4D4D4 — Body text, code
* Text Secondary: #858585 — Captions, metadata

## Usage Guidelines

**Title slides**:
- Background: #1E1E1E
- Title: Primary (#569CD6)
- Subtitle: Text Secondary (#858585)

**Content slides**:
- Background: #1E1E1E
- Headings: Primary (#569CD6)
- Body text: Text Primary (#D4D4D4)
- Code blocks: Surface background (#252526)

**Diagrams**:
- Container fills: Surface (#252526)
- Borders/strokes: Secondary (#4EC9B0)
- Highlights: Accent (#F4BF75)
- Arrows: Primary (#569CD6)

## Validation Checklist

- [x] Contrast ratio Text Primary/Background = 11.25:1 (exceeds WCAG AAA)
- [x] Contrast ratio Primary/Background = 5.65:1 (meets WCAG AA, close to AAA)
- [x] Palette limited to 7 colors
- [x] Colors tested on projector (high contrast maintained)
- [x] Consistent with VS Code theme (familiar to developers)
```

## Example 2: Light Professional Palette

```markdown
## Color Strategy

**Strategy**: Light Professional
**Reasoning**: Business presentation for mixed audience (technical + management), formal setting, printed handouts

## Color Palette

* Background: #FAFAFA — Main slide background (off-white, print-friendly)
* Surface: #FFFFFF — Panels, cards
* Primary: #2E75B6 — Titles, headings (corporate blue)
* Secondary: #5B9BD5 — Subheadings (lighter blue)
* Accent: #F39C12 — Highlights, callouts (orange)
* Text Primary: #2C2C2C — Body text (near-black)
* Text Secondary: #666666 — Captions

## Usage Guidelines

**Title slides**:
- Background: #FAFAFA
- Title: Primary (#2E75B6)
- Subtitle: Text Secondary (#666666)

**Content slides**:
- Background: #FAFAFA
- Headings: Primary (#2E75B6)
- Body text: Text Primary (#2C2C2C)
- Important items: Accent (#F39C12)

**Charts/Diagrams**:
- Main elements: Primary (#2E75B6)
- Secondary elements: Secondary (#5B9BD5)
- Highlights: Accent (#F39C12)
- Backgrounds: Surface (#FFFFFF)

## Validation Checklist

- [x] Contrast ratio Text Primary/Background = 14.2:1 (exceeds WCAG AAA)
- [x] Contrast ratio Primary/Background = 5.8:1 (meets WCAG AA)
- [x] Palette limited to 7 colors
- [x] Colors work for printing and projection
- [x] Professional, conservative appearance suitable for business
```

## See Also

- `index.md` - Reference navigation hub
- `color-design/output-template.md` - Color design output template
- `color-palettes.md` - Palette index
