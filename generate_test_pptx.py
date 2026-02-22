#!/usr/bin/env python3
import json
import sys

# Import the generators
from document_analyzer_agent import analyze_document
from modern_pptx_generator import create_modern_presentation

# Load the summary data
with open('test_summary_data.json', 'r') as f:
    data = json.load(f)

# Extract the document to get images
doc_result = analyze_document(
    "data/input/Pan-cancer scRNA-seq recurring programs cellular heterogeneity Kinker 2020.pdf",
    pages="1-2"
)

# Prepare images for PPTX generator
images = []
for img in doc_result['images']:
    images.append({
        'id': img['id'],
        'data': img['data']
    })

# Generate PPTX with Royal Purple theme
output_file = "sanity_check_presentation.pptx"
create_modern_presentation(
    summary_data=data['summary_data'],
    images=images,
    output_file=output_file,
    theme_name="purple",
    title="Pan-cancer scRNA-seq Study Summary"
)

print(f"\n✅ Sanity check complete!")
print(f"   Presentation: {output_file}")
print(f"   Theme: Royal Purple")
print(f"   Slides: {len(data['summary_data']['sections']) + 1}")
print(f"   Images: {len(images)}")
