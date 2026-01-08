# Marpit Markdown Authoring

## Core Rule

ALWAYS output **valid Marpit-compatible Markdown** that can be directly rendered.

- Do NOT explain Marpit syntax unless explicitly asked
- Do NOT output non-Markdown prose
- Do NOT mix presentation content with commentary
- Output must be directly renderable by Marpit/Marp

---

## Design Principles for Effective Slides

### Visual Consistency: The Golden Rule

**CRITICAL: Consistency from beginning to end is paramount.**

A presentation with inconsistent styling appears unprofessional and distracts from content. Before starting, establish a design system and apply it uniformly.

**Consistency Checklist:**

1. **Color Palette**
   - ✅ Choose ONE accent color for all section dividers
   - ✅ Use the same background color throughout (or establish clear pattern)
   - ✅ Maintain consistent text colors for similar content types
   - ❌ Avoid: Different colors for each section divider (unless intentional theming)

2. **Spacing System**
   - ✅ Use ONE standard gap size for all grid layouts (e.g., 48px)
   - ✅ Use ONE standard margin-top value (e.g., 32px)
   - ✅ Maintain consistent padding around content blocks
   - ❌ Avoid: Mixing 32px, 40px, 48px gaps randomly

3. **Layout Patterns**
   - ✅ Reuse the same grid template for similar content
   - ✅ Keep two-column splits at same proportions (1fr 1fr or specific widths)
   - ✅ Use consistent border radius, stroke width across all custom elements
   - ❌ Avoid: Different layout structures for similar content types

4. **Typography**
   - ✅ Use consistent font weights (e.g., 700 for all section titles)
   - ✅ Maintain heading hierarchy (H1 for titles, H2 for subtitles, H3 for sections)
   - ✅ Keep emoji/icon usage consistent in position and style
   - ❌ Avoid: Random font weight changes, inconsistent heading levels

5. **Directives Usage**
   - ✅ Apply `<!-- _class: lead -->` to ALL section dividers or NONE
   - ✅ Use consistent background colors for lead slides
   - ✅ Apply pagination consistently (show on all or hide on specific slides)
   - ❌ Avoid: Some section dividers with lead class, others without

**Practical Example:**

```markdown
<!-- GOOD: Consistent section dividers -->
<!-- _class: lead -->
<!-- _backgroundColor: #0891b2 -->
<!-- _color: #ffffff -->
# Section 1

---
<!-- ... content ... -->
---

<!-- _class: lead -->
<!-- _backgroundColor: #0891b2 -->
<!-- _color: #ffffff -->
# Section 2

<!-- BAD: Inconsistent colors -->
<!-- _class: lead -->
<!-- _backgroundColor: #0891b2 -->
# Section 1

<!-- _class: lead -->
<!-- _backgroundColor: #7c3aed -->
# Section 2

<!-- _class: lead -->
<!-- _backgroundColor: #10b981 -->
# Section 3
```

**When to Break Consistency:**

Only break consistency for intentional emphasis:
- Final "thank you" or "contact" slide may use different color
- Warning/alert slides may use red/orange intentionally
- Before/after comparisons may use contrasting styles

**Design System Template:**

Before creating slides, define these constants:

```markdown
Design System:
- Primary accent: #0891b2 (all section dividers)
- Background: #f8fafc (all content slides)
- Text color: #1e293b (all body text)
- Grid gap: 48px (all layouts)
- Margin-top: 32px (all spacing)
- Border radius: 12px (all cards/containers)
```

### Visual Design Fundamentals

**Core Principle: Less is More**

Effective slides prioritize clarity over completeness. Each slide should communicate ONE key idea.

**Design Hierarchy (in order of importance):**

1. **Clarity** - Can the audience understand at a glance?
2. **Simplicity** - Remove everything non-essential
3. **Consistency** - Use patterns that repeat across slides
4. **Beauty** - Polish the visual presentation

### Layout & Composition

**Slide Real Estate Management**

On a 16:9 slide, visual weight is distributed as:

