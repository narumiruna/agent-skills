# Output Format Examples

Complete examples of expected outputs for each module.

---

## Color Design Output

### Format Structure

```markdown
## Color Strategy
[Chosen strategy + reasoning]

## Color Palette
* Background: #XXXXXX — [purpose]
* Surface: #XXXXXX — [purpose]
* Primary: #XXXXXX — [purpose]
* Secondary: #XXXXXX — [purpose]
* Accent: #XXXXXX — [purpose]
* Text Primary: #XXXXXX — [purpose]
* Text Secondary: #XXXXXX — [purpose]

## Usage Guidelines
[How to apply colors]

## Validation Checklist
- [ ] Contrast ratio >= 4.5:1
- [ ] Palette limited to 5-7 colors
- [ ] Colors work on projector
```

### Example 1: Dark Technical Palette

```markdown
## Color Strategy

**Strategy**: Dark Technical
**Reasoning**: Code-heavy presentation for developer audience, projector environment, need high contrast for code readability

## Color Palette

* Background: #1E1E1E — Main slide background (VS Code dark)
* Surface: #252526 — Code blocks, diagram containers
* Primary: #569CD6 — Titles, headings (VS Code blue)
* Secondary: #4EC9B0 — Section dividers, icons (cyan)
* Accent: #F4BF75 — Important callouts, highlights (amber)
* Text Primary: #D4D4D4 — Body text, code
* Text Secondary: #858585 — Captions, metadata

## Usage Guidelines

**Title slides**:
- Background: #1E1E1E
- Title: Primary (#569CD6)
- Subtitle: Text Secondary (#858585)

**Content slides**:
- Background: #1E1E1E
- Headings: Primary (#569CD6)
- Body text: Text Primary (#D4D4D4)
- Code blocks: Surface background (#252526)

**Diagrams**:
- Container fills: Surface (#252526)
- Borders/strokes: Secondary (#4EC9B0)
- Highlights: Accent (#F4BF75)
- Arrows: Primary (#569CD6)

## Validation Checklist

- [x] Contrast ratio Text Primary/Background = 11.25:1 (exceeds WCAG AAA)
- [x] Contrast ratio Primary/Background = 5.65:1 (meets WCAG AA, close to AAA)
- [x] Palette limited to 7 colors
- [x] Colors tested on projector (high contrast maintained)
- [x] Consistent with VS Code theme (familiar to developers)
```

### Example 2: Light Professional Palette

```markdown
## Color Strategy

**Strategy**: Light Professional
**Reasoning**: Business presentation for mixed audience (technical + management), formal setting, printed handouts

## Color Palette

* Background: #FAFAFA — Main slide background (off-white, print-friendly)
* Surface: #FFFFFF — Panels, cards
* Primary: #2E75B6 — Titles, headings (corporate blue)
* Secondary: #5B9BD5 — Subheadings (lighter blue)
* Accent: #F39C12 — Highlights, callouts (orange)
* Text Primary: #2C2C2C — Body text (near-black)
* Text Secondary: #666666 — Captions

## Usage Guidelines

**Title slides**:
- Background: #FAFAFA
- Title: Primary (#2E75B6)
- Subtitle: Text Secondary (#666666)

**Content slides**:
- Background: #FAFAFA
- Headings: Primary (#2E75B6)
- Body text: Text Primary (#2C2C2C)
- Important items: Accent (#F39C12)

**Charts/Diagrams**:
- Main elements: Primary (#2E75B6)
- Secondary elements: Secondary (#5B9BD5)
- Highlights: Accent (#F39C12)
- Backgrounds: Surface (#FFFFFF)

## Validation Checklist

- [x] Contrast ratio Text Primary/Background = 14.2:1 (exceeds WCAG AAA)
- [x] Contrast ratio Primary/Background = 5.8:1 (meets WCAG AA)
- [x] Palette limited to 7 colors
- [x] Colors work for printing and projection
- [x] Professional, conservative appearance suitable for business
```

