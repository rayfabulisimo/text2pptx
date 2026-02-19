#!/usr/bin/env python3
"""
Unified PDF Summarizer Agent - Works with both OpenAI and Anthropic
Uses Claude Agent SDK with custom tool for provider selection
"""

import asyncio
import subprocess
import sys
import os
from pathlib import Path
from typing import Optional, Literal

try:
    from claude_agent_sdk import query, ClaudeAgentOptions
except ImportError:
    print("Error: claude-agent-sdk not installed. Install with: pip install claude-agent-sdk")
    sys.exit(1)

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


def extract_pdf_text(pdf_path: str, start_page: int = 1, end_page: int = None) -> str:
    """Extract text from PDF using pdftotext."""
    try:
        cmd = ["pdftotext"]
        if start_page:
            cmd.extend(["-f", str(start_page)])
        if end_page:
            cmd.extend(["-l", str(end_page)])
        cmd.extend([pdf_path, "-"])

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error extracting PDF: {e}")
        return None
    except FileNotFoundError:
        print("Error: pdftotext not found. Install with: apt-get install poppler-utils")
        return None


def summarize_with_provider(
    text: str,
    pdf_name: str,
    provider: Literal["anthropic", "openai"],
    model: str
) -> str:
    """Summarize using the specified provider."""

    prompt = f"""I have extracted text from a scientific paper PDF: {pdf_name}

Please provide:
a) A summary of the main ideas (in paragraph form, covering key findings, biological insights, and clinical relevance)
b) Detailed bullet points on the methods used

Here is the extracted text:

{text}

Please structure your response clearly with headers for each section."""

    if provider == "anthropic":
        if not ANTHROPIC_AVAILABLE:
            return "Error: anthropic package not installed"

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            return "Error: ANTHROPIC_API_KEY not set"

        client = anthropic.Anthropic(api_key=api_key)

        try:
            response = client.messages.create(
                model=model,
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Error calling Anthropic API: {e}"

    else:  # openai
        if not OPENAI_AVAILABLE:
            return "Error: openai package not installed"

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return "Error: OPENAI_API_KEY not set"

        client = openai.OpenAI(api_key=api_key)

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an expert at analyzing and summarizing scientific papers."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4096,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error calling OpenAI API: {e}"


async def unified_agent_summarizer(
    pdf_path: str,
    start_page: Optional[int] = None,
    end_page: Optional[int] = None,
    provider: Optional[Literal["anthropic", "openai"]] = None,
    model: Optional[str] = None,
    output_file: Optional[str] = None
) -> str:
    """
    Unified agent-based PDF summarizer.

    Args:
        pdf_path: Path to PDF file
        start_page: Start page number
        end_page: End page number
        provider: AI provider (anthropic or openai)
        model: Specific model to use
        output_file: Optional output file path

    Returns:
        Summary text
    """

    # Validate PDF exists
    if not Path(pdf_path).exists():
        return f"Error: PDF file not found: {pdf_path}"

    # Check available providers
    available = []
    if ANTHROPIC_AVAILABLE and os.environ.get("ANTHROPIC_API_KEY"):
        available.append("anthropic")
    if OPENAI_AVAILABLE and os.environ.get("OPENAI_API_KEY"):
        available.append("openai")

    if not available:
        return "Error: No AI providers available. Install packages and set API keys."

    # Interactive provider selection if not specified
    if not provider:
        print("\n" + "="*60)
        print("SELECT AI PROVIDER")
        print("="*60)
        print("\nAvailable providers:")
        for i, p in enumerate(available, 1):
            print(f"  {i}. {p.capitalize()}")

        while True:
            choice = input("\nSelect provider (enter number): ").strip()
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(available):
                    provider = available[idx]
                    break
            except ValueError:
                pass
            print("Invalid choice. Try again.")

    # Set default model if not specified
    if not model:
        if provider == "anthropic":
            model = "claude-opus-4-6"
        else:
            model = "gpt-4"

    print(f"\n✓ Using: {provider} - {model}")

    # Extract PDF text
    print(f"\nExtracting text from {Path(pdf_path).name}...")
    if start_page and end_page:
        print(f"Pages: {start_page}-{end_page}")

    text = extract_pdf_text(pdf_path, start_page, end_page)

    if not text or not text.strip():
        return "Error: No text extracted from PDF"

    print(f"Extracted {len(text)} characters")

    # Use agent for orchestration
    pdf_name = Path(pdf_path).name
    agent_prompt = f"""You are a PDF summarizer agent. I have already extracted the text from a PDF.

Your task: Analyze this scientific paper and provide a structured summary.

PDF: {pdf_name}
Provider: {provider}
Model: {model}
Pages: {start_page}-{end_page if end_page else 'end'}

I will now call the {provider} API with the extracted text to generate the summary.
Please wait while I process this...

The summary should include:
a) Summary of main ideas (paragraph form)
b) Detailed methods bullet points"""

    print(f"\nAgent processing with {provider}...")

    # Call the selected provider
    summary = summarize_with_provider(text, pdf_name, provider, model)

    # Save or display
    if output_file:
        with open(output_file, "w") as f:
            f.write(summary)
        print(f"\n✓ Summary saved to: {output_file}")
    else:
        print("\n" + "="*80)
        print("SUMMARY")
        print("="*80 + "\n")
        print(summary)

    return summary


async def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Unified PDF Summarizer Agent - Works with both OpenAI and Anthropic",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python pdf_summarizer_unified_agent.py paper.pdf --pages 1-27

  # Specify provider
  python pdf_summarizer_unified_agent.py paper.pdf --provider anthropic --pages 1-27
  python pdf_summarizer_unified_agent.py paper.pdf --provider openai --model gpt-4-turbo --pages 1-27

  # Save output
  python pdf_summarizer_unified_agent.py paper.pdf --pages 1-27 --output summary.txt
        """
    )
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("--pages", help="Page range (e.g., 1-27)", default=None)
    parser.add_argument("--output", help="Output file path", default=None)
    parser.add_argument(
        "--provider",
        help="AI provider (anthropic or openai)",
        choices=["anthropic", "openai"],
        default=None
    )
    parser.add_argument("--model", help="Specific model to use", default=None)

    args = parser.parse_args()

    # Parse page range
    start_page = None
    end_page = None
    if args.pages:
        try:
            parts = args.pages.split("-")
            start_page = int(parts[0])
            end_page = int(parts[1]) if len(parts) > 1 else None
        except ValueError:
            print(f"Error: Invalid page range: {args.pages}")
            sys.exit(1)

    # Run the agent
    await unified_agent_summarizer(
        args.pdf_path,
        start_page,
        end_page,
        args.provider,
        args.model,
        args.output
    )


if __name__ == "__main__":
    asyncio.run(main())
