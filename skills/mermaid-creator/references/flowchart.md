# Flowchart Diagrams

Flowcharts represent processes, workflows, and decision trees.

## Basic Syntax

```mermaid
flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Process 1]
    B -->|No| D[Process 2]
    C --> E[End]
    D --> E
```

## Direction

- `TD` or `TB` - Top to bottom
- `BT` - Bottom to top
- `LR` - Left to right
- `RL` - Right to left

## Node Shapes

```mermaid
flowchart LR
    A[Rectangle]
    B(Rounded)
    C([Stadium])
    D[[Subroutine]]
    E[(Database)]
    F((Circle))
    G>Flag]
    H{Diamond}
    I{{Hexagon}}
    J[/Parallelogram/]
    K[\Parallelogram alt\]
    L[/Trapezoid\]
    M[\Trapezoid alt/]
```

## Connections

```mermaid
flowchart LR
    A --> B        %% Arrow
    C --- D        %% Line
    E -.-> F       %% Dotted arrow
    G -.- H        %% Dotted line
    I ==> J        %% Thick arrow
    K == L         %% Thick line
```

## Labeled Links

```mermaid
flowchart LR
    A -->|Label| B
    C -.->|Text| D
    E ==>|Thick| F
```

## Common Patterns

### Simple Process Flow

```mermaid
flowchart TD
    Start[Start Process] --> Input[Get Input]
    Input --> Validate{Valid?}
    Validate -->|Yes| Process[Process Data]
    Validate -->|No| Error[Show Error]
    Process --> Save[(Save to DB)]
    Save --> End[Complete]
    Error --> End
```

### Decision Tree

```mermaid
flowchart TD
    Start[User Request] --> Auth{Authenticated?}
    Auth -->|No| Login[Redirect to Login]
    Auth -->|Yes| Role{Check Role}
    Role -->|Admin| AdminDash[Admin Dashboard]
    Role -->|User| UserDash[User Dashboard]
    Role -->|Guest| Limited[Limited Access]
```

### Workflow with Subprocesses

```mermaid
flowchart TD
    A[Receive Order] --> B[[Validate Order]]
    B --> C{Valid?}
    C -->|Yes| D[[Process Payment]]
    C -->|No| E[Reject Order]
    D --> F{Payment OK?}
    F -->|Yes| G[[Ship Order]]
    F -->|No| H[Cancel Order]
    G --> I[Complete]
```

## Best Practices

- Use descriptive labels for nodes and connections
- Keep flows top-to-bottom or left-to-right for readability
- Group related processes visually
- Use consistent node shapes (rectangles for processes, diamonds for decisions)
- Limit complexity - split large flows into multiple diagrams
- Use subgraphs for logical grouping (see advanced features)

## Advanced Features

### Subgraphs

```mermaid
flowchart TD
    A[Start] --> B[Process]

    subgraph Processing
        B --> C[Step 1]
        C --> D[Step 2]
        D --> E[Step 3]
    end

    E --> F[End]
```

### Styling

```mermaid
flowchart LR
    A[Normal]
    B[Styled Node]
    C[Another Styled]

    style B fill:#f9f,stroke:#333,stroke-width:4px
    style C fill:#bbf,stroke:#333,stroke-width:2px
```

### Class Definitions

```mermaid
flowchart TD
    A[Start]:::startClass --> B[Process]:::processClass
    B --> C[End]:::endClass

    classDef startClass fill:#90EE90,stroke:#333
    classDef processClass fill:#87CEEB,stroke:#333
    classDef endClass fill:#FFB6C1,stroke:#333
```
