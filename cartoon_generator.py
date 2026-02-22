#!/usr/bin/env python3
"""
Cartoon/Illustration Generator for Presentations
Generates visual aids to complement slide content
"""

import io
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, Optional


def create_simple_illustration(
    concept: str,
    style: str = "diagram",
    width: int = 800,
    height: int = 600,
    theme_colors: Dict = None
) -> bytes:
    """
    Create a simple illustration for a slide concept.

    Args:
        concept: The concept to illustrate (e.g., "workflow", "comparison", "process")
        style: Style of illustration ("diagram", "icon", "chart", "process")
        width: Image width in pixels
        height: Image height in pixels
        theme_colors: Dict with 'primary', 'secondary', 'accent' RGB tuples

    Returns:
        bytes: PNG image data
    """
    if theme_colors is None:
        theme_colors = {
            'primary': (74, 20, 140),
            'secondary': (123, 31, 162),
            'accent': (186, 104, 200),
            'background': (248, 245, 250)
        }

    # Create image with background
    img = Image.new('RGB', (width, height), theme_colors['background'])
    draw = ImageDraw.Draw(img)

    # Generate based on style
    if style == "workflow":
        _draw_workflow_diagram(draw, width, height, theme_colors, concept)
    elif style == "comparison":
        _draw_comparison_diagram(draw, width, height, theme_colors, concept)
    elif style == "process":
        _draw_process_diagram(draw, width, height, theme_colors, concept)
    elif style == "key_finding":
        _draw_key_finding_visual(draw, width, height, theme_colors, concept)
    else:
        _draw_generic_diagram(draw, width, height, theme_colors, concept)

    # Convert to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    return img_bytes.getvalue()


def _draw_workflow_diagram(draw, width, height, colors, concept):
    """Draw a workflow diagram with connected boxes."""
    box_width = 180
    box_height = 80
    spacing = 60

    # Calculate starting position for 3 boxes
    total_width = (box_width * 3) + (spacing * 2)
    start_x = (width - total_width) // 2
    y = height // 2 - box_height // 2

    steps = ["Input", "Process", "Output"]

    for i, step in enumerate(steps):
        x = start_x + i * (box_width + spacing)

        # Draw box
        draw.rectangle(
            [(x, y), (x + box_width, y + box_height)],
            fill=colors['primary'],
            outline=colors['accent'],
            width=3
        )

        # Draw arrow to next box
        if i < len(steps) - 1:
            arrow_y = y + box_height // 2
            arrow_start = x + box_width
            arrow_end = x + box_width + spacing
            draw.line([(arrow_start, arrow_y), (arrow_end, arrow_y)],
                     fill=colors['secondary'], width=4)
            # Arrowhead
            draw.polygon([
                (arrow_end, arrow_y),
                (arrow_end - 15, arrow_y - 10),
                (arrow_end - 15, arrow_y + 10)
            ], fill=colors['secondary'])


def _draw_comparison_diagram(draw, width, height, colors, concept):
    """Draw a comparison diagram with two columns."""
    col_width = 250
    col_height = 300
    spacing = 100

    total_width = (col_width * 2) + spacing
    start_x = (width - total_width) // 2
    y = (height - col_height) // 2

    # Left column
    draw.rectangle(
        [(start_x, y), (start_x + col_width, y + col_height)],
        fill=colors['primary'],
        outline=colors['accent'],
        width=3
    )

    # Right column
    draw.rectangle(
        [(start_x + col_width + spacing, y),
         (start_x + col_width * 2 + spacing, y + col_height)],
        fill=colors['secondary'],
        outline=colors['accent'],
        width=3
    )

    # VS text in middle
    vs_x = start_x + col_width + spacing // 2
    vs_y = height // 2
    draw.ellipse(
        [(vs_x - 30, vs_y - 30), (vs_x + 30, vs_y + 30)],
        fill=colors['accent']
    )


