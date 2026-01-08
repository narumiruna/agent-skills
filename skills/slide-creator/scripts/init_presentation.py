#!/usr/bin/env python3
"""Initialize a new Marp presentation from template."""

import sys
import shutil
from pathlib import Path
from datetime import datetime

# Template paths relative to script location
TEMPLATES = {
    'technical-dark': 'assets/templates/technical-dark.md',
    'professional-light': 'assets/templates/professional-light.md',
    'minimal-keynote': 'assets/templates/minimal-keynote.md'
}


def init_presentation(template_name: str, output_path: Path, title: str, author: str):
    """Create new presentation from template."""
    # Get template path relative to skill root
    script_dir = Path(__file__).parent
    skill_root = script_dir.parent
    template_path = skill_root / TEMPLATES[template_name]

    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        print(f"   Expected at: {template_path.absolute()}")
        sys.exit(1)

    # Read template
    content = template_path.read_text()

    # Replace placeholders
    content = content.replace('Your Presentation Title', title)
    content = content.replace('Your Name', author)
    content = content.replace('Date', datetime.now().strftime('%Y-%m-%d'))
    content = content.replace('your.email@example.com', f'{author.lower().replace(" ", ".")}@example.com')

    # Write output
    output_path.write_text(content)
    print(f"✅ Created presentation: {output_path}")
    print(f"   Template: {template_name}")
    print(f"   Title: {title}")
    print(f"   Author: {author}")
    print(f"\nNext steps:")
    print(f"  1. Edit {output_path} to add your content")
    print(f"  2. Create diagrams/ folder for SVG illustrations")
    print(f"  3. Preview with Marp CLI or VS Code extension")


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: init_presentation.py <template> <output-file> <title> [author]")
        print(f"\nAvailable templates:")
        for name, desc in {
            'technical-dark': 'Dark theme for code/technical content',
            'professional-light': 'Light theme for business presentations',
            'minimal-keynote': 'Minimal design for story-driven talks'
        }.items():
            print(f"  {name:20} - {desc}")
        print("\nExample:")
        print('  init_presentation.py technical-dark my-talk.md "System Architecture" "John Doe"')
        sys.exit(1)

    template = sys.argv[1]
    output = Path(sys.argv[2])
    title = sys.argv[3]
    author = sys.argv[4] if len(sys.argv) > 4 else "Author Name"

    if template not in TEMPLATES:
        print(f"❌ Unknown template: {template}")
        print(f"Available: {', '.join(TEMPLATES.keys())}")
        sys.exit(1)

    if output.exists():
        response = input(f"⚠️  {output} already exists. Overwrite? (y/N): ")
        if response.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)

    init_presentation(template, output, title, author)