---

## Marpit Authoring Output

### Minimal Presentation

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

### Full Presentation with Colors

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

---

## SVG Illustration Output

### Simple Diagram

```xml
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow-sm">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Background (optional) -->
  <rect width="800" height="600" fill="#FAFAFA"/>

  <!-- Service Box -->
  <rect x="100" y="200" width="250" height="200" rx="16"
        fill="#FFFFFF" stroke="#2E75B6" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="225" y="290" font-family="sans-serif" font-size="24"
        font-weight="600" fill="#2C2C2C" text-anchor="middle">
    API Service
  </text>
  <text x="225" y="320" font-family="sans-serif" font-size="16"
        fill="#666666" text-anchor="middle">
    FastAPI + PostgreSQL
  </text>

  <!-- Arrow -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10"
            refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#2E75B6"/>
    </marker>
  </defs>
  <line x1="350" y1="300" x2="450" y2="300"
        stroke="#2E75B6" stroke-width="3" marker-end="url(#arrowhead)"/>

  <!-- Database -->
  <ellipse cx="550" cy="300" rx="100" ry="80"
           fill="#F0F9FF" stroke="#2E75B6" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="550" y="310" font-family="sans-serif" font-size="24"
        font-weight="600" fill="#2C2C2C" text-anchor="middle">
    Database
  </text>
</svg>
```

### Architecture Diagram with Multiple Services

```xml
<svg viewBox="0 0 1200 675" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow-sm">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
    <marker id="arrowhead" markerWidth="10" markerHeight="10"
            refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#2E75B6"/>
    </marker>
  </defs>

  <!-- Frontend Service -->
  <rect x="100" y="250" width="280" height="180" rx="16"
        fill="#E0F2FE" stroke="#2E75B6" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="240" y="330" font-family="sans-serif" font-size="24"
        font-weight="600" fill="#2C2C2C" text-anchor="middle">
    Frontend
  </text>
  <text x="240" y="360" font-family="sans-serif" font-size="16"
        fill="#666666" text-anchor="middle">
    React + TypeScript
  </text>

  <!-- Arrow to API Gateway -->
  <line x1="380" y1="340" x2="480" y2="340"
        stroke="#2E75B6" stroke-width="3" marker-end="url(#arrowhead)"/>
  <text x="430" y="330" font-family="sans-serif" font-size="14"
        fill="#666666" text-anchor="middle">
    HTTPS
  </text>

  <!-- API Gateway -->
  <rect x="480" y="250" width="280" height="180" rx="16"
        fill="#E0F2FE" stroke="#2E75B6" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="620" y="330" font-family="sans-serif" font-size="24"
        font-weight="600" fill="#2C2C2C" text-anchor="middle">
    API Gateway
  </text>
  <text x="620" y="360" font-family="sans-serif" font-size="16"
        fill="#666666" text-anchor="middle">
    FastAPI
  </text>

  <!-- Arrow to Database -->
  <line x1="760" y1="340" x2="860" y2="340"
        stroke="#2E75B6" stroke-width="3" marker-end="url(#arrowhead)"/>
  <text x="810" y="330" font-family="sans-serif" font-size="14"
        fill="#666666" text-anchor="middle">
    SQL
  </text>

  <!-- Database -->
  <ellipse cx="980" cy="340" rx="100" ry="80"
           fill="#DBEAFE" stroke="#2E75B6" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="980" y="350" font-family="sans-serif" font-size="24"
        font-weight="600" fill="#2C2C2C" text-anchor="middle">
    PostgreSQL
  </text>

  <!-- Cache (below) -->
  <rect x="480" y="480" width="150" height="100" rx="12"
        fill="#FEF3C7" stroke="#F39C12" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="555" y="540" font-family="sans-serif" font-size="18"
        font-weight="600" fill="#2C2C2C" text-anchor="middle">
    Redis Cache
  </text>

  <!-- Arrow from Gateway to Cache -->
  <line x1="580" y1="430" x2="555" y2="480"
        stroke="#F39C12" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#arrowhead)"/>
</svg>
```

