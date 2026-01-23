# Marp Authoring Output Examples

Complete examples of expected outputs for Marp/Marpit authoring.

## Minimal Presentation

````markdown
---
marp: true
theme: default
---

<!-- _class: lead -->

# Presentation Title
Subtitle

Author Name · 2026-01-09

---

## Content Slide

- Key point 1
- Key point 2
- Key point 3

---

## Code Example

```python
def calculate(x, y):
    return x + y

result = calculate(5, 3)
print(result)  # Output: 8
```

---

<!-- _class: lead -->

# Thank You
Questions?
````

## Full Presentation with Colors

````markdown
---
marp: true
theme: default
paginate: true
backgroundColor: #1E1E1E
color: #D4D4D4
---

<!-- _class: lead -->
<!-- _backgroundColor: #0C0C0C -->
<!-- _color: #ABB2BF -->

# System Architecture Overview
Technical deep dive

Engineering Team · 2026-01-09

---

<!-- _class: lead -->
<!-- _backgroundColor: #0C0C0C -->
<!-- _color: #ABB2BF -->

# Section 1: Backend Services

---

## Service Architecture

- **API Gateway**: Request routing and authentication
- **Service Mesh**: Inter-service communication
- **Data Layer**: PostgreSQL + Redis caching

![width:900px](diagrams/architecture.svg)

---

## Code Example: Service Setup

```python
from fastapi import FastAPI
from loguru import logger

app = FastAPI()

@app.on_event("startup")
async def startup():
    logger.info("Service starting up")
    await connect_database()
```

**Key features**: Async startup, structured logging

---

<!-- _class: lead -->
<!-- _backgroundColor: #0C0C0C -->
<!-- _color: #ABB2BF -->

# Questions?

Your feedback is appreciated
````

## See Also

- `index.md` - Reference navigation hub
- `syntax-guide.md` - Marp/Marpit syntax rules
- `patterns.md` - Common slide patterns
