# Marp Preview Workflow

Use this when visual inspection is required.

## Preconditions

- `marp` CLI is installed.
- The deck and assets use repository-relative paths.

## Preview

```bash
marp -s examples/slides
```

Open the printed URL, usually:

```text
http://localhost:8080/<deck>.md
```

Jump to a slide with `#N`, for example `deck.md#5`.

## Export Check

```bash
marp examples/slides/deck.md -o /tmp/deck.html
```

Inspect the title slide, the densest slide, and every slide that uses images or SVGs.

## Common Fixes

- Broken image: use a relative path from the deck file.
- Cropped SVG: check the SVG `viewBox` and use `![bg fit]`.
- Low contrast: adjust the palette or image background, then re-export.