```
┌─────────────────────────────────────┐
│  [Safe Zone: 90% of slide]          │
│                                     │
│  ┌────────────────────────────┐    │
│  │   [Primary Focus Area]      │    │
│  │   Top-center or Center      │    │
│  │   ~60% of attention         │    │
│  └────────────────────────────┘    │
│                                     │
│  [Supporting Content: Bottom 20%]   │
└─────────────────────────────────────┘
```

**Layout Patterns**

1. **Centered Layout** (Title slides, emphasis)
   - Use `<!-- _class: lead -->` for auto-centering
   - Large heading + short subtitle
   - Minimal text (< 15 words total)

2. **Title + Content** (Most common)
   - H1 title at top
   - 3-5 bullet points in center
   - Optional supporting visual (right side or below)

3. **Two-Column Split** (Comparison, text + visual)
   - Use HTML grid/flex layout
   - Left: text (40-50% width)
   - Right: visual (50-60% width)

4. **Full-Visual** (Background image + overlay text)
   - Use `backgroundImage:` directive
   - Minimal text overlay
   - Ensure text contrast

**Visual Balance Rules**

- **Rule of thirds**: Place important elements at 1/3 or 2/3 positions
- **White space**: Minimum 15% of slide should be empty
- **Alignment**: Pick one alignment (left/center/right) per slide
- **Symmetry vs Asymmetry**: Symmetry = stable, asymmetry = dynamic

### Typography Hierarchy

**Font Size Scale (Default Theme)**

```
Hero/Title (lead slides):    64-80px
H1 (slide titles):           42-48px
H2 (section headers):        32-36px
Body text (bullets):         24-28px
Captions/footnotes:          18-20px
```

**Text Density Guidelines**

- **Title slide**: 5-10 words max
- **Content slide**: 20-40 words max (including bullets)
- **Data slide**: Minimize text, let visual speak
- **Section divider**: 3-7 words

**Reading Patterns**

People read in **F-pattern** or **Z-pattern**:
- Place most important info top-left
- Supporting info follows natural reading flow
- Call-to-action goes bottom-right

**Font Weight Usage**

- **Bold (700)**: Titles, emphasis (use sparingly)
- **Semibold (600)**: Headings
- **Regular (400)**: Body text (most text)
- **Light (300)**: Avoid (poor legibility on slides)

### Color Psychology & Application

**Theme-Based Color Guidance**

Align colors with content meaning:

- **Trust/Stability**: Blue shades → corporate, technical
- **Energy/Attention**: Orange/Amber → warnings, highlights
- **Growth/Success**: Green → progress, completion
- **Innovation**: Cyan/Purple → creativity, forward-thinking
- **Neutral/Professional**: Gray → background, supporting text

**Color Usage Rules**

1. **Background**: Always light or always dark (pick one)
2. **Text**: High contrast with background (4.5:1 minimum)
3. **Accent**: Use ONE accent color consistently across ALL section dividers
4. **Consistency**: Same colors for same meaning across entire deck

**Modern Color Palette Example (Recommended: Van Gogh Starry Night)**

Based on successful presentations, this palette provides artistic yet professional results:

```markdown
---
backgroundColor: #fef7cd  (creamy yellow: warm, artistic)
color: #0f1f2e           (midnight blue-black: strong contrast)
---

Section dividers (lead slides):
<!-- _backgroundColor: #2a5f8f -->  (swirling blue: artistic, trust)
<!-- _color: #fef7cd -->             (light text on dark background)

Accent colors in content:
- Primary: #2a5f8f (swirling blue)
- Highlight: #f4e5a0 (bright star gold)
- Success: #4a7ba7 (sky accent)
- Warm: #d4a574 (village light)
```

**Why Van Gogh Starry Night Works:**
- Distinctive and memorable
- Artistic without sacrificing professionalism
- Blues convey depth and trustworthiness
- Golds add warmth and draw attention
- Creates emotional connection with audience
- Perfect for creative and technical content alike

**Alternative: Modern Tech Palette (for purely corporate presentations)**

