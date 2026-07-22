---
name: creating-mermaid-diagrams
description: Create, revise, convert, or validate Mermaid diagrams, including flowcharts, sequence, ER, class, state, Gantt, and optional SVG rendering for documents or slides.
---

# Mermaid Diagrams

Preserve editable Mermaid source. Render a static asset only when the consumer requires one.

## Route by Structure

| Type | Best for | Reference | Example |
| --- | --- | --- | --- |
| Flowchart | processes and decisions | `references/flowchart.md` | `assets/examples/flowchart/basic.mmd` |
| Sequence | ordered system interactions | `references/sequence.md` | `assets/examples/sequence/basic.mmd` |
| Class | object models | `references/class.md` | `assets/examples/class/basic.mmd` |
| State | lifecycle transitions | `references/state.md` | `assets/examples/state/basic.mmd` |
| ER | data entities and relationships | `references/er.md` | `assets/examples/er/basic.mmd` |
| Other | Gantt, pie, git, journey, timeline, mindmap, requirement, C4 | `references/other-types.md` | `assets/examples/other/gantt-basic.mmd` |

Load only the matching reference.

## Workflow

1. Identify the relationships, sequence, or states the diagram must communicate and choose the matching type.
2. Write one focused `.mmd` source with descriptive labels and simple alphanumeric or underscore IDs. Split a graph that becomes unreadable.
3. Validate with the consumer's Mermaid renderer when known. Otherwise, use Mermaid CLI when available:

```shell
mmdc -i diagram.mmd -o /tmp/diagram-check.svg
```

4. If a slide or document needs a static asset, render the requested SVG with an appropriate theme, background, and dimensions, then inspect it in the target artifact.
5. Return or preserve the source, any requested rendered artifact, validation performed, and renderer/version compatibility caveats.

Quote labels containing punctuation. Prefer high contrast for slides. Diagram creation does not authorize a Git commit or publication.
