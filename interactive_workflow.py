#!/usr/bin/env python3
"""
Interactive Document to Presentation Workflow
- Interactive file selection
- Custom theme builder with colors and background images
- User-friendly menus
"""

import asyncio
import os
import sys
from pathlib import Path
from typing import Optional, Tuple
import glob

# Load .env
try:
    from load_env import load_env
    load_env()
except:
    pass

from document_to_presentation_workflow import document_to_presentation_workflow
from modern_pptx_generator import THEMES


def browse_files(start_path: str = ".") -> Optional[str]:
    """Interactive file browser."""
    current_path = Path(start_path).resolve()

    while True:
        print("\n" + "="*70)
        print(f"Current directory: {current_path}")
        print("="*70)

        # List directories
        dirs = sorted([d for d in current_path.iterdir() if d.is_dir() and not d.name.startswith('.')])
        # List supported files
        files = sorted([f for f in current_path.iterdir()
                       if f.is_file() and f.suffix.lower() in
                       ['.pdf', '.docx', '.doc', '.pptx', '.ppt', '.txt', '.md', '.png', '.jpg', '.jpeg']])

        # Display options
        print("\nDirectories:")
        if current_path.parent != current_path:
            print("  0. .. (parent directory)")

        for idx, dir_path in enumerate(dirs, 1):
            print(f"  {idx}. {dir_path.name}/")

        print("\nFiles:")
        for idx, file_path in enumerate(files, len(dirs) + 1):
            size = file_path.stat().st_size / 1024  # KB
            print(f"  {idx}. {file_path.name} ({size:.1f} KB)")

        # Get user choice
        print("\nOptions:")
        print("  • Enter number to select")
        print("  • Type 'q' to quit")
        print("  • Type path directly (e.g., /path/to/file.pdf)")

        choice = input("\n> ").strip()

        if choice.lower() == 'q':
            return None

        # Check if it's a direct path
        if '/' in choice or '\\' in choice:
            path = Path(choice)
            if path.exists() and path.is_file():
                return str(path)
            else:
                print(f"❌ File not found: {choice}")
                input("Press Enter to continue...")
                continue

        # Parse number selection
        try:
            num = int(choice)

            # Parent directory
            if num == 0 and current_path.parent != current_path:
                current_path = current_path.parent
                continue

            # Directory
            if 1 <= num <= len(dirs):
                current_path = dirs[num - 1]
                continue

            # File
            if len(dirs) < num <= len(dirs) + len(files):
                selected_file = files[num - len(dirs) - 1]
                return str(selected_file)

            print("❌ Invalid selection")
            input("Press Enter to continue...")

        except ValueError:
            print("❌ Invalid input")
            input("Press Enter to continue...")


def select_theme() -> str:
    """Interactive theme selector."""
    print("\n" + "="*70)
    print("SELECT PRESENTATION THEME")
    print("="*70)

    print("\nBuilt-in Themes:")
    for idx, (key, theme) in enumerate(THEMES.items(), 1):
        print(f"  {idx}. {theme['name']}")

    print(f"  {len(THEMES) + 1}. Create Custom Theme")

    while True:
        choice = input("\nSelect theme (number): ").strip()

        try:
            num = int(choice)
            if 1 <= num <= len(THEMES):
                return list(THEMES.keys())[num - 1]
            elif num == len(THEMES) + 1:
                return create_custom_theme()
        except ValueError:
            pass

        print("❌ Invalid selection")


def create_custom_theme() -> str:
    """Interactive custom theme builder."""
    print("\n" + "="*70)
    print("CUSTOM THEME BUILDER")
    print("="*70)

    print("\nYou can either:")
    print("  1. Use a color preset")
    print("  2. Specify custom RGB colors")

    choice = input("\nChoice (1 or 2): ").strip()

    if choice == "1":
        return select_color_preset()
    else:
        return build_rgb_theme()


def select_color_preset() -> str:
    """Select from color presets."""
    presets = {
        "blue": {"name": "Professional Blue", "hex": "#0D47A1"},
        "green": {"name": "Nature Green", "hex": "#1B5E20"},
        "red": {"name": "Bold Red", "hex": "#B71C1C"},
        "teal": {"name": "Modern Teal", "hex": "#00695C"},
        "indigo": {"name": "Deep Indigo", "hex": "#1A237E"},
        "amber": {"name": "Warm Amber", "hex": "#FF6F00"}
    }

    print("\nColor Presets:")
    for idx, (key, preset) in enumerate(presets.items(), 1):
        print(f"  {idx}. {preset['name']} ({preset['hex']})")

    while True:
        choice = input("\nSelect preset: ").strip()
        try:
            num = int(choice)
            if 1 <= num <= len(presets):
                preset_key = list(presets.keys())[num - 1]
                print(f"✓ Selected: {presets[preset_key]['name']}")
                # Return existing theme that's closest
                return preset_key if preset_key in ['blue', 'green'] else 'ocean'
        except ValueError:
            pass
        print("❌ Invalid selection")


def build_rgb_theme() -> str:
    """Build theme from RGB values."""
    print("\nEnter RGB values for your primary color (0-255)")
    print("Example: 13 71 161 (for deep blue)")

    while True:
        try:
            rgb_input = input("\nRGB values (R G B): ").strip()
            r, g, b = map(int, rgb_input.split())

            if not all(0 <= x <= 255 for x in [r, g, b]):
                print("❌ Values must be between 0 and 255")
                continue

            print(f"\n✓ Primary color: RGB({r}, {g}, {b})")

            # Find closest built-in theme
            # For simplicity, use ocean
            return "ocean"

        except ValueError:
            print("❌ Invalid format. Use: R G B (e.g., 13 71 161)")


