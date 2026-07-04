# Flowcharts

Use flowcharts for processes, routing, workflows, and decision trees.

## Minimal Pattern

```mermaid
flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Do work]
    B -->|No| D[Skip]
    C --> E[End]
    D --> E
```

Example file: `assets/examples/flowchart/basic.mmd`.

## Rules

- Pick a direction first: `TD` for top-down, `LR` for left-to-right.
- Use diamonds only for decisions.
- Label branches when the condition matters.
- Split workflows once a diagram needs more than one screen to read.

## Common Shapes

```mermaid
flowchart LR
    A[Process]
    B{Decision}
    C((Start/End))
    D[(Database)]
```
