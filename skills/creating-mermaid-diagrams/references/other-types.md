# Other Mermaid Diagram Types

Use these when the structure is not a flow, sequence, class, state, or ER diagram.

## Gantt

Use for schedules and dependencies. Example file: `assets/examples/other/gantt-basic.mmd`.

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    section Build
    Task A :a1, 2026-01-01, 5d
    Task B :after a1, 3d
```

## Pie

Use for small part-to-whole breakdowns.

```mermaid
pie title Traffic Sources
    "Search" : 55
    "Direct" : 30
    "Referral" : 15
```

## Git Graph

Use for branch and release explanations.

```mermaid
gitGraph
    commit
    branch feature
    checkout feature
    commit
    checkout main
    merge feature
```

## Journey

Use for user experience steps and sentiment.

```mermaid
journey
    title Signup
    section Account
      Enter email: 4: User
      Verify: 3: User,System
```

## Quadrant

Use for two-axis prioritization.

```mermaid
quadrantChart
    x-axis Low Effort --> High Effort
    y-axis Low Value --> High Value
    Quick win: [0.2, 0.8]
```

## Timeline

Use for chronological events.

```mermaid
timeline
    title Release
    2026-01-01 : Kickoff
    2026-02-01 : Launch
```

## Mindmap

Use for topic breakdowns.

```mermaid
mindmap
  root((Skills))
    Python
    Writing
    Slides
```

## Requirement

Use for requirement traceability.

```mermaid
requirementDiagram
    requirement req_login {
        id: 1
        text: User can sign in
        risk: medium
        verifymethod: test
    }
```

## C4 Context

Use only when Mermaid C4 is available in the target renderer.

```mermaid
C4Context
    Person(user, "User")
    System(app, "Application")
    Rel(user, app, "uses")
```
