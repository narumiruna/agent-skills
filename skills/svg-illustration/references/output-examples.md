# SVG Illustration Output Examples

Complete examples of expected outputs for SVG diagrams.

## Simple Diagram

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

## Architecture Diagram with Multiple Services

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

## Flowchart Example

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

## See Also

- `index.md` - Reference navigation hub
- `pattern-examples.md` - More SVG examples
