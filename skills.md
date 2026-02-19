# PDF Summarizer Skills

This directory contains four implementations of a PDF summarizer tool, each using a different approach.

## Available Implementations

### 1. Unified Version (`pdf_summarizer_unified.py`) ⭐ RECOMMENDED
**Works with BOTH OpenAI and Anthropic!**

Interactive agent that lets you choose which AI provider to use at runtime.

**Best for:**
- Flexibility - switch between providers without changing code
- Comparing outputs from different models
- When you have API keys for both providers
- Interactive workflows

**Features:**
- Interactive menu to select provider (OpenAI or Anthropic)
- Choose specific model for each provider
- Or specify via command line: `--provider openai` or `--provider anthropic`
- Automatic API key detection and validation

**Requirements:**
- `pip install anthropic openai` (install both for full flexibility)
- At least one of: `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`

**Usage:**
```bash
# Interactive mode - choose at runtime
python pdf_summarizer_unified.py paper.pdf --pages 1-27

# Command line mode - specify provider
python pdf_summarizer_unified.py paper.pdf --provider openai --model gpt-4-turbo
python pdf_summarizer_unified.py paper.pdf --provider anthropic --model claude-opus-4-6

# Save to file
python pdf_summarizer_unified.py paper.pdf --pages 1-27 --output summary.txt
```

**Interactive Menu Example:**
```
============================================================
PDF SUMMARIZER - Select AI Provider
============================================================

Available providers:
  1. Anthropic (Claude)
  2. OpenAI (GPT)

Select provider (enter number): 2

Available OpenAI models:
  1. gpt-4 (high quality)
  2. gpt-4-turbo (faster, cheaper)
  3. gpt-4o (latest)
  4. gpt-3.5-turbo (fast, economical)

Select model (enter number, or press Enter for default): 2

✓ Selected: openai - gpt-4-turbo
============================================================
```

---

### 2. Anthropic API Version (`pdf_summarizer.py`)
Uses Claude API directly via the Anthropic Python SDK.

**Best for:**
- High-quality, detailed summaries
- Long-form analysis
- Academic paper summarization

**Requirements:**
- `pip install anthropic`
- `ANTHROPIC_API_KEY` environment variable

**Usage:**
```bash
python pdf_summarizer.py paper.pdf --pages 1-27 --output summary.txt
```

---

### 3. OpenAI API Version (`pdf_summarizer_openai.py`)
Uses GPT models via the OpenAI Python SDK.

**Best for:**
- When you already have OpenAI credits
- Fast processing with GPT-4 Turbo
- Cost optimization with GPT-3.5 Turbo

**Requirements:**
- `pip install openai`
- `OPENAI_API_KEY` environment variable

**Usage:**
```bash
# Use default GPT-4
python pdf_summarizer_openai.py paper.pdf --pages 1-27

# Use GPT-4 Turbo for faster processing
python pdf_summarizer_openai.py paper.pdf --pages 1-27 --model gpt-4-turbo

# Use GPT-4o for latest model
python pdf_summarizer_openai.py paper.pdf --pages 1-27 --model gpt-4o
```

---

### 4. Unified Agent Version (`pdf_summarizer_unified_agent.py`) ⭐ AGENT
**Agent-based approach that works with BOTH OpenAI and Anthropic!**

Combines the flexibility of the unified version with agent-based orchestration.

**Best for:**
- Agent-based workflows
- When you want provider flexibility with agent capabilities
- Integration with larger agent systems
- Future extensibility with tools

**Requirements:**
- `pip install claude-agent-sdk anthropic openai`
- At least one of: `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`

**Usage:**
```bash
# Interactive mode
python pdf_summarizer_unified_agent.py paper.pdf --pages 1-27

# Specify provider
python pdf_summarizer_unified_agent.py paper.pdf --provider openai --pages 1-27
python pdf_summarizer_unified_agent.py paper.pdf --provider anthropic --model claude-opus-4-6 --pages 1-27
```

---

### 5. Agent SDK Version (`pdf_summarizer_agent.py`)
Uses Claude Agent SDK (Anthropic only).

