"""
post_gen_project.py

Automated post-generation hook for cookiecutter-pywebvue.
Bootstraps the Python virtual environment with system site-packages,
scaffolds the Vue/Vite UI via degit, configures relative asset paths,
and initializes a Git repository.
"""

from pathlib import Path
import subprocess
import sys


def main():
    project_root = Path.cwd()
    print(f"\nRunning post-generation setup for {project_root.name}...")

    # 1. Create Python Virtual Environment with system site-packages
    print("Creating Python virtual environment (.venv) with system site-packages...")
    try:
        subprocess.run(
            ["uv", "venv", "--python", "/usr/bin/python3", "--system-site-packages", ".venv"],
            check=True,
        )
        subprocess.run(["uv", "sync"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"WARNING: Virtual environment creation failed: {e}")

    # 2. Scaffold Vite/Vue frontend inside 'ui/' using degit
    print("Scaffolding Vue/Vite application into 'ui/' via degit...")
    try:
        subprocess.run(
            [
                "npx",
                "--yes",
                "degit",
                "vitejs/vite/packages/create-vite/template-vue",
                "ui",
            ],
            check=True,
        )

        # 3. Write custom vite.config.js with base: './' for pywebview
        print("Configuring Vite for relative asset paths (base: './')...")
        ui_dir = project_root / "ui"
        vite_config_path = ui_dir / "vite.config.js"
        vite_config_content = """import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
    plugins: [vue()],
    base: './',
})
"""
        vite_config_path.write_text(vite_config_content, encoding="utf-8")

        print("Installing frontend node modules...")
        subprocess.run(["npm", "install"], cwd=ui_dir, check=True)

    except subprocess.CalledProcessError as e:
        print(
            f"WARNING: Frontend scaffolding or node installation encountered an"
            f" issue: {e}"
        )



    # 4. Initialize Git repository and make initial commit
    print("Initializing Git repository...")
    subprocess.run(["git", "init"], capture_output=True)
    subprocess.run(["git", "add", "README.md", "LICENSE"], capture_output=True)

    name_check = subprocess.run(
        ["git", "config", "user.name"], capture_output=True, text=True
    )
    if not name_check.stdout.strip():
        print(
            "NOTE: Git user.name/email not globally configured. Skipping initial"
            " commit steps."
        )
    else:
        subprocess.run(
            ["git", "commit", "-m", f"docs: initial commit for {project_root.name}"],
            capture_output=True,
        )
        print("Successfully created initial Git commit with README and license!")

        subprocess.run(["git", "add", "."], capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", f"feat: commit project files for {project_root.name}"],
            capture_output=True,
        )
        print("Successfully added project files to git!")

    print(f"\nSUCCESS: Project '{project_root.name}' is fully set up and ready!")
    print("  cd <project-name>")
    print("  ./scripts/build_run.sh\n")


if __name__ == "__main__":
    main()
