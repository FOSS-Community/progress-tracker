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


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Convert a README/Markdown file to HTML"
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Path to the input file, e.g., README.md"
    )
    parser.add_argument(
        "-t", "--title", default="Progress", help="Title of the HTML page"
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output filename (will be saved in dist/ folder), e.g., output.html",
    )
    args = parser.parse_args()

    FILE_NAME = args.input
    TITLE = args.title
    OUTPUT_NAME = (
        Path("dist") / Path(args.output).name
    )  # Only take filename, ignore any folder

    # Ensure output has .html extension
    if not OUTPUT_NAME.suffix:
        OUTPUT_NAME = OUTPUT_NAME.with_suffix(".html")

    # Make sure output folder exists
    OUTPUT_NAME.parent.mkdir(parents=True, exist_ok=True)

    # Check input file exists
    if not Path(FILE_NAME).is_file():
        raise FileNotFoundError(f"The input file does not exist: {FILE_NAME}")

    # Check if npx and node are installed
    if not shutil.which("npx"):
        raise EnvironmentError(
            "`npx` is not installed. Please install Node.js first: https://nodejs.org/"
        )

    if not shutil.which("node"):
        raise EnvironmentError(
            "`node` is not installed or not in PATH. Please install Node.js first: https://nodejs.org/"
        )

    use_shell = sys.platform.startswith("win")  # Needed for Windows

    # Install github-readme-to-html if missing
    try:
        subprocess.run(
            ["npx", "github-readme-to-html", "--version"],
            check=True,
            capture_output=True,
            text=True,
            shell=use_shell,
        )
    except subprocess.CalledProcessError:
        print("Installing 'github-readme-to-html' globally via npm...")
        try:
            subprocess.run(
                ["npm", "install", "-g", "github-readme-to-html"],
                check=True,
                capture_output=True,
                text=True,
                shell=use_shell,
            )
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.stderr}", file=sys.stderr)
            raise RuntimeError(
                f"Failed to install 'github-readme-to-html' (exit code {e.returncode})"
            )

    # Convert README/Markdown to HTML
    print("Converting file, please wait...")
    time.sleep(1)

    try:
        subprocess.run(
            [
                "npx",
                "github-readme-to-html",
                "-i",
                FILE_NAME,
                "-t",
                TITLE,
                "-o",
                str(OUTPUT_NAME.name),
            ],
            check=True,
            capture_output=True,
            text=True,
            shell=use_shell,
        )
        print(f"Conversion successful! HTML saved to: {OUTPUT_NAME}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)
        raise RuntimeError(
            f"Conversion failed (exit code {e.returncode}). Please check your input file and command."
        ) from e


# Entry point
if __name__ == "__main__":
    main()
