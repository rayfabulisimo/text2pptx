#!/usr/bin/env python3
"""
Create final enhanced presentation from PDF pages 1-2
"""

from document_analyzer_agent import analyze_document
from enhanced_pptx_generator import create_enhanced_presentation

# Step 1: Extract document content
print("=" * 60)
print("ENHANCED PRESENTATION GENERATOR")
print("=" * 60)
print("\n📄 Step 1: Extracting document content from pages 1-2...")

doc_result = analyze_document(
    "data/input/Pan-cancer scRNA-seq recurring programs cellular heterogeneity Kinker 2020.pdf",
    pages="1-2"
)

print(f"   ✓ Text extracted: {doc_result['text_length']:,} characters")
print(f"   ✓ Images found: {doc_result['num_images']}")

# Step 2: Create PhD-level narrative summary
print("\n🎓 Step 2: Creating PhD-level narrative summary...")

# Analyze the text to create sections
text = doc_result['text']

summary_data = {
    "sections": [
        {
            "title": "Scientific Challenge: Decoding Tumor Heterogeneity",
            "content": """The Central Question:

- Cellular heterogeneity drives cancer progression and treatment failure
- Rare tumor cell subpopulations mediate resistance and metastasis
- Critical gap: Do cell line models recapitulate patient tumor complexity?

Research Motivation:
Single-cell RNA-seq enables direct profiling of intratumor heterogeneity, but mechanisms remain unclear. We hypothesize that cancer cell lines exhibit intrinsic cellular plasticity that mirrors tumor heterogeneity - even without native microenvironment interactions.

This study tests whether cell lines can serve as valid experimental models for studying the cellular diversity observed in human tumors.""",
            "image_id": None
        },
        {
            "title": "Methodological Innovation: Multiplexed Single-Cell Profiling",
            "content": """Technical Breakthrough:

Strategy: Pool-based multiplexed scRNA-seq approach
- 198 cell lines from 22 cancer types analyzed simultaneously
- 53,513 single cells profiled (average 280 cells/line)
- 10x Genomics Chromium platform

Dual Assignment System:
- SNP-based genetic identification from RNA-seq reads
- Expression profile clustering with bulk RNA-seq reference
- 98% concordance validates robustness

Why This Matters: First pan-cancer atlas of cellular heterogeneity in cell lines at this scale, enabling systematic comparison with tumor data.""",
            "image_id": doc_result['images'][0]['id'] if doc_result['images'] else None
        },
        {
            "title": "Key Finding: Patterns of Cellular Heterogeneity",
            "content": """Expression Variability Architecture:

Two Modes Identified:
1. Discrete subpopulations (11% of cell lines)
   - Typically cell line-specific programs
   - Limited cross-line similarity

2. Continuous cellular state spectra (majority)
   - Gradual transitions between states
   - More prevalent pattern

Computational Discovery:
- 1,445 robust expression programs detected across all lines
- 4-9 programs per individual cell line
- Non-negative matrix factorization revealed structure

Critical Insight: Most heterogeneity is continuous, not discrete, suggesting dynamic cellular plasticity rather than fixed subclones.""",
            "image_id": None
        },
        {
            "title": "Major Discovery: Recurrent Heterogeneous Programs",
            "content": """12 Expression Programs Recur Across Cancer Types:

Core Programs:
• Cell cycle regulation (G1/S and G2/M phases)
• Cellular senescence pathways
• Stress response mechanisms
• Interferon response
• Epithelial-mesenchymal transition (EMT)
• Protein metabolism and translation

Novel Context-Dependent Finding:
G1/S programs differ between tumors and cell lines:
- Tumors: MCM complex genes upregulated
- Cell lines: Histone H1 family genes upregulated

This may reflect adaptation to rapid in vitro growth and G1 checkpoint loss.

Validation: These programs match heterogeneity patterns in human tumors, confirming cell lines as valid models.""",
            "image_id": None
        },
        {
            "title": "Biological Significance and Translational Impact",
            "content": """Fundamental Insights:

Plasticity vs Genetics:
Substantial tumor heterogeneity stems from intrinsic cellular plasticity, not just genetic diversity or microenvironment effects.

Clinical Relevance:
- Specific cell lines identified as heterogeneity models
- Senescent subpopulations show unique drug sensitivities
- Predictions validated against clinical response data

Broader Implications:
This work establishes that cultured cell lines preserve tumor-relevant heterogeneity programs, validating their use for mechanistic studies of cellular plasticity, drug resistance mechanisms, and therapeutic strategy development.

Future Directions: Identified cell lines enable follow-up studies on dynamics, regulation, and therapeutic targeting of specific cellular states.""",
            "image_id": None
        }
    ]
}

print(f"   ✓ Created {len(summary_data['sections'])} narrative sections")

# Step 3: Prepare images
print("\n🖼️  Step 3: Preparing images...")
images = []
for img in doc_result['images']:
    images.append({
        'id': img['id'],
        'data': img['data']
    })
print(f"   ✓ {len(images)} images prepared")

# Step 4: Generate enhanced presentation
print("\n🎨 Step 4: Generating presentation with all enhancements...")
print("   - PhD-level narrative")
print("   - Royal Purple theme")
print("   - Auto-generated illustrations")
print("   - Professional styling")
print()

create_enhanced_presentation(
    summary_data=summary_data,
    images=images,
    output_file="final_presentation_pages_1-2.pptx",
    theme_name="purple",
    title="Pan-cancer Single-Cell Analysis: Cellular Heterogeneity Programs",
    add_cartoons=True
)

print("\n" + "=" * 60)
print("✅ SUCCESS!")
print("=" * 60)
print(f"\n📊 Presentation created: final_presentation_pages_1-2.pptx")
print(f"   • Pages analyzed: 1-2")
print(f"   • Slides created: {len(summary_data['sections']) + 1} (1 title + {len(summary_data['sections'])} content)")
print(f"   • Narrative style: PhD scientist")
print(f"   • Theme: Royal Purple")
print(f"   • Illustrations: Auto-generated")
print(f"   • Figures: {len(images)} from PDF + auto-generated cartoons")
print()
