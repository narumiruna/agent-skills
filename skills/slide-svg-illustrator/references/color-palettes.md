# Color Palettes

Curated color schemes for different presentation contexts.

---

## Default Palette (Neutral + Blue)

**Best for**: Technical documentation, professional presentations

```
Dark:    #111827  (gray-900)
Mid:     #6B7280  (gray-500)
Light:   #E5E7EB  (gray-200)
Accent:  #2563EB  (blue-600)
Success: #10B981  (green-500)
Warning: #F59E0B  (amber-500)
Error:   #EF4444  (red-500)
```

**Usage:**
- Dark: Primary text, strokes, borders
- Mid: Secondary text, inactive elements
- Light: Backgrounds, fills
- Accent: Highlights, active states, CTAs

---

## Corporate Professional

**Best for**: Business presentations, formal reports

```
Primary:   #1E3A8A  (navy)
Secondary: #0F766E  (teal)
Neutral:   #374151  (gray-700)
Light:     #F3F4F6  (gray-100)
Accent:    #DC2626  (red-600)
```

**Example:**
```xml
<rect fill="#F3F4F6" stroke="#1E3A8A" stroke-width="4"/>
<text fill="#374151">Label</text>
```

---

## Creative & Modern

**Best for**: Marketing, creative pitches, modern products

```
Primary:   #7C3AED  (purple-600)
Secondary: #EC4899  (pink-500)
Tertiary:  #F59E0B  (amber-500)
Dark:      #1F2937  (gray-800)
Light:     #FEF3C7  (amber-100)
```

**Example:**
```xml
<linearGradient id="gradient1" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" style="stop-color:#7C3AED"/>
  <stop offset="100%" style="stop-color:#EC4899"/>
</linearGradient>
<rect fill="url(#gradient1)"/>
```

---

## Minimal Monochrome

**Best for**: Elegant, distraction-free presentations

```
Black:     #000000
DarkGray:  #404040
MidGray:   #808080
LightGray: #E0E0E0
White:     #FFFFFF
```

**Example:**
```xml
<rect fill="#FFFFFF" stroke="#000000" stroke-width="4"/>
<text fill="#404040">Subtle label</text>
```

---

## Data Visualization

**Best for**: Charts, graphs, multi-category comparisons

```
Category1: #2563EB  (blue-600)
Category2: #10B981  (green-500)
Category3: #F59E0B  (amber-500)
Category4: #EF4444  (red-500)
Category5: #8B5CF6  (purple-500)
Category6: #06B6D4  (cyan-500)
Neutral:   #6B7280  (gray-500)
```

**Usage**: Each category gets a distinct color for clarity.

---

## Academic / Scientific

**Best for**: Research presentations, educational content

```
Primary:   #1E40AF  (blue-800)
Secondary: #059669  (green-600)
Neutral:   #374151  (gray-700)
Light:     #F9FAFB  (gray-50)
Highlight: #FBBF24  (yellow-400)
```

---

## Dark Mode

**Best for**: Night presentations, developer content

```
Background: #0F172A  (slate-900)
Surface:    #1E293B  (slate-800)
Primary:    #60A5FA  (blue-400)
Secondary:  #34D399  (green-400)
Text:       #F1F5F9  (slate-100)
Muted:      #64748B  (slate-500)
```

**Example:**
```xml
<svg viewBox="0 0 1920 1080" width="1920" height="1080">
  <rect width="1920" height="1080" fill="#0F172A"/>
  <rect x="240" y="320" width="400" height="200" rx="16" fill="#1E293B" stroke="#60A5FA" stroke-width="4"/>
  <text fill="#F1F5F9">Dark mode text</text>
</svg>
```

---

## Van Gogh Starry Night

**Best for**: Artistic presentations, creative content, emotional storytelling

**Inspired by Vincent van Gogh's "The Starry Night" (1889)**

```
Night Sky:     #1e3a5f  (deep prussian blue)
Swirling Blue: #2a5f8f  (cobalt blue)
Bright Star:   #f4e5a0  (pale gold)
Moon Glow:     #fef7cd  (creamy yellow)
Cypress Tree:  #1a4d2e  (dark forest green)
Village Light: #d4a574  (warm ochre)
Accent Blue:   #4a7ba7  (cerulean)
Dark Stroke:   #0f1f2e  (midnight blue-black)
```

**Color Psychology:**
- Deep blues evoke night, tranquility, and depth
- Warm yellows/golds create contrast and hope
- Swirling patterns suggest movement and emotion
- Dark greens ground the composition

