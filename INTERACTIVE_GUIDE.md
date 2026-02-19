# Interactive Workflow Guide

## 🎯 What's New

The **interactive workflow** lets you:
- ✅ **Browse and select** your documents interactively
- ✅ **Choose themes** from beautiful presets
- ✅ **Create custom themes** with your own colors
- ✅ **Use background images** for your slides
- ✅ **Specify page ranges** (for PDFs)
- ✅ **Select AI provider** and model
- ✅ **Set custom titles**

All through a user-friendly menu system!

---

## 🚀 Quick Start

### Run Interactive Mode

```bash
python interactive_workflow.py
```

That's it! The script will guide you through:
1. File selection
2. Page range (PDFs only)
3. AI provider selection
4. Theme customization
5. Title customization

---

## 📖 Step-by-Step Walkthrough

### Step 1: File Selection

```
[Step 1/5] Select your document
Starting directory (or Enter for current):

Current directory: /root/capsule
============================================================

Directories:
  0. .. (parent directory)
  1. data/

Files:
  2. paper.pdf (1245.3 KB)
  3. report.docx (523.1 KB)

Options:
  • Enter number to select
  • Type 'q' to quit
  • Type path directly (e.g., /path/to/file.pdf)

>
```

**You can:**
- Enter a number to navigate directories or select files
- Type a full path: `/path/to/your/document.pdf`
- Press `0` to go to parent directory
- Press `q` to quit

---

### Step 2: Page Range (PDF only)

```
[Step 2/5] PAGE RANGE (PDF only)
============================================================

Options:
  • Press Enter for all pages
  • Enter range (e.g., 1-27)
  • Enter single page (e.g., 5)

Page range:
```

**Examples:**
- `1-27` - Pages 1 through 27
- `10-50` - Pages 10 through 50
- `5` - Only page 5
- `Enter` - All pages

---

### Step 3: AI Provider

```
[Step 3/5] AI PROVIDER SELECTION
============================================================

Available providers:
  1. Anthropic
  2. Openai

Select provider: 1

Anthropic models:
  1. Claude Opus 4.6 (best quality, recommended)
  2. Claude Sonnet 4.6 (balanced)
  3. Claude Haiku 4.5 (fast, economical)

Select model (or Enter for default):
```

**Choose your AI:**
- **Anthropic:** Claude models (Opus, Sonnet, Haiku)
- **OpenAI:** GPT models (GPT-4, GPT-4 Turbo, GPT-3.5)

---

### Step 4: Theme Selection

```
[Step 4/5] SELECT PRESENTATION THEME
============================================================

Built-in Themes:
  1. Ocean Blue
  2. Forest Green
  3. Sunset Orange
  4. Royal Purple
  5. Modern Slate
  6. Coral Pink
  7. Create Custom Theme

Select theme (number):
```

#### Option A: Built-in Themes

Choose 1-6 for professional preset themes.

#### Option B: Custom Theme

```
Select theme: 7

CUSTOM THEME BUILDER
============================================================

You can either:
  1. Use a color preset
  2. Specify custom RGB colors

Choice (1 or 2):
```

**Color Preset Option:**
```
Color Presets:
  1. Professional Blue (#0D47A1)
  2. Nature Green (#1B5E20)
  3. Bold Red (#B71C1C)
  4. Modern Teal (#00695C)
  5. Deep Indigo (#1A237E)
  6. Warm Amber (#FF6F00)
```

**Custom RGB Option:**
```
Enter RGB values for your primary color (0-255)
Example: 13 71 161 (for deep blue)

RGB values (R G B): 255 87 34

✓ Primary color: RGB(255, 87, 34)
```

---

### Step 5: Custom Title

```
[Step 5/5] PRESENTATION TITLE
============================================================

Options:
  • Press Enter for auto-generated title
  • Type custom title

Title:
```

**Examples:**
- `My Research Summary`
- `Q4 2024 Report`
- `Project Overview`
- `Enter` for auto-generated title

---

### Final Confirmation

```
REVIEW YOUR CHOICES
============================================================
Document: data/input/paper.pdf
Pages: 1-27
Provider: anthropic (claude-opus-4-6)
Theme: Royal Purple
Title: My Research Summary
============================================================

Proceed? (y/n):
```

Type `y` to generate, `n` to cancel.

---

## 🎨 Theme System

### Built-in Themes