def _draw_process_diagram(draw, width, height, colors, concept):
    """Draw a circular process diagram."""
    center_x = width // 2
    center_y = height // 2
    radius = 100

    # Draw center circle
    draw.ellipse(
        [(center_x - radius, center_y - radius),
         (center_x + radius, center_y + radius)],
        fill=colors['primary'],
        outline=colors['accent'],
        width=4
    )

    # Draw satellite circles
    import math
    num_circles = 4
    satellite_radius = 60
    orbit_radius = 180

    for i in range(num_circles):
        angle = (2 * math.pi * i) / num_circles
        x = center_x + orbit_radius * math.cos(angle)
        y = center_y + orbit_radius * math.sin(angle)

        # Draw connecting line
        line_end_x = center_x + radius * math.cos(angle)
        line_end_y = center_y + radius * math.sin(angle)
        draw.line([(line_end_x, line_end_y), (x, y)],
                 fill=colors['secondary'], width=3)

        # Draw satellite circle
        draw.ellipse(
            [(x - satellite_radius, y - satellite_radius),
             (x + satellite_radius, y + satellite_radius)],
            fill=colors['secondary'],
            outline=colors['accent'],
            width=3
        )


def _draw_key_finding_visual(draw, width, height, colors, concept):
    """Draw a visual for key findings with emphasis."""
    # Draw large central shape
    center_x = width // 2
    center_y = height // 2
    size = 200

    # Draw star or burst shape
    import math
    num_points = 8
    outer_radius = size
    inner_radius = size // 2

    points = []
    for i in range(num_points * 2):
        angle = (2 * math.pi * i) / (num_points * 2) - math.pi / 2
        radius = outer_radius if i % 2 == 0 else inner_radius
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append((x, y))

    draw.polygon(points, fill=colors['primary'], outline=colors['accent'])


def _draw_generic_diagram(draw, width, height, colors, concept):
    """Draw a generic diagram placeholder."""
    # Draw concentric rectangles for abstract representation
    margin = 100
    for i in range(3):
        offset = i * 40
        draw.rectangle(
            [(margin + offset, margin + offset),
             (width - margin - offset, height - margin - offset)],
            outline=colors['primary'] if i == 0 else colors['secondary'],
            width=4 - i
        )


def suggest_illustration_for_content(slide_title: str, slide_content: str) -> Dict:
    """
    Suggest appropriate illustration type based on slide content.

    Returns:
        Dict with 'style', 'concept', and 'description'
    """
    title_lower = slide_title.lower()
    content_lower = slide_content.lower()

    # Detect workflow/process
    if any(word in title_lower + content_lower for word in
           ['workflow', 'pipeline', 'method', 'approach', 'procedure']):
        return {
            'style': 'workflow',
            'concept': 'process_flow',
            'description': 'Step-by-step workflow diagram'
        }

    # Detect comparisons
    if any(word in title_lower + content_lower for word in
           ['comparison', 'versus', 'vs', 'different', 'compared']):
        return {
            'style': 'comparison',
            'concept': 'side_by_side',
            'description': 'Side-by-side comparison visual'
        }

    # Detect key findings
    if any(word in title_lower for word in
           ['finding', 'result', 'conclusion', 'discovery']):
        return {
            'style': 'key_finding',
            'concept': 'highlight',
            'description': 'Highlighted key finding visual'
        }

    # Detect processes
    if any(word in title_lower + content_lower for word in
           ['cycle', 'process', 'system', 'mechanism']):
        return {
            'style': 'process',
            'concept': 'circular_process',
            'description': 'Circular process diagram'
        }

    # Default
    return {
        'style': 'diagram',
        'concept': 'generic',
        'description': 'Abstract concept diagram'
    }


if __name__ == "__main__":
    # Test illustration generation
    print("Testing cartoon generator...")

    # Generate sample illustrations
    styles = ['workflow', 'comparison', 'process', 'key_finding']

    for style in styles:
        img_data = create_simple_illustration(
            concept=f"test_{style}",
            style=style
        )

        with open(f"test_illustration_{style}.png", 'wb') as f:
            f.write(img_data)

        print(f"✓ Generated {style} illustration")

    print("\nDone! Check test_illustration_*.png files")
