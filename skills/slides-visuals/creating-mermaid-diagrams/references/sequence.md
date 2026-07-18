# Sequence Diagrams

Use sequence diagrams for ordered interactions between people, services, APIs, or databases.

## Minimal Pattern

```mermaid
sequenceDiagram
    participant Client
    participant API
    participant DB
    Client->>API: Request
    API->>DB: Query
    DB-->>API: Result
    API-->>Client: Response
```

Example file: `assets/examples/sequence/basic.mmd`.

## Rules

- Name participants after roles or systems, not implementation classes.
- Use `->>` for calls and `-->>` for responses.
- Add `alt`, `opt`, or `loop` only when the branch is essential.
- Prefer one scenario per diagram.

## Useful Blocks

```mermaid
sequenceDiagram
    participant U as User
    participant S as Service
    U->>S: Submit
    alt valid
        S-->>U: Success
    else invalid
        S-->>U: Error
    end
```
