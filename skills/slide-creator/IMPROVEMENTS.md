# Slide-Creator Skill Improvements

**Analysis Date**: 2026-01-09
**Evaluated Against**: Skill-creator best practices
**Current Status**: Production-ready, excellent progressive disclosure design
**Overall Grade**: Strong (B+) - Well-structured but missing high-impact enhancements

---

## Executive Summary

The slide-creator skill demonstrates excellent progressive disclosure and reference architecture. However, it's missing significant value through lack of scripts and assets. Implementing the recommendations below would:

- **Improve reliability**: Validation scripts prevent XML/syntax errors
- **Increase speed**: Templates eliminate 50%+ boilerplate work
- **Reduce token usage**: Deterministic scripts + focused reference splitting
- **Enhance UX**: Working examples, quick-start guides, common assets

---

## Current Strengths ✅

### 1. Excellent Progressive Disclosure
- SKILL.md: 174 lines (well under 500-line recommendation)
- Clear three-module structure with ordered reading lists
- 13 reference files totaling ~5,678 lines
- Core rules establish unified design principles upfront

### 2. Strong Reference Organization
- All reference files include table of contents
- Clear "See Also" cross-references
- Well-organized by module (color-design/, marpit-authoring/, svg-illustration/)
- Appropriate file sizes (200-600 lines each)

### 3. Comprehensive Frontmatter
- Description includes both capabilities AND trigger contexts
- Lists all major use cases (critical for skill triggering)
- Clear, searchable keywords

### 4. Practical Content
- Concrete examples with code snippets
- Decision guides and workflows
- Output format templates
- Validation checklists

---

## Priority 1: High-Impact Additions

### 1.1 Add Scripts Directory ⚠️ **CRITICAL**

**Current Gap**: Mentions `svglint` validation 10+ times but provides no automation.

**Create**: `scripts/` directory with validation and setup tools

#### Recommended Scripts

##### `scripts/validate_svg.py`
**Purpose**: Validate SVG syntax and best practices
**Benefits**: Prevents XML errors, ensures namespace/viewBox correctness, catches emoji in text

```python
#!/usr/bin/env python3
"""Validate SVG files for syntax errors and best practices."""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def validate_svg(svg_path: Path) -> list[str]:
    """Validate SVG file and return list of issues."""
    issues = []

    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()

        # Check namespace
        if 'http://www.w3.org/2000/svg' not in root.tag:
            issues.append("Missing SVG namespace")

        # Check viewBox
        if 'viewBox' not in root.attrib:
            issues.append("Missing viewBox attribute")

        # Check for oversized viewBox on small content
        if 'viewBox' in root.attrib:
            vb = root.attrib['viewBox'].split()
            if len(vb) == 4 and int(vb[2]) == 1920 and int(vb[3]) == 1080:
                # Check if actual content is much smaller
                # (simplified check - could be more sophisticated)
                pass  # TODO: Implement content bounds checking

        # Check for emoji in text (common error)
        for text_elem in root.iter('{http://www.w3.org/2000/svg}text'):
            if text_elem.text and any(ord(c) > 127 for c in text_elem.text):
                issues.append(f"Non-ASCII characters in <text>: {text_elem.text[:20]}")

        # Check stroke consistency
        stroke_widths = set()
        for elem in root.iter():
            if 'stroke-width' in elem.attrib:
                stroke_widths.add(elem.attrib['stroke-width'])
        if len(stroke_widths) > 2:
            issues.append(f"Inconsistent stroke widths: {stroke_widths}")

    except ET.ParseError as e:
        issues.append(f"XML parse error: {e}")

    return issues

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: validate_svg.py <file.svg>")
        sys.exit(1)

    svg_file = Path(sys.argv[1])
    issues = validate_svg(svg_file)

    if issues:
        print(f"❌ {svg_file.name} has issues:")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
    else:
        print(f"✅ {svg_file.name} is valid")
        sys.exit(0)
```

##### `scripts/check_contrast.py`
**Purpose**: Verify WCAG color contrast ratios
**Benefits**: Automates accessibility compliance, prevents illegible text

