---
name: creating-mermaid-diagrams
description: Use when creating or converting Mermaid diagrams, including flowcharts, sequence diagrams, ER diagrams, class diagrams, state diagrams, Gantt charts, and SVG exports.
---

# Mermaid Creator

Create Mermaid source files for docs or slides, then export to SVG only when a rendered asset is needed.

## Workflow

1. Pick the diagram type that matches the structure.
2. Write one focused `.mmd` file.
3. Validate or render with Mermaid CLI.
4. Commit source `.mmd`; commit SVG only when the consumer needs a static asset.

## Diagram Type Selection

| Type | Use when | Reference | Example |
| --- | --- | --- | --- |
| Flowchart | processes, workflows, decisions | `references/flowchart.md` | `assets/examples/flowchart/basic.mmd` |
| Sequence | temporal system/API interactions | `references/sequence.md` | `assets/examples/sequence/basic.mmd` |
| Class | object models and relationships | `references/class.md` | `assets/examples/class/basic.mmd` |
| State | state machines and lifecycle states | `references/state.md` | `assets/examples/state/basic.mmd` |
| ER | database/entity relationships | `references/er.md` | `assets/examples/er/basic.mmd` |
| Other | Gantt, pie, git, journey, quadrant, timeline, mindmap, requirement, C4 | `references/other-types.md` | `assets/examples/other/gantt-basic.mmd` |

Load only the reference for the diagram type you are creating.

## Mermaid CLI

```shell
mmdc -i diagram.mmd -o diagram.svg
mmdc -i diagram.mmd -o diagram.svg -t dark -b transparent
```

Useful flags:

- `-t`: theme (`default`, `dark`, `forest`, `neutral`)
- `-b`: background color or `transparent`
- `-w` / `-H`: output width and height

## Rules

- Keep diagrams small; split large diagrams instead of making one unreadable chart.
- Use descriptive labels; avoid unexplained abbreviations.
- For slides, prefer high contrast and SVG output.
- Store generated SVG next to the source when the slide or doc references it.

## Troubleshooting

- Run `mmdc -i file.mmd -o /tmp/mermaid-check.svg` for parser errors.
- Quote labels with punctuation or special characters.
- Use alphanumeric node IDs with underscores.
- Reduce graph size if layout overlaps.
