---
name: authoring-marp-slides
description: Write, revise, structure, or validate Marp/Marpit Markdown slides, including directives, layouts, themes, templates, and rendered-deck checks. Use for slide authoring when palette or illustration design is not the primary task.
---

# Marp Authoring

Load only the authoring detail the deck needs.

| Need | Read or use |
| --- | --- |
| Directives and syntax | `references/syntax-guide.md` |
| Common layouts | `references/patterns.md` |
| Complex layouts | `references/advanced-layouts.md` |
| Theme behavior | `references/themes.md` |
| Content and QA guidance | `references/best-practices.md` |
| Source validation | `scripts/validate_marpit.sh <deck.md>` |
| Render and visual checks | `references/preview-workflow.md` |
| Starting point | `assets/templates/` |
| Known-good patterns | `assets/examples/` |

## Workflow

1. Inspect the request, existing deck, theme, assets, output target, and repository conventions.
2. Start from the nearest template or preserve the current structure. Define valid Marp frontmatter and repository-relative asset paths.
3. Author a clear slide sequence with consistent hierarchy and layouts. Use `bg` syntax for full-slide or split-layout visuals; keep logos, icons, and other small visuals inline.
4. Load color or SVG guidance only when the task requires new palette or illustration work.
5. Resolve this skill directory and validate exactly one deck with `bash "$SKILL_DIR/scripts/validate_marpit.sh" path/to/deck.md`. Then follow `references/preview-workflow.md` when rendering is available and inspect the title, densest slide, and every image/SVG slide.
6. Return the deck artifact first, followed by checks performed and any rendering, font, asset, or environment caveat.

Do not claim visual validation from Markdown inspection alone. Do not commit, publish, or convert formats unless requested.
