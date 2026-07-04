# Marp Authoring Best Practices

## Content

- One message per slide.
- Prefer 3-5 bullets; split dense slides.
- Use concrete nouns and verbs in headings.
- Keep code and tables readable at presentation size.

## Design

- Reuse one palette, one spacing unit, and one heading hierarchy.
- Prefer background image syntax for diagrams and photos.
- Use high contrast for projected decks.
- Keep diagrams, tables, and text aligned to a simple grid.

## HTML Policy

Use Markdown first. Use inline HTML only when Marp Markdown cannot express the layout and the target renderer is known to allow HTML.

## Accessibility

- Maintain text contrast of at least WCAG AA.
- Do not encode meaning by color alone.
- Avoid tiny captions and overcrowded diagrams.
- Avoid emoji when predictable rendering matters.

## Pre-Commit Check

Before handing off a deck:

```shell
bash skills/authoring-marp-slides/scripts/validate_marpit.sh deck.md
```

Then preview or export the deck and inspect at least title, densest content slide, and every slide with an SVG/background image.
