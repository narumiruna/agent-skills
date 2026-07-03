# Other Diagram Types

Additional Mermaid diagram types for specialized use cases.

## Gantt Charts

Project timelines and task scheduling.

### Basic Syntax

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD

    section Planning
    Requirements    :a1, 2024-01-01, 7d
    Design         :a2, after a1, 5d
```

### Task Status

- `done` - Completed task
- `active` - In progress
- `crit` - Critical task
- No keyword - Planned task

**Examples**:
- `assets/examples/other/gantt-basic.mmd`
- `assets/examples/other/gantt-status.mmd`

## Pie Charts

Data distribution visualization.

```mermaid
pie title Distribution
    "Category A" : 45
    "Category B" : 30
    "Category C" : 25
```

Use `showData` to display percentages.

**Examples**:
- `assets/examples/other/pie-basic.mmd`
- `assets/examples/other/pie-showdata.mmd`

## Git Graphs

Git commit history and branching.

```mermaid
gitGraph
    commit
    branch develop
    checkout develop
    commit
    checkout main
    merge develop
```

Add IDs and tags: `commit id: "Initial"`, `merge develop tag: "v1.0"`

**Examples**:
- `assets/examples/other/git-basic.mmd`
- `assets/examples/other/git-feature-branch.mmd`
- `assets/examples/other/git-tags.mmd`

## User Journey

User experience and interaction flows with satisfaction scores (1-5).

```mermaid
journey
    title User Journey
    section Browse
      Action 1: 5: User
      Action 2: 4: User, System
```

**Examples**:
- `assets/examples/other/journey-shopping.mmd`
- `assets/examples/other/journey-service.mmd`

## Quadrant Chart

2D comparison and categorization.

```mermaid
quadrantChart
    title Priority Matrix
    x-axis Low --> High
    y-axis Low --> High
    quadrant-1 Top Right
    quadrant-2 Top Left
    quadrant-3 Bottom Left
    quadrant-4 Bottom Right

    Item A: [0.7, 0.8]
```

**Examples**:
- `assets/examples/other/quadrant-basic.mmd`
- `assets/examples/other/quadrant-priority.mmd`

## Timeline

Chronological events.

```mermaid
timeline
    title History
    2020 : Event 1
         : Event 2
    2021 : Event 3
```

Use `section` for grouping.

**Examples**:
- `assets/examples/other/timeline-basic.mmd`
- `assets/examples/other/timeline-project.mmd`

## Mindmap

Hierarchical idea organization.

```mermaid
mindmap
  root((Central Idea))
    Topic 1
      Subtopic A
      Subtopic B
    Topic 2
```

**Example**: `assets/examples/other/mindmap-basic.mmd`

## Requirement Diagram

Requirements and their relationships.

```mermaid
requirementDiagram
    requirement Req1 {
        id: 1
        text: Description
        risk: high
        verifymethod: test
    }

    element System {
        type: system
    }

    System - satisfies -> Req1
```

**Example**: `assets/examples/other/requirement-basic.mmd`

## C4 Diagram

Software architecture context.

```mermaid
C4Context
    title System Context

    Person(user, "User", "Description")
    System(system, "System", "Description")

    Rel(user, system, "Uses")
```

**Example**: `assets/examples/other/c4-context.mmd`

## Best Practices by Type

### Gantt
- Use realistic date formats
- Mark critical path with `crit`
- Group related tasks in sections
- Use `after` for dependencies

### Pie
- Keep to 5-7 slices maximum
- Combine small slices into "Other"
- Use `showData` for transparency

### Git
- Use meaningful commit IDs
- Tag important releases
- Show realistic branch patterns

### Journey
- Keep to 3-5 sections
- Use consistent actor names
- Score from user perspective (1=worst, 5=best)

### Quadrant
- Choose meaningful axis labels
- Use all four quadrants
- Place items thoughtfully

### Timeline
- Group by logical periods
- Use sections for organization
- Keep descriptions concise