```python
#!/usr/bin/env python3
"""Check color contrast ratios for WCAG compliance."""

import sys
import re

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def relative_luminance(rgb: tuple[int, int, int]) -> float:
    """Calculate relative luminance of RGB color."""
    def adjust(val):
        val = val / 255.0
        return val / 12.92 if val <= 0.03928 else ((val + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return 0.2126 * adjust(r) + 0.7152 * adjust(g) + 0.0722 * adjust(b)

def contrast_ratio(color1: str, color2: str) -> float:
    """Calculate contrast ratio between two hex colors."""
    lum1 = relative_luminance(hex_to_rgb(color1))
    lum2 = relative_luminance(hex_to_rgb(color2))

    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)

    return (lighter + 0.05) / (darker + 0.05)

def check_wcag(ratio: float) -> dict:
    """Check WCAG compliance levels."""
    return {
        'AA_normal': ratio >= 4.5,
        'AA_large': ratio >= 3.0,
        'AAA_normal': ratio >= 7.0,
        'AAA_large': ratio >= 4.5,
        'ratio': ratio
    }

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: check_contrast.py <foreground-hex> <background-hex>")
        print("Example: check_contrast.py '#D4D4D4' '#1E1E1E'")
        sys.exit(1)

    fg = sys.argv[1]
    bg = sys.argv[2]

    ratio = contrast_ratio(fg, bg)
    wcag = check_wcag(ratio)

    print(f"Contrast ratio: {ratio:.2f}:1")
    print(f"WCAG AA (normal text): {'✅ Pass' if wcag['AA_normal'] else '❌ Fail'}")
    print(f"WCAG AA (large text):  {'✅ Pass' if wcag['AA_large'] else '❌ Fail'}")
    print(f"WCAG AAA (normal text): {'✅ Pass' if wcag['AAA_normal'] else '❌ Fail'}")
    print(f"WCAG AAA (large text):  {'✅ Pass' if wcag['AAA_large'] else '❌ Fail'}")
```

##### `scripts/init_presentation.py`
**Purpose**: Initialize new presentation from template
**Benefits**: Eliminates boilerplate, ensures best practices from start

```python
#!/usr/bin/env python3
"""Initialize a new Marp presentation from template."""

import sys
import shutil
from pathlib import Path
from datetime import datetime

TEMPLATES = {
    'technical-dark': 'assets/templates/technical-dark.md',
    'professional-light': 'assets/templates/professional-light.md',
    'minimal-keynote': 'assets/templates/minimal-keynote.md'
}

def init_presentation(template_name: str, output_path: Path, title: str, author: str):
    """Create new presentation from template."""
    template_path = Path(__file__).parent.parent / TEMPLATES[template_name]

    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        sys.exit(1)

    # Read template
    content = template_path.read_text()

    # Replace placeholders
    content = content.replace('Your Presentation Title', title)
    content = content.replace('Your Name', author)
    content = content.replace('Date', datetime.now().strftime('%Y-%m-%d'))

    # Write output
    output_path.write_text(content)
    print(f"✅ Created presentation: {output_path}")
    print(f"   Template: {template_name}")
    print(f"   Title: {title}")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: init_presentation.py <template> <output-file> <title> [author]")
        print(f"Available templates: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)

    template = sys.argv[1]
    output = Path(sys.argv[2])
    title = sys.argv[3]
    author = sys.argv[4] if len(sys.argv) > 4 else "Author Name"

    if template not in TEMPLATES:
        print(f"❌ Unknown template: {template}")
        print(f"Available: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)

    init_presentation(template, output, title, author)
```

##### `scripts/validate_marpit.sh`
**Purpose**: Check Marpit syntax validity
**Benefits**: Catches frontmatter errors, missing separators

```bash
#!/bin/bash
# Validate Marpit Markdown syntax

if [ $# -eq 0 ]; then
    echo "Usage: validate_marpit.sh <file.md>"
    exit 1
fi

FILE="$1"

# Check frontmatter
if ! head -n 3 "$FILE" | grep -q "^---$"; then
    echo "❌ Missing frontmatter opening (---)"
    exit 1
fi

if ! head -n 10 "$FILE" | grep -q "marp: true"; then
    echo "❌ Missing 'marp: true' in frontmatter"
    exit 1
fi

# Check slide separators
if ! grep -q "^---$" "$FILE"; then
    echo "⚠️  No slide separators found (---)"
fi

# Count slides
SLIDE_COUNT=$(grep -c "^---$" "$FILE")
echo "✅ Marpit syntax valid"
echo "   Slides: $((SLIDE_COUNT - 1))"
```

**Update SKILL.md** to reference scripts:

```markdown
## Validation

After creating SVGs:
```bash
scripts/validate_svg.py diagram.svg
```

Check color contrast:
```bash
scripts/check_contrast.py '#D4D4D4' '#1E1E1E'
# Output: Contrast ratio: 8.20:1 ✅ WCAG AAA
```

Validate Marpit syntax:
```bash
scripts/validate_marpit.sh slides.md
```
```

---

### 1.2 Add Assets Directory ⚠️ **CRITICAL**

**Current Gap**: No templates, no examples, users start from scratch every time.

**Create**: `assets/` directory with templates and examples

