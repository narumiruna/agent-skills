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

# Locate the frontmatter closing delimiter.
FRONTMATTER_END=$(awk 'NR > 1 && $0 == "---" { print NR; exit }' "$FILE")
if [ -z "$FRONTMATTER_END" ]; then
    echo "❌ Missing frontmatter closing delimiter (---)"
    ERRORS=$((ERRORS + 1))
else
    # Check marp: true inside frontmatter only.
    if ! awk -v end="$FRONTMATTER_END" 'NR > 1 && NR < end' "$FILE" | grep -Eq '^marp:[[:space:]]*true[[:space:]]*$'; then
        echo "❌ Missing 'marp: true' in frontmatter"
        ERRORS=$((ERRORS + 1))
    fi
fi

# Check slide separators
SEPARATOR_COUNT=$(grep -c "^---$" "$FILE" || true)

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
