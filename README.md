# Roshan System

Roshan System — source code for a desktop-like OS prototype. The repository contains two implementations:

- New Roshan System — C# / WPF (Windows desktop experience)
- Old Roshan System — Python / Tkinter (earlier prototype)

Languages (approximate): C# 69.4% · Python 30.6%

---

## Table of contents

- [Overview](#overview)
- [Features](#features)
- [Repository layout](#repository-layout)
- [Notable files](#notable-files)
- [Requirements](#requirements)
- [Run / Build instructions](#run--build-instructions)
  - [New Roshan System (C# / WPF)](#new-roshan-system-c--wpf)
  - [Old Roshan System (Python / Tkinter)](#old-roshan-system-python--tkinter)
- [Assets & resources](#assets--resources)
- [Troubleshooting](#troubleshooting)
- [Development & contributing](#development--contributing)
- [Contact](#contact)

---

## Overview

Roshan System implements a simple desktop environment with apps such as a Start Menu, Notepad, Calculator, Browser component, Overclocker, Run dialog, and a winver/info window. The C# WPF version is the more recent desktop-like UI; the Python Tkinter version is an older prototype.

---

## Features

- Main desktop window and Start menu
- Notepad with open/save functionality (supports Ctrl+S / Ctrl+O shortcuts)
- Calculator (basic arithmetic)
- Browser window (loads an initial URL)
- Overclocker demo UI (simple numeric adjustment)
- Run dialog to launch built-in windows or arbitrary executables
- Python prototype that wires separate GUI and function modules

---

## Repository layout

- New Roshan System/
  - Roshan System/
    - *.xaml / *.xaml.cs — WPF UI and code-behind
    - App.xaml.cs, AssemblyInfo.cs — application metadata
- Old Roshan System/
  - main.py — Tkinter entry point
  - gui/ — GUI components used by main.py
  - functions/ — helper modules referenced by main.py
  - textures/ — images used by the Python UI (e.g. background)

---

## Notable files

- New Roshan System/Roshan System/MainWindow.xaml.cs — main window and app launch handlers
- New Roshan System/Roshan System/Startmenu.xaml.cs — Start menu logic
- New Roshan System/Roshan System/Notepad.xaml.cs — notepad logic (open/save, keyboard shortcuts)
- New Roshan System/Roshan System/Calculator.xaml.cs — calculator logic
- New Roshan System/Roshan System/Browser.xaml.cs — browser component
- New Roshan System/Roshan System/Run.xaml.cs — Run dialog (starts exe or built-in dialogs)
- New Roshan System/Roshan System/Overclocker.xaml.cs — overclocker demo
- New Roshan System/Roshan System/winver.xaml.cs — information window
- Old Roshan System/main.py — Python Tkinter entry script
- Old Roshan System/gui/desktop.py — desktop background setup (references textures/background2.png)

---

## Requirements

New Roshan System (C# / WPF)
- Windows OS
- Visual Studio (2017, 2019, 2022) or another IDE that can build WPF projects
- .NET Framework or .NET SDK as required by the project (open the .csproj to confirm target)

Old Roshan System (Python / Tkinter)
- Python 3.x (Tkinter included in standard installers for most platforms)
- On some systems, install system packages for Tk (e.g., `sudo apt install python3-tk`)

---

## Run / Build instructions

### New Roshan System (C# / WPF)
1. Open `New Roshan System/Roshan System` in Visual Studio (or open the solution if a .sln exists).
2. Restore any NuGet packages if prompted.
3. Build the project.
4. Run the app from Visual Studio (Start Debugging or Start Without Debugging).

Notes:
- The app uses WPF so it must run on Windows.
- If you do not have a .sln file, open the folder containing the `.csproj` and load it in Visual Studio.

### Old Roshan System (Python / Tkinter)
1. From repository root run:
   - python "Old Roshan System/main.py"
2. The script launches a fullscreen Tkinter window that relies on modules under `Old Roshan System/functions` and assets under `Old Roshan System/textures`.

Notes:
- Ensure the `textures` folder and any referenced image files exist where the code expects them.
- Run in a terminal to view any error output for missing modules or files.

---

## Assets & resources

- Verify images under `Old Roshan System/textures` (e.g., `background2.png`) are present. Missing assets may cause immediate runtime errors.
- The C# project may reference additional resources in the project files; inspect the .csproj and .xaml files if resource load failures occur.

---

## Troubleshooting

- C# build errors: confirm the project target framework and install the corresponding .NET SDK; ensure Visual Studio has the ".NET desktop development" workload.
- Python runtime errors: check that all modules imported by `main.py` exist in `Old Roshan System/functions`. Use the terminal tracebacks to locate missing dependencies.
- Missing image file errors: place the expected image files at the exact relative paths referenced by the code.

---

## Development & contributing

- Follow a fork-and-branch workflow:
  1. Fork the repository
  2. Create a descriptive branch
  3. Add changes with clear commits
  4. Open a pull request with a description of what changed and why
- Suggested additions: tests, more defensive error handling, and packaging instructions for the C# app.

---

## Contact

Repository owner: RoshanGamer7791
