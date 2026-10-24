"""
pre_prompt.py

Automated pre-prompt hook for cookiecutter-pywebvue.
Validates that prerequisites are available for the pywebview cookiecutter.
"""


import sys
import subprocess

def is_node_installed() -> bool:
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    if not is_node_installed():
        print("ERROR: node is not installed or not found.")
        sys.exit(1)