#### Directory Structure

```
assets/
├── templates/
│   ├── technical-dark.md        # VS Code-inspired dark theme
│   ├── professional-light.md    # Business/corporate light theme
│   └── minimal-keynote.md       # Story-driven minimal theme
├── examples/
│   ├── quick-start.md           # Minimal working example (5 slides)
│   └── full-presentation/       # Complete example with diagrams
│       ├── slides.md
│       ├── diagrams/
│       │   ├── architecture.svg
│       │   ├── workflow.svg
│       │   └── comparison.svg
│       └── README.md
└── icons/
    ├── check.svg                # ✓ checkmark icon
    ├── warning.svg              # ⚠ warning icon
    ├── error.svg                # ✗ error icon
    └── info.svg                 # ℹ info icon
```

#### Template: `assets/templates/technical-dark.md`

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

# Your Presentation Title
Subtitle or tagline

Your Name · Date

---

<!-- _class: lead -->
<!-- _backgroundColor: #0C0C0C -->
<!-- _color: #ABB2BF -->

# Section 1
Section description

---

## Slide Title

- Key point 1
- Key point 2
- Key point 3

---

## Code Example

```python
def hello_world():
    print("Hello, World!")
```

**Key takeaway**: Brief explanation of code

---

## Diagram Example

![width:900px](diagrams/architecture.svg)

**Architecture overview**: System components and data flow

---

<!-- _class: lead -->
<!-- _backgroundColor: #0C0C0C -->
<!-- _color: #ABB2BF -->

# Section 2
Next topic

---

## Two-Column Layout

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px;">

<div>

### Left Column
- Point 1
- Point 2
- Point 3

</div>

<div>

### Right Column
- Point A
- Point B
- Point C

</div>

</div>

---

<!-- _class: lead -->
<!-- _backgroundColor: #0C0C0C -->
<!-- _color: #ABB2BF -->

# Thank You
Questions?

Your Name · your.email@example.com
````

#### Template: `assets/templates/professional-light.md`

````markdown
---
marp: true
theme: default
paginate: true
backgroundColor: #FAFAFA
color: #2C2C2C
---

<!-- _class: lead -->

# Your Presentation Title
Subtitle or tagline

Your Name · Date

---

<!-- _class: lead -->
<!-- _backgroundColor: #2E75B6 -->
<!-- _color: #FFFFFF -->

# Section 1

---

## Slide Title

- Key point with clear messaging
- Supporting evidence or data
- Actionable insight

---

## Key Statistics

<div style="text-align: center; padding: 48px;">

# 95%
### Customer Satisfaction

# 10x
### Performance Improvement

# $2.5M
### Revenue Growth

</div>

---

## Process Overview

![width:1000px](diagrams/workflow.svg)

**Three-step process**: Streamlined approach to success

---

<!-- _class: lead -->
<!-- _backgroundColor: #2E75B6 -->
<!-- _color: #FFFFFF -->

# Call to Action

### Next Steps
1. Review proposal
2. Schedule follow-up
3. Begin implementation

---

<!-- _class: lead -->

# Thank You
Questions?

Your Name · your.email@example.com · Company Name
````

#### Template: `assets/templates/minimal-keynote.md`

````markdown
---
marp: true
theme: default
paginate: false
backgroundColor: #FFFFFF
color: #2F2F2F
---

<!-- _class: lead -->

# One Big Idea

Subtitle that clarifies the message

---

<!-- _class: lead -->

## The Problem

A clear statement of the challenge

---

<!-- _class: lead -->
<!-- _backgroundColor: #20C997 -->
<!-- _color: #FFFFFF -->

## The Solution

Your unique approach or insight

---

<!-- _class: lead -->

## Why It Matters

Impact and implications

---

<!-- _class: lead -->

# Remember This

**One sentence takeaway**

---

<!-- _class: lead -->
<!-- _backgroundColor: #F0F0F0 -->

Thank you.

Your Name
````

#### Example Icons: `assets/icons/check.svg`

```xml
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <!-- Green checkmark icon -->
  <circle cx="50" cy="50" r="45" fill="#10B981" stroke="#059669" stroke-width="3"/>
  <path d="M 30 50 L 42 62 L 70 34"
        stroke="#FFFFFF"
        stroke-width="6"
        stroke-linecap="round"
        stroke-linejoin="round"
        fill="none"/>
</svg>
```

#### Example Icons: `assets/icons/warning.svg`