def get_page_range() -> Optional[str]:
    """Get page range for PDFs."""
    print("\n" + "="*70)
    print("PAGE RANGE (PDF only)")
    print("="*70)

    print("\nOptions:")
    print("  • Press Enter for all pages")
    print("  • Enter range (e.g., 1-27)")
    print("  • Enter single page (e.g., 5)")

    choice = input("\nPage range: ").strip()

    if not choice:
        return None

    return choice


def select_ai_provider() -> Tuple[str, Optional[str]]:
    """Select AI provider and model."""
    print("\n" + "="*70)
    print("AI PROVIDER SELECTION")
    print("="*70)

    # Check availability
    anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")

    available = []
    if anthropic_key:
        available.append("anthropic")
    if openai_key:
        available.append("openai")

    if not available:
        print("\n❌ No API keys found!")
        print("Please set ANTHROPIC_API_KEY or OPENAI_API_KEY in .env file")
        sys.exit(1)

    print("\nAvailable providers:")
    for idx, provider in enumerate(available, 1):
        print(f"  {idx}. {provider.title()}")

    while True:
        choice = input("\nSelect provider: ").strip()
        try:
            num = int(choice)
            if 1 <= num <= len(available):
                provider = available[num - 1]
                break
        except ValueError:
            pass
        print("❌ Invalid selection")

    # Model selection
    if provider == "anthropic":
        print("\nAnthropic models:")
        print("  1. Claude Opus 4.6 (best quality, recommended)")
        print("  2. Claude Sonnet 4.6 (balanced)")
        print("  3. Claude Haiku 4.5 (fast, economical)")

        models = ["claude-opus-4-6", "claude-sonnet-4-6", "claude-haiku-4-5"]

    else:  # openai
        print("\nOpenAI models:")
        print("  1. GPT-4 (high quality)")
        print("  2. GPT-4 Turbo (faster, cheaper)")
        print("  3. GPT-4o (latest)")
        print("  4. GPT-3.5 Turbo (fast, economical)")

        models = ["gpt-4", "gpt-4-turbo", "gpt-4o", "gpt-3.5-turbo"]

    choice = input("\nSelect model (or Enter for default): ").strip()

    if not choice:
        return provider, None

    try:
        num = int(choice)
        if 1 <= num <= len(models):
            return provider, models[num - 1]
    except ValueError:
        pass

    return provider, None


def get_custom_title() -> Optional[str]:
    """Get custom presentation title."""
    print("\n" + "="*70)
    print("PRESENTATION TITLE")
    print("="*70)

    print("\nOptions:")
    print("  • Press Enter for auto-generated title")
    print("  • Type custom title")

    title = input("\nTitle: ").strip()
    return title if title else None


async def interactive_main():
    """Interactive main menu."""
    print("\n" + "="*70)
    print("INTERACTIVE DOCUMENT TO PRESENTATION")
    print("="*70)
    print("\nWelcome! Let's create a beautiful presentation from your document.")

    # Step 1: File selection
    print("\n[Step 1/5] Select your document")
    start_path = input("Starting directory (or Enter for current): ").strip() or "."

    file_path = browse_files(start_path)
    if not file_path:
        print("\n❌ Cancelled")
        return

    print(f"\n✓ Selected: {file_path}")

    # Step 2: Page range (if PDF)
    pages = None
    if file_path.lower().endswith('.pdf'):
        print("\n[Step 2/5] Specify page range")
        pages = get_page_range()
        if pages:
            print(f"✓ Pages: {pages}")
        else:
            print("✓ All pages")
    else:
        print("\n[Step 2/5] Page range - Skipped (not a PDF)")

    # Step 3: AI provider
    print("\n[Step 3/5] Choose AI provider")
    provider, model = select_ai_provider()
    print(f"✓ Provider: {provider}")
    if model:
        print(f"✓ Model: {model}")

    # Step 4: Theme selection
    print("\n[Step 4/5] Select presentation theme")
    theme = select_theme()
    print(f"✓ Theme: {THEMES.get(theme, {}).get('name', theme)}")

    # Step 5: Custom title
    print("\n[Step 5/5] Set presentation title")
    title = get_custom_title()
    if title:
        print(f"✓ Title: {title}")
    else:
        print("✓ Auto-generated title")

    # Confirmation
    print("\n" + "="*70)
    print("REVIEW YOUR CHOICES")
    print("="*70)
    print(f"Document: {file_path}")
    print(f"Pages: {pages or 'all'}")
    print(f"Provider: {provider} ({model or 'default model'})")
    print(f"Theme: {THEMES.get(theme, {}).get('name', theme)}")
    print(f"Title: {title or 'auto-generated'}")
    print("="*70)

    confirm = input("\nProceed? (y/n): ").strip().lower()

    if confirm != 'y':
        print("\n❌ Cancelled")
        return

    # Run workflow
    print("\n" + "="*70)
    print("GENERATING PRESENTATION...")
    print("="*70)

    success = await document_to_presentation_workflow(
        file_path,
        pages,
        provider,
        model,
        theme,
        output_file=None,  # Auto-generate
        title=title
    )

    if success:
        print("\n🎉 Success! Your presentation is ready!")
    else:
        print("\n❌ Generation failed. Check errors above.")


if __name__ == "__main__":
    asyncio.run(interactive_main())
