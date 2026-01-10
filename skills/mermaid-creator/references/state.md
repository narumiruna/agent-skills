# State Diagrams

State diagrams model the states of a system and transitions between them.

## Basic Syntax

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing : start
    Processing --> Complete : finish
    Complete --> [*]
```

## States

```mermaid
stateDiagram-v2
    state "Waiting for Input" as waiting
    state "Processing Data" as processing

    [*] --> waiting
    waiting --> processing : received
    processing --> waiting : complete
```

## Composite States

```mermaid
stateDiagram-v2
    [*] --> Active

    state Active {
        [*] --> Running
        Running --> Paused : pause
        Paused --> Running : resume
    }

    Active --> [*] : stop
```

## Choice (Conditional)

```mermaid
stateDiagram-v2
    [*] --> Input
    Input --> Validate

    state Validate <<choice>>
    Validate --> Success : valid
    Validate --> Error : invalid

    Success --> [*]
    Error --> Input : retry
```

## Fork and Join

```mermaid
stateDiagram-v2
    [*] --> Start

    state fork_state <<fork>>
    Start --> fork_state
    fork_state --> Task1
    fork_state --> Task2

    state join_state <<join>>
    Task1 --> join_state
    Task2 --> join_state
    join_state --> Complete

    Complete --> [*]
```

## Common Patterns

### Simple State Machine

```mermaid
stateDiagram-v2
    [*] --> Off
    Off --> On : power_on
    On --> Off : power_off
    On --> Standby : idle_timeout
    Standby --> On : activity
    Standby --> Off : power_off
```

### Order Processing

```mermaid
stateDiagram-v2
    [*] --> Pending
    Pending --> Confirmed : payment_received
    Pending --> Cancelled : timeout

    Confirmed --> Processing : start_fulfillment
    Processing --> Shipped : dispatched
    Shipped --> Delivered : received
    Delivered --> [*]

    Confirmed --> Cancelled : customer_cancel
    Processing --> Cancelled : out_of_stock
```

### User Authentication

```mermaid
stateDiagram-v2
    [*] --> LoggedOut

    LoggedOut --> Authenticating : login_attempt

    state Authenticating {
        [*] --> Validating
        Validating --> CheckingMFA : credentials_valid
        Validating --> Failed : credentials_invalid
        CheckingMFA --> Verified : mfa_success
        CheckingMFA --> Failed : mfa_failed
    }

    Authenticating --> LoggedIn : Verified
    Authenticating --> LoggedOut : Failed

    LoggedIn --> LoggedOut : logout
    LoggedIn --> LoggedOut : session_timeout
```

### Document Workflow

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Review : submit
    Draft --> Archived : delete

    Review --> Approved : approve
    Review --> Rejected : reject
    Review --> Draft : request_changes

    Rejected --> Draft : revise
    Approved --> Published : publish
    Published --> Archived : archive

    Archived --> [*]
```

## Best Practices

- Start with `[*]` for initial state
- End with `[*]` for final state
- Use descriptive state names
- Label all transitions clearly
- Use composite states for complex subsystems
- Use choice states for conditional branching
- Keep diagrams focused on one workflow
- Use fork/join for parallel operations

## Advanced Features

### State Descriptions

```mermaid
stateDiagram-v2
    Processing : Processing order
    Processing : Validating payment
    Processing : Updating inventory

    [*] --> Processing
    Processing --> Complete
    Complete --> [*]
```

### Notes

```mermaid
stateDiagram-v2
    [*] --> Active
    Active --> Inactive

    note right of Active
        This is the main
        operational state
    end note

    note left of Inactive
        System is idle
    end note
```

### Concurrency (Parallel States)

```mermaid
stateDiagram-v2
    [*] --> Active

    state Active {
        [*] --> ProcessA
        --
        [*] --> ProcessB
    }

    Active --> [*]
```

The `--` separator creates parallel regions within a composite state.

### Direction

Use `direction LR` for left-to-right layout:

```mermaid
stateDiagram-v2
    direction LR
    [*] --> A
    A --> B
    B --> [*]
```

## Complex Example

```mermaid
stateDiagram-v2
    [*] --> Initialized

    Initialized --> Ready : config_loaded

    state Ready {
        [*] --> Idle
        Idle --> Busy : task_received
        Busy --> Idle : task_complete
        Busy --> Error : task_failed

        state Error {
            [*] --> Retrying
            Retrying --> Idle : retry_success
            Retrying --> Failed : retry_limit
        }

        Failed --> Idle : reset
    }

    Ready --> Shutdown : stop_signal
    Shutdown --> [*]
```
