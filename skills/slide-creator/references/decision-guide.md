# Decision Guide

## Table of Contents

- [Quick Decision Matrix](#quick-decision-matrix)
- [Module Selection Flowchart](#module-selection-flowchart)
- [Context Loading Strategy](#context-loading-strategy)
- [When to Load Advanced References](#when-to-load-advanced-references)
- [Progressive Disclosure in Action](#progressive-disclosure-in-action)
- [See Also](#see-also)

## Quick Decision Matrix

| User Request | Modules Needed | Primary References |
|--------------|----------------|-------------------|
| "Create a slide deck" | Marpit authoring | marpit-authoring/syntax-guide.md, marpit-authoring/patterns.md |
| "Design slide colors" | Color design | color-design/workflow.md, color-design/strategies.md, color-palettes.md |
| "Draw a diagram" | SVG illustration | svg-illustration/core-rules.md, color-palettes.md |
| "Create presentation with brand colors" | Color design -> Marpit | color-design/workflow.md, marpit-authoring/patterns.md |
| "Build tech talk with diagrams" | All three modules | Core rules from each, load details as needed |

## Module Selection Flowchart

```
User request
    |
    +-- Mentions "slides" or "deck" or "presentation"?
    |       |
    |       +-- Marpit authoring
    |       |
    |       +-- Also mentions "colors" or "theme" or "brand"?
    |       |       |
    |       |       +-- Add color design (run first)
    |       |
    |       +-- Also mentions "diagrams" or "flowchart" or "architecture"?
    |               |
    |               +-- Add SVG illustration
    |
    +-- Mentions "diagram" or "illustration" or "SVG" only?
            |
            +-- SVG illustration
            |
            +-- Needs custom colors?
                    |
                    +-- Add color design
```

## Context Loading Strategy

### For Simple Requests (1-5 slides or 1 diagram)

Load:
- SKILL.md core rules
- One module primary reference

Example: "Draw a workflow diagram"
- Read: `svg-illustration/core-rules.md`
- Read: `color-palettes.md` for palette selection
- Skip patterns and troubleshooting unless needed

### For Medium Requests (Deck + few diagrams)

Load:
- Core rules
- Patterns and best practices for the module(s)

Example: "Create a 10-slide technical presentation with 2 diagrams"
- Read: `color-design/workflow.md` -> `color-design/strategies.md`
- Read: `marpit-authoring/syntax-guide.md` -> `marpit-authoring/patterns.md`
- Read: `svg-illustration/core-rules.md`

### For Complex Requests (Branded deck, many diagrams)

Load:
- All relevant references progressively as needs appear

Example: "Create a full conference deck with brand colors"
- Phase 1: Color design
- Phase 2: Marpit authoring
- Phase 3: SVG illustration

## When to Load Advanced References

### `marpit-authoring/advanced-layouts.md`

Load when:
- User requests complex layouts or mixed content
- Standard patterns are insufficient

Skip when:
- Simple bullet lists and code blocks

### `svg-illustration/pattern-examples.md`

Load when:
- User requests specific diagram types
- You need a structure example

Skip when:
- Creating simple shapes or icons

### `color-palettes.md`

Load when:
- User wants recommendations or pre-made systems
- Palette is not already specified

Skip when:
- User provides brand colors

## Progressive Disclosure in Action

Example: "Create a tech talk with diagrams"

1. Assess scope (slides, diagrams, palette)
2. Load core rules and minimal references
3. Draft slide structure
4. Add diagrams only after slide outline is stable
5. Load troubleshooting only if an issue appears

## See Also

- [SKILL.md](../SKILL.md) - Core workflow and module overview
- [output-examples.md](output-examples.md) - Expected outputs for each module
