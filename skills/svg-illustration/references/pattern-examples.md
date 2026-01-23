# Pattern Examples

## Table of Contents

- [Process Flow (5 Steps)](#process-flow-5-steps)
- [Timeline (4 Milestones)](#timeline-4-milestones)
- [Architecture Diagram (3-Tier)](#architecture-diagram-3-tier)
- [Comparison (3 Columns)](#comparison-3-columns)
- [KPI Dashboard](#kpi-dashboard)
- [Icon Set (6 Icons)](#icon-set-6-icons)
- [Tips for Adapting Patterns](#tips-for-adapting-patterns)

Complete SVG examples for common slide diagram types.

---

## Process Flow (5 Steps)

**Use case**: Sequential process, workflow, pipeline

```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <title>5-Step Process Flow</title>
  <desc>Horizontal process flow with 5 sequential steps</desc>

  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#111827" />
    </marker>
  </defs>

  <g id="main">
    <!-- Step 1 -->
    <rect x="120" y="440" width="240" height="200" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="240" y="520" font-family="system-ui" font-size="24" text-anchor="middle" font-weight="bold" fill="#111827">Step 1</text>
    <text x="240" y="560" font-family="system-ui" font-size="18" text-anchor="middle" fill="#6B7280">Prepare</text>

    <!-- Arrow 1 -->
    <line x1="360" y1="540" x2="440" y2="540" stroke="#111827" stroke-width="4" marker-end="url(#arrowhead)"/>

    <!-- Step 2 -->
    <rect x="440" y="440" width="240" height="200" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="560" y="520" font-family="system-ui" font-size="24" text-anchor="middle" font-weight="bold" fill="#111827">Step 2</text>
    <text x="560" y="560" font-family="system-ui" font-size="18" text-anchor="middle" fill="#6B7280">Process</text>

    <!-- Arrow 2 -->
    <line x1="680" y1="540" x2="760" y2="540" stroke="#111827" stroke-width="4" marker-end="url(#arrowhead)"/>

    <!-- Step 3 -->
    <rect x="760" y="440" width="240" height="200" rx="16" fill="#2563EB" stroke="#111827" stroke-width="4"/>
    <text x="880" y="520" font-family="system-ui" font-size="24" text-anchor="middle" font-weight="bold" fill="white">Step 3</text>
    <text x="880" y="560" font-family="system-ui" font-size="18" text-anchor="middle" fill="white">Execute</text>

    <!-- Arrow 3 -->
    <line x1="1000" y1="540" x2="1080" y2="540" stroke="#111827" stroke-width="4" marker-end="url(#arrowhead)"/>

    <!-- Step 4 -->
    <rect x="1080" y="440" width="240" height="200" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="1200" y="520" font-family="system-ui" font-size="24" text-anchor="middle" font-weight="bold" fill="#111827">Step 4</text>
    <text x="1200" y="560" font-family="system-ui" font-size="18" text-anchor="middle" fill="#6B7280">Verify</text>

    <!-- Arrow 4 -->
    <line x1="1320" y1="540" x2="1400" y2="540" stroke="#111827" stroke-width="4" marker-end="url(#arrowhead)"/>

    <!-- Step 5 -->
    <rect x="1400" y="440" width="240" height="200" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="1520" y="520" font-family="system-ui" font-size="24" text-anchor="middle" font-weight="bold" fill="#111827">Step 5</text>
    <text x="1520" y="560" font-family="system-ui" font-size="18" text-anchor="middle" fill="#6B7280">Deploy</text>
  </g>
</svg>
```

**Embed in Marp:**
```markdown
![w:1400](assets/process-flow.svg)
```

---

## Timeline (4 Milestones)

**Use case**: Project roadmap, historical events, release schedule

```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <title>Project Timeline</title>
  <desc>Horizontal timeline with 4 major milestones</desc>

  <g id="main">
    <!-- Baseline -->
    <line x1="240" y1="540" x2="1680" y2="540" stroke="#6B7280" stroke-width="4"/>

    <!-- Milestone 1 -->
    <circle cx="400" cy="540" r="24" fill="#2563EB" stroke="#111827" stroke-width="4"/>
    <text x="400" y="480" font-family="system-ui" font-size="20" text-anchor="middle" font-weight="bold" fill="#111827">Q1 2024</text>
    <text x="400" y="620" font-family="system-ui" font-size="18" text-anchor="middle" fill="#6B7280">Planning</text>

    <!-- Milestone 2 -->
    <circle cx="720" cy="540" r="24" fill="#2563EB" stroke="#111827" stroke-width="4"/>
    <text x="720" y="480" font-family="system-ui" font-size="20" text-anchor="middle" font-weight="bold" fill="#111827">Q2 2024</text>
    <text x="720" y="620" font-family="system-ui" font-size="18" text-anchor="middle" fill="#6B7280">Development</text>

    <!-- Milestone 3 -->
    <circle cx="1040" cy="540" r="24" fill="#2563EB" stroke="#111827" stroke-width="4"/>
    <text x="1040" y="480" font-family="system-ui" font-size="20" text-anchor="middle" font-weight="bold" fill="#111827">Q3 2024</text>
    <text x="1040" y="620" font-family="system-ui" font-size="18" text-anchor="middle" fill="#6B7280">Testing</text>

    <!-- Milestone 4 -->
    <circle cx="1360" cy="540" r="24" fill="#2563EB" stroke="#111827" stroke-width="4"/>
    <text x="1360" y="480" font-family="system-ui" font-size="20" text-anchor="middle" font-weight="bold" fill="#111827">Q4 2024</text>
    <text x="1360" y="620" font-family="system-ui" font-size="18" text-anchor="middle" fill="#6B7280">Launch</text>
  </g>
</svg>
```

**Embed in Marp:**
```markdown
![w:1200](assets/timeline.svg)
```

---

## Architecture Diagram (3-Tier)

**Use case**: System architecture, layered design, stack overview

```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <title>3-Tier Architecture</title>
  <desc>Three-layer architecture diagram with components</desc>

  <g id="main">
    <!-- Layer 1: Presentation -->
    <rect x="240" y="200" width="1440" height="200" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="960" y="260" font-family="system-ui" font-size="28" text-anchor="middle" font-weight="bold" fill="#111827">Presentation Layer</text>

    <!-- Components -->
    <rect x="360" y="300" width="280" height="80" rx="8" fill="white" stroke="#2563EB" stroke-width="4"/>
    <text x="500" y="350" font-family="system-ui" font-size="20" text-anchor="middle" fill="#111827">React UI</text>

    <rect x="700" y="300" width="280" height="80" rx="8" fill="white" stroke="#2563EB" stroke-width="4"/>
    <text x="840" y="350" font-family="system-ui" font-size="20" text-anchor="middle" fill="#111827">Mobile App</text>

    <rect x="1040" y="300" width="280" height="80" rx="8" fill="white" stroke="#2563EB" stroke-width="4"/>
    <text x="1180" y="350" font-family="system-ui" font-size="20" text-anchor="middle" fill="#111827">Admin Panel</text>

    <!-- Layer 2: Business Logic -->
    <rect x="240" y="440" width="1440" height="200" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="960" y="500" font-family="system-ui" font-size="28" text-anchor="middle" font-weight="bold" fill="#111827">Business Logic Layer</text>

    <!-- Components -->
    <rect x="480" y="540" width="280" height="80" rx="8" fill="white" stroke="#2563EB" stroke-width="4"/>
    <text x="620" y="590" font-family="system-ui" font-size="20" text-anchor="middle" fill="#111827">API Gateway</text>

    <rect x="820" y="540" width="280" height="80" rx="8" fill="white" stroke="#2563EB" stroke-width="4"/>
    <text x="960" y="590" font-family="system-ui" font-size="20" text-anchor="middle" fill="#111827">Services</text>

    <!-- Layer 3: Data -->
    <rect x="240" y="680" width="1440" height="200" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="960" y="740" font-family="system-ui" font-size="28" text-anchor="middle" font-weight="bold" fill="#111827">Data Layer</text>

    <!-- Components -->
    <rect x="480" y="780" width="280" height="80" rx="8" fill="white" stroke="#2563EB" stroke-width="4"/>
    <text x="620" y="830" font-family="system-ui" font-size="20" text-anchor="middle" fill="#111827">PostgreSQL</text>

    <rect x="820" y="780" width="280" height="80" rx="8" fill="white" stroke="#2563EB" stroke-width="4"/>
    <text x="960" y="830" font-family="system-ui" font-size="20" text-anchor="middle" fill="#111827">Redis Cache</text>
  </g>
</svg>
```

**Embed in Marp:**
```markdown
![w:1400](assets/architecture.svg)
```

---

## Comparison (3 Columns)

**Use case**: Feature comparison, pros/cons, options evaluation

```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <title>3-Option Comparison</title>
  <desc>Side-by-side comparison of three options</desc>

  <g id="main">
    <!-- Column 1 -->
    <rect x="200" y="280" width="440" height="520" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="420" y="360" font-family="system-ui" font-size="32" text-anchor="middle" font-weight="bold" fill="#111827">Option A</text>

    <!-- Icon placeholder -->
    <circle cx="420" cy="460" r="40" fill="#2563EB" stroke="#111827" stroke-width="4"/>

    <!-- Features -->
    <text x="240" y="560" font-family="system-ui" font-size="20" fill="#111827">✓ Fast</text>
    <text x="240" y="600" font-family="system-ui" font-size="20" fill="#111827">✓ Simple</text>
    <text x="240" y="640" font-family="system-ui" font-size="20" fill="#6B7280">✗ Limited scale</text>

    <!-- Column 2 -->
    <rect x="680" y="280" width="440" height="520" rx="16" fill="#2563EB" stroke="#111827" stroke-width="4"/>
    <text x="900" y="360" font-family="system-ui" font-size="32" text-anchor="middle" font-weight="bold" fill="white">Option B</text>

    <!-- Icon placeholder -->
    <circle cx="900" cy="460" r="40" fill="white" stroke="#111827" stroke-width="4"/>

    <!-- Features -->
    <text x="720" y="560" font-family="system-ui" font-size="20" fill="white">✓ Balanced</text>
    <text x="720" y="600" font-family="system-ui" font-size="20" fill="white">✓ Scalable</text>
    <text x="720" y="640" font-family="system-ui" font-size="20" fill="white">✓ Reliable</text>

    <!-- Recommended badge -->
    <rect x="820" y="720" width="160" height="40" rx="20" fill="white"/>
    <text x="900" y="748" font-family="system-ui" font-size="18" text-anchor="middle" font-weight="bold" fill="#2563EB">Recommended</text>

    <!-- Column 3 -->
    <rect x="1160" y="280" width="440" height="520" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="1380" y="360" font-family="system-ui" font-size="32" text-anchor="middle" font-weight="bold" fill="#111827">Option C</text>

    <!-- Icon placeholder -->
    <circle cx="1380" cy="460" r="40" fill="#2563EB" stroke="#111827" stroke-width="4"/>

    <!-- Features -->
    <text x="1200" y="560" font-family="system-ui" font-size="20" fill="#111827">✓ Enterprise</text>
    <text x="1200" y="600" font-family="system-ui" font-size="20" fill="#111827">✓ Full features</text>
    <text x="1200" y="640" font-family="system-ui" font-size="20" fill="#6B7280">✗ Complex</text>
  </g>
</svg>
```

**Embed in Marp:**
```markdown
![w:1400](assets/comparison.svg)
```

---

## KPI Dashboard

**Use case**: Metrics, statistics, data visualization

```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <title>KPI Dashboard</title>
  <desc>Key performance indicators with trend lines</desc>

  <g id="main">
    <!-- KPI 1 -->
    <rect x="240" y="320" width="400" height="240" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="440" y="420" font-family="system-ui" font-size="72" text-anchor="middle" font-weight="bold" fill="#2563EB">1.2M</text>
    <text x="440" y="470" font-family="system-ui" font-size="24" text-anchor="middle" fill="#6B7280">Active Users</text>
    <text x="440" y="520" font-family="system-ui" font-size="20" text-anchor="middle" fill="#10B981">↑ 15%</text>

    <!-- KPI 2 -->
    <rect x="680" y="320" width="400" height="240" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="880" y="420" font-family="system-ui" font-size="72" text-anchor="middle" font-weight="bold" fill="#2563EB">$4.5M</text>
    <text x="880" y="470" font-family="system-ui" font-size="24" text-anchor="middle" fill="#6B7280">Revenue</text>
    <text x="880" y="520" font-family="system-ui" font-size="20" text-anchor="middle" fill="#10B981">↑ 22%</text>

    <!-- KPI 3 -->
    <rect x="1120" y="320" width="400" height="240" rx="16" fill="#E5E7EB" stroke="#111827" stroke-width="4"/>
    <text x="1320" y="420" font-family="system-ui" font-size="72" text-anchor="middle" font-weight="bold" fill="#2563EB">98.5%</text>
    <text x="1320" y="470" font-family="system-ui" font-size="24" text-anchor="middle" fill="#6B7280">Uptime</text>
    <text x="1320" y="520" font-family="system-ui" font-size="20" text-anchor="middle" fill="#10B981">↑ 0.3%</text>

    <!-- Simple sparkline for KPI 1 -->
    <polyline points="280,500 320,480 360,490 400,470 440,460 480,450 520,440 560,430 600,420"
              fill="none" stroke="#2563EB" stroke-width="3"/>
  </g>
</svg>
```

**Embed in Marp:**
```markdown
![w:1200](assets/kpi-dashboard.svg)
```

---

## Icon Set (6 Icons)

**Use case**: Consistent iconography for feature lists, navigation

```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080" xmlns="http://www.w3.org/2000/svg">
  <title>Icon Set</title>
  <desc>6 consistent outline icons</desc>

  <g id="main" stroke="#111827" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <!-- Icon 1: Settings -->
    <g transform="translate(280, 440)">
      <circle cx="60" cy="60" r="40"/>
      <circle cx="60" cy="60" r="20" fill="#E5E7EB"/>
      <line x1="60" y1="0" x2="60" y2="20"/>
      <line x1="60" y1="100" x2="60" y2="120"/>
      <line x1="0" y1="60" x2="20" y2="60"/>
      <line x1="100" y1="60" x2="120" y2="60"/>
    </g>

    <!-- Icon 2: Users -->
    <g transform="translate(540, 440)">
      <circle cx="60" cy="40" r="24"/>
      <path d="M 20 100 Q 20 60, 60 60 Q 100 60, 100 100" fill="#E5E7EB" stroke="#111827"/>
    </g>

    <!-- Icon 3: Chart -->
    <g transform="translate(800, 440)">
      <rect x="20" y="80" width="20" height="40" fill="#E5E7EB"/>
      <rect x="50" y="60" width="20" height="60" fill="#E5E7EB"/>
      <rect x="80" y="40" width="20" height="80" fill="#E5E7EB"/>
    </g>

    <!-- Icon 4: Lock -->
    <g transform="translate(1060, 440)">
      <rect x="30" y="60" width="60" height="60" rx="8" fill="#E5E7EB"/>
      <path d="M 40 60 L 40 40 A 20 20 0 0 1 80 40 L 80 60"/>
      <circle cx="60" cy="85" r="8" fill="#111827"/>
    </g>

    <!-- Icon 5: Lightning -->
    <g transform="translate(1320, 440)">
      <path d="M 70 20 L 40 70 L 60 70 L 50 120 L 90 60 L 70 60 Z" fill="#2563EB"/>
    </g>

    <!-- Icon 6: Check -->
    <g transform="translate(1580, 440)">
      <circle cx="60" cy="60" r="40" fill="#10B981" stroke="#111827"/>
      <polyline points="40,60 55,75 80,45" stroke="white" stroke-width="6"/>
    </g>
  </g>
</svg>
```

**Embed in Marp:**
```markdown
![w:1200](assets/icons.svg)
```

---

## Tips for Adapting Patterns

1. **Spacing**: Use multiples of 8px for all gaps and margins
2. **Colors**: Swap accent color `#2563EB` to match your theme
3. **Text size**: Scale font sizes proportionally if changing canvas size
4. **Stroke width**: Keep at 4px for 1920×1080, scale proportionally for other sizes
5. **Safe area**: Keep all content 120px from edges
