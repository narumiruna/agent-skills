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

# Custom Palette Example
Professional light theme with corporate colors

Business Presentation · 2026-01-09

---

## Color Palette Applied

This presentation uses the **Light Professional** strategy:

* Background: `#FAFAFA` — Main slide background
* Surface: `#FFFFFF` — Panels and cards
* Primary: `#2E75B6` — Titles and headings
* Secondary: `#5B9BD5` — Subheadings
* Accent: `#F39C12` — Highlights and callouts
* Text Primary: `#2C2C2C` — Body text
* Text Secondary: `#666666` — Captions

Generated using: `uv run skills/slide-color-design/scripts/generate_palette.py show clean-corporate`

---

## Content Slide

<div style="background: #FFFFFF; padding: 32px; border-radius: 8px; border-left: 4px solid #2E75B6;">

### Key Insight

Body text uses **Text Primary** (`#2C2C2C`) on **Surface** (`#FFFFFF`).

Important callouts use <span style="color: #F39C12; font-weight: bold;">Accent</span> (`#F39C12`).

Metadata uses <span style="color: #666666;">Text Secondary</span> (`#666666`).

</div>

---

## Visual Hierarchy

# Primary Heading
Uses Primary color (`#2E75B6`)

## Secondary Heading
Uses Secondary color (`#5B9BD5`)

### Body Text
Uses Text Primary (`#2C2C2C`)

<span style="color: #F39C12; font-weight: bold;">⚠ Important Callout</span>
Uses Accent (`#F39C12`)

---

## Diagram with Palette

<svg viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg">
  <!-- Background panel -->
  <rect x="50" y="50" width="400" height="200" fill="#FFFFFF" stroke="#2E75B6" stroke-width="2" rx="8"/>

  <!-- Left box -->
  <rect x="80" y="90" width="140" height="80" fill="#5B9BD5" rx="4"/>
  <text x="150" y="135" font-size="16" fill="#FFFFFF" text-anchor="middle" font-weight="bold">Input</text>

  <!-- Arrow -->
  <path d="M 230 130 L 280 130" stroke="#2E75B6" stroke-width="3" marker-end="url(#arrow)"/>

  <!-- Right box -->
  <rect x="290" y="90" width="140" height="80" fill="#F39C12" rx="4"/>
  <text x="360" y="135" font-size="16" fill="#FFFFFF" text-anchor="middle" font-weight="bold">Output</text>

  <!-- Caption -->
  <text x="250" y="240" font-size="14" fill="#666666" text-anchor="middle">Process Flow</text>

  <!-- Arrow marker -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#2E75B6"/>
    </marker>
  </defs>
</svg>

Notice: Diagram uses palette colors consistently

---

<!-- _class: lead -->
<!-- _backgroundColor: #2E75B6 -->
<!-- _color: #FFFFFF -->

# Consistency is Key

One palette, applied everywhere:
slides + code + diagrams

---
