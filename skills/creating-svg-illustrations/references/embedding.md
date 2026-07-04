# Embedding SVG in Marp/Marpit

## Preferred: Background Image Syntax

```markdown
![bg fit](assets/diagram.svg)
![bg right:45% fit](assets/architecture.svg)
![bg left:40% fit](assets/process.svg)
```

Use this for full-slide or split-layout diagrams. It keeps sizing in Marp instead of hard-coding it in SVG.

## Inline Image

Use only for small logos or icons.

```markdown
![w:320](assets/logo.svg)
```

## Path Rules

- Paths are relative to the slide Markdown file.
- Do not use absolute local paths.
- Keep SVG assets near the deck, for example `examples/slides/assets/system-map.svg`.

## Sizing Rules

- Let `viewBox` define the SVG's internal bounds.
- Let Marp control displayed size with `bg`, `fit`, `cover`, or `w:`.
- If content appears tiny, shrink the SVG `viewBox` to the actual content.

## Production Option

Inline base64 only when the deck must be a single self-contained Markdown file. Otherwise keep SVG as a normal file.
