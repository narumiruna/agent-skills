# Advanced Layouts

## Table of Contents

- [Split Layouts with Background Images](#split-layouts-with-background-images)
  - [Left-Right Split (40/60)](#left-right-split-4060)
  - [Right-Side Image](#right-side-image)
  - [Vertical Split](#vertical-split)
- [Multiple Background Images](#multiple-background-images)
  - [Side-by-Side Comparison](#side-by-side-comparison)
  - [Three-Image Layout](#three-image-layout)
- [Table-Based Layouts](#table-based-layouts)
  - [Two-Column Content](#two-column-content)
  - [Three-Column Layout](#three-column-layout)
- [Mixed Content Layouts](#mixed-content-layouts)
  - [Code + Explanation](#code-explanation)
  - [Image + Code](#image-code)
- [List Layouts](#list-layouts)
  - [Multi-Column Lists (Using Tables)](#multi-column-lists-using-tables)
  - [Nested Lists with Emphasis](#nested-lists-with-emphasis)
- [Quote Layouts](#quote-layouts)
  - [Large Quote](#large-quote)
  - [Quote with Context](#quote-with-context)
- [Hero Section](#hero-section)
- [Dashboard Layout](#dashboard-layout)
- [Code Comparison](#code-comparison)
- [Icon/Emoji Lists](#iconemoji-lists)
- [Timeline Layout](#timeline-layout)
- [Grid Layout (Pseudo)](#grid-layout-pseudo)
- [Highlight Box Pattern](#highlight-box-pattern)
- [Process Flow](#process-flow)
- [Comparison Matrix](#comparison-matrix)
- [Image Gallery](#image-gallery)
- [Math-Heavy Slide](#math-heavy-slide)
- [Mixed Media](#mixed-media)
- [Full-Screen Image with Caption](#full-screen-image-with-caption)
- [Source Code with Annotations](#source-code-with-annotations)
- [Tips for Advanced Layouts](#tips-for-advanced-layouts)
- [Troubleshooting](#troubleshooting)

Complex slide structures and multi-column techniques for Marpit.

---

## Split Layouts with Background Images

### Left-Right Split (40/60)

```markdown
![bg left:40%](diagram.png)

# Explanation

- Key point about diagram
- Second observation
- Third insight
```

**Variations:**
- `![bg left:30%](img.png)` - 30% left, 70% right
- `![bg left:50%](img.png)` - 50/50 split
- `![bg left:60%](img.png)` - 60% left, 40% right

---

### Right-Side Image

```markdown
![bg right:40%](screenshot.png)

# Feature Description

**What it does:**
- Capability 1
- Capability 2
- Capability 3
```

---

### Vertical Split

```markdown
![bg vertical](top-image.png)
![bg](bottom-image.png)

# Content
```

**Effect:** Images stacked vertically in background

---

## Multiple Background Images

### Side-by-Side Comparison

```markdown
![bg left:50%](before.png)
![bg right:50%](after.png)

# Before and After
```

### Three-Image Layout

```markdown
![bg left:33%](img1.png)
![bg](img2.png)
![bg right:33%](img3.png)

# Three Perspectives
```

---

## Table-Based Layouts

### Two-Column Content

```markdown
# Comparison

| **Approach A** | **Approach B** |
|----------------|----------------|
| Pros: | Pros: |
| • Fast | • Reliable |
| • Simple | • Scalable |
| | |
| Cons: | Cons: |
| • Limited | • Complex |
```

---

### Three-Column Layout

```markdown
| Frontend | Backend | Database |
|----------|---------|----------|
| React | Node.js | PostgreSQL |
| TypeScript | Express | Redis |
| Vite | GraphQL | MongoDB |
```

**Tip:** Keep columns balanced for best appearance.

---

## Mixed Content Layouts

### Code + Explanation

````markdown
# Implementation

```python
def process(data):
    return transform(data)
```

**Key aspects:**
- Pure function (no side effects)
- Type-safe with annotations
- Easily testable
````

---

### Image + Code

```markdown
![bg right:45%](architecture-diagram.png)

# System Design

```python
class DataPipeline:
    def __init__(self):
        self.stages = []
```

Processes data in stages
```

---

## List Layouts

### Multi-Column Lists (Using Tables)

```markdown
# Feature Coverage

| Core | Advanced |
|------|----------|
| • Authentication | • SSO |
| • CRUD ops | • Webhooks |
| • Search | • Analytics |
| • Export | • Custom fields |
```

---

### Nested Lists with Emphasis

```markdown
# Architecture Layers

1. **Presentation Layer**
   - React components
   - Tailwind CSS

2. **Business Logic**
   - Domain models
   - Service layer

3. **Data Access**
   - Repository pattern
   - ORM integration
```

---

## Quote Layouts

### Large Quote

```markdown
<!-- _class: lead -->

> "Design is not just what it looks like.
> Design is how it works."

— Steve Jobs
```

---

### Quote with Context

```markdown
# Industry Perspective

> "Software is eating the world"
> — Marc Andreessen, 2011

**This means:**
- Digital transformation is inevitable
- Every company becomes a tech company
```

---

## Hero Section

```markdown
<!-- _class: lead invert -->
<!-- _backgroundImage: url('hero-background.jpg') -->
<!-- _backgroundSize: cover -->

# **BIG BOLD MESSAGE**

Compelling subtitle that drives home the point

[Call to Action]
```

---

## Dashboard Layout

```markdown
# Key Metrics Q4 2024

| Metric | Value | Trend |
|--------|-------|-------|
| Users | 1.2M | ↑ 15% |
| Revenue | $4.5M | ↑ 22% |
| NPS | 72 | ↑ 8pts |

*All metrics vs. Q3 2024*
```

---

## Code Comparison

````markdown
# Refactoring Example

**Before:**
```python
def calc(a,b,c):
    return a+b*c
```

**After:**
```python
def calculate_total(base: int, rate: int, quantity: int) -> int:
    """Calculate total with rate and quantity."""
    return base + (rate * quantity)
```
````

---

## Icon/Emoji Lists

```markdown
# Workflow

✅ **Plan** - Define requirements
🔨 **Build** - Implement features
🧪 **Test** - Verify quality
🚀 **Deploy** - Release to production
```

**Note:** Use sparingly; ensure emojis display correctly in your environment.

---

## Timeline Layout

```markdown
# Project Phases

| Q1 2024 | Q2 2024 | Q3 2024 | Q4 2024 |
|---------|---------|---------|---------|
| Planning | Development | Testing | Launch |
| Research | Alpha | Beta | GA |
```

Or vertical:

```markdown
# Roadmap

**Phase 1: Foundation** (Jan-Mar)
- Core infrastructure

**Phase 2: Features** (Apr-Jun)
- User-facing functionality

**Phase 3: Scale** (Jul-Sep)
- Performance optimization
```

---

## Grid Layout (Pseudo)

```markdown
# Tech Stack

| Frontend | Backend | DevOps | Data |
|----------|---------|--------|------|
| React | Django | Docker | PostgreSQL |
| Next.js | FastAPI | K8s | Redis |
| Tailwind | Node | GitHub Actions | Elasticsearch |
```

---

## Highlight Box Pattern

Using tables for visual separation:

```markdown
# Key Takeaway

| 💡 Important Insight |
|----------------------|
| The most impactful optimization was caching at the edge, reducing latency by 85%. |
```

Or with quotes:

```markdown
> **📌 Remember:**
> Always validate user input at API boundaries, not just in the UI.
```

---

## Process Flow

```markdown
# Data Pipeline

```
User Input → Validation → Processing → Storage → Response
```

**Steps:**
1. **Validation** - Check format and constraints
2. **Processing** - Transform and enrich
3. **Storage** - Persist to database
4. **Response** - Return confirmation
```

---

## Comparison Matrix

```markdown
# Solution Comparison

|              | Solution A | Solution B | Solution C |
|--------------|------------|------------|------------|
| **Cost**     | Low        | Medium     | High       |
| **Speed**    | Fast       | Medium     | Slow       |
| **Scale**    | Limited    | Good       | Excellent  |
| **Ease**     | Easy       | Medium     | Complex    |
```

---

## Image Gallery

```markdown
![bg contain](image1.png)
![bg contain](image2.png)
![bg contain](image3.png)

# Portfolio Examples
```

**Effect:** Shows multiple images in a grid/sequence.

---

## Math-Heavy Slide

```markdown
# Algorithm Complexity

**Time complexity:**
$$
O(n \log n)
$$

**Space complexity:**
$$
O(n)
$$

Optimal for datasets < 1M records
```

---

## Mixed Media

```markdown
![bg right:50% fit](demo-screenshot.png)

# Live Demo

**Try it yourself:**
https://demo.example.com

**Features shown:**
- Real-time updates
- Drag and drop
- Auto-save
```

---

## Full-Screen Image with Caption

```markdown
<!-- _class: lead -->
<!-- _backgroundImage: url('impactful-image.jpg') -->
<!-- _backgroundSize: cover -->
<!-- _color: white -->

# Memorable Caption
```

---

## Source Code with Annotations

````markdown
# Key Implementation

```python
class UserService:
    def __init__(self, db: Database):        # ← Dependency injection
        self.db = db

    async def get_user(self, id: int):       # ← Async for performance
        return await self.db.fetch_one(...)  # ← Single query
```

**Design principles:**
- DI for testability
- Async for scalability
````

---

## Tips for Advanced Layouts

1. **Test across renderers** - Marp CLI, Marp VS Code, browsers may render differently
2. **Keep it simple** - Complex layouts can be fragile
3. **Use tables sparingly** - They're powerful but can be hard to maintain
4. **Background images** - Most reliable for splits
5. **Preview frequently** - Check rendering after each slide

---

## Troubleshooting

**Issue:** Images not splitting correctly
**Fix:** Ensure `![bg left:XX%]` comes before content

**Issue:** Text overlapping images
**Fix:** Adjust percentage or use solid background with opacity

**Issue:** Tables breaking layout
**Fix:** Reduce content or split across slides

**Issue:** Code blocks too wide
**Fix:** Shorten lines or use smaller font in `<style>` section