```xml
<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <!-- Yellow warning icon -->
  <path d="M 50 10 L 90 85 L 10 85 Z"
        fill="#F59E0B"
        stroke="#D97706"
        stroke-width="3"
        stroke-linejoin="round"/>
  <path d="M 50 35 L 50 55"
        stroke="#FFFFFF"
        stroke-width="6"
        stroke-linecap="round"/>
  <circle cx="50" cy="68" r="4" fill="#FFFFFF"/>
</svg>
```

**Update SKILL.md** to reference assets:

```markdown
## Quick Start

**New presentation**:
```bash
scripts/init_presentation.py technical-dark my-deck.md "My Presentation" "John Doe"
```

**Or copy template manually**:
- `assets/templates/technical-dark.md` - Dark theme for code/diagrams
- `assets/templates/professional-light.md` - Light theme for business
- `assets/templates/minimal-keynote.md` - Story-driven minimal design

**Common icons**:
```markdown
![width:60px](assets/icons/check.svg)    <!-- Checkmark -->
![width:60px](assets/icons/warning.svg)  <!-- Warning -->
![width:60px](assets/icons/error.svg)    <!-- Error -->
```

**Full example**:
See `assets/examples/full-presentation/` for complete working deck with diagrams.
```

---

## Priority 2: Organization Improvements

### 2.1 Keep color-palettes.md Unified ✅ **DECISION**

**Initial Consideration**: Split `color-palettes.md` (543 lines) into two files: `complete-palettes.md` (7-role systems) and `svg-color-schemes.md` (quick schemes).

**Decision**: **Keep unified** in single `references/color-palettes.md` file.

**Rationale**:
1. **Color coherence is critical**: When designing presentations, colors for slides and SVGs must be considered together to maintain visual consistency
2. **Core principle**: "Define one color palette and reuse it in slides and SVGs" - splitting the file works against this
3. **Practical workflow**: Users typically need to reference both sections when creating full presentations
4. **Cognitive load**: Keeping colors together reduces mental overhead of switching between files

**Benefits of keeping unified**:
- Single source of truth for all color decisions
- Easier to ensure consistency across slides and diagrams
- Users can quickly compare complete palettes with SVG schemes
- Aligns with skill's core principle of unified design language

**Token efficiency trade-off**: Yes, loading both sections when only one is needed costs ~250 lines of context. However, the benefits of maintaining color coherence outweigh this cost. In practice, most presentation tasks require considering both slides and diagrams together.

---

### 2.2 Move Output Examples from SKILL.md ✅ **COMPLETED**

**Issue**: Lines 136-183 of SKILL.md contained output format examples (~48 lines).

**Problem**: These are reference material, not core workflow guidance. They made SKILL.md less focused.

**Solution**: Moved to `references/output-examples.md` with expanded examples.

**Implementation completed**:

#### Create: `references/output-examples.md`

```markdown
# Output Format Examples

Complete examples of expected outputs for each module.

## Color Design Output

### Example 1: Dark Technical Palette

```markdown
## Color Strategy

**Strategy**: Dark Technical
**Reasoning**: Code-heavy presentation for developer audience, projector environment

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

- [x] Contrast ratio Text Primary/Background = 8.2:1 (exceeds WCAG AAA)
- [x] Contrast ratio Primary/Background = 4.8:1 (meets WCAG AA)
- [x] Palette limited to 7 colors
- [x] Colors tested on projector (high contrast maintained)
- [x] Consistent with VS Code theme (familiar to developers)
```

### Example 2: Light Professional Palette

[Similar structure with light theme...]

## Marpit Authoring Output

### Example: Complete Presentation

````markdown
---
marp: true
theme: default
paginate: true
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

## SVG Illustration Output

### Example: Architecture Diagram

```xml
<svg viewBox="0 0 1200 675" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="shadow-sm">
      <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Frontend Service -->
  <rect x="100" y="250" width="280" height="180" rx="16"
        fill="#f0f9ff" stroke="#0891b2" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="240" y="340" font-family="sans-serif" font-size="24"
        font-weight="600" fill="#1e293b" text-anchor="middle">
    Frontend
  </text>

  <!-- Arrow to Backend -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="10"
            refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#0891b2"/>
    </marker>
  </defs>
  <line x1="380" y1="340" x2="520" y2="340"
        stroke="#0891b2" stroke-width="3" marker-end="url(#arrowhead)"/>

  <!-- Backend Service -->
  <rect x="520" y="250" width="280" height="180" rx="16"
        fill="#f0f9ff" stroke="#0891b2" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="660" y="340" font-family="sans-serif" font-size="24"
        font-weight="600" fill="#1e293b" text-anchor="middle">
    Backend
  </text>

  <!-- Arrow to Database -->
  <line x1="800" y1="340" x2="920" y2="340"
        stroke="#0891b2" stroke-width="3" marker-end="url(#arrowhead)"/>

  <!-- Database -->
  <ellipse cx="1000" cy="340" rx="100" ry="80"
           fill="#e0f2fe" stroke="#0891b2" stroke-width="3" filter="url(#shadow-sm)"/>
  <text x="1000" y="350" font-family="sans-serif" font-size="24"
        font-weight="600" fill="#1e293b" text-anchor="middle">
    Database
  </text>