**Best for:**
- Pure Anthropic workflows
- When you only need Claude models
- Built-in permission controls

**Requirements:**
- `pip install claude-agent-sdk`
- `ANTHROPIC_API_KEY` environment variable

**Usage:**
```bash
python pdf_summarizer_agent.py paper.pdf --pages 1-27 --output summary.txt
```

---

## Quick Start

### Installation

```bash
# Install system dependencies
apt-get install poppler-utils

# Install Python packages (choose based on which version you want)
pip install anthropic          # For Anthropic API version
pip install openai             # For OpenAI version
pip install claude-agent-sdk   # For Agent SDK version
```

### Set API Keys

```bash
# For Anthropic versions (API and Agent)
export ANTHROPIC_API_KEY='your-anthropic-key'

# For OpenAI version
export OPENAI_API_KEY='your-openai-key'

# Make permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export ANTHROPIC_API_KEY="your-key"' >> ~/.bashrc
source ~/.bashrc
```

---

## Common Parameters

All versions support these parameters:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `pdf_path` | Path to PDF file (required) | `paper.pdf` |
| `--pages` | Page range to summarize | `--pages 1-27` |
| `--output` | Save to file instead of stdout | `--output summary.txt` |
| `--model` | Model to use (OpenAI only) | `--model gpt-4-turbo` |

---

## Output Format

All versions provide structured output with:

### a) Summary of Main Ideas
- Paragraph-form summary
- Key findings
- Biological insights (for scientific papers)
- Clinical relevance (if applicable)

### b) Methods Bullet Points
- Detailed methodology breakdown
- Technical approaches
- Tools and technologies used
- Analysis methods

---

## Examples

### Summarize entire PDF
```bash
python pdf_summarizer.py research_paper.pdf
```

### Summarize specific pages
```bash
python pdf_summarizer.py research_paper.pdf --pages 1-10
```

### Save to file
```bash
python pdf_summarizer.py research_paper.pdf --pages 1-27 --output summary.txt
```

### Use different model (OpenAI version)
```bash
python pdf_summarizer_openai.py paper.pdf --model gpt-3.5-turbo  # Cheaper, faster
python pdf_summarizer_openai.py paper.pdf --model gpt-4          # Default
python pdf_summarizer_openai.py paper.pdf --model gpt-4-turbo    # Faster GPT-4
python pdf_summarizer_openai.py paper.pdf --model gpt-4o         # Latest model
```

---

## Comparison

| Feature | Unified Script | Unified Agent | Anthropic API | OpenAI API | Agent SDK |
|---------|---------------|---------------|--------------|------------|-----------|
| **Flexibility** | ⭐ Both providers | ⭐ Both providers | Anthropic only | OpenAI only | Anthropic only |
| **Architecture** | Script | Agent | Script | Script | Agent |
| **Quality** | Excellent | Excellent | Excellent | Excellent | Excellent |
| **Speed** | Fast | Fast | Fast | Very Fast (GPT-4 Turbo) | Fast |
| **Cost** | Variable | Variable | $5-25/1M tokens | $1-30/1M tokens | $5-25/1M tokens |
| **Max Context** | 200K/128K | 200K/128K | 200K tokens | 128K tokens (GPT-4) | 200K tokens |
| **Model Options** | All models | All models | Claude Opus 4.6 | GPT-4, GPT-4 Turbo, GPT-3.5 | Claude Opus 4.6 |
| **Interactive** | ✓ Yes | ✓ Yes | No | No | No |
| **Extensibility** | Code-based | Agent-based | Code-based | Code-based | Agent-based |
| **Setup Complexity** | Simple | Simple | Simple | Simple | Simple |

---

## Cost Estimates

For a typical 27-page scientific paper (~50,000 input tokens, ~2,000 output tokens):