```markdown
---
backgroundColor: #f8fafc  (slate-50: subtle, professional)
color: #1e293b           (slate-800: readable, strong contrast)
---

Section dividers (lead slides):
<!-- _backgroundColor: #0891b2 -->  (cyan-600: trust, modern)
<!-- _color: #ffffff -->

Accent colors in content:
- Primary: #0891b2 (cyan-600)
- Success: #10b981 (emerald-500)
- Warning: #f59e0b (amber-500)
```

**Default Theme Best Practices**

```markdown
---
backgroundColor: #f8fafc
color: #1e293b
---

# Title in dark slate (#1e293b)

**Emphasis** in same color, bold weight

Key term in <mark style="background:#fef3c7;color:#92400e;">highlighted yellow</mark>
```

### Visual Rhythm & Pacing

**Content Density Variation**

Don't make every slide the same density:

```
Slide 1: Title (Low density) ●
Slide 2: Content (Medium)    ●●●
Slide 3: Content (Medium)    ●●●
Slide 4: Visual (Low)        ●
Slide 5: Content (High)      ●●●●●
Slide 6: Section (Low)       ●
```

This creates visual "breathing room" and maintains attention.

**Progressive Disclosure**

For complex topics, break into sequence:

```
Slide 1: Introduce concept
Slide 2: Show first component
Slide 3: Add second component
Slide 4: Complete picture
```

Better than cramming everything on one slide.

**Slide Transitions (Conceptual)**

While Marpit doesn't support animations, design slides to create narrative flow:

- Use consistent positioning for recurring elements
- Maintain color themes across related slides
- Use section dividers to signal topic changes

### Content Strategy

**What Makes a Good Slide**

✅ **Do:**
- One clear message per slide
- Use visuals to support (not decorate)
- Keep bullets concise (< 10 words each)
- Use specific examples over abstract concepts
- Show data visually (charts > tables > text)

❌ **Don't:**
- Wall of text (> 50 words)
- Tiny fonts (< 20px body text)
- Low contrast text
- Cluttered layouts (> 5 elements competing)
- Mixing too many fonts or colors

**Bullet Point Best Practices**

```markdown
# Good: Concise, Parallel Structure

- Install marketplace from GitHub
- Add plugins with single command
- Start coding immediately

# Bad: Verbose, Inconsistent

- First, you need to install the marketplace by cloning from GitHub
- Plugins can be added
- Then start coding and enjoy the benefits
```

**Visual-to-Text Ratio**

Aim for these ratios based on slide purpose:

- **Explanation**: 60% text, 40% visual
- **Demonstration**: 40% text, 60% visual
- **Impact**: 20% text, 80% visual
- **Transition**: 10% text, 90% visual (or solid color)

---

## Required Document Structure

Every Marpit document MUST start with a frontmatter block:

```markdown
---
marp: true
theme: default
paginate: true
---
```

**Required fields:**
- `marp: true` - Enables Marpit processing (mandatory)
- `theme` - Use `default`, `gaia`, or `uncover` (defaults to `default` if omitted)
- `paginate` - Show page numbers (recommended: `true`)

**Optional fields:**
- `backgroundColor: #fff` - Custom background color (recommended: `#f8fafc` or `#fef7cd` for Starry Night)
- `color: #333` - Custom text color (recommended: `#0f1f2e` for Starry Night)
- `class: invert` - Apply global class to all slides

**Recommended Frontmatter (Van Gogh Starry Night Theme):**

```markdown
---
marp: true
theme: default
paginate: true
backgroundColor: #fef7cd
color: #0f1f2e
---
```

**Why these colors?**
- Background `#fef7cd` (creamy yellow) - soft, artistic, reduces eye strain
- Text `#0f1f2e` (midnight blue-black) - excellent contrast, readable
- Evokes Van Gogh's artistic style while maintaining professionalism

---

## Slide Separation

Slides are separated using `---` (three hyphens) on a single line.

```markdown
---
marp: true
---

# Slide 1

Content here

---

# Slide 2

More content

---

# Slide 3

Final content
```

---

## Slide Writing Guidelines

### 1. One Slide = One Idea

- Each slide should convey a single concept
- Prefer bullet points over paragraphs
- **Guideline**: 3-5 bullets per slide for optimal readability
- Avoid long sentences (15 words or less per bullet)