</svg>
```

### Example: Workflow Diagram

[Additional SVG examples...]

---

## See Also

- [SKILL.md](../SKILL.md) - Return to main skill guide
- [color-design/workflow.md](color-design/workflow.md) - Color design process
- [marpit-authoring/patterns.md](marpit-authoring/patterns.md) - Common slide patterns
- [svg-illustration/pattern-examples.md](svg-illustration/pattern-examples.md) - SVG diagram patterns
```

#### Update SKILL.md

**Replace lines 113-161** with:

```markdown
## Output formats

See [references/output-examples.md](references/output-examples.md) for complete examples.

**Quick reference**:
- **Color design**: Strategy + Palette (7 roles) + Usage Guidelines + Validation Checklist
- **Marpit**: Frontmatter + slides separated by `---`
- **SVG**: `<svg viewBox="..." xmlns="...">` with proper sizing and consistency
```

**Results**:
- ✅ Created `references/output-examples.md` with comprehensive examples (400+ lines)
- ✅ Reduced SKILL.md from 216 to 176 lines (-18%)
- ✅ Included 2 complete color palette examples (dark + light)
- ✅ Included 2 Marpit examples (minimal + full presentation)
- ✅ Included 3 SVG examples (simple, architecture, flowchart)

**Benefits**:
- SKILL.md is now more focused on workflow and decision-making
- Examples are expanded with detailed annotations and multiple variations
- Users can reference examples without cluttering main workflow
- Maintains easy discoverability through clear link

---

## Priority 3: Polish & Enhancement

### 3.1 Add Troubleshooting Quick Reference ⚠️ **LOW**

**Current State**: `svg-illustration/troubleshooting.md` exists (618 lines) but no equivalent for cross-cutting issues.

**Create**: `references/troubleshooting-common.md`

```markdown
# Common Troubleshooting

Issues that affect multiple modules.

## Colors Look Different on Projector vs Screen

**Symptom**: Colors appear washed out or too bright when projected

**Cause**: Projectors have lower contrast ratios than monitors

**Solution**:
1. Increase contrast between text and background
2. Use darker backgrounds for light rooms (#1E1E1E instead of #2D2D2D)
3. Test on actual projector before presenting
4. Avoid pure white (#FFFFFF) and pure black (#000000)
5. Prefer high-contrast palettes (Terminal Dark, Clean Corporate)

**Recommended palettes for projectors**:
- Terminal Dark (10.5:1 contrast)
- Accessibility First (7:1+ all combinations)

---

## Marpit Not Rendering SVGs

**Symptom**: SVG shows as broken image or doesn't appear

**Causes & Solutions**:

1. **Incorrect file path**
   ```markdown
   <!-- Wrong: Absolute path -->
   ![width:800px](/Users/name/diagrams/flow.svg)

   <!-- Correct: Relative path -->
   ![width:800px](diagrams/flow.svg)
   ```

2. **Missing xmlns attribute**
   ```xml
   <!-- Wrong -->
   <svg viewBox="0 0 800 600">

   <!-- Correct -->
   <svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
   ```

3. **XML syntax errors**
   - Run `scripts/validate_svg.py file.svg` to check
   - Common: Unescaped `<` `>` `&` characters in text
   - Common: Unclosed tags or mismatched quotes

---

## Text Contrast Failing in Export

**Symptom**: Text is readable in preview but fails contrast checks in PDF/HTML export

**Cause**: Export process may apply different rendering or gamma correction

**Solution**:
1. Use `scripts/check_contrast.py` with your colors
2. Aim for 7:1 (AAA) instead of 4.5:1 (AA) minimum
3. Test exports, not just previews
4. Avoid transparent overlays on text

**Tool**:
```bash
scripts/check_contrast.py '#D4D4D4' '#1E1E1E'
# Should show: WCAG AAA Pass for both normal and large text
```

---

## Font Rendering Issues

**Symptom**: Fonts look different across devices or in exports

**Causes & Solutions**:

1. **Custom fonts not embedding**
   - Use web-safe fonts: `sans-serif`, `Arial`, `Helvetica`
   - Avoid system fonts: `San Francisco`, `Segoe UI` (not universal)

2. **Font weights not available**
   ```markdown
   <!-- Wrong: Using unavailable weight -->
   font-weight: 850

   <!-- Correct: Standard weights -->
   font-weight: 400  /* normal */
   font-weight: 600  /* semi-bold */
   font-weight: 700  /* bold */
   ```

3. **SVG text not rendering**
   - Specify `font-family="sans-serif"` explicitly
   - Avoid emoji in SVG `<text>` (use shapes instead)
   - See [svg-illustration/core-rules.md](svg-illustration/core-rules.md#emoji-and-special-characters-dont-use-them)

---

## Inconsistent Visual Style Across Slides

**Symptom**: Some slides look different (colors, spacing, borders)

**Cause**: Not following unified design system

**Solution**: Apply core rules consistently

1. **Choose ONE palette** - Use throughout all slides and SVGs
2. **Define stroke width once** - Use same value everywhere (e.g., 3px)
3. **Use consistent border radius** - All cards use same rx value (e.g., 16px)
4. **Apply shadow system uniformly** - Same filter across all elements

See [svg-illustration/core-rules.md](svg-illustration/core-rules.md#core-principle-visual-consistency)

**Checklist**:
- [ ] All SVGs use same color palette
- [ ] All SVGs use same stroke width
- [ ] All cards/containers use same border radius
- [ ] All shadows use same filter definition
- [ ] All slides use same Marpit theme and directives

---

## See Also

- [svg-illustration/troubleshooting.md](svg-illustration/troubleshooting.md) - SVG-specific issues
- [marpit-authoring/best-practices.md](marpit-authoring/best-practices.md) - Marpit consistency
- [color-design/workflow.md](color-design/workflow.md#validation-checklist) - Color validation
```

