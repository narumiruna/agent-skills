# Color Palettes Reference

Comprehensive color palette reference for both complete slide design systems and quick SVG illustration colors.

---

## Part 1: Complete Palette Systems

These palettes define full 7-role color systems for comprehensive slide design. Each palette includes Background, Surface, Primary, Secondary, Accent, Text Primary, and Text Secondary with contrast validation.

### Available Palettes

Use the palette generation script to browse and retrieve palette details:

**List all available palettes:**
```bash
uv run scripts/generate_palette.py list
```

**Show details for a specific palette:**
```bash
uv run scripts/generate_palette.py show <palette-name>
```

**Examples:**
```bash
# List all palettes grouped by category
uv run scripts/generate_palette.py list

# Show Code-Focused Blue palette
uv run scripts/generate_palette.py show code-blue

# Show Modern Minimal palette
uv run scripts/generate_palette.py show modern-minimal

# Show Data Visualization palette
uv run scripts/generate_palette.py show data-viz
```

### Palette Categories

**Dark Technical:**
- `code-blue` - Code-Focused Blue
- `terminal-dark` - Terminal Dark
- `midnight-professional` - Midnight Professional

**Light Professional:**
- `clean-corporate` - Clean Corporate
- `modern-minimal` - Modern Minimal
- `warm-professional` - Warm Professional

**Accent-Driven:**
- `minimal-teal` - Minimal with Teal Focus
- `grayscale-red` - Gray Scale with Red Accent

**Specialized:**
- `data-viz` - Data Visualization (Categorical)
- `accessibility` - Accessibility First (High Contrast)

### Choosing a Palette

1. **Start with context:** Dark Technical for code/diagrams, Light Professional for business, Accent-Driven for storytelling
2. **Consider environment:** Projectors benefit from higher contrast (Terminal Dark, Clean Corporate)
3. **Match brand if applicable:** Adapt palette colors to incorporate brand colors while maintaining structure
4. **Test contrast:** Verify text remains legible in the actual presentation environment

### Custom Palettes

**Generate from brand color:**
```bash
# Generate light theme from brand color
uv run scripts/generate_palette.py brand "#2E75B6" light

# Generate dark theme from brand color
uv run scripts/generate_palette.py brand "#569CD6" dark
```

---

## Part 2: SVG Quick Reference

Quick color schemes with SVG code examples for rapid illustration creation.

### Available SVG Palettes

Use the palette generation script to browse and retrieve SVG palette details:

**List all available SVG palettes:**
```bash
uv run scripts/generate_palette.py svg-list
```

**Show details for a specific SVG palette:**
```bash
uv run scripts/generate_palette.py svg-show <palette-name>
```

**Examples:**
```bash
# List all SVG palettes
uv run scripts/generate_palette.py svg-list

# Show Default palette
uv run scripts/generate_palette.py svg-show default

# Show Creative & Modern palette
uv run scripts/generate_palette.py svg-show creative

# Show Dark Mode palette
uv run scripts/generate_palette.py svg-show dark-mode
```

### SVG Palette List

- `default` - Default Palette (Neutral + Blue)
- `corporate` - Corporate Professional
- `creative` - Creative & Modern
- `monochrome` - Minimal Monochrome
- `data-viz` - Data Visualization
- `academic` - Academic / Scientific
- `dark-mode` - Dark Mode
- `pastel` - Pastel Soft
- `high-contrast` - High Contrast

### Common SVG Patterns

**Brand-Specific Template:**

When working with brand colors, define them consistently:

```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .brand-primary { fill: #CUSTOM1; }
      .brand-secondary { fill: #CUSTOM2; }
      .brand-accent { fill: #CUSTOM3; }
      .brand-text { fill: #CUSTOM4; }
    </style>
  </defs>

  <rect class="brand-primary" ... />
  <text class="brand-text" ... />
</svg>
```

**Gradient Examples:**

Linear Gradient (Blue to Purple):
```xml
<defs>
  <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#2563EB"/>
    <stop offset="100%" stop-color="#7C3AED"/>
  </linearGradient>
</defs>
<rect fill="url(#grad1)" />
```

Radial Gradient (Spotlight Effect):
```xml
<defs>
  <radialGradient id="grad2" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#000000" stop-opacity="0.2"/>
  </radialGradient>
</defs>
<rect fill="url(#grad2)" />
```

**Semantic Color Usage:**

Status Indicators:
```
Success: #10B981  (green-500)
Warning: #F59E0B  (amber-500)
Error:   #EF4444  (red-500)
Info:    #3B82F6  (blue-500)
```

Interactive States:
```
Default:  #6B7280  (gray-500)
Hover:    #2563EB  (blue-600)
Active:   #1D4ED8  (blue-700)
Disabled: #D1D5DB  (gray-300)
```

---

## Universal Guidelines

### Color Selection

1. **Limit palette:** 3-5 colors per diagram, 5-7 for complete slide system
2. **Sufficient contrast:** Text should be legible against background (≥4.5:1 AA, ≥7:1 AAA)
3. **Consistent meaning:** Same color = same meaning across all slides
4. **Accessibility:** Test with color blindness simulators
5. **Cultural context:** Consider cultural color associations for international audiences

### Tools for Palette Generation

- **Coolors.co:** Generate harmonious palettes
- **Adobe Color:** Extract from images
- **Tailwind CSS:** Pre-defined, accessible colors
- **WCAG Contrast Checker:** Verify accessibility

### Quick Color Swaps

To change the default palette to another:

```
Find:    #2563EB
Replace: #7C3AED  (for purple)

Find:    #E5E7EB
Replace: #F3F4F6  (for lighter gray)

Find:    #111827
Replace: #1F2937  (for softer black)
```
