# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Generate slide color palettes from brand colors or strategies."""

import sys
from colorsys import rgb_to_hls, hls_to_rgb


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise ValueError(f"Invalid hex color: {hex_color}")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b)


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    """Convert RGB tuple to hex color."""
    r, g, b = [max(0, min(255, int(x))) for x in rgb]
    return f"#{r:02x}{g:02x}{b:02x}"


def adjust_lightness(hex_color: str, factor: float) -> str:
    """Adjust color lightness. Factor > 1 lightens, < 1 darkens."""
    r, g, b = hex_to_rgb(hex_color)
    h, lightness, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    lightness = max(0, min(1, lightness * factor))
    r, g, b = hls_to_rgb(h, lightness, s)
    return rgb_to_hex((int(r * 255), int(g * 255), int(b * 255)))


def adjust_saturation(hex_color: str, factor: float) -> str:
    """Adjust color saturation. Factor > 1 more saturated, < 1 less saturated."""
    r, g, b = hex_to_rgb(hex_color)
    h, lightness, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    s = max(0, min(1, s * factor))
    r, g, b = hls_to_rgb(h, lightness, s)
    return rgb_to_hex((int(r * 255), int(g * 255), int(b * 255)))


def generate_palette_from_brand(
    brand_color: str, style: str = "light"
) -> dict[str, str]:
    """
    Generate 7-role color palette from single brand color.

    Args:
        brand_color: Hex color of brand (used as Primary)
        style: "light" or "dark" background style

    Returns:
        Dictionary with 7 color roles
    """
    if style == "dark":
        return {
            "Background": "#1E1E1E",
            "Surface": "#252526",
            "Primary": brand_color,
            "Secondary": adjust_saturation(adjust_lightness(brand_color, 1.2), 0.8),
            "Accent": adjust_lightness(brand_color, 1.4),
            "Text Primary": "#D4D4D4",
            "Text Secondary": "#858585",
        }
    else:  # light
        return {
            "Background": "#FAFAFA",
            "Surface": "#FFFFFF",
            "Primary": brand_color,
            "Secondary": adjust_lightness(brand_color, 1.3),
            "Accent": adjust_saturation(brand_color, 1.2),
            "Text Primary": "#2C2C2C",
            "Text Secondary": "#666666",
        }


def generate_preset_palette(preset: str) -> dict[str, str]:
    """Generate preset palette by name."""
    presets = {
        "code-blue": {
            "Background": "#1E1E1E",
            "Surface": "#252526",
            "Primary": "#569CD6",
            "Secondary": "#4EC9B0",
            "Accent": "#F4BF75",
            "Text Primary": "#D4D4D4",
            "Text Secondary": "#858585",
        },
        "terminal-dark": {
            "Background": "#0C0C0C",
            "Surface": "#1A1A1A",
            "Primary": "#61AFEF",
            "Secondary": "#98C379",
            "Accent": "#E06C75",
            "Text Primary": "#ABB2BF",
            "Text Secondary": "#5C6370",
        },
        "clean-corporate": {
            "Background": "#FAFAFA",
            "Surface": "#FFFFFF",
            "Primary": "#2E75B6",
            "Secondary": "#5B9BD5",
            "Accent": "#F39C12",
            "Text Primary": "#2C2C2C",
            "Text Secondary": "#666666",
        },
        "modern-minimal": {
            "Background": "#F5F5F5",
            "Surface": "#FFFFFF",
            "Primary": "#1976D2",
            "Secondary": "#757575",
            "Accent": "#FF6F00",
            "Text Primary": "#212121",
            "Text Secondary": "#616161",
        },
    }

    if preset not in presets:
        raise ValueError(f"Unknown preset: {preset}")

    return presets[preset]


def format_palette_markdown(palette: dict[str, str], strategy: str = "") -> str:
    """Format palette as markdown output."""
    output = []
    output.append("## Color Palette\n")

    if strategy:
        output.append(f"**Strategy**: {strategy}\n")

    for role, color in palette.items():
        output.append(f"* **{role}:** `{color.upper()}`")

    output.append("\n## Usage Guidelines\n")
    output.append("Apply this palette to slides and SVGs consistently:\n")
    output.append(
        "- **Slides**: Use Background for slide backgrounds, Primary for titles"
    )
    output.append(
        "- **SVG**: Use Primary for main elements, Secondary for supporting elements"
    )
    output.append("- **Text**: Use Text Primary for body, Text Secondary for captions")

    output.append("\n## Validation\n")
    output.append("Check contrast ratios:")
    output.append(
        f"```bash\nuv run scripts/check_contrast.py '{palette['Text Primary']}' '{palette['Background']}'\n```"
    )

    return "\n".join(output)


def format_palette_css(palette: dict[str, str]) -> str:
    """Format palette as CSS variables."""
    output = [":root {"]
    for role, color in palette.items():
        var_name = role.lower().replace(" ", "-")
        output.append(f"  --color-{var_name}: {color.upper()};")
    output.append("}")
    return "\n".join(output)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: generate_palette.py <mode> [options]")
        print("\nModes:")
        print("  preset <name>           - Generate from preset palette")
        print(
            "  brand <hex> [style]     - Generate from brand color (style: light/dark)"
        )
        print("\nPresets:")
        print("  code-blue, terminal-dark, clean-corporate, modern-minimal")
        print("\nExamples:")
        print("  uv run scripts/generate_palette.py preset code-blue")
        print('  uv run scripts/generate_palette.py brand "#2E75B6" light')
        print('  uv run scripts/generate_palette.py brand "#569CD6" dark')
        sys.exit(1)

    mode = sys.argv[1]

    try:
        if mode == "preset":
            if len(sys.argv) < 3:
                print("❌ Error: Preset name required")
                sys.exit(1)
            preset_name = sys.argv[2]
            palette = generate_preset_palette(preset_name)
            output = format_palette_markdown(palette, f"Preset: {preset_name}")

        elif mode == "brand":
            if len(sys.argv) < 3:
                print("❌ Error: Brand color hex required")
                sys.exit(1)
            brand_color = sys.argv[2]
            style = sys.argv[3] if len(sys.argv) > 3 else "light"

            if style not in ["light", "dark"]:
                print("❌ Error: Style must be 'light' or 'dark'")
                sys.exit(1)

            palette = generate_palette_from_brand(brand_color, style)
            output = format_palette_markdown(palette, f"Brand-based ({style})")

        else:
            print(f"❌ Error: Unknown mode: {mode}")
            sys.exit(1)

        print(output)

    except ValueError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
