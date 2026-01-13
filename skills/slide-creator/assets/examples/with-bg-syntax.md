---
marp: true
theme: default
paginate: true
backgroundColor: #FAFAFA
color: #2C2C2C
---

<!-- _class: lead -->
<!-- _backgroundColor: #2E75B6 -->
<!-- _color: #FFFFFF -->

# Example with bg Syntax
Demonstrating background image patterns

Tech Presentation · 2026-01-13

---

## Full-Page Diagram

![bg fit](diagrams/architecture.svg)

# System Architecture

*Full-page background with overlay title*

---

## Split Layout: Image Right

![bg right fit](diagrams/workflow.svg)

# Process Workflow

**Key Steps:**
1. User initiates request
2. System validates input
3. Process executes
4. Results returned

*Image auto-sized on right (50%)*
*Text content on left (50%)*

---

## Split Layout: Image Left

![bg left fit](diagrams/components.svg)

# Component Diagram

The diagram on the left shows our microservices architecture with three main components:

- API Gateway
- Service Mesh
- Data Layer

---

## Custom Split Ratio

![bg right:40% fit](diagrams/detail.svg)

# Detailed View

When you need more space for text, use a custom ratio.

**Benefits:**
- Image takes 40% on right
- Text has 60% space on left
- Perfect for explanations
- Still auto-sized with `fit`

---

## Side-by-Side Comparison

![bg left:50% fit](diagrams/before.svg)
![bg right:50% fit](diagrams/after.svg)

# Before → After

---

## With Small Icon (Exception)

![width:60px](../icons/check.svg) Feature completed

![width:60px](../icons/warning.svg) Needs attention

![width:60px](../icons/info.svg) Additional info

*Only use regular syntax for tiny inline icons*

---

<!-- _class: lead -->
<!-- _backgroundColor: #2E75B6 -->
<!-- _color: #FFFFFF -->

# Key Takeaway

Always use `![bg fit]` syntax for diagrams
- No manual sizing needed
- Consistent appearance
- Auto-scales perfectly
- Better split layouts

---

<!-- _class: lead -->

# Thank You

Questions?

your.email@example.com

---
