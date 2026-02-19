#!/usr/bin/env python3
"""
Load environment variables from .env file
"""
import os
from pathlib import Path


def load_env():
    """Load .env file if it exists."""
    env_file = Path(__file__).parent / ".env"

    if not env_file.exists():
        return False

    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()

            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue

            # Parse KEY=value
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()

                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]

                # Set environment variable
                os.environ[key] = value

    return True


if __name__ == "__main__":
    if load_env():
        print("✓ Loaded .env file")
        print(f"  ANTHROPIC_API_KEY: {'set' if os.environ.get('ANTHROPIC_API_KEY') else 'not set'}")
        print(f"  OPENAI_API_KEY: {'set' if os.environ.get('OPENAI_API_KEY') else 'not set'}")
    else:
        print("No .env file found")