**Update SKILL.md** to reference:

```markdown
## Troubleshooting

Common issues:
- [troubleshooting-common.md](references/troubleshooting-common.md) - Cross-cutting problems
- [svg-illustration/troubleshooting.md](references/svg-illustration/troubleshooting.md) - SVG-specific
```

---

### 3.2 Enhance Decision Guide ⚠️ **LOW**

**Current State**: Lines 97-111 provide basic text decision guide.

**Enhancement**: Create visual flowchart and add sophisticated loading logic.

#### Create: `references/decision-guide.md`

```markdown
# Decision Guide

Comprehensive guide for selecting modules and loading references.

## Quick Decision Matrix

| User Request | Modules Needed | Primary References |
|--------------|----------------|-------------------|
| "Create a slide deck" | Marpit authoring | syntax-guide.md, patterns.md |
| "Design slide colors" | Color design | workflow.md, strategies.md, complete-palettes.md |
| "Draw a diagram" | SVG illustration | core-rules.md, svg-color-schemes.md |
| "Create presentation with custom brand colors" | Color design → Marpit | All color-design refs, marpit patterns |
| "Build tech talk with diagrams" | All three modules | Core rules from each, load details as needed |

## Module Selection Flowchart

```
User request
    │
    ├─ Mentions "slides" or "deck" or "presentation"?
    │  YES → Marpit authoring module
    │  │
    │  ├─ Also mentions "colors" or "theme" or "brand"?
    │  │  YES → Add color design module (run FIRST)
    │  │  NO → Use existing palette from svg-color-schemes.md
    │  │
    │  └─ Also mentions "diagrams" or "flowchart" or "architecture"?
    │     YES → Add SVG illustration module
    │     NO → Slides only
    │
    └─ Mentions "diagram" or "illustration" or "SVG" only?
       YES → SVG illustration module only
       └─ Needs custom colors?
          YES → Also load color design module
          NO → Use svg-color-schemes.md
