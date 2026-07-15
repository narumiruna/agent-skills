#!/bin/bash
# Validate Marpit Markdown syntax

set -e

if [ $# -ne 1 ]; then
    echo "Usage: validate_marpit.sh <file.md>"
    echo ""
    echo "Validates Marpit Markdown files for:"
    echo "  - Frontmatter presence and format"
    echo "  - Required 'marp: true' directive"
    echo "  - Slide separators"
    exit 1
fi

FILE="$1"
case "$FILE" in
    /*) ;;
    *) FILE="./$FILE" ;;
esac

if [ ! -f "$FILE" ]; then
    echo "❌ File not found: $FILE"
    exit 1
fi

ERRORS=0

# Check frontmatter opening, accepting CRLF input.
FIRST_LINE=$(head -n 1 -- "$FILE")
FIRST_LINE=${FIRST_LINE%$'\r'}
if [ "$FIRST_LINE" != "---" ]; then
    echo "❌ Missing frontmatter opening (---) on line 1"
    ERRORS=$((ERRORS + 1))
fi

# Locate the frontmatter closing delimiter.
FRONTMATTER_END=$(awk '{ sub(/\r$/, "") } NR > 1 && $0 == "---" { print NR; exit }' "$FILE")
if [ -z "$FRONTMATTER_END" ]; then
    echo "❌ Missing frontmatter closing delimiter (---)"
    ERRORS=$((ERRORS + 1))
else
    # Check marp: true inside frontmatter only.
    if ! awk -v end="$FRONTMATTER_END" '{ sub(/\r$/, "") } NR > 1 && NR < end' "$FILE" | grep -Eq '^marp:[[:space:]]*[Tt][Rr][Uu][Ee]([[:space:]]*#.*)?[[:space:]]*$'; then
        echo "❌ Missing 'marp: true' in frontmatter"
        ERRORS=$((ERRORS + 1))
    fi
fi

# Count separators and slides, accepting CRLF input and avoiding negative counts.
SEPARATOR_COUNT=$(awk '{ sub(/\r$/, "") } $0 == "---" { count++ } END { print count + 0 }' "$FILE")
if [ "$SEPARATOR_COUNT" -gt 0 ]; then
    SLIDE_COUNT=$((SEPARATOR_COUNT - 1))
else
    SLIDE_COUNT=0
fi

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
