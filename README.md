# cookiecutter-pywebvue

`cookiecutter-pywebvue` is a lightweight, high-performance Cookiecutter template for bootstrapping custom desktop applications using **Python (`pywebview`)** and a **Vue.js / Vite** frontend. 

It is designed as a modern, resource-efficient alternative to heavy Electron-based desktop apps, leveraging native OS web-rendering bindings and fast modern tooling.

---

## Key Features

- **Native OS Rendering:** Uses `pywebview` to render the web UI via native system web-view bindings, bypassing the very large memory and disk footprint of Electron.
- **Modern Reactive Frontend:** Pre-configured with **Vue.js** and **Vite** inside a clean `ui/` directory.
- **Automated Post-Generation Hooks:** Automatically sets up your Python virtual environment (`uv`), scaffolds the frontend via `degit`, installs node packages, and initializes a Git repository on creation.
- **Fast Python Tooling:** Built from the ground up to integrate seamlessly with **`uv`** for lightning-fast dependency management and virtual environments.

---

## Tech Stack

- **Backend:** Python 3.10+ with `pywebview`
- **Frontend:** Vue.js / Vite (`ui/`)
- **Package Management & Orchestration:** `uv`
- **Frontend Scaffolding:** `degit` & `npm`

---

## Prerequisites

Before generating a project from this template, ensure you have the following installed on your system:
- **Python 3.10+**
- **`uv`** (Fast Python package installer and resolver)
- **Node.js & npm** (For frontend asset compilation)

---

## Quickstart

To create a new desktop application from this template, run the following command using `uvx` (or standard `cookiecutter`):

```bash
uvx cookiecutter [https://github.com/john518/cookiecutter-pywebvue](https://github.com/john518/cookiecutter-pywebvue)

```

You will be prompted to enter your project details:

1. **`project_name`**: Human-readable name (e.g., `My Desktop App`)
2. **`project_slug`**: Clean directory name (auto-derived, e.g., `my-desktop-app`)
3. **`python_package`**: Safe Python module name (auto-derived, e.g., `my_desktop_app`)

Once completed, the post-generation hook will automatically:

* Create a `.venv` using `uv venv --system-site-packages` (ensuring access to native OS graphics/rendering bindings).
* Scaffold the Vue/Vite template into `ui/` via `degit`.
* Inject `base: './'` into `ui/vite.config.js` to support local file URI asset resolution in `pywebview`.
* Install frontend node modules via `npm install`.
* Initialize a local Git repository and create an initial commit.

---

## Project Structure

Once generated, your project will follow this clean layout:

```text
my-desktop-app/
├── .gitignore
├── LICENSE
├── README.md
├── AGENTS.md
├── pyproject.toml
├── <python_package>/
│   ├── __init__.py
│   └── main.py
├── scripts/
│   └── build_run.sh
└── ui/
    ├── package.json
    ├── vite.config.js
    └── src/

```

---

## Development & Running

To build the frontend assets and launch your desktop application:

```bash
cd my-desktop-app
./scripts/build_run.sh

```
