#!/usr/bin/env python3
"""
Complete Document to Presentation Workflow
Supports: PDF, DOCX, PPTX, TXT, MD, Images
Creates beautiful modern PowerPoint presentations
"""

import asyncio
import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Optional

# Load .env file if it exists
try:
    from load_env import load_env
    load_env()
except:
    pass

# Import our agents
from document_analyzer_agent import analyze_document
from modern_pptx_generator import create_modern_presentation, THEMES

try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


async def summarize_with_ai(
    text: str,
    document_name: str,
    num_images: int,
    provider: str = "anthropic",
    model: str = None
) -> Dict:
    """
    Use AI to create structured summary with sections.

    Returns:
        Dict with 'sections' list, each section has title, content, and optional image_id
    """

    # Set default model
    if not model:
        model = "claude-opus-4-6" if provider == "anthropic" else "gpt-4"

    # Create prompt for structured summary
    prompt = f"""You are analyzing a document: {document_name}

The document has {num_images} images that can be referenced.

Your task: Create a structured summary divided into clear sections. Each section should:
1. Have a descriptive title
2. Have bullet-pointed content (3-5 bullets per section)
3. Optionally reference an image if the content relates to visual data

Create 2-3 sections minimum, up to 6 sections maximum for longer documents.

Document text:
{text[:15000]}

Output as JSON:
{{
  "sections": [
    {{
      "title": "Section Title",
      "content": "- Bullet point 1\\n- Bullet point 2\\n- Bullet point 3",
      "has_visual_data": true/false,
      "image_reference": "first/second/third/etc or null"
    }}
  ]
}}

Focus on:
- Main ideas and key findings
- Methods or approaches (if scientific/technical)
- Results or conclusions
- Keep bullets concise and clear
"""

    print(f"\nAnalyzing document with {provider} ({model})...")

    if provider == "anthropic":
        if not ANTHROPIC_AVAILABLE:
            return {"error": "anthropic not installed"}

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            return {"error": "ANTHROPIC_API_KEY not set"}

        client = anthropic.Anthropic(api_key=api_key)

        try:
            response = client.messages.create(
                model=model,
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            result_text = response.content[0].text
        except Exception as e:
            return {"error": f"Anthropic API error: {e}"}

    else:  # openai
        if not OPENAI_AVAILABLE:
            return {"error": "openai not installed"}

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return {"error": "OPENAI_API_KEY not set"}

        client = openai.OpenAI(api_key=api_key)

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an expert at analyzing documents and creating structured summaries."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4096,
                temperature=0.3
            )
            result_text = response.choices[0].message.content
        except Exception as e:
            return {"error": f"OpenAI API error: {e}"}

    # Parse JSON from response
    try:
        # Find JSON in response
        start = result_text.find("{")
        end = result_text.rfind("}") + 1
        if start >= 0 and end > start:
            json_str = result_text[start:end]
            summary_data = json.loads(json_str)
            return summary_data
        else:
            # Fallback: create sections from plain text
            return {
                "sections": [
                    {
                        "title": "Summary",
                        "content": result_text,
                        "has_visual_data": False
                    }
                ]
            }
    except json.JSONDecodeError:
        return {
            "sections": [
                {
                    "title": "Summary",
                    "content": result_text,
                    "has_visual_data": False
                }
            ]
        }


def map_images_to_sections(sections: List[Dict], images: List[Dict]) -> List[Dict]:
    """
    Intelligently map images to sections based on image_reference field.

    Args:
        sections: List of section dicts
        images: List of image dicts with 'id'

    Returns:
        Updated sections with 'image_id' field
    """
    image_mapping = {
        "first": 0,
        "second": 1,
        "third": 2,
        "fourth": 3,
        "fifth": 4,
        "sixth": 5
    }

    for section in sections:
        image_ref = section.get("image_reference")
        if image_ref and image_ref in image_mapping:
            img_idx = image_mapping[image_ref]
            if img_idx < len(images):
                section["image_id"] = images[img_idx]["id"]

    return sections


