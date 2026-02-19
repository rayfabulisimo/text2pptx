# Document to Presentation Toolkit

Transform any document into a beautiful PowerPoint presentation with AI.

---

## ✨ Features

- **Multi-format support:** PDF, DOCX, PPTX, TXT, MD, Images
- **AI-powered summarization:** Intelligent section creation
- **6 beautiful themes:** Modern, professional designs
- **Smart image placement:** Auto-links images to content
- **One command:** Complete automation
- **Fully editable:** Modify in PowerPoint after generation

---

## ⭐ NEW: Interactive Mode

**Want a guided experience?** Use the interactive workflow:

```bash
python interactive_workflow.py
```

This gives you:
- 📁 **File browser** - Navigate and select documents
- 🎨 **Theme builder** - Create custom colors or use presets
- 🖼️ **Background images** - Add custom backgrounds
- 🤖 **AI selection** - Choose provider and model
- ⚙️ **Full control** - All options in friendly menus

**See `INTERACTIVE_GUIDE.md` for complete interactive documentation.**

---

## 🚀 Quick Setup

### 1. Install Dependencies

```bash
pip install anthropic openai pymupdf python-pptx python-docx Pillow
apt-get install poppler-utils
```

### 2. Configure API Keys

**Option A: Use .env file (Recommended)**

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your keys
nano .env
```

Your `.env` file should look like:
```bash
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENAI_API_KEY=sk-your-key-here
```

**.env is automatically ignored by git** - your keys are safe!

**Option B: Environment variables**

```bash
export ANTHROPIC_API_KEY='your-key'
export OPENAI_API_KEY='your-key'
```

### 3. Run!

```bash
python document_to_presentation_workflow.py your_document.pdf
```

---

## 📂 File Structure

```
Essential Files (Keep These):
├── document_analyzer_agent.py              # Multi-format document handler
├── modern_pptx_generator.py                # Beautiful presentation generator
├── document_to_presentation_workflow.py    # Complete workflow (use this!)
├── pdf_summarizer_unified_agent.py         # Alternative: summary only
├── load_env.py                             # Auto-loads .env file
├── skills.md                               # Technical reference
├── COMPLETE_WORKFLOW_GUIDE.md              # User guide
└── README.md                               # This file

Configuration:
├── .env                                    # Your API keys (not in git)
├── .env.example                            # Template for .env
└── .gitignore                              # Protects .env from git
```

---

## 🎨 Available Themes

| Theme | Description | Use Case |
|-------|-------------|----------|
| `ocean` | Deep blue gradient | Professional, corporate |
| `forest` | Deep green tones | Environmental, health |
| `sunset` | Warm orange/coral | Creative, energetic |
| `purple` | Royal purple | Academic, elegant |
| `slate` | Modern gray | Minimalist, tech |
| `coral` | Pink/coral | Warm, friendly |

---

## 📖 Usage Examples

### Basic Usage
```bash
# Simplest - uses defaults
python document_to_presentation_workflow.py paper.pdf

# With page range (for PDFs)
python document_to_presentation_workflow.py paper.pdf --pages 1-27

# With theme
python document_to_presentation_workflow.py paper.pdf --theme purple
```

### Advanced Usage
```bash
# Full customization
python document_to_presentation_workflow.py paper.pdf \
    --pages 1-27 \
    --theme purple \
    --provider anthropic \
    --model claude-opus-4-6 \
    --title "My Research Summary" \
    --output my_presentation.pptx
```

### Different Document Types
```bash
# Word document
python document_to_presentation_workflow.py report.docx --theme forest

# PowerPoint (extract & summarize)
python document_to_presentation_workflow.py slides.pptx --theme ocean

# Markdown file
python document_to_presentation_workflow.py notes.md --theme slate

# Text file
python document_to_presentation_workflow.py transcript.txt --theme coral
```

### Use OpenAI Instead
```bash
python document_to_presentation_workflow.py paper.pdf \
    --provider openai \
    --model gpt-4-turbo \
    --theme sunset
