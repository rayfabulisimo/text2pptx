#!/usr/bin/env python3
"""
Enhanced PPTX Generator with Cartoons/Illustrations
Creates professional presentations with visual aids
"""

import sys
from pathlib import Path

# Import the modern generator and cartoon generator
from modern_pptx_generator import (
    create_modern_presentation,
    THEMES
)
from cartoon_generator import (
    create_simple_illustration,
    suggest_illustration_for_content
)


def create_enhanced_presentation(
    summary_data: dict,
    images: list,
    output_file: str,
    theme_name: str = "purple",
    title: str = "Document Summary",
    custom_theme: dict = None,
    add_cartoons: bool = True
):
    """
    Create an enhanced presentation with cartoons for slides without figures.

    Args:
        summary_data: Dict with 'sections' containing title and content
        images: List of image dicts with 'id', 'data'
        output_file: Output PPTX path
        theme_name: Theme name or "custom"
        title: Presentation title
        custom_theme: Custom theme dict
        add_cartoons: Whether to add generated illustrations
    """
    # Get theme colors
    if custom_theme:
        theme = custom_theme
    else:
        theme = THEMES.get(theme_name, THEMES["purple"])

    # Convert theme RGBColors to tuples for cartoon generator
    # RGBColor is a tuple subclass, so we can cast it directly
    theme_colors = {
        'primary': tuple(theme['primary']),
        'secondary': tuple(theme['secondary']),
        'accent': tuple(theme['accent']),
        'background': tuple(theme['background'])
    }

    # Create image dictionary
    image_dict = {img["id"]: img["data"] for img in images}

    # Enhance sections with cartoons where no image exists
    enhanced_sections = []
    for section in summary_data.get("sections", []):
        enhanced_section = section.copy()

        # If no image linked and cartoons are enabled, generate one
        if add_cartoons and not section.get("image_id"):
            suggestion = suggest_illustration_for_content(
                section.get("title", ""),
                section.get("content", "")
            )

            # Generate cartoon
            try:
                cartoon_data = create_simple_illustration(
                    concept=suggestion['concept'],
                    style=suggestion['style'],
                    width=1200,
                    height=900,
                    theme_colors=theme_colors
                )

                # Add to image dict with unique ID
                cartoon_id = f"cartoon_{len(image_dict)}"
                image_dict[cartoon_id] = cartoon_data
                enhanced_section["image_id"] = cartoon_id

                print(f"  Generated {suggestion['style']} illustration for: {section.get('title', '')[:50]}")

            except Exception as e:
                print(f"  Warning: Could not generate cartoon: {e}")

        enhanced_sections.append(enhanced_section)

    # Update summary data with enhanced sections
    enhanced_summary_data = summary_data.copy()
    enhanced_summary_data["sections"] = enhanced_sections

    # Convert image dict back to list
    enhanced_images = [{"id": k, "data": v} for k, v in image_dict.items()]

    # Call the modern presentation generator
    create_modern_presentation(
        summary_data=enhanced_summary_data,
        images=enhanced_images,
        output_file=output_file,
        theme_name=theme_name,
        title=title,
        custom_theme=custom_theme
    )


if __name__ == "__main__":
    import json
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate enhanced PowerPoint presentations with illustrations"
    )
    parser.add_argument("summary_json", help="JSON file with summary sections")
    parser.add_argument("--output", default="enhanced_presentation.pptx", help="Output file")
    parser.add_argument("--theme", default="purple", choices=list(THEMES.keys()), help="Color theme")
    parser.add_argument("--title", default="Document Summary", help="Presentation title")
    parser.add_argument("--no-cartoons", action="store_true", help="Disable cartoon generation")

    args = parser.parse_args()

    # Load data
    with open(args.summary_json, 'r') as f:
        data = json.load(f)

    summary_data = data.get("summary_data", {})
    images = data.get("images", [])

    create_enhanced_presentation(
        summary_data,
        images,
        args.output,
        args.theme,
        args.title,
        add_cartoons=not args.no_cartoons
    )