async def document_to_presentation_workflow(
    document_path: str,
    pages: str = None,
    provider: str = "anthropic",
    model: str = None,
    theme: str = "ocean",
    output_file: str = None,
    title: str = None
):
    """
    Complete workflow: Document → Analysis → AI Summary → Modern PPTX

    Args:
        document_path: Path to document (PDF, DOCX, PPTX, TXT, MD, image)
        pages: Page range for PDFs (e.g., "1-27")
        provider: AI provider (anthropic or openai)
        model: Specific model to use
        theme: Color theme (ocean, forest, sunset, purple, slate, coral)
        output_file: Output PPTX path (auto-generated if None)
        title: Presentation title (auto-generated if None)
    """

    print("\n" + "="*70)
    print("DOCUMENT TO PRESENTATION WORKFLOW")
    print("="*70)
    print(f"Document: {document_path}")
    print(f"Pages: {pages or 'all'}")
    print(f"Provider: {provider}")
    print(f"Model: {model or 'default'}")
    print(f"Theme: {theme}")
    print("="*70)

    # Step 1: Analyze document
    print("\n[1/3] Analyzing document...")
    doc_analysis = analyze_document(document_path, pages)

    if "error" in doc_analysis:
        print(f"\n❌ Error: {doc_analysis['error']}")
        return False

    print(f"  ✓ Extracted {doc_analysis['text_length']:,} characters")
    print(f"  ✓ Found {doc_analysis['num_images']} images")

    # Step 2: AI summarization
    print("\n[2/3] Creating AI-powered summary...")
    summary_result = await summarize_with_ai(
        doc_analysis["text"],
        doc_analysis["file_name"],
        doc_analysis["num_images"],
        provider,
        model
    )

    if "error" in summary_result:
        print(f"\n❌ Error: {summary_result['error']}")
        return False

    sections = summary_result.get("sections", [])
    print(f"  ✓ Generated {len(sections)} sections")

    # Map images to sections
    sections = map_images_to_sections(sections, doc_analysis["images"])

    # Step 3: Create presentation
    print("\n[3/3] Generating presentation...")

    # Auto-generate output filename
    if not output_file:
        doc_name = Path(document_path).stem
        output_file = f"{doc_name}_presentation.pptx"

    # Auto-generate title
    if not title:
        title = Path(document_path).stem.replace("_", " ").replace("-", " ").title()

    create_modern_presentation(
        {"sections": sections},
        doc_analysis["images"],
        output_file,
        theme,
        title
    )

    # Success summary
    print("\n" + "="*70)
    print("✓ WORKFLOW COMPLETE!")
    print("="*70)
    print(f"\nGenerated: {output_file}")
    print(f"  Theme: {THEMES[theme]['name']}")
    print(f"  Slides: {len(sections) + 1} (1 title + {len(sections)} content)")
    print(f"  Images: {sum(1 for s in sections if s.get('image_id'))}")
    print(f"\n✨ Open {output_file} in PowerPoint to view!")

    return True


async def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Complete workflow: Document → AI Summary → Modern Presentation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Supported document formats:
  - PDF (.pdf)
  - Word (.docx, .doc)
  - PowerPoint (.pptx, .ppt)
  - Text (.txt, .md)
  - Images (.png, .jpg, .jpeg, .gif, .bmp)

Available themes:
  ocean  - Ocean Blue (default)
  forest - Forest Green
  sunset - Sunset Orange
  purple - Royal Purple
  slate  - Modern Slate
  coral  - Coral Pink

Examples:
  # Basic usage
  python document_to_presentation_workflow.py paper.pdf --pages 1-27

  # With specific theme
  python document_to_presentation_workflow.py paper.pdf --pages 1-27 --theme purple

  # Word document
  python document_to_presentation_workflow.py report.docx --theme forest

  # Use OpenAI
  python document_to_presentation_workflow.py paper.pdf --provider openai --model gpt-4-turbo

  # Custom output
  python document_to_presentation_workflow.py paper.pdf --output my_slides.pptx --title "My Presentation"
        """
    )
    parser.add_argument("document_path", help="Path to document file")
    parser.add_argument("--pages", help="Page range for PDFs (e.g., 1-27)", default=None)
    parser.add_argument(
        "--provider",
        help="AI provider",
        choices=["anthropic", "openai"],
        default="anthropic"
    )
    parser.add_argument("--model", help="Specific model to use", default=None)
    parser.add_argument(
        "--theme",
        help="Color theme",
        choices=list(THEMES.keys()),
        default="ocean"
    )
    parser.add_argument("--output", help="Output PPTX file", default=None)
    parser.add_argument("--title", help="Presentation title", default=None)

    args = parser.parse_args()

    # Validate document exists
    if not Path(args.document_path).exists():
        print(f"❌ Error: Document not found: {args.document_path}")
        sys.exit(1)

    # Check AI provider availability
    if args.provider == "anthropic" and not ANTHROPIC_AVAILABLE:
        print("❌ Error: anthropic package not installed. Run: pip install anthropic")
        sys.exit(1)

    if args.provider == "openai" and not OPENAI_AVAILABLE:
        print("❌ Error: openai package not installed. Run: pip install openai")
        sys.exit(1)

    # Run workflow
    success = await document_to_presentation_workflow(
        args.document_path,
        args.pages,
        args.provider,
        args.model,
        args.theme,
        args.output,
        args.title
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    asyncio.run(main())