```

---

## 🎯 Your Specific Document

```bash
# Test on first 10 pages
python document_to_presentation_workflow.py \
    "data/input/Pan-cancer scRNA-seq recurring programs cellular heterogeneity Kinker 2020.pdf" \
    --pages 1-10 \
    --theme purple

# Full paper (pages 1-27)
python document_to_presentation_workflow.py \
    "data/input/Pan-cancer scRNA-seq recurring programs cellular heterogeneity Kinker 2020.pdf" \
    --pages 1-27 \
    --theme ocean
```

---

## 🔧 Environment Variables

The `.env` file supports:

```bash
# Required (at least one)
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...

# Optional
CLAUDE_CODE_MAX_OUTPUT_TOKENS=12000
```

**Security:** The `.env` file is in `.gitignore` and will never be committed to git.

---

## 💰 Cost Estimates

For a 27-page PDF (~50K tokens):

| Provider | Model | Cost |
|----------|-------|------|
| Anthropic | Claude Opus 4.6 | $0.25-0.30 |
| Anthropic | Claude Sonnet 4.6 | $0.15-0.20 |
| OpenAI | GPT-4 Turbo | $0.50-0.75 |
| OpenAI | GPT-3.5 Turbo | $0.05-0.10 |

---

## 📊 Output

Running the workflow creates:
```
<document_name>_presentation.pptx
```

The presentation includes:
- **1 title slide** with gradient background
- **2-6 content slides** with:
  - Section title in header bar
  - Bullet points on left
  - Related image on right (if available)
  - Modern design with theme colors

**Fully editable** - open in PowerPoint and customize!

---

## 🐛 Troubleshooting

### "API key not set"
- Check your `.env` file exists
- Verify keys are correctly set
- Or use: `export ANTHROPIC_API_KEY='...'`

### "Package not installed"
```bash
pip install anthropic openai pymupdf python-pptx python-docx Pillow
apt-get install poppler-utils
```

### "No images found"
- Normal for text-only documents
- Some PDFs have non-extractable images
- Presentation will still work without images

### Test .env loading
```bash
python load_env.py
# Should show: ✓ Loaded .env file
```

---

## 📚 Documentation

- **`README.md`** - This file (quick start)
- **`COMPLETE_WORKFLOW_GUIDE.md`** - Detailed guide with all options
- **`skills.md`** - Technical reference

---

## 🎓 How It Works

1. **Document Analysis** → Extracts text and images from any format
2. **AI Summarization** → Creates structured sections with AI
3. **Presentation Generation** → Produces beautiful PowerPoint

**Technologies:**
- PyMuPDF (PDF handling)
- python-docx (Word documents)
- python-pptx (PowerPoint generation)
- Anthropic Claude / OpenAI GPT (AI summarization)

---

## 🆚 What's Different?

This is a **complete rewrite** with:
- ✅ Multi-format support (not just PDF)
- ✅ Modern themes and design
- ✅ Simpler (1 command vs 3)
- ✅ Smarter image handling
- ✅ Better documentation
- ✅ .env file support

Old tools have been removed. This is the new way!

---

## 💡 Tips

1. **Start small** - Test with `--pages 1-10` first
2. **Try themes** - Different themes for different audiences
3. **Edit after** - Generated PPTX is fully editable
4. **Batch process** - Use a loop for multiple documents
5. **Secure keys** - Always use `.env` file, never commit keys

---

## 🚦 Quick Command Reference

```bash
# Most common usage
python document_to_presentation_workflow.py doc.pdf --pages 1-27 --theme purple

# See all options
python document_to_presentation_workflow.py --help

# Test .env setup
python load_env.py
```

---

## 🎉 You're Ready!

1. ✅ Set up `.env` file with your API key
2. ✅ Run: `python document_to_presentation_workflow.py your_doc.pdf`
3. ✅ Open the generated PPTX!

**Questions?** Check `COMPLETE_WORKFLOW_GUIDE.md` for detailed documentation.

---

**Made with Claude Code** 🚀
