# Class Diagrams

Use class diagrams for object models, domain concepts, and typed relationships.

## Minimal Pattern

```mermaid
classDiagram
    class User {
        +String name
        +login()
    }
    class Post {
        +String title
        +publish()
    }
    User "1" --> "*" Post : creates
```

Example file: `assets/examples/class/basic.mmd`.

## Rules

- Show only fields and methods needed for the discussion.
- Prefer domain relationships over every implementation detail.
- Use cardinality labels when multiplicity matters.
- Do not model interfaces unless the diagram explains a real boundary.

## Relationships

```mermaid
classDiagram
    Animal <|-- Dog : inherits
    Order *-- LineItem : contains
    Team o-- Member : aggregates
    Service ..> Repository : uses
```