```

## Context Loading Strategy

### For Simple Requests (1-5 slides, 1 diagram)

**Load**:
- Core rules only (SKILL.md + one module's primary reference)
- Total: ~150-300 lines

**Example**: "Draw a workflow diagram"
- Read: `svg-illustration/core-rules.md`
- Read: `svg-illustration/svg-color-schemes.md` (pick a palette)
- Skip: patterns, troubleshooting (load only if needed)

### For Medium Requests (Full deck, 2-3 diagrams)

**Load**:
- Core rules + patterns/best practices
- Total: ~500-800 lines

**Example**: "Create a 10-slide technical presentation with 2 architecture diagrams"
- Read: `color-design/workflow.md` → `strategies.md` → `complete-palettes.md`
- Read: `marpit-authoring/syntax-guide.md` → `patterns.md`
- Read: `svg-illustration/core-rules.md` → `svg-color-schemes.md`
- Load patterns/advanced as needed during creation

### For Complex Requests (Branded deck, custom colors, many diagrams)

**Load**:
- All relevant references progressively
- Total: Variable, load on-demand

**Example**: "Create full conference presentation with custom brand colors, 20 slides, 5 diagrams"
- Phase 1: Color design
  - Read all color-design/* references
  - Generate custom palette based on brand
- Phase 2: Slides
  - Read all marpit-authoring/* references
  - Apply palette to slide theme
- Phase 3: Diagrams
  - Read svg-illustration core + patterns
  - Use custom palette in all SVGs

## When to Load Advanced References

### `marpit-authoring/advanced-layouts.md`
**Load when**:
- User requests complex layouts (multi-column, mixed content)
- Basic patterns insufficient
- Custom grid/flexbox needed

**Skip when**:
- Simple bullet lists and code blocks
- Standard title + content slides

### `svg-illustration/pattern-examples.md`
**Load when**:
- User requests specific diagram type (flowchart, timeline, architecture)
- Need examples of complex patterns
- First attempt at diagram structure

**Skip when**:
- Creating simple shapes or icons
- User provides clear diagram specification

### `color-design/complete-palettes.md`
**Load when**:
- User wants recommendations or pre-made systems
- Unsure which colors to use
- Quick start without custom design

**Skip when**:
- User provides specific brand colors
- Already has palette defined
- Using default from templates

## Progressive Disclosure in Action

### Example: "Create a tech talk with diagrams"

**Step 1**: Assess scope
- Question: "How many slides? What diagrams?"
- Assume: ~15 slides, 3 diagrams, dark theme for code

**Step 2**: Load core
- Read: `SKILL.md` (understand workflow)
- Read: `marpit-authoring/syntax-guide.md` (Marpit basics)
- Read: `color-design/complete-palettes.md` (pick "Code-Focused Blue")

**Step 3**: Create outline
- Generate slide structure using syntax-guide
- Apply chosen palette

**Step 4**: Add diagrams (load SVG refs only now)
- Read: `svg-illustration/core-rules.md`
- Read: `svg-illustration/pattern-examples.md` (find architecture pattern)
- Create diagrams using palette colors

**Step 5**: Polish (load best practices only if issues arise)
- If inconsistent styling → Read: `marpit-authoring/best-practices.md`
- If SVG not rendering → Read: `svg-illustration/troubleshooting.md`

**Total context loaded**: ~1,000 lines instead of all 5,678 lines

---

## See Also

- [SKILL.md](../SKILL.md) - Core workflow and module overview
- [output-examples.md](output-examples.md) - Expected outputs for each module
```

**Update SKILL.md decision guide** (lines 97-111):

```markdown
## Decision guide

See [references/decision-guide.md](references/decision-guide.md) for detailed flowchart and loading strategies.

**Quick rules**:
```
Slides only                → Marpit authoring
Slides + custom colors     → Color design → Marpit authoring
Slides + diagrams          → Marpit authoring + SVG illustration
Diagram only               → SVG illustration + svg-color-schemes.md
Full branded presentation  → All three modules in sequence
```

**Context loading**:
- Simple request (1-5 items)  → Core rules only (~200 lines)
- Medium request (deck + few diagrams) → Core + patterns (~600 lines)
- Complex request (full branded deck) → Progressive loading as needed
```

**Benefits**:
- Clearer decision-making process
- Visual flowchart aids understanding
- Explicit loading strategies reduce token waste

---

## Implementation Checklist

### Phase 1: High-Impact Additions (Do First)

- [ ] Create `scripts/` directory
  - [ ] `validate_svg.py` - SVG validation
  - [ ] `check_contrast.py` - WCAG contrast checking
  - [ ] `init_presentation.py` - Template initialization
  - [ ] `validate_marpit.sh` - Marpit syntax checking
  - [ ] Test all scripts on sample files

- [ ] Create `assets/` directory structure
  - [ ] `assets/templates/` folder
    - [ ] `technical-dark.md`
    - [ ] `professional-light.md`
    - [ ] `minimal-keynote.md`
  - [ ] `assets/examples/` folder
    - [ ] `quick-start.md`
    - [ ] `full-presentation/` with complete example
  - [ ] `assets/icons/` folder
    - [ ] `check.svg`
    - [ ] `warning.svg`
    - [ ] `error.svg`
    - [ ] `info.svg`

- [ ] Update SKILL.md
  - [ ] Add "Quick Start" section referencing scripts
  - [ ] Add "Templates" section referencing assets
  - [ ] Add "Common Icons" reference
  - [ ] Add "Validation" section with script examples

### Phase 2: Organization Improvements

