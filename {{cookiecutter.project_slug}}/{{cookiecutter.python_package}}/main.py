"""Main entry point for the pywebview desktop application.

Initializes the application window and points it toward the local UI server
or static production build files.
"""

# /// script
# dependencies = [
#     "pywebview",
# ]
# ///

import sys
from pathlib import Path

import webview


def main():
  """Initialize and start the pywebview desktop window."""
  # Get absolute path to the built index.html
  dist_path = Path("ui/dist/index.html").resolve().as_uri()

  print(f"Starting desktop window pointing to {dist_path}...")

  window = webview.create_window(
      title="{{cookiecutter.project_name}}",
      url=dist_path,
      width=1200,
      height=800,
  )

  webview.start(debug=True)


if __name__ == "__main__":
  main()