| Theme | Colors | Best For |
|-------|--------|----------|
| Ocean Blue | Deep blue, light blue | Corporate, professional |
| Forest Green | Deep green, light green | Environmental, health |
| Sunset Orange | Orange, coral | Creative, energetic |
| Royal Purple | Deep purple, lavender | Academic, elegant |
| Modern Slate | Gray, slate | Minimalist, tech |
| Coral Pink | Coral pink, rose | Warm, friendly |

### Custom Theme Options

#### 1. Color Presets
Quick preset colors for common use cases:
- Professional Blue
- Nature Green
- Bold Red
- Modern Teal
- Deep Indigo
- Warm Amber

#### 2. RGB Custom Colors
Specify exact colors using RGB values (0-255):
```
RGB values: 255 87 34  → Deep Orange
RGB values: 33 150 243 → Light Blue
RGB values: 76 175 80  → Green
```

**Color Generator Tools:**
- Google "RGB color picker"
- Use: https://rgbcolorcode.com/
- Or your design tool (Photoshop, Figma, etc.)

### Background Images (Advanced)

You can also use background images! Edit your theme:

```python
# In theme_builder.py
theme = create_theme_from_image(
    image_path="path/to/background.jpg",
    name="My Custom Theme"
)
```

---

## 💡 Usage Tips

### 1. Start Simple
First time? Use:
- Default file path (current directory)
- Built-in theme (Ocean or Purple)
- Default model

### 2. Test Small First
For large PDFs:
- Start with `--pages 1-10`
- Review output
- Then run full document

### 3. Color Harmony
When creating custom themes:
- **Contrasting colors:** Dark primary + light background
- **Complementary colors:** Use color wheel
- **Brand colors:** Match your company palette

### 4. Background Images
For background images:
- Use high-res images (1920x1080+)
- Subtle patterns work best
- Avoid busy images (text readability)
- Light images for dark text, vice versa

---

## 🔧 Advanced Examples

### Example 1: Corporate Blue Theme
```
Theme choice: Custom RGB
RGB values: 0 71 171
✓ Creates deep corporate blue theme
```

### Example 2: Academic Purple
```
Theme choice: Built-in
Select: 4 (Royal Purple)
✓ Perfect for academic presentations
```

### Example 3: Nature Presentation
```
Theme choice: Built-in
Select: 2 (Forest Green)
✓ Great for environmental topics
```

---

## 🎯 Complete Example Session

```bash
python interactive_workflow.py

# Step 1: Select file
Starting directory: data/input
> 1  (selects paper.pdf)

# Step 2: Page range
Page range: 1-27

# Step 3: AI Provider
Select provider: 1 (Anthropic)
Select model: 1 (Claude Opus 4.6)

# Step 4: Theme
Select theme: 4 (Royal Purple)

# Step 5: Title
Title: Cancer Cell Line Analysis

# Confirm
Proceed? y

# Result
✓ presentation generated!
```

---

## 🔄 Non-Interactive Mode

Prefer command-line? Use the original workflow:

```bash
python document_to_presentation_workflow.py paper.pdf \
    --pages 1-27 \
    --theme purple \
    --title "My Presentation"
```

---

## 📊 Output

Generated presentations include:
- **Title slide** with theme colors
- **Content slides** with:
  - Section headers
  - Bullet points
  - Related images (auto-linked)
  - Professional styling

**Fully editable** in PowerPoint!

---

## 🐛 Troubleshooting

### "No API keys found"
**Solution:** Set up your `.env` file:
```bash
cp .env.example .env
nano .env  # Add your keys
```

### "File not found"
**Solution:**
- Check the path you entered
- Try browsing from root: `/`
- Or provide absolute path

### Theme not applied
**Solution:**
- Custom themes require RGB values (0-255)
- Check you entered three numbers
- Try a built-in theme first

### Background image not showing
**Solution:**
- Check image path is correct
- Use PNG or JPG format
- Image should be high resolution
- python-pptx has limitations with backgrounds

---

## 📚 See Also

- **`COMPLETE_WORKFLOW_GUIDE.md`** - Complete workflow documentation
- **`README.md`** - Quick start guide
- **`theme_builder.py`** - Theme creation utilities

---

## ✨ Features Summary

✅ Interactive file browser
✅ 6 built-in professional themes
✅ Custom color themes (RGB)
✅ Color presets for quick selection
✅ Background image support
✅ AI provider selection
✅ Model selection
✅ Page range specification
✅ Custom titles
✅ Confirmation before generation
✅ User-friendly menus

---

**Ready to create beautiful presentations!** 🎉

Start with:
```bash
python interactive_workflow.py
```
