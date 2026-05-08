# RoshanSystem

> A small experimental "desktop" implemented in Python — a GUI-based toy operating-system-like environment.

[![Python](https://img.shields.io/badge/python-100%25-blue)]()
[![License](https://img.shields.io/badge/license--see%20LICENSE-lightgrey)]()
[![Status](https://img.shields.io/badge/status-experimental-orange)]()

This repository contains the Python version of "Roshan System" — a windowed GUI environment built with CustomTkinter and Pillow. It provides a simple taskbar, a start menu placeholder, window manager utilities, a Notepad app, a File Explorer, and an image viewer helper.

## Quick overview

- Entry point: `Roshan System - Python Version/main.py`
- Dependencies: `Roshan System - Python Version/requirements.txt` (customtkinter, Pillow)
- Main GUI package: `Roshan System - Python Version/gui/`
- Textures / images: `Roshan System - Python Version/textures/`
- A local working directory is created/used at runtime: `user_dir/`
- Repository root includes community and governance files:
  - `LICENSE`
  - `CONTRIBUTING.md`
  - `CODE_OF_CONDUCT.md`
  - `ISSUE_TEMPLATE.md`

## Features

- Full-window desktop with background image and resizable layout.
- Taskbar with app-launch buttons (Start button, Notepad, File Explorer).
- Notepad: create, load, and save `.txt` files.
- File Explorer: browse `user_dir/`, open text files in Notepad, open images.
- Simple window management utilities (drag, close, pack/grid window styles).
- Image assets reside in `Roshan System - Python Version/textures/`. The main background referenced in the code is `textures/background13.png`.

## Requirements

- Python 3.8+ (3.10+ recommended)
- pip
- The repository includes exact Python package versions in:
  `Roshan System - Python Version/requirements.txt`
  - customtkinter==5.2.2
  - Pillow==12.2.0

Install dependencies with:

```bash
python -m pip install -r "Roshan System - Python Version/requirements.txt"
```

Note: Paths contain spaces; wrap them in quotes or change directory before running commands.

## Run

From the repository root, run one of the following:

Option A — run directly (from repository root):

```bash
python "Roshan System - Python Version/main.py"
```

Option B — change directory then run:

```bash
cd "Roshan System - Python Version"
python main.py
```

On first run the File Explorer will create `user_dir/` if it does not exist.

## Project structure

Root files:
- README.md — this file
- LICENSE
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- ISSUE_TEMPLATE.md

Roshan System - Python Version/
- main.py — application entrypoint; sets up the desktop, taskbar, and app buttons.
- requirements.txt — dependencies.
- textures/ — image assets used by the app (background, icons, etc.).
- gui/
  - window.py — window management classes (pack/grid window managers, drag/close behavior).
  - taskbar.py — Taskbar container used by main app.
  - startmenu.py — StartMenu frame (placeholder).
  - notepad.py — Notepad application (save/load, text box).
  - fileexplorer.py — File Explorer and a SaveAs dialog helper.
  - imageviewer.py — helper to open/display images.

## Usage notes & platform considerations

- The app uses CustomTkinter (modern themed tkinter). If the UI appears inconsistent, verify that the installed customtkinter version matches the pinned version in `requirements.txt`.
- File Explorer treats `user_dir/` as the default user folder; files saved via the Notepad Save-as helper are stored in that directory.
- Opening image files uses the OS default handlers (`os.startfile(...)` is used in code). Behavior may differ across platforms; adjustments may be required for Linux/macOS.

## Development

- To add new GUI applications, extend `WindowPackManager` or `WindowGridManager` in `gui/window.py` and register a launcher button in `main.py`.
- To change the background or icons, replace images in `Roshan System - Python Version/textures/`. Filenames are referenced directly from `main.py`.
- Keep UI components focused; place each app in its own module under `gui/`.

## Troubleshooting

- Import errors: ensure the virtual environment is active and the requirements are installed for the Python interpreter in use.
- customtkinter theme/layout differences: use the pinned version in `requirements.txt` for reproducible behavior.
- If textures fail to load, confirm image files exist in `Roshan System - Python Version/textures/` and that `main.py` is executed with correct working directory so relative paths resolve.

## Contributing & governance

This project includes CONTRIBUTING and CODE_OF_CONDUCT documents. Contributions should follow the guidelines in `CONTRIBUTING.md`.

## License

See the `LICENSE` file at the repository root for licensing details.
