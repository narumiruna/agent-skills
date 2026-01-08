# Marpit Markdown Authoring

## Core Rule

ALWAYS output **valid Marpit-compatible Markdown** that can be directly rendered.

- Do NOT explain Marpit syntax unless explicitly asked
- Do NOT output non-Markdown prose
- Do NOT mix presentation content with commentary
- Output must be directly renderable by Marpit/Marp

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
- `backgroundColor: #fff` - Custom background color
- `color: #333` - Custom text color
- `class: invert` - Apply global class to all slides

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
<!-- _class: lead invert -->

# Section Title

Brief description or transition text
```

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