### 2. Heading Usage

- Use `#` for slide title (one per slide)
- Use `##` sparingly for sub-sections within a slide
- Do NOT nest deeper than `##`

**Good:**
```markdown
# Main Topic

## Sub-topic (optional)

- Point A
- Point B
```

**Avoid:**
```markdown
# Title
## Sub
### Too deep
#### Way too deep
```

### 3. Content Overflow Prevention

**CRITICAL: Slides have fixed vertical space (~1080px). Content must fit within viewport.**

**Common Causes of Overflow:**

1. **Too many bullets** (> 7 items)
2. **Long code blocks** (> 15 lines)
3. **Multiple sections with headings** (> 3 H3 headings)
4. **Large images + text** (image + 5+ bullets)
5. **Two-column layouts with unbalanced content**

**How to Detect Overflow:**

Check if your slide has:
- Title (H2) = ~80px
- Each bullet = ~40-50px
- Each H3 heading = ~60px
- Code block = ~30px per line
- Grid/layout overhead = ~80px
- Safe margin = ~100px

**Example Calculation:**
```
H2 title:           80px
margin-top:         32px
3 × H3 headings:   180px (3 × 60px)
12 × bullets:      480px (12 × 40px)
Code block (7):    210px (7 × 30px)
Grid overhead:      80px
Safe margin:       100px
----------------------------
TOTAL:            1162px ❌ OVERFLOW! (> 1080px)
```

**Solutions:**

**Solution 1: Split into Multiple Slides**
```markdown
<!-- BEFORE: Overflowing slide -->
## 🛠️ Configuration

### Section A
- Point 1
- Point 2
- Point 3

### Section B
- Point 4
- Point 5

### Section C
```python
# 15 lines of code
```

<!-- AFTER: Split into 2 slides -->
## 🛠️ Configuration - Part 1

### Section A
- Point 1
- Point 2
- Point 3

### Section B
- Point 4
- Point 5

---

## 🛠️ Configuration - Part 2

### Section C
```python
# 15 lines of code
```
```

**Solution 2: Reduce Content Density**
```markdown
<!-- BEFORE: Too dense -->
## Features

### Category A
- Feature 1 with long description
- Feature 2 with long description
- Feature 3 with long description

### Category B
- Feature 4 with long description
- Feature 5 with long description

<!-- AFTER: Concise -->
## Features

### Category A
- Feature 1: Auto-format
- Feature 2: Smart fixes
- Feature 3: Type checks

### Category B
- Feature 4: Integration
- Feature 5: Workflows
```

**Solution 3: Use Smaller Font Sizes (Last Resort)**
```markdown
<div style="font-size: 0.9em;">

## Content Here

- Slightly smaller text
- Fits more content

</div>
```

**⚠️ Warning:** Only use smaller fonts if splitting slides is not possible. Readability should never be compromised.

**Solution 4: Optimize Two-Column Layouts**
```markdown
<!-- BEFORE: One column too long -->
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:48px;">
<div>
### Left
- 10 bullets (overflows!)
</div>
<div>
### Right
- 3 bullets
</div>
</div>

<!-- AFTER: Balanced or split -->
<div style="display:grid; grid-template-columns: 1fr 1fr; gap:48px;">
<div>
### Left
- 5 bullets
</div>
<div>
### Right
- 5 bullets
</div>
</div>
```

**Solution 5: Code Block Management**
```markdown
<!-- BEFORE: Too long -->
```python
# 25 lines of code that overflow the slide
```

<!-- AFTER: Show essential parts only -->
```python
# Key function (simplified)
def main():
    setup()
    process()
    cleanup()
```

**Or split across slides:**

Slide 1: Show setup
Slide 2: Show processing
Slide 3: Show cleanup
```

**Best Practices to Prevent Overflow:**

1. **Rule of thumb: Max content per slide**
   - H2 title + 5-7 bullets = ✅ Safe
   - H2 title + 2 × H3 + 8 bullets total = ✅ Safe
   - H2 title + 3 × H3 + 12 bullets + code = ❌ Overflow

