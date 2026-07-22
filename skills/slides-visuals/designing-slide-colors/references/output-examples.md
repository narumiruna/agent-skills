# Color Design Output Examples

Use these as evidence patterns, not fixed templates. Recalculate every ratio if a value changes.

## Dark Technical Example

```markdown
## Color Strategy

Dark Technical — starting point for a code-heavy deck in a controlled-light room; projector behavior remains untested.

## Color Palette

- Background: `#1E1E1E` — slide field
- Surface: `#252526` — code and diagram containers
- Primary: `#569CD6` — headings and primary connectors
- Secondary: `#4EC9B0` — secondary diagram structure
- Accent: `#F4BF75` — limited callouts
- Text Primary: `#D4D4D4` — body text
- Text Secondary: `#858585` — metadata only where its pairing passes

## Usage

- Body: Text Primary on Background
- Code: Text Primary on Surface
- Diagrams: Surface fills, Primary connectors, Accent highlights

## Validation

- [x] Text Primary/Background: `11.25:1` (meets 7:1 AAA)
- [x] Primary/Background: `5.65:1` (meets 4.5:1 AA for normal text)
- [ ] Calculate Text Secondary on every assigned background
- [ ] Inspect the exported deck on the target projector
```

## Light Professional Example

```markdown
## Color Strategy

Light Professional — starting point for a formal mixed-content deck and handout; print and venue output remain untested.

## Color Palette

- Background: `#FAFAFA` — slide field
- Surface: `#FFFFFF` — panels
- Primary: `#2E75B6` — headings
- Secondary: `#5B9BD5` — supporting emphasis
- Accent: `#F39C12` — limited callouts
- Text Primary: `#2C2C2C` — body text
- Text Secondary: `#666666` — captions

## Usage

- Body: Text Primary on Background or Surface
- Headings: Primary on Background
- Visuals: Primary main series, Secondary comparison, Accent highlight

## Validation

- [x] Text Primary/Background: `13.38:1` (meets 7:1 AAA)
- [x] Primary/Background: `4.64:1` (meets 4.5:1 AA for normal text)
- [ ] Calculate remaining assigned pairings
- [ ] Inspect a representative print and exported deck in the target venue
```

See `color-design/output-template.md` for required handoff content.
