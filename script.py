# Simple README to HTML converter
# Run like this:
# python script.py -i README.md -o output.html -t "My Project"
# Output will always go in the 'dist/' folder, so just pass a filename for -o

import argparse
import subprocess
import shutil
import sys
import time
from pathlib import Path

# ------------------------------
# Parse command line arguments
# ------------------------------
parser = argparse.ArgumentParser(description="Convert a README/Markdown file to HTML")
parser.add_argument("-i", "--input", required=True, help="Path to the input file, e.g., README.md")
parser.add_argument("-t", "--title", default="Progress", help="Title of the HTML page")
parser.add_argument("-o", "--output", required=True, help="Output filename (will be saved in dist/ folder), e.g., output.html")
args = parser.parse_args()

FILE_NAME = args.input
TITLE = args.title
OUTPUT_NAME = Path("dist") / Path(args.output).name  # Only take filename, ignore any folder

# Make sure output folder exists
OUTPUT_NAME.parent.mkdir(parents=True, exist_ok=True)

# ------------------------------
# Check input file exists
# ------------------------------
if not Path(FILE_NAME).is_file():
    print(f"Error: The input file does not exist: {FILE_NAME}", file=sys.stderr)
    sys.exit(1)

# ------------------------------
# Check if npx is installed
# ------------------------------
if not shutil.which("npx"):
    print("Error: 'npx' is not installed. Please install Node.js first: https://nodejs.org/", file=sys.stderr)
    sys.exit(1)

use_shell = sys.platform.startswith("win")  # Needed for Windows

# ------------------------------
# Install github-readme-to-html if missing
# ------------------------------
try:
    subprocess.run(
        ["npx", "github-readme-to-html", "--version"],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=use_shell
    )
except subprocess.CalledProcessError:
    print("Installing 'github-readme-to-html' globally via npm...")
    try:
        subprocess.run(["npm", "install", "-g", "github-readme-to-html"], check=True, shell=use_shell)
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to install 'github-readme-to-html' (exit code {e.returncode})", file=sys.stderr)
        sys.exit(e.returncode)

# ------------------------------
# Convert README/Markdown to HTML
# ------------------------------
print("Converting file, please wait...")
time.sleep(1)

try:
    subprocess.run(
        ["npx", "github-readme-to-html", "-i", FILE_NAME, "-t", TITLE, "-o", str(OUTPUT_NAME.name)],
        check=True,
        shell=use_shell
    )
    print(f"Conversion successful! HTML saved to: {OUTPUT_NAME}")
except subprocess.CalledProcessError as e:
    print(f"Error: Conversion failed (exit code {e.returncode}). Please check your input file and command.", file=sys.stderr)
    sys.exit(e.returncode)
