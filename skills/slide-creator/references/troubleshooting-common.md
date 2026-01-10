# Common Troubleshooting

## Table of Contents

- [Projector Color Shift](#projector-color-shift)
- [SVG Not Rendering in Marpit](#svg-not-rendering-in-marpit)
- [Text Contrast Fails in Export](#text-contrast-fails-in-export)
- [Font Rendering Issues](#font-rendering-issues)
- [Inconsistent Visual Style](#inconsistent-visual-style)
- [See Also](#see-also)

## Projector Color Shift

Symptom: Colors appear washed out or too bright on projector.

Cause: Projectors have lower contrast ratios than monitors.

Fix:
1. Increase contrast between text and background.
2. Use darker backgrounds for light rooms (#1E1E1E instead of #2D2D2D).
3. Test on the actual projector when possible.
4. Avoid pure white (#FFFFFF) and pure black (#000000).
5. Prefer high-contrast palettes from `references/color-palettes.md`.

## SVG Not Rendering in Marpit

Symptom: SVG shows as broken image or does not appear.

Fix:
1. Confirm relative paths:

```markdown
<!-- Wrong: absolute path -->
![width:800px](/Users/name/diagrams/flow.svg)

<!-- Correct: relative path -->
![width:800px](diagrams/flow.svg)
```

2. Ensure SVG root has xmlns:

```xml
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
```

3. Run SVG validation:

```bash
svglint diagrams/flow.svg
```

## Text Contrast Fails in Export

Symptom: Text is readable in preview but fails contrast in PDF/HTML export.

Fix:
1. Check contrast ratio:

```bash
uv run scripts/check_contrast.py '#D4D4D4' '#1E1E1E'
```

2. Aim for 7:1 (AAA) when possible.
3. Avoid transparent overlays on text.
4. Validate on exported PDF, not just preview.

## Font Rendering Issues

Symptom: Fonts look different across devices or exports.

Fix:
1. Use web-safe fonts: `sans-serif`, `Arial`, `Helvetica`.
2. Avoid system-only fonts that may not embed.
3. Use standard weights (400, 600, 700).
4. For SVG text, set `font-family` explicitly and avoid emoji.

## Inconsistent Visual Style

Symptom: Slides or diagrams feel inconsistent in spacing, colors, or borders.

Fix:
1. Choose one palette and apply it across slides and SVG.
2. Use one stroke width (e.g., 3px) for all diagram shapes.
3. Use one border radius value (e.g., 16px).
4. Apply the same shadow system consistently.

Checklist:
- [ ] Palette applied consistently
- [ ] Stroke width consistent
- [ ] Border radius consistent
- [ ] Shadows consistent
- [ ] Marpit directives consistent

## See Also

- [svg-illustration/troubleshooting.md](svg-illustration/troubleshooting.md) - SVG-specific issues
- [marpit-authoring/best-practices.md](marpit-authoring/best-practices.md) - Marpit consistency
- [color-design/workflow.md](color-design/workflow.md#validation-checklist) - Color validation
