# Common Slide Patterns

## Table of Contents

- [1. Title Slide (Opening)](#1-title-slide-opening)
- [2. Agenda / Table of Contents](#2-agenda-table-of-contents)
- [3. Problem → Solution](#3-problem-solution)
- [4. Before / After Comparison](#4-before-after-comparison)
- [5. Feature Showcase](#5-feature-showcase)
- [6. Quote / Testimonial](#6-quote-testimonial)
- [7. Key Takeaway](#7-key-takeaway)
- [8. Pros and Cons](#8-pros-and-cons)
- [9. Step-by-Step Process](#9-step-by-step-process)
- [10. Data / Statistics](#10-data-statistics)
- [11. Section Divider](#11-section-divider)
- [12. Q&A / Thank You](#12-qa-thank-you)
- [13. Diagram Placeholder](#13-diagram-placeholder)
- [14. Code Example with Context](#14-code-example-with-context)
- [15. Two-Column Concept](#15-two-column-concept)
- [16. Image with Text (Split Layout)](#16-image-with-text-split-layout)
- [17. Full-Page Image](#17-full-page-image)
- [18. Multiple Image Comparison](#18-multiple-image-comparison)

Quick reference for frequently used presentation structures.

---

## 1. Title Slide (Opening)

```markdown
---
marp: true
theme: default
---

# Presentation Title

**Subtitle or Key Message**

Presenter Name · Organization
Date
```

---

## 2. Agenda / Table of Contents

```markdown
# Today's Agenda

1. Introduction to Topic
2. Core Concepts
3. Practical Examples
4. Q&A Session
```

---

## 3. Problem → Solution

```markdown
# The Challenge

**Problem:**
- Issue description point 1
- Issue description point 2

**Solution:**
- How we address point 1
- How we address point 2
```

---

## 4. Before / After Comparison

```markdown
# Transformation

| Before | After |
|--------|-------|
| Old way | New way |
| Slow | Fast |
| Complex | Simple |
```

Or vertical layout:

```markdown
# Evolution

**Before:**
- Previous state
- Limitations

**After:**
- Current state
- Improvements
```

---

## 5. Feature Showcase

```markdown
# Key Features

**Feature 1: Name**
Brief description

**Feature 2: Name**
Brief description

**Feature 3: Name**
Brief description
```

---

## 6. Quote / Testimonial

```markdown
<!-- _class: lead -->

> "Memorable quote that supports your message"

— Source / Author
```

---

## 7. Key Takeaway

```markdown
<!-- _class: lead invert -->

# Remember This

**Critical insight in bold**

Supporting detail if needed
```

---

## 8. Pros and Cons

```markdown
# Trade-offs Analysis

**Pros:**
- ✓ Advantage 1
- ✓ Advantage 2

**Cons:**
- ✗ Limitation 1
- ✗ Limitation 2
```

---

## 9. Step-by-Step Process

```markdown
# Implementation Steps

1. **Prepare** - Gather requirements
2. **Build** - Create solution
3. **Test** - Verify functionality
4. **Deploy** - Release to production
```

---

## 10. Data / Statistics

```markdown
# By the Numbers

- **85%** of users report improvement
- **2x** faster than previous version
- **$1M** in cost savings

*Source: Internal metrics Q4 2024*
```

---

## 11. Section Divider

```markdown
<!-- _class: lead -->

# Part Two

Moving from Theory to Practice

---
```

---

## 12. Q&A / Thank You

```markdown
<!-- _class: lead -->

# Questions?

**Contact Information**
email@example.com
github.com/username
```

---

## 13. Diagram Placeholder

When diagrams aren't available yet:

```markdown
# System Architecture

```
[Diagram: Three-tier architecture]
- Frontend Layer
- API Layer
- Database Layer
```

Description in bullets until diagram is ready.
```

---

## 14. Code Example with Context

````markdown
# Implementation

**Approach:**
Use async/await for better performance

```python
async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()
```

**Result:** 3x faster response time
````

---

## 15. Two-Column Concept

```markdown
# Comparison

**Option A**                    | **Option B**
- Characteristic 1               | - Characteristic 1
- Characteristic 2               | - Characteristic 2
- Trade-off                      | - Trade-off
```

Note: True two-column layout depends on theme support. This uses table syntax as fallback.

---

## 16. Image with Text (Split Layout)

**Text on left, image on right:**

```markdown
![bg right fit](diagrams/architecture-diagram.svg)

# System Architecture

**Key Components:**
- Frontend: React + TypeScript
- Backend: Python FastAPI
- Database: PostgreSQL
- Cache: Redis

**Benefits:** Scalable, maintainable, performant
```

**Image on left, text on right:**

```markdown
![bg left fit](diagrams/workflow.svg)

# Process Flow

The diagram shows our three-stage pipeline:

1. **Ingestion** - Data collection
2. **Processing** - Transformation
3. **Output** - Results delivery
```

**Custom split ratio (60/40):**

```markdown
![bg left:60% fit](diagrams/detailed-view.svg)

# Architecture Details

More space for the diagram (60%), less for text (40%).
```

---

## 17. Full-Page Image

**Background image filling entire slide:**

```markdown
![bg fit](diagrams/pretrip-checklist.svg)

# Optional Overlay Title
Optional text overlays on the image
```

**Without text (pure image slide):**

```markdown
![bg fit](diagrams/complex-system.svg)
```

**With centered caption:**

```markdown
<!-- _class: lead -->
![bg fit](diagrams/key-concept.svg)

# Key Concept
```

---

## 18. Multiple Image Comparison

**Side-by-side comparison:**

```markdown
![bg left:50% fit](diagrams/before.svg)
![bg right:50% fit](diagrams/after.svg)

# Before → After
```

**Vertical stacking:**

```markdown
![bg vertical fit](diagrams/header.svg)
![bg fit](diagrams/main-content.svg)

# Layered View
```