2. **Visual estimation**
   - If content takes more than 3/4 of your editor screen, it will likely overflow

3. **Test early**
   - Preview slides frequently during creation
   - Check the most content-heavy slides first

4. **Progressive disclosure**
   - Don't put everything on one slide
   - Break complex topics into 2-3 slides
   - Use section dividers between major topics

5. **Content hierarchy**
   - Only use H3 when absolutely necessary
   - Prefer H2 + bullets over H2 + H3 + bullets

**Quick Checklist Before Finalizing:**

- [ ] No slide has more than 10 bullets
- [ ] No code block exceeds 12 lines
- [ ] Two-column layouts are balanced
- [ ] No more than 3 H3 headings per slide
- [ ] Each slide previews without scrolling

---

## Common Slide Patterns

### Title Slide

```markdown
---
marp: true
theme: default
---

# Presentation Title

**Subtitle or Description**

Author Name · Date
```

---

### Content Slide with Bullets

```markdown
# Key Concepts

- First important point
- Second important point
- Third important point
- Optional fourth point
```

---

### Quote Slide

```markdown
<!-- _class: lead -->

> "Inspiring quote or key message"

— Author Name
```

---

### Comparison Slide

```markdown
# Approach A vs Approach B

**Approach A:**
- Advantage 1
- Advantage 2

**Approach B:**
- Advantage 1
- Advantage 2
```

---

### Section Divider

```markdown
<!-- _class: lead -->
<!-- _backgroundColor: #0891b2 -->
<!-- _color: #ffffff -->

# Section Title

**Brief description or transition text**
```

**Consistency Note:** Use the SAME background color for ALL section dividers throughout your presentation.

---

### Two-Column Layout (Grid)

**Standard Pattern with Consistent Spacing:**

```markdown
## Feature Comparison

<div style="display:grid; grid-template-columns: 1fr 1fr; gap:48px; margin-top:32px;">

<div>

### Feature Set A

- Automatic formatting
- Smart fixes
- Type checking

### Use Cases

Best for small teams

</div>

<div>

### Feature Set B

- Full integration
- Custom workflows
- Advanced patterns

### Use Cases

Best for large projects

</div>

</div>
```

**Key Consistency Rules:**
- Always use `gap:48px` for two-column layouts
- Always use `margin-top:32px` for spacing below headers
- Use `1fr 1fr` for equal columns or specific widths (e.g., `1fr 2fr`)
- Maintain same structure across all two-column slides

---

### Three-Column Layout (Grid)

**Standard Pattern:**

```markdown
## Core Values

<div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:48px; margin-top:32px;">

<div style="text-align:center;">

### ⚡ Speed

Fast execution
Zero config

</div>

<div style="text-align:center;">

### 📚 Standards

Unified tools
Team sync

</div>

<div style="text-align:center;">

### 🔧 Flexible

Easy additions
Custom flows

</div>

</div>
```

**Key Consistency Rules:**
- Use `repeat(3, 1fr)` for three equal columns
- Use `gap:48px` consistently (never mix with 32px or 40px)
- Use `text-align:center` for icon/emoji + text combinations
- Keep content length similar across all three columns

---

## Directives (Slide-specific Styling)

Use HTML comments to apply directives to individual slides:

```markdown
<!-- _class: lead -->
# Centered Content
```

**Common directives:**
- `<!-- _class: lead -->` - Center content, larger text
- `<!-- _class: invert -->` - Invert colors (dark background)
- `<!-- _backgroundColor: #123456 -->` - Custom background for this slide
- `<!-- _paginate: false -->` - Hide page number on this slide

Directives starting with `_` apply only to the current slide.

---

## Working with Assets

### Asset Organization

**Standard directory structure:**
```
presentation-root/
├── slides.md          # Your presentation (this file)
└── assets/
    ├── diagrams/      # Process flows, architecture diagrams
    ├── icons/         # Icon sets, badges
    ├── charts/        # Data visualizations, graphs
    ├── backgrounds/   # Full-slide background images
    └── images/        # Other images (photos, screenshots)
```

