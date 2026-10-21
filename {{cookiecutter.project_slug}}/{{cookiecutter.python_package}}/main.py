"""Main entry point for the pywebview desktop application.

Initializes the application window and points it toward the local UI server
or static production build files.
"""

# /// script
# dependencies = [
#     "pywebview",
# ]
# ///

import argparse
from pathlib import Path

import webview

from {{cookiecutter.python_package}} import Api


def get_target_window_size(scale=0.8):
    """Calculates window size as a percentage of the primary monitor resolution."""
    screen = webview.screens[0]
    width = int(screen.width * scale)
    height = int(screen.height * scale)

    return width, height


def main():
    """Initialize and start the pywebview desktop window."""
    parser = argparse.ArgumentParser(description="Starts the application")
    parser.add_argument("-d", "--debug", action="store_true", help="Open inspection panel.")
    args = parser.parse_args()

    # Initialize API instance
    api = Api()

    win_width, win_height = get_target_window_size(scale=0.8)

    # Get absolute path to the built in dex.html
    dist_path = Path("ui/dist/index.html").resolve().as_uri()

    print(f"Starting desktop window pointing to {dist_path}...")

    _ = webview.create_window(
        title="{{cookiecutter.project_name}}",
        url=dist_path,
        width=win_width,
        height=win_height,
        js_api=api,
    )

    webview.start(debug=args.debug)


if __name__ == "__main__":
  main()
