#!/bin/bash
# Validate Marpit Markdown syntax

set -e

if [ $# -eq 0 ]; then
    echo "Usage: validate_marpit.sh <file.md>"
    echo ""
    echo "Validates Marpit Markdown files for:"
    echo "  - Frontmatter presence and format"
    echo "  - Required 'marp: true' directive"
    echo "  - Slide separators"
    exit 1
fi

FILE="$1"

if [ ! -f "$FILE" ]; then
    echo "❌ File not found: $FILE"
    exit 1
fi

ERRORS=0

# Check frontmatter opening
if ! head -n 1 "$FILE" | grep -q "^---$"; then
    echo "❌ Missing frontmatter opening (---) on line 1"
    ERRORS=$((ERRORS + 1))
fi

# Check marp: true
if ! head -n 10 "$FILE" | grep -q "marp: true"; then
    echo "❌ Missing 'marp: true' in frontmatter"
    ERRORS=$((ERRORS + 1))
fi

# Check frontmatter closing
if ! head -n 10 "$FILE" | tail -n +2 | grep -q "^---$"; then
    echo "⚠️  Frontmatter may not be properly closed with ---"
fi

# Check slide separators
SEPARATOR_COUNT=$(grep -c "^---$" "$FILE" || true)
if [ "$SEPARATOR_COUNT" -lt 2 ]; then
    echo "⚠️  Only $SEPARATOR_COUNT separator(s) found. Expected at least 2 (frontmatter + slides)"
fi

# Count slides (separators minus frontmatter)
SLIDE_COUNT=$((SEPARATOR_COUNT - 1))

if [ $ERRORS -eq 0 ]; then
    echo "✅ Marpit syntax valid"
    echo "   File: $FILE"
    echo "   Slides: $SLIDE_COUNT"
    exit 0
else
    echo ""
    echo "❌ Found $ERRORS error(s) in Marpit syntax"
    exit 1
fi
