#!/usr/bin/env python3
"""
Theme Builder - Create custom PowerPoint themes
Supports custom colors and background images
"""

from pptx.dml.color import RGBColor
from pathlib import Path
from typing import Dict, Optional


def hex_to_rgb(hex_color: str) -> RGBColor:
    """Convert hex color to RGB."""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return RGBColor(r, g, b)


def create_custom_theme(
    primary_color: str,
    secondary_color: Optional[str] = None,
    accent_color: Optional[str] = None,
    background_color: Optional[str] = None,
    text_color: str = "#212121",
    name: str = "Custom Theme"
) -> Dict:
    """
    Create a custom theme from color specifications.

    Args:
        primary_color: Main color (hex, e.g., "#0D47A1")
        secondary_color: Secondary color (auto-generated if None)
        accent_color: Accent color (auto-generated if None)
        background_color: Background color (auto-generated if None)
        text_color: Text color (default: dark gray)
        name: Theme name

    Returns:
        Theme dictionary compatible with modern_pptx_generator
    """

    primary = hex_to_rgb(primary_color)

    # Auto-generate complementary colors if not provided
    if not secondary_color:
        # Lighten primary color for secondary
        p_rgb = primary_color.lstrip('#')
        r, g, b = tuple(int(p_rgb[i:i+2], 16) for i in (0, 2, 4))
        r = min(255, r + 40)
        g = min(255, g + 40)
        b = min(255, b + 40)
        secondary = RGBColor(r, g, b)
    else:
        secondary = hex_to_rgb(secondary_color)

    if not accent_color:
        # Further lighten for accent
        p_rgb = primary_color.lstrip('#')
        r, g, b = tuple(int(p_rgb[i:i+2], 16) for i in (0, 2, 4))
        r = min(255, r + 80)
        g = min(255, g + 80)
        b = min(255, b + 80)
        accent = RGBColor(r, g, b)
    else:
        accent = hex_to_rgb(accent_color)

    if not background_color:
        # Very light version of primary for background
        p_rgb = primary_color.lstrip('#')
        r, g, b = tuple(int(p_rgb[i:i+2], 16) for i in (0, 2, 4))
        # Calculate luminance and create light version
        background = RGBColor(
            min(255, int(r * 0.2 + 240)),
            min(255, int(g * 0.2 + 240)),
            min(255, int(b * 0.2 + 240))
        )
    else:
        background = hex_to_rgb(background_color)

    text = hex_to_rgb(text_color)

    return {
        "name": name,
        "primary": primary,
        "secondary": secondary,
        "accent": accent,
        "background": background,
        "text": text
    }


def create_theme_from_image(image_path: str, name: str = "Image Theme") -> Dict:
    """
    Create a theme based on dominant colors in an image.

    Args:
        image_path: Path to background image
        name: Theme name

    Returns:
        Theme dictionary with image_path included
    """
    try:
        from PIL import Image
        import colorsys

        # Open image and get dominant color
        img = Image.open(image_path)
        img = img.resize((150, 150))  # Downscale for speed
        pixels = list(img.getdata())

        # Get most common color
        from collections import Counter
        most_common = Counter(pixels).most_common(1)[0][0]

        if len(most_common) == 4:  # RGBA
            r, g, b, a = most_common
        else:  # RGB
            r, g, b = most_common

        # Convert to hex
        primary_hex = f"#{r:02x}{g:02x}{b:02x}"

        # Create theme with this primary color
        theme = create_custom_theme(
            primary_color=primary_hex,
            name=name
        )

        # Add background image path
        theme["background_image"] = str(image_path)

        return theme

    except Exception as e:
        print(f"Warning: Could not extract colors from image: {e}")
        # Return default theme
        return create_custom_theme("#0D47A1", name=name)


# Quick color palettes
PALETTES = {
    "professional_blue": {
        "primary": "#0D47A1",
        "secondary": "#1976D2",
        "accent": "#42A5F5",
        "name": "Professional Blue"
    },
    "nature_green": {
        "primary": "#1B5E20",
        "secondary": "#388E3C",
        "accent": "#81C784",
        "name": "Nature Green"
    },
    "sunset_orange": {
        "primary": "#E65100",
        "secondary": "#F57C00",
        "accent": "#FFB74D",
        "name": "Sunset Orange"
    },
    "royal_purple": {
        "primary": "#4A148C",
        "secondary": "#7B1FA2",
        "accent": "#BA68C8",
        "name": "Royal Purple"
    },
    "modern_teal": {
        "primary": "#00695C",
        "secondary": "#00897B",
        "accent": "#4DB6AC",
        "name": "Modern Teal"
    },
    "warm_red": {
        "primary": "#B71C1C",
        "secondary": "#D32F2F",
        "accent": "#EF5350",
        "name": "Warm Red"
    }
}


def get_palette(palette_name: str) -> Dict:
    """Get a predefined color palette."""
    if palette_name not in PALETTES:
        palette_name = "professional_blue"

    palette = PALETTES[palette_name]
    return create_custom_theme(
        primary_color=palette["primary"],
        secondary_color=palette["secondary"],
        accent_color=palette["accent"],
        name=palette["name"]
    )


if __name__ == "__main__":
    # Test theme creation
    print("Testing theme builder...")

    # Create custom theme
    theme = create_custom_theme(
        primary_color="#FF5722",
        name="Test Orange"
    )
    print(f"Created theme: {theme['name']}")

    # Test palettes
    for name in PALETTES:
        palette = get_palette(name)
        print(f"  - {palette['name']}")
