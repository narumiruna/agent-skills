# Other Diagram Types

This reference covers additional Mermaid diagram types: Gantt, Pie, Git, Journey, Quadrant, Timeline, and more.

## Gantt Charts

Project timelines and task scheduling.

### Basic Gantt

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD

    section Planning
    Requirements    :a1, 2024-01-01, 7d
    Design         :a2, after a1, 5d

    section Development
    Backend        :b1, 2024-01-15, 14d
    Frontend       :b2, after b1, 10d
    Testing        :b3, after b2, 7d

    section Deployment
    Staging        :c1, after b3, 3d
    Production     :c2, after c1, 2d
```

### Task Status

```mermaid
gantt
    title Task Status Example
    dateFormat YYYY-MM-DD

    section Completed
    Task 1         :done, t1, 2024-01-01, 5d
    Task 2         :done, t2, after t1, 3d

    section In Progress
    Task 3         :active, t3, after t2, 4d

    section Planned
    Task 4         :t4, after t3, 6d
    Task 5         :crit, t5, after t4, 5d
```

Status keywords:
- `done` - Completed task
- `active` - In progress
- `crit` - Critical task
- No keyword - Planned task

## Pie Charts

Data distribution visualization.

```mermaid
pie title Distribution of Sales by Region
    "North America" : 45
    "Europe" : 30
    "Asia" : 20
    "Other" : 5
```

```mermaid
pie showData
    title Programming Languages Used
    "Python" : 35
    "JavaScript" : 28
    "Java" : 18
    "Go" : 12
    "Other" : 7
```

Use `showData` to display percentages.

## Git Graphs

Git commit history and branching.

```mermaid
gitGraph
    commit
    commit
    branch develop
    checkout develop
    commit
    commit
    checkout main
    merge develop
    commit
```

### Feature Branch Workflow

```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Add login"

    branch feature/payment
    checkout feature/payment
    commit id: "Payment gateway"
    commit id: "Tests"

    checkout main
    branch feature/notifications
    checkout feature/notifications
    commit id: "Email service"

    checkout main
    merge feature/payment tag: "v1.1.0"
    commit id: "Hotfix"

    checkout feature/notifications
    commit id: "SMS support"
    checkout main
    merge feature/notifications tag: "v1.2.0"
```

### With Tags and IDs

```mermaid
gitGraph
    commit id: "Setup project"
    commit id: "Add README" tag: "v0.1.0"

    branch develop
    checkout develop
    commit id: "Feature A"

    branch feature/auth
    checkout feature/auth
    commit id: "Login page"
    commit id: "Auth logic"

    checkout develop
    merge feature/auth

    checkout main
    merge develop tag: "v1.0.0"
```

## User Journey

User experience and interaction flows.

```mermaid
journey
    title User Shopping Journey
    section Browse
      Visit homepage: 5: User
      Search products: 4: User
      View product: 4: User
    section Purchase
      Add to cart: 3: User
      Enter details: 2: User
      Make payment: 1: User, Payment Gateway
    section Post-Purchase
      Confirmation: 5: User, System
      Track order: 4: User
      Receive product: 5: User
```

Score meanings:
- 5 - Very satisfied
- 4 - Satisfied
- 3 - Neutral
- 2 - Dissatisfied
- 1 - Very dissatisfied

### Service Experience

```mermaid
journey
    title Customer Support Experience
    section Contact
      Find contact info: 3: Customer
      Wait in queue: 1: Customer
      Connect with agent: 4: Customer, Agent
    section Resolution
      Explain issue: 3: Customer, Agent
      Investigate: 2: Customer, Agent, System
      Provide solution: 5: Customer, Agent
    section Follow-up
      Rate experience: 4: Customer
      Close ticket: 5: Agent, System
```

## Quadrant Chart

2D comparison and categorization.

```mermaid
quadrantChart
    title Technical Debt vs Business Value
    x-axis Low Value --> High Value
    y-axis Low Effort --> High Effort
    quadrant-1 Quick Wins
    quadrant-2 Strategic
    quadrant-3 Fill-ins
    quadrant-4 Hard Slog

    Feature A: [0.7, 0.8]
    Feature B: [0.3, 0.2]
    Feature C: [0.8, 0.3]
    Feature D: [0.2, 0.7]
    Feature E: [0.5, 0.5]
```

### Priority Matrix

```mermaid
quadrantChart
    title Task Priority Matrix
    x-axis Low Impact --> High Impact
    y-axis Low Urgency --> High Urgency
    quadrant-1 Do First
    quadrant-2 Schedule
    quadrant-3 Delegate
    quadrant-4 Eliminate

    Security patch: [0.85, 0.9]
    New feature: [0.7, 0.3]
    Bug fix: [0.4, 0.6]
    Refactoring: [0.3, 0.2]
    Documentation: [0.5, 0.4]
```

## Timeline

Chronological events.

```mermaid
timeline
    title Company History
    2020 : Founded
         : Seed funding
    2021 : First product launch
         : Series A funding
         : Reached 1K users
    2022 : Expanded to Europe
         : Series B funding
    2023 : Acquired competitor
         : IPO
```

### Project Milestones

```mermaid
timeline
    title Product Development
    section Q1 2024
        Planning : Requirements gathering
                : Architecture design
    section Q2 2024
        Development : Backend complete
                    : Frontend complete
    section Q3 2024
        Testing : QA phase
                : Beta release
    section Q4 2024
        Launch : Production release
              : Marketing campaign
```

## Mindmap

Hierarchical idea organization.

```mermaid
mindmap
  root((Project))
    Planning
      Requirements
      Timeline
      Budget
    Development
      Backend
        API
        Database
      Frontend
        UI
        UX
    Testing
      Unit tests
      Integration
      E2E
    Deployment
      Staging
      Production
```

## Requirement Diagram

Requirements and their relationships.

```mermaid
requirementDiagram
    requirement UserAuth {
        id: 1
        text: System shall authenticate users
        risk: high
        verifymethod: test
    }

    requirement DataEncryption {
        id: 2
        text: Data shall be encrypted at rest
        risk: high
        verifymethod: inspection
    }

    element LoginPage {
        type: interface
    }

    element Database {
        type: system
    }

    LoginPage - satisfies -> UserAuth
    Database - satisfies -> DataEncryption
```

## C4 Diagram

Software architecture context.

```mermaid
C4Context
    title System Context for Online Banking

    Person(customer, "Customer", "Banking customer")
    System(banking, "Online Banking", "Allows customers to manage accounts")
    System_Ext(email, "Email System", "Sends notifications")
    System_Ext(mainframe, "Mainframe", "Legacy banking system")

    Rel(customer, banking, "Uses")
    Rel(banking, email, "Sends emails")
    Rel(banking, mainframe, "Reads/writes data")
```

## Best Practices by Type

### Gantt
- Use realistic date formats
- Mark critical path tasks with `crit`
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
- Score from user perspective

### Quadrant
- Choose meaningful axis labels
- Use all four quadrants
- Place items thoughtfully

### Timeline
- Group by logical periods
- Use sections for organization
- Keep descriptions concise
