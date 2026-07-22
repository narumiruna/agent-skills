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

**Diagram summary:** Requests pass from clients through the gateway to application services and storage.

*Full-page background with overlay title*

---

## Split Layout: Image Right

![bg right fit](diagrams/workflow.svg)

# Process Workflow

**Diagram summary:** The request moves through validation and processing before a result returns to the user.

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

**Diagram summary:** The microservices architecture contains three main components:

- API Gateway
- Service Mesh
- Data Layer

---

## Custom Split Ratio

![bg right:40% fit](diagrams/detail.svg)

# Detailed View

**Diagram summary:** The detailed view expands the selected component into its inputs, processing stage, and outputs.

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

**Comparison summary:** The revised flow removes the intermediate handoff and reduces the path from four steps to three.

---

## With Small Icon (Exception)

<img src="../icons/check.svg" width="60" alt="" aria-hidden="true"> Feature completed

<img src="../icons/warning.svg" width="60" alt="" aria-hidden="true"> Needs attention

<img src="../icons/info.svg" width="60" alt="" aria-hidden="true"> Additional info

*Only use regular syntax for tiny inline icons*

---

<!-- _class: lead -->
<!-- _backgroundColor: #2E75B6 -->
<!-- _color: #FFFFFF -->

# Key Takeaway

Use `bg fit` for full-slide or split-layout diagrams
- Provide an adjacent semantic equivalent for meaningful backgrounds
- Keep descriptive host-level alt text for inline images
- Let Marp control background sizing
- Verify the exported accessibility tree

---

<!-- _class: lead -->

# Thank You

Questions?

your.email@example.com

---
