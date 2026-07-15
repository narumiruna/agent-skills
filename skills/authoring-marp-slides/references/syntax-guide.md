# Marp/Marpit Syntax Guide

Use this as the minimum syntax checklist before writing slides.

## Required Structure

```markdown
---
marp: true
theme: default
paginate: true
---

# Title

---

## Slide title

Body text.
```

Rules:

- Start with YAML frontmatter and `marp: true`.
- Separate slides with `---` on its own line.
- Use one `#` title per slide; use `##` and lists for body structure.
- Keep speaker notes in HTML comments only if the renderer supports them.

## Directives

Global directives live in frontmatter. Per-slide directives use HTML comments before the slide content.

```markdown
<!-- _class: lead invert -->
<!-- _backgroundColor: #111827 -->
<!-- _color: #F9FAFB -->
```

Common directives: `theme`, `paginate`, `size`, `class`, `backgroundColor`, `color`, `header`, `footer`.

## Images

Prefer background image syntax; it avoids manual resizing.

```markdown
![bg fit](assets/diagram.svg)
![bg right:45% fit](assets/architecture.svg)
![bg left:40% fit](assets/photo.jpg)
```

Use regular image sizing only for small inline images:

```markdown
![w:600](assets/logo.svg)
```

## Code

````markdown
```python
def hello() -> str:
    return "world"
```
````

Rules:

- Add a language for highlighting.
- Keep code blocks short enough to read on a slide.
- Move long examples to a repo file and show the relevant excerpt.

## Tables

Use Markdown tables only for small comparisons. For dense data, simplify or use a chart/SVG.

## Validation

Resolve `scripts/validate_marpit.sh` against the `authoring-marp-slides` skill directory, then run the local syntax check by absolute path:

```shell
AUTHORING_MARP_SLIDES_SKILL_DIR="/absolute/path/to/authoring-marp-slides"
bash "$AUTHORING_MARP_SLIDES_SKILL_DIR/scripts/validate_marpit.sh" deck.md
```
