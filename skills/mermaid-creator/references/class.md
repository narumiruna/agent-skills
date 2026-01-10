# Class Diagrams

Class diagrams represent object-oriented structures, showing classes, attributes, methods, and relationships.

## Basic Syntax

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +makeSound()
    }
```

## Visibility

- `+` Public
- `-` Private
- `#` Protected
- `~` Package/Internal

```mermaid
classDiagram
    class BankAccount {
        +String accountNumber
        -double balance
        #String ownerName
        ~int transactionCount
        +deposit(amount)
        +withdraw(amount)
        -calculateInterest()
    }
```

## Relationships

```mermaid
classDiagram
    A --|> B : Inheritance
    C --* D : Composition
    E --o F : Aggregation
    G --> H : Association
    I -- J : Link
    K ..> L : Dependency
    M ..|> N : Realization
```

### Relationship Notation

- `--|>` Inheritance (extends)
- `--*` Composition (strong ownership)
- `--o` Aggregation (weak ownership)
- `-->` Association (uses)
- `--` Link (general connection)
- `..>` Dependency (temporary usage)
- `..|>` Realization (implements)

## Cardinality

```mermaid
classDiagram
    Customer "1" --> "*" Order
    Order "*" --> "1..*" OrderItem
    OrderItem "*" --> "1" Product
```

Common multiplicities:
- `1` - Exactly one
- `0..1` - Zero or one
- `*` or `0..*` - Zero or more
- `1..*` - One or more
- `n..m` - Range

## Common Patterns

### Inheritance Hierarchy

```mermaid
classDiagram
    class Animal {
        +String name
        +int age
        +eat()
        +sleep()
    }

    class Dog {
        +String breed
        +bark()
    }

    class Cat {
        +int livesLeft
        +meow()
    }

    Animal <|-- Dog
    Animal <|-- Cat
```

### Interface Implementation

```mermaid
classDiagram
    class Drawable {
        <<interface>>
        +draw()
    }

    class Resizable {
        <<interface>>
        +resize(width, height)
    }

    class Circle {
        +int radius
        +draw()
        +resize(width, height)
    }

    Drawable <|.. Circle
    Resizable <|.. Circle
```

### Composition vs Aggregation

```mermaid
classDiagram
    class Car {
        -Engine engine
        -List~Wheel~ wheels
        +start()
    }

    class Engine {
        +int horsepower
        +start()
    }

    class Wheel {
        +int diameter
    }

    %% Composition: Engine cannot exist without Car
    Car *-- Engine

    %% Aggregation: Wheels can exist independently
    Car o-- Wheel
```

### Full System Example

```mermaid
classDiagram
    class User {
        +String username
        +String email
        -String passwordHash
        +login()
        +logout()
    }

    class Post {
        +String title
        +String content
        +DateTime createdAt
        +publish()
    }

    class Comment {
        +String text
        +DateTime createdAt
        +edit()
    }

    class Category {
        +String name
        +String description
    }

    User "1" --> "*" Post : creates
    Post "1" --> "*" Comment : has
    User "1" --> "*" Comment : writes
    Post "*" --> "*" Category : belongs to
```

## Best Practices

- Use meaningful class and attribute names
- Show only relevant attributes and methods (not every getter/setter)
- Use proper visibility modifiers
- Choose appropriate relationships (composition vs aggregation)
- Keep diagrams focused - split large systems into multiple diagrams
- Use interfaces and abstract classes where appropriate
- Include cardinality on associations
- Group related classes visually

## Advanced Features

### Annotations

```mermaid
classDiagram
    class Shape {
        <<abstract>>
        +draw()
    }

    class Utility {
        <<static>>
        +helper()
    }

    class Config {
        <<singleton>>
    }
```

Common annotations:
- `<<interface>>`
- `<<abstract>>`
- `<<service>>`
- `<<enumeration>>`
- `<<singleton>>`

### Generics

```mermaid
classDiagram
    class List~T~ {
        +add(T item)
        +T get(int index)
    }

    class HashMap~K,V~ {
        +put(K key, V value)
        +V get(K key)
    }
```

### Namespaces

```mermaid
classDiagram
    namespace Models {
        class User
        class Post
    }

    namespace Services {
        class UserService
        class PostService
    }

    UserService --> User
    PostService --> Post
```

### Notes

```mermaid
classDiagram
    class User {
        +String email
        +login()
    }

    note for User "This class handles
    user authentication
    and profile management"
```

### Return Types and Parameters

```mermaid
classDiagram
    class UserRepository {
        +User findById(int id)
        +List~User~ findAll()
        +void save(User user)
        +boolean delete(int id)
    }
```