| Implementation | Model | Estimated Cost |
|----------------|-------|----------------|
| Unified | Claude Opus 4.6 | $0.25 - $0.30 |
| Unified | GPT-4 | $1.50 - $2.00 |
| Unified | GPT-4 Turbo | $0.50 - $0.75 |
| Unified | GPT-3.5 Turbo | $0.05 - $0.10 |
| Anthropic API | Claude Opus 4.6 | $0.25 - $0.30 |
| OpenAI API | GPT-4 | $1.50 - $2.00 |
| OpenAI API | GPT-4 Turbo | $0.50 - $0.75 |
| OpenAI API | GPT-3.5 Turbo | $0.05 - $0.10 |
| Agent SDK | Claude Opus 4.6 | $0.25 - $0.30 |

---

## Troubleshooting

### "pdftotext not found"
```bash
apt-get install poppler-utils
```

### "API key not set"
```bash
export ANTHROPIC_API_KEY='your-key'
# or
export OPENAI_API_KEY='your-key'
```

### "No text extracted from PDF"
- PDF might be image-based (scanned) - needs OCR
- Try opening the PDF manually to verify it contains text
- Check if the page range is valid

### "anthropic/openai package not installed"
```bash
pip install anthropic
# or
pip install openai
```

### Agent SDK: "Claude Code CLI not found"
```bash
pip install claude-agent-sdk
```

---

## Advanced Usage

### Batch Processing Multiple PDFs

```bash
#!/bin/bash
# Process all PDFs in a directory

for pdf in data/input/*.pdf; do
    echo "Processing: $pdf"
    python pdf_summarizer.py "$pdf" --output "summaries/$(basename "$pdf" .pdf).txt"
done
```

### Custom Prompts

To modify the summarization prompt, edit the `prompt` variable in the respective Python file:

```python
# In pdf_summarizer.py, pdf_summarizer_openai.py, or pdf_summarizer_agent.py
prompt = f"""Your custom prompt here...

{text}
"""
```

### Integration with Other Tools

```python
from pdf_summarizer_agent import summarize_pdf_with_agent
import asyncio

async def my_workflow():
    summary = await summarize_pdf_with_agent(
        "paper.pdf",
        start_page=1,
        end_page=27
    )
    # Process summary further
    print(summary)

asyncio.run(my_workflow())
```

---

## Contributing

To add new features:

1. **Add parameters** - Update `argparse` section
2. **Modify prompt** - Edit the prompt template
3. **Change output format** - Modify the output processing section
4. **Add new model support** - Update model choices (OpenAI version)

---

## License

These tools are provided as-is for educational and research purposes.

---

---

## 🆕 PowerPoint Generation Workflow

### NEW: PDF to PPTX Pipeline

Three new agents that work together to create PowerPoint presentations from PDFs:

#### **1. Figure Linker Agent** (`figure_linker_agent.py`)
Extracts figures from PDF and links them to summary points using AI.

**Usage:**
```bash
python figure_linker_agent.py paper.pdf summary.txt --pages 1-27 --output mappings.json
```

#### **2. PPTX Generator Agent** (`pptx_generator_agent.py`)
Creates editable PowerPoint with text and figures, smart image sizing.

**Usage:**
```bash
python pptx_generator_agent.py mappings.json paper.pdf --output presentation.pptx
```

#### **3. Complete Workflow** (`pdf_to_pptx_workflow.py`) ⭐ RECOMMENDED
Runs all steps automatically: Summarize → Link Figures → Generate PPTX

**Usage:**
```bash
# One command does everything!
python pdf_to_pptx_workflow.py paper.pdf --pages 1-27
```

**Features:**
- Automatic figure extraction from PDF
- AI-powered figure-summary linking
- Smart image sizing (preserves aspect ratio)
- Fully editable PowerPoint output
- Works with both Anthropic and OpenAI

**Requirements:**
```bash
pip install pymupdf python-pptx Pillow
```

**See `README_PPTX_WORKFLOW.md` for complete documentation.**

---

## Support

For issues or questions:
- Check `README_PDF_SUMMARIZER.md` for PDF summarizer documentation
- Check `README_PPTX_WORKFLOW.md` for PowerPoint generation documentation
- Check `QUICK_START.md` for quick reference
- Verify API keys are set correctly
- Ensure all dependencies are installed
- Check that the PDF contains extractable text and images
