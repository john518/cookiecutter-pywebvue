# /// script
# dependencies = [
#     "cookiecutter",
# ]
# ///

from pathlib import Path
import sys

exe = sys.executable
print(f"sys.executable: {exe}")

path = Path(exe).resolve()
print(f"Path resolved: {path}")
