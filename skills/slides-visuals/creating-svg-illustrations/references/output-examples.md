# SVG Illustration Output Examples

## Handoff Summary

```markdown
Created `examples/slides/assets/system-map.svg`.

Checks:
- viewBox matches content bounds: `0 0 1200 675`
- palette matches deck colors
- validated with `svglint examples/slides/assets/system-map.svg`
```

## Minimal SVG

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220" role="img" aria-labelledby="title">
  <title id="title">Two-step flow</title>
  <defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#475569"/></marker></defs>
  <rect width="400" height="220" rx="16" fill="#F8FAFC"/>
  <circle cx="110" cy="110" r="48" fill="#DBEAFE" stroke="#2563EB" stroke-width="3"/>
  <circle cx="290" cy="110" r="48" fill="#DCFCE7" stroke="#16A34A" stroke-width="3"/>
  <path d="M160 110 H240" stroke="#475569" stroke-width="3" marker-end="url(#arrow)"/>
</svg>
```

Use `references/core-rules.md` for required root attributes and validation.