**Usage:**
```xml
<!-- Starry night background with gradient -->
<defs>
  <linearGradient id="starry-bg" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" style="stop-color:#0f1f2e;stop-opacity:1" />
    <stop offset="50%" style="stop-color:#1e3a5f;stop-opacity:1" />
    <stop offset="100%" style="stop-color:#2a5f8f;stop-opacity:1" />
  </linearGradient>
  
  <radialGradient id="star-glow" cx="50%" cy="50%" r="50%">
    <stop offset="0%" style="stop-color:#fef7cd;stop-opacity:1" />
    <stop offset="70%" style="stop-color:#f4e5a0;stop-opacity:0.6" />
    <stop offset="100%" style="stop-color:#f4e5a0;stop-opacity:0" />
  </radialGradient>
</defs>

<!-- Background -->
<rect fill="url(#starry-bg)" width="100%" height="100%"/>

<!-- Stars with glow effect -->
<circle cx="300" cy="200" r="20" fill="url(#star-glow)"/>
<circle cx="300" cy="200" r="8" fill="#fef7cd"/>

<!-- Text in village light color -->
<text fill="#d4a574" stroke="#0f1f2e" stroke-width="1">Artistic Content</text>
```

**Perfect for:**
- Creative agency presentations
- Art and design portfolios
- Emotional storytelling
- Night-themed content
- Inspirational talks

**Variations:**
- Use swirling brush-like strokes (curved paths) for authenticity
- Layer translucent blues for depth
- Add circular/spiral patterns to mimic Van Gogh's style
- Combine with textured effects for painterly feel

---

## Pastel Soft

**Best for**: Friendly, approachable content, design presentations

```
Pink:    #FBCFE8  (pink-200)
Purple:  #DDD6FE  (purple-200)
Blue:    #BFDBFE  (blue-200)
Green:   #BBF7D0  (green-200)
Yellow:  #FEF08A  (yellow-200)
Dark:    #374151  (gray-700)
```

**Example:**
```xml
<rect fill="#BFDBFE" stroke="#374151" stroke-width="3"/>
<text fill="#374151">Soft, friendly label</text>
```

---

## High Contrast

**Best for**: Accessibility, large venue presentations

```
Black:    #000000
White:    #FFFFFF
Yellow:   #FACC15  (yellow-400)
Cyan:     #22D3EE  (cyan-400)
Magenta:  #F472B6  (pink-400)
```

**Accessibility note**: Ensure text-to-background contrast ratio ≥ 7:1 for AAA compliance.

---

## Brand-Specific Template

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

---

## Gradient Examples

### Linear Gradient (Blue to Purple)

```xml
<defs>
  <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#2563EB"/>
    <stop offset="100%" stop-color="#7C3AED"/>
  </linearGradient>
</defs>
<rect fill="url(#grad1)" />
```

### Radial Gradient (Spotlight Effect)

```xml
<defs>
  <radialGradient id="grad2" cx="50%" cy="50%" r="50%">
    <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.8"/>
    <stop offset="100%" stop-color="#000000" stop-opacity="0.2"/>
  </radialGradient>
</defs>
<rect fill="url(#grad2)" />
```

---

## Semantic Color Usage

### Status Indicators

```
Success: #10B981  (green-500)
Warning: #F59E0B  (amber-500)
Error:   #EF4444  (red-500)
Info:    #3B82F6  (blue-500)
```

### Interactive States

```
Default:  #6B7280  (gray-500)
Hover:    #2563EB  (blue-600)
Active:   #1D4ED8  (blue-700)
Disabled: #D1D5DB  (gray-300)
```

---

## Color Selection Guidelines

1. **Limit palette**: 3-5 colors per diagram
2. **Sufficient contrast**: Text should be legible against background
3. **Consistent meaning**: Same color = same meaning across all slides
4. **Accessibility**: Test with color blindness simulators
5. **Cultural context**: Consider cultural color associations for international audiences

---

## Tools for Palette Generation

- **Coolors.co**: Generate harmonious palettes
- **Adobe Color**: Extract from images
- **Tailwind CSS**: Pre-defined, accessible colors
- **WCAG Contrast Checker**: Verify accessibility

---

## Quick Swaps

To change the default palette to another, replace:

```
Find:    #2563EB
Replace: #7C3AED  (for purple)

Find:    #E5E7EB
Replace: #F3F4F6  (for lighter gray)

Find:    #111827
Replace: #1F2937  (for softer black)
```
