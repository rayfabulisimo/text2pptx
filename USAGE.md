# How to Use This Agent

## 📁 What You Have (10 files)

```
Core Agent (3 files):
├── interactive_workflow.py           ⭐ USE THIS!
├── document_analyzer_agent.py        (helper)
└── modern_pptx_generator.py          (helper)

Alternative Tools:
├── document_to_presentation_workflow.py  (command-line mode)
├── pdf_summarizer_unified_agent.py       (summary-only)
├── theme_builder.py                      (theme utilities)
└── load_env.py                           (auto-loads .env)

Documentation:
├── README.md                         (quick start)
├── INTERACTIVE_GUIDE.md              (detailed guide)
└── skills.md                         (technical reference)
```

---

## 🚀 Quick Start (3 Steps)

### Step 1: Set Up API Key (One Time)

```bash
# Create .env file
cp .env.example .env

# Add your API key
nano .env
# Add line: ANTHROPIC_API_KEY=sk-ant-your-key-here
# Save and exit (Ctrl+X, Y, Enter)
```

### Step 2: Run the Agent

```bash
python interactive_workflow.py
```

### Step 3: Follow the Menus

The agent will guide you through:
1. **Select document** - Browse and choose your file
2. **Page range** - Specify pages (PDFs only)
3. **AI provider** - Choose Anthropic or OpenAI
4. **Theme** - Pick a color theme or create custom
5. **Title** - Set presentation title
6. **Confirm** - Review and generate!

**Done!** Your presentation is created.

---

## 💡 Example Session

```
$ python interactive_workflow.py

[Step 1/5] Select your document
Current directory: /root/capsule
Files:
  1. data/input/paper.pdf
> 1

[Step 2/5] Page range
Page range: 1-10

[Step 3/5] AI provider
1. Anthropic
> 1
Model: (Enter for default)
> Enter

[Step 4/5] Theme
1. Ocean Blue
2. Forest Green
3. Royal Purple
> 3

[Step 5/5] Title
Title: My Research Summary
> My Research Summary

Review:
✓ Document: paper.pdf
✓ Pages: 1-10
✓ Provider: anthropic
✓ Theme: Royal Purple
✓ Title: My Research Summary

Proceed? (y/n): y

[Generating...]
✓ Complete! Open: paper_presentation.pptx
```

---

## 🎨 Choosing Themes

### Built-in Themes (Easy)
1. **Ocean Blue** - Corporate, professional
2. **Forest Green** - Environmental, nature
3. **Sunset Orange** - Creative, warm
4. **Royal Purple** - Academic, elegant
5. **Modern Slate** - Minimalist, tech
6. **Coral Pink** - Friendly, approachable

### Custom Themes (Advanced)
Choose option 7 to create custom:
- **RGB colors** - Enter: `R G B` (0-255)
  - Example: `255 87 34` = Deep orange
- **Presets** - 6 quick professional palettes

---

## ⚡ Command-Line Mode (Advanced)

For automation or quick generation:

```bash
python document_to_presentation_workflow.py \
    your_document.pdf \
    --pages 1-27 \
    --theme purple \
    --title "My Presentation"
```

All options:
```bash
--pages 1-27              # Page range
--provider anthropic      # or openai
--model claude-opus-4-6   # Specific model
--theme purple            # Color theme
--title "Custom Title"    # Presentation title
--output custom.pptx      # Output filename
```

---

## 📄 Supported File Types

✅ **PDF** - Scientific papers, reports
✅ **Word** - .docx, .doc files
✅ **PowerPoint** - .pptx, .ppt files
✅ **Text** - .txt, .md files
✅ **Images** - .png, .jpg, .jpeg

---

## 🔧 Configuration

### API Keys (.env file)

```bash
# Required (at least one)
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...

# Optional
CLAUDE_CODE_MAX_OUTPUT_TOKENS=12000
```

### Get API Keys
- **Anthropic:** https://console.anthropic.com/
- **OpenAI:** https://platform.openai.com/

---

## 💰 Cost

For a 27-page PDF:
- **Anthropic Opus:** $0.25-0.30
- **Anthropic Sonnet:** $0.15-0.20
- **OpenAI GPT-4 Turbo:** $0.50-0.75

---

## 🐛 Troubleshooting

### "API key not set"
```bash
# Check your .env file
cat .env
# Should show: ANTHROPIC_API_KEY=sk-ant-...

# Test loading
python load_env.py
# Should show: ✓ Loaded .env file
```

### "Package not installed"
```bash
pip install anthropic openai pymupdf python-pptx python-docx Pillow
```

### "File not found"
- Use absolute path: `/full/path/to/file.pdf`
- Or navigate using the file browser

---

## 📊 What You Get

Generated `.pptx` file with:
- **1 title slide** (gradient background, theme colors)
- **2-6 content slides** (bullets + images)
- **Fully editable** in PowerPoint
- **Modern design** with your theme

---

## 🎓 Tips

1. **Test with small range first:** `--pages 1-5`
2. **Try different themes** to find your favorite
3. **Edit in PowerPoint** after generation
4. **Use .env file** for API keys (safer)

---

## 📚 More Help

- **Quick start:** See `README.md`
- **Interactive details:** See `INTERACTIVE_GUIDE.md`
- **Technical:** See `skills.md`

---

## ✅ Quick Checklist

- [ ] Install packages
- [ ] Create `.env` file
- [ ] Add API key
- [ ] Test: `python load_env.py`
- [ ] Run: `python interactive_workflow.py`
- [ ] Follow menus
- [ ] Get presentation!

---

**That's it! Start creating presentations now:** 🚀

```bash
python interactive_workflow.py
```