### Flowchart Example

```xml
<svg viewBox="0 0 1000 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow-sm">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
    <marker id="arrowhead" markerWidth="10" markerHeight="10"
            refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#2E75B6"/>
    </marker>
  </defs>

  <!-- Start -->
  <ellipse cx="500" cy="80" rx="80" ry="40"
           fill="#10B981" stroke="#059669" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="500" y="88" font-family="sans-serif" font-size="18"
        font-weight="600" fill="#FFFFFF" text-anchor="middle">
    Start
  </text>

  <!-- Arrow down -->
  <line x1="500" y1="120" x2="500" y2="170"
        stroke="#2E75B6" stroke-width="3" marker-end="url(#arrowhead)"/>

  <!-- Decision -->
  <path d="M 500 170 L 650 240 L 500 310 L 350 240 Z"
        fill="#FEF3C7" stroke="#F39C12" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="500" y="235" font-family="sans-serif" font-size="16"
        font-weight="600" fill="#2C2C2C" text-anchor="middle">
    Valid input?
  </text>
  <text x="500" y="255" font-family="sans-serif" font-size="14"
        fill="#666666" text-anchor="middle">
    (check data)
  </text>

  <!-- Yes path -->
  <line x1="650" y1="240" x2="750" y2="240"
        stroke="#2E75B6" stroke-width="3" marker-end="url(#arrowhead)"/>
  <text x="700" y="230" font-family="sans-serif" font-size="14"
        fill="#059669" text-anchor="middle">
    Yes
  </text>

  <!-- Process -->
  <rect x="750" y="200" width="180" height="80" rx="12"
        fill="#E0F2FE" stroke="#2E75B6" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="840" y="245" font-family="sans-serif" font-size="16"
        font-weight="600" fill="#2C2C2C" text-anchor="middle">
    Process Data
  </text>

  <!-- No path -->
  <line x1="350" y1="240" x2="250" y2="240"
        stroke="#2E75B6" stroke-width="3" marker-end="url(#arrowhead)"/>
  <text x="300" y="230" font-family="sans-serif" font-size="14"
        fill="#EF4444" text-anchor="middle">
    No
  </text>

  <!-- Error -->
  <rect x="70" y="200" width="180" height="80" rx="12"
        fill="#FEE2E2" stroke="#EF4444" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="160" y="245" font-family="sans-serif" font-size="16"
        font-weight="600" fill="#2C2C2C" text-anchor="middle">
    Show Error
  </text>

  <!-- End -->
  <ellipse cx="500" cy="480" rx="80" ry="40"
           fill="#EF4444" stroke="#DC2626" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="500" y="488" font-family="sans-serif" font-size="18"
        font-weight="600" fill="#FFFFFF" text-anchor="middle">
    End
  </text>

  <!-- Arrows to end -->
  <line x1="840" y1="280" x2="840" y2="450" x3="520" y3="480"
        stroke="#2E75B6" stroke-width="3" marker-end="url(#arrowhead)"/>
  <path d="M 840 280 L 840 450 L 520 480"
        stroke="#2E75B6" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>
  <path d="M 160 280 L 160 450 L 480 480"
        stroke="#2E75B6" stroke-width="3" fill="none" marker-end="url(#arrowhead)"/>
</svg>
```

---

## See Also

- [SKILL.md](../SKILL.md) - Return to main skill guide
- [color-design/workflow.md](color-design/workflow.md) - Color design process
- [color-design/output-template.md](color-design/output-template.md) - Detailed color output template
- [marpit-authoring/patterns.md](marpit-authoring/patterns.md) - Common slide patterns
- [svg-illustration/pattern-examples.md](svg-illustration/pattern-examples.md) - More SVG examples
