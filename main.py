import os
import re
import tkinter as tk
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = os.getenv("APP_TITLE", "CodeCleaner")
DEFAULT_DIR = os.getenv("DEFAULT_DIR", str(Path.home()))


def clean_code(text: str) -> str:
    # Remove trailing whitespace from each line
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    # Collapse multiple blank lines into one
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main():
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry("800x600")

    # TODO: build UI here

    root.mainloop()


if __name__ == "__main__":
    main()
