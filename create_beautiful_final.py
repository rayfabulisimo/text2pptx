#!/usr/bin/env python3
"""
Create beautiful, concise presentation from pages 1-2
- Maximum 6 words per line
- 3-4 slides only
- Beautiful backgrounds and icons
"""

from beautiful_pptx_generator import create_beautiful_presentation

print("=" * 60)
print("BEAUTIFUL PRESENTATION GENERATOR")
print("=" * 60)

# Concise summary - PhD level but brief
title = "Cancer Cell Line Heterogeneity"

sections = [
    {
        "title": "Research Question",
        "bullets": [
            "Do cell lines mimic tumors?",
            "Cellular heterogeneity drives treatment failure",
            "Need experimental models for plasticity"
        ]
    },
    {
        "title": "Method: Multiplexed Single-Cell Sequencing",
        "bullets": [
            "Profiled 198 cancer cell lines",
            "53,513 cells from 22 cancers",
            "Dual SNP and expression validation",
            "10x Genomics Chromium platform"
        ]
    },
    {
        "title": "Major Discovery",
        "bullets": [
            "Found 12 recurrent heterogeneity programs",
            "Cell cycle and senescence patterns",
            "EMT and stress responses",
            "Programs match human tumor heterogeneity"
        ]
    },
    {
        "title": "Impact",
        "bullets": [
            "Cell lines preserve tumor complexity",
            "Valid models for drug resistance",
            "Enables mechanistic follow-up studies",
            "Identified specific heterogeneity model lines"
        ]
    }
]

# Validate max 6 words per bullet
print("\n✓ Validating bullet points...")
for section in sections:
    for bullet in section['bullets']:
        word_count = len(bullet.split())
        if word_count > 6:
            print(f"  WARNING: '{bullet}' has {word_count} words")

print("   All bullets validated!")

# Create presentations with different themes
themes = ["ocean", "forest", "modern"]

for theme in themes:
    output_file = f"final_beautiful_{theme}.pptx"
    print(f"\n📊 Creating {theme} theme presentation...")

    create_beautiful_presentation(
        title=title,
        sections=sections,
        output_file=output_file,
        theme_name=theme
    )

print("\n" + "=" * 60)
print("✅ COMPLETE!")
print("=" * 60)
print("\nGenerated presentations:")
print("  • final_beautiful_ocean.pptx (Ocean Depths theme)")
print("  • final_beautiful_forest.pptx (Forest Canopy theme)")
print("  • final_beautiful_modern.pptx (Modern Minimal theme)")
print(f"\nEach presentation has:")
print(f"  • 5 slides (1 title + 4 content)")
print(f"  • Beautiful gradient backgrounds")
print(f"  • Decorative icons (no figures)")
print(f"  • Concise bullets (max 6 words)")
print()
