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
            issues.append("Missing SVG namespace (xmlns='http://www.w3.org/2000/svg')")

        # Check viewBox
        if 'viewBox' not in root.attrib:
            issues.append("Missing viewBox attribute")

        # Check for oversized viewBox on potentially small content
        if 'viewBox' in root.attrib:
            vb = root.attrib['viewBox'].split()
            if len(vb) == 4:
                width, height = int(float(vb[2])), int(float(vb[3]))
                if width == 1920 and height == 1080:
                    issues.append(
                        "Using full 1920×1080 viewBox - verify this matches actual content bounds"
                    )

        # Check for emoji/special characters in text (common error)
        for text_elem in root.iter('{http://www.w3.org/2000/svg}text'):
            if text_elem.text:
                non_ascii = [c for c in text_elem.text if ord(c) > 127]
                if non_ascii:
                    issues.append(
                        f"Non-ASCII characters in <text>: '{text_elem.text[:30]}' "
                        f"(may not render reliably)"
                    )

        # Check stroke consistency
        stroke_widths = set()
        for elem in root.iter():
            if 'stroke-width' in elem.attrib:
                stroke_widths.add(elem.attrib['stroke-width'])

        if len(stroke_widths) > 3:
            issues.append(
                f"Inconsistent stroke widths: {sorted(stroke_widths)} "
                f"(recommend using 1-2 values consistently)"
            )

    except ET.ParseError as e:
        issues.append(f"XML parse error: {e}")
    except Exception as e:
        issues.append(f"Validation error: {e}")

    return issues


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: validate_svg.py <file.svg>")
        print("\nValidates SVG files for:")
        print("  - XML syntax errors")
        print("  - Missing namespace/viewBox")
        print("  - Non-ASCII characters in text")
        print("  - Stroke width consistency")
        sys.exit(1)

    svg_file = Path(sys.argv[1])

    if not svg_file.exists():
        print(f"❌ File not found: {svg_file}")
        sys.exit(1)

    issues = validate_svg(svg_file)

    if issues:
        print(f"❌ {svg_file.name} has {len(issues)} issue(s):")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        sys.exit(1)
    else:
        print(f"✅ {svg_file.name} is valid")
        sys.exit(0)