**Key principle:** All media assets go in `assets/` subdirectories, organized by type.

### Image References

**ALWAYS use relative paths from the markdown file location:**

```markdown
# Correct - relative paths from slides.md
![Description](assets/diagram.svg)
![w:1200](assets/diagrams/workflow.svg)
![Icon](assets/icons/feature.svg)

# Incorrect - absolute paths
![Description](/home/user/assets/diagram.svg)
![Description](/assets/diagram.svg)
```

**Guidelines:**
- Always provide meaningful alt text
- Use relative paths (as shown above)
- Assume assets exist if referenced in conversation
- For sizing, use Marp's `w:` directive (e.g., `![w:1200](...)`)

**Centered image:**
```markdown
![center w:1200](assets/diagrams/example.svg)
```

### Integration with slide-svg-illustrator

When you need custom SVG illustrations, the `slide-svg-illustrator` skill will:

1. **Create the SVG file** using Write tool
2. **Save to correct location** (e.g., `assets/diagrams/workflow.svg`)
3. **Return embedding code** with proper relative path

**Your role:** Insert the provided embedding code into the Marpit document at the appropriate location.

**Example workflow:**
```
User: "Create a workflow diagram for slide 2"
→ slide-svg-illustrator creates assets/diagrams/workflow.svg
→ slide-svg-illustrator returns: ![w:1200](assets/diagrams/workflow.svg)
→ You insert this reference into slide 2 of the presentation
```

### Presentation File Location

**Default filename:** `slides.md` in the presentation root directory.

If the presentation file doesn't exist yet, create it using Write tool at the project root with proper frontmatter:

```markdown
---
marp: true
theme: default
paginate: true
---

# Presentation Title
...
```

---

## Code Blocks

Always use fenced code blocks with language specification:

````markdown
```python
def hello():
    print("Hello Marpit")
```
````

**Best practices:**
- Keep code snippets short (< 15 lines per slide)
- Use syntax highlighting (specify language)
- Consider splitting long code across multiple slides

---

## Lists

**Unordered lists:**
```markdown
- Item 1
- Item 2
  - Nested item
  - Another nested item
```

**Ordered lists:**
```markdown
1. First step
2. Second step
3. Third step
```

**Guideline**: Avoid nesting beyond 2 levels.

---

## Tables

Use standard Markdown tables:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Row 1    | Data     | Data     |
| Row 2    | Data     | Data     |
```

**Note**: Keep tables small (3-4 columns max) for readability.

---

## Math (if supported by theme)

Use LaTeX syntax:

```markdown
Inline math: $E = mc^2$

Block math:
$$
\int_{0}^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$
```

---

## Output Constraints

When generating Marpit content:

1. **Output Markdown ONLY** - No explanations before or after
2. **No meta-commentary** - Don't describe what you're doing
3. **No analysis** - Just the slide content
4. **Make reasonable assumptions** - If details are missing, infer sensible defaults
5. **Complete documents only** - Always include frontmatter

**Correct output:**
```markdown
---
marp: true
---

# Title
Content here
```

**Incorrect output:**
```
Here's your Marpit presentation:

[... markdown ...]

I've created 5 slides covering your topic.
```

---

## Quality Checklist

Before finalizing output, verify:

- [ ] Frontmatter includes `marp: true`
- [ ] Slides separated by `---`
- [ ] Each slide has clear focus
- [ ] 3-5 bullets per content slide
- [ ] Code blocks have language tags
- [ ] Images have alt text
- [ ] No raw HTML (unless absolutely necessary)
- [ ] Output is pure Markdown

---

## References

For detailed examples and advanced patterns, see:
- `references/slide-patterns.md` - Common presentation structures
- `references/themes-and-directives.md` - Styling and customization
- `references/advanced-layouts.md` - Complex slide layouts

**Related Skills:**
- [slide-color-design](../slide-color-design/SKILL.md) — How to design accessible, consistent color palettes for slides
- [slide-svg-illustrator](../slide-svg-illustrator/SKILL.md) — How to create and embed consistent SVG diagrams and icons
