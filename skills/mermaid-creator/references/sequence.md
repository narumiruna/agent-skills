# Sequence Diagrams

Sequence diagrams show interactions between actors and systems over time.

## Basic Syntax

```mermaid
sequenceDiagram
    participant A as Alice
    participant B as Bob
    A->>B: Hello Bob!
    B->>A: Hi Alice!
```

## Participants

```mermaid
sequenceDiagram
    participant User
    participant API
    participant Database
    actor Admin

    User->>API: Request
    API->>Database: Query
    Database-->>API: Result
    API-->>User: Response
```

Use `participant` for systems, `actor` for human actors.

## Message Types

```mermaid
sequenceDiagram
    A->>B: Solid arrow
    A-->>B: Dotted arrow
    A-)B: Async solid
    A--)B: Async dotted
    A-xB: Solid with X
    A--xB: Dotted with X
```

## Activations

```mermaid
sequenceDiagram
    participant Client
    participant Server

    Client->>+Server: Request
    Server->>+Database: Query
    Database-->>-Server: Data
    Server-->>-Client: Response
```

`+` activates, `-` deactivates.

## Notes

```mermaid
sequenceDiagram
    participant A
    participant B

    Note left of A: Left note
    Note right of B: Right note
    Note over A: Note over A
    Note over A,B: Note spanning both

    A->>B: Message
```

## Loops and Conditionals

```mermaid
sequenceDiagram
    participant User
    participant API

    loop Every 5 seconds
        User->>API: Poll for updates
        API-->>User: Data
    end

    alt Successful case
        API->>User: Success
    else Failure case
        API->>User: Error
    end

    opt Optional flow
        User->>API: Optional action
    end
```

## Common Patterns

### REST API Call

```mermaid
sequenceDiagram
    participant Client
    participant API
    participant Auth
    participant DB

    Client->>+API: POST /api/login
    API->>+Auth: Validate credentials
    Auth->>+DB: Query user
    DB-->>-Auth: User data
    Auth-->>-API: Token
    API-->>-Client: 200 OK + Token

    Client->>+API: GET /api/data (with token)
    API->>Auth: Verify token
    Auth-->>API: Valid
    API->>+DB: Fetch data
    DB-->>-API: Results
    API-->>-Client: 200 OK + Data
```

### Authentication Flow

```mermaid
sequenceDiagram
    actor User
    participant App
    participant AuthServer
    participant ResourceServer

    User->>App: Click Login
    App->>AuthServer: Authorization Request
    AuthServer->>User: Login Page
    User->>AuthServer: Credentials
    AuthServer->>AuthServer: Validate
    AuthServer-->>App: Authorization Code
    App->>AuthServer: Exchange Code for Token
    AuthServer-->>App: Access Token
    App->>ResourceServer: API Request + Token
    ResourceServer-->>App: Protected Resource
    App-->>User: Display Data
```

### Error Handling

```mermaid
sequenceDiagram
    participant Client
    participant Server
    participant DB

    Client->>+Server: Request
    Server->>+DB: Query

    alt Success
        DB-->>Server: Data
        Server-->>Client: 200 OK
    else Database Error
        DB--xServer: Connection failed
        Server-->>Client: 503 Service Unavailable
    else Validation Error
        Server-->>Client: 400 Bad Request
    end

    deactivate DB
    deactivate Server
```

## Best Practices

- Use clear participant names (User, API, Database, not A, B, C)
- Show activation bars for long-running operations
- Use notes to explain complex logic
- Keep sequences focused - split complex flows into multiple diagrams
- Use `actor` for human users, `participant` for systems
- Label messages with meaningful descriptions
- Use alt/else/opt for branching logic
- Show both request and response messages

## Advanced Features

### Autonumber

```mermaid
sequenceDiagram
    autonumber
    Alice->>John: Hello
    John->>Alice: Hi
    Alice->>John: How are you?
```

### Background Colors

```mermaid
sequenceDiagram
    participant A
    participant B

    rect rgb(200, 220, 250)
        A->>B: Request
        B-->>A: Response
    end

    rect rgba(0, 255, 0, 0.1)
        Note over A,B: Success scenario
    end
```

### Critical Region

```mermaid
sequenceDiagram
    participant Client
    participant Server

    critical Establish connection
        Client->>Server: Connect
        Server-->>Client: ACK
    option Connection timeout
        Server-->>Client: Timeout error
    end
```
