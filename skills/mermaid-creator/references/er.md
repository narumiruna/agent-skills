# Entity-Relationship Diagrams

ER diagrams model database schemas, showing entities, attributes, and relationships.

## Basic Syntax

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER-ITEM : contains
    PRODUCT ||--o{ ORDER-ITEM : "ordered in"
```

## Entities and Attributes

```mermaid
erDiagram
    CUSTOMER {
        int id PK
        string name
        string email UK
        date created_at
    }

    ORDER {
        int id PK
        int customer_id FK
        date order_date
        decimal total
    }
```

Attribute annotations:
- `PK` - Primary Key
- `FK` - Foreign Key
- `UK` - Unique Key

## Relationship Cardinality

Cardinality notation:
- `||` - Exactly one
- `o|` - Zero or one
- `}o` - Zero or more
- `}|` - One or more

```mermaid
erDiagram
    A ||--|| B : "one to one"
    C ||--o{ D : "one to many"
    E }o--o{ F : "many to many"
    G }|--|{ H : "one or more to one or more"
```

## Common Patterns

### Blog System

```mermaid
erDiagram
    USER {
        int id PK
        string username UK
        string email UK
        string password_hash
        datetime created_at
    }

    POST {
        int id PK
        int user_id FK
        string title
        text content
        datetime published_at
        boolean is_published
    }

    COMMENT {
        int id PK
        int post_id FK
        int user_id FK
        text content
        datetime created_at
    }

    CATEGORY {
        int id PK
        string name UK
        string slug UK
    }

    TAG {
        int id PK
        string name UK
    }

    USER ||--o{ POST : writes
    USER ||--o{ COMMENT : writes
    POST ||--o{ COMMENT : has
    POST }o--o{ CATEGORY : "belongs to"
    POST }o--o{ TAG : "tagged with"
```

### E-commerce

```mermaid
erDiagram
    CUSTOMER {
        int id PK
        string email UK
        string name
        string phone
    }

    ORDER {
        int id PK
        int customer_id FK
        datetime order_date
        decimal total_amount
        string status
    }

    ORDER_ITEM {
        int id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal price
    }

    PRODUCT {
        int id PK
        string sku UK
        string name
        decimal price
        int stock_quantity
    }

    CATEGORY {
        int id PK
        string name UK
        int parent_id FK
    }

    ADDRESS {
        int id PK
        int customer_id FK
        string street
        string city
        string postal_code
        string country
    }

    CUSTOMER ||--o{ ORDER : places
    CUSTOMER ||--o{ ADDRESS : has
    ORDER ||--|{ ORDER_ITEM : contains
    PRODUCT ||--o{ ORDER_ITEM : "ordered in"
    PRODUCT }o--|| CATEGORY : "belongs to"
    CATEGORY ||--o{ CATEGORY : "parent of"
```

### User Management

```mermaid
erDiagram
    USER {
        int id PK
        string username UK
        string email UK
        boolean is_active
    }

    ROLE {
        int id PK
        string name UK
        string description
    }

    PERMISSION {
        int id PK
        string name UK
        string resource
        string action
    }

    USER_ROLE {
        int user_id FK
        int role_id FK
    }

    ROLE_PERMISSION {
        int role_id FK
        int permission_id FK
    }

    USER }o--o{ ROLE : "has"
    ROLE }o--o{ PERMISSION : "grants"
```

### Course Management

```mermaid
erDiagram
    STUDENT {
        int id PK
        string name
        string email UK
        date enrollment_date
    }

    COURSE {
        int id PK
        string code UK
        string title
        int credits
    }

    INSTRUCTOR {
        int id PK
        string name
        string email UK
        string department
    }

    ENROLLMENT {
        int student_id FK
        int course_id FK
        date enrolled_at
        string grade
        string status
    }

    SECTION {
        int id PK
        int course_id FK
        int instructor_id FK
        string semester
        int capacity
    }

    STUDENT }o--o{ COURSE : enrolls
    INSTRUCTOR ||--o{ SECTION : teaches
    COURSE ||--o{ SECTION : "offered as"
```

## Best Practices

- Use singular nouns for entity names (USER, not USERS)
- Use UPPERCASE for entity names
- Include primary keys (PK) for all entities
- Mark foreign keys (FK) explicitly
- Use meaningful relationship labels
- Show cardinality correctly
- Include important constraints (UK for unique keys)
- Keep attribute types clear (int, string, date, etc.)
- Don't over-complicate - focus on key relationships

## Advanced Features

### Self-Referencing Relationships

```mermaid
erDiagram
    EMPLOYEE {
        int id PK
        string name
        int manager_id FK
    }

    CATEGORY {
        int id PK
        string name
        int parent_id FK
    }

    EMPLOYEE ||--o{ EMPLOYEE : manages
    CATEGORY ||--o{ CATEGORY : "parent of"
```

### Weak Entities

```mermaid
erDiagram
    ORDER {
        int id PK
        date order_date
    }

    ORDER_LINE {
        int order_id FK
        int line_number
        int product_id FK
        int quantity
    }

    ORDER ||--|{ ORDER_LINE : contains
```

### Ternary Relationships

```mermaid
erDiagram
    DOCTOR {
        int id PK
        string name
    }

    PATIENT {
        int id PK
        string name
    }

    MEDICATION {
        int id PK
        string name
    }

    PRESCRIPTION {
        int doctor_id FK
        int patient_id FK
        int medication_id FK
        date prescribed_date
        string dosage
    }

    DOCTOR ||--o{ PRESCRIPTION : prescribes
    PATIENT ||--o{ PRESCRIPTION : receives
    MEDICATION ||--o{ PRESCRIPTION : "prescribed as"
```

## Relationship Labels

Use clear, meaningful labels:

```mermaid
erDiagram
    AUTHOR ||--o{ BOOK : writes
    BOOK }o--|| PUBLISHER : "published by"
    BOOK }o--o{ CATEGORY : "belongs to"
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--o{ SHIPMENT : "shipped via"
```