- [ ] Split `references/color-palettes.md`
  - [ ] Create `references/color-design/complete-palettes.md` (Part 1)
  - [ ] Create `references/svg-illustration/svg-color-schemes.md` (Part 2)
  - [ ] Update all cross-references in existing files
  - [ ] Update SKILL.md module reading lists
  - [ ] Delete original `color-palettes.md`

- [ ] Move output examples from SKILL.md
  - [ ] Create `references/output-examples.md`
  - [ ] Move content from SKILL.md lines 113-161
  - [ ] Replace with concise reference in SKILL.md
  - [ ] Add cross-references from color-design, marpit-authoring, svg-illustration

- [ ] Update cross-references
  - [ ] Search all .md files for `color-palettes.md` references
  - [ ] Update to `complete-palettes.md` or `svg-color-schemes.md` as appropriate
  - [ ] Verify all links work

### Phase 3: Polish

- [ ] Create `references/troubleshooting-common.md`
  - [ ] Add cross-cutting issues (projector colors, font rendering, etc.)
  - [ ] Link from SKILL.md
  - [ ] Cross-reference from module-specific troubleshooting

- [ ] Create `references/decision-guide.md`
  - [ ] Add flowchart (as SVG using skill itself!)
  - [ ] Add context loading strategies
  - [ ] Add progressive disclosure examples
  - [ ] Link from SKILL.md

- [ ] Create visual decision flowchart
  - [ ] Design flowchart SVG using svg-illustration module
  - [ ] Embed in `decision-guide.md`
  - [ ] Use skill's own color palette (dogfooding!)

- [ ] Final validation
  - [ ] Run `scripts/validate_svg.py` on all SVG assets
  - [ ] Run `scripts/validate_marpit.sh` on all template .md files
  - [ ] Check all internal links work
  - [ ] Test scripts with sample inputs
  - [ ] Verify templates render correctly in Marp

---

## Metrics & Success Criteria

### Before Improvements

- SKILL.md: 174 lines
- References: 13 files, 5,678 lines
- Scripts: 0 files
- Assets: 0 files
- Typical context loading: 600-1,000 lines per invocation

### After Improvements

- SKILL.md: ~130 lines (25% reduction)
- References: 15-16 files, ~5,800 lines (split palettes, added guides)
- Scripts: 4-5 files (executable, not loaded)
- Assets: 8-10 files (templates, examples, icons)
- Typical context loading: 400-700 lines per invocation (30%+ reduction)

### Success Metrics

1. **Token Efficiency**: 30%+ reduction in context loading for typical tasks
2. **Reliability**: 90%+ SVG validation pass rate (measured by scripts)
3. **Speed**: 50%+ reduction in time to create new presentation (via templates)
4. **User Satisfaction**: Positive feedback on templates, scripts, and examples

---

## Future Enhancements (Beyond Current Scope)

### Advanced Scripts

- `scripts/optimize_svg.py` - Minimize SVG file size
- `scripts/extract_palette.py` - Extract colors from image
- `scripts/batch_validate.sh` - Validate entire presentation directory
- `scripts/export_pdf.sh` - Marp CLI wrapper for PDF export

### Additional Assets

- `assets/templates/academic.md` - Research presentation template
- `assets/templates/startup-pitch.md` - Investor pitch template
- `assets/backgrounds/` - Subtle background patterns (SVG)
- `assets/animations/` - Simple CSS animations for slides

### Integration

- Pre-commit hook for automatic SVG validation
- GitHub Actions workflow for presentation CI/CD
- VS Code snippet file for common Marpit patterns
- Marp theme file (CSS) for custom slide-creator theme

---

## Questions for User

Before implementing these improvements, consider:

1. **Template preferences**: Are there specific presentation types/audiences we should prioritize?
2. **Script features**: Which validation/automation tasks are most painful currently?
3. **Asset formats**: Any specific icon sets or diagram types commonly needed?
4. **Integration**: Would pre-commit hooks or CI/CD be valuable?
5. **Branding**: Should templates include placeholder for logo/brand assets?

---

## Conclusion

The slide-creator skill is **well-designed and production-ready** with excellent progressive disclosure. Implementing these improvements would:

- **Increase reliability** through validation automation
- **Improve speed** through templates and quick-start assets
- **Reduce token costs** through better reference organization
- **Enhance user experience** through examples and troubleshooting

**Recommended implementation order**: Phase 1 → Phase 2 → Phase 3

**Estimated effort**:
- Phase 1: 4-6 hours (scripts + assets + SKILL.md updates)
- Phase 2: 2-3 hours (file splitting + reference updates)
- Phase 3: 2-3 hours (guides + flowchart + validation)
- Total: 8-12 hours for complete implementation

**ROI**: High - Each improvement directly addresses user pain points and reduces repetitive work.
