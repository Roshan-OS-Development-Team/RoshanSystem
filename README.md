# RoshanSystem

> An experimental desktop-environment simulation written in Python.

[![Python](https://img.shields.io/badge/Python-CustomTkinter-3776ab?logo=python&logoColor=white)](Roshan%20System%20-%20Python%20Version)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Experimental-orange.svg)]()

RoshanSystem provides an OS-style desktop built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) and Pillow. It includes a login screen, taskbar and Start menu, configurable appearance settings, draggable application windows, a local file workspace, and a suite of built-in tools.

## Features

### Desktop experience

- Fullscreen or windowed desktop with a resizable background.
- Login/sign-up screen. Credentials are stored locally with a SHA3-512 password hash.
- Taskbar with Start menu, application icons, shutdown control, and an app search field.
- Search results update while typing and can launch matching apps.
- Draggable, closable application windows with shared title-bar styling and icons.
- Optional shutdown confirmation dialog.

### Personalization

The Control Panel includes the following settings, which are saved in `settings.json` when the system exits:

- Dark and Light appearance modes.
- Three CustomTkinter colour themes: `dark-blue`, `blue`, and `green`.
- Fifteen bundled desktop backgrounds.
- Fullscreen toggle.
- Shutdown-confirmation toggle.

Changing the colour theme restarts RoshanSystem so the selected theme can be applied consistently.

### Built-in applications

| Application | What it does |
| --- | --- |
| Notepad | Edit text files with Save and Load controls. |
| Calculator | Perform basic arithmetic with decimal support. |
| File Explorer | Browse folders, navigate with an address bar, and open text and supported image files. |
| Image Viewer | Open and scale PNG, JPG, JPEG, ICO, GIF, and BMP images. |
| Paint | Draw on a canvas using a 10-colour palette. |
| Terminal | Run shell commands and show their output in an in-app terminal. |
| Run | Launch registered applications by name. |
| Rosver | Show Roshan OS version, licensing, and credits. Available through Run. |

Notepad, File Explorer, and the file dialogs use `user_dir/` as the initial workspace. The directory is created automatically when the desktop starts.

## Quick start

Prerequisites: Python 3.10+ is recommended and a desktop environment capable of running Tkinter.

```bash
python -m pip install -r "Roshan System - Python Version/requirements.txt"
python "Roshan System - Python Version/main.py"
```

Alternatively, run it from the application directory:

```bash
cd "Roshan System - Python Version"
python main.py
```

On the first launch, enter a username and password to create the local account. Later launches show the login form.

## Using the desktop

- Select an app from the taskbar or Start menu.
- Use the taskbar search box to find an application by name.
- Drag a window by its title bar; select its red **X** button to hide it.
- Open **Control Panel** from the taskbar or Start menu to change the appearance, background, fullscreen setting, or shutdown behaviour.
- Use **Run** to launch `Rosver`, `Terminal`, `Notepad`, `Calculator`, `File Explorer`, `Image Viewer`, or `Paint` by name.
- Choose **Shutdown** in the taskbar or Start menu when you are done.

## Project layout

```text
Roshan System - Python Version/
+-- main.py                 # Desktop shell, taskbar, Start menu, search, Control Panel
+-- login_page.py           # Local sign-up and login UI
+-- apps.json               # Taskbar and Start-menu application registry
+-- settings.json           # Appearance and desktop preferences
+-- requirements.txt        # Python dependencies
+-- gui/
|   +-- window.py           # Reusable draggable window base class
|   +-- calculator.py       # Calculator
|   +-- fileexplorer.py     # File browser and file picker windows
|   +-- imageviewer.py      # Image viewer
|   +-- notepad.py          # Text editor
|   +-- paint.py            # Drawing canvas
|   +-- run.py              # Run dialog
|   +-- terminal.py         # Command terminal
+-- run_apps/
|   +-- run_apps.json       # Applications registered with Run
|   +-- rosver.py           # Version and credits window
+-- messagebox/             # Custom confirmation dialogs
+-- textures/               # Icons, backgrounds, and UI assets
+-- user_dir/               # Local files created by the user
```

## Configuration files

| File | Purpose |
| --- | --- |
| `settings.json` | Stores the background, appearance mode, colour theme, fullscreen option, and shutdown preference. |
| `apps.json` | Defines the applications shown in the taskbar and Start menu. |
| `run_apps/run_apps.json` | Defines the applications that can be opened through Run. |
| `login_details.json` | Created after sign-up; stores the local username and password hash. |

## Dependencies

```text
customtkinter
Pillow
```

## Notes

RoshanSystem is an educational, experimental desktop simulation, not an operating system or a security boundary. In particular, the Terminal executes commands through the host shell, so use it only with commands you trust.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the project [Code of Conduct](CODE_OF_CONDUCT.md).

## License

RoshanSystem is available under the [MIT License](LICENSE).
