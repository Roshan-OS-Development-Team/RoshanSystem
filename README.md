# RoshanSystem

> A multi-language experimental operating system simulation with desktop GUI and utility applications.

[![Python](https://img.shields.io/badge/Python-86.2%25-3776ab?logo=python&logoColor=white)]()
[![C++](https://img.shields.io/badge/C%2B%2B-10.8%25-00599c?logo=cplusplus&logoColor=white)](https://github.com/RoshanGamer7791/RoshanSystem/tree/main/RoshanOS-Cpp-version)
[![CMake](https://img.shields.io/badge/CMake-3%25-064f8c?logo=cmake&logoColor=white)](https://github.com/RoshanGamer7791/RoshanSystem/tree/main/RoshanOS-Cpp-version)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-experimental-orange)]()

RoshanSystem is an experimental project that implements an OS-like environment with desktop GUI capabilities. The project includes two distinct implementations: a **Python-based version** featuring a desktop environment with native applications, and a **C++ version** using Qt framework for cross-platform compatibility.

## 📁 Repository Structure

```
RoshanSystem/
├── Roshan System - Python Version/    # 86.2% of codebase
│   ├── main.py                        # Desktop application entry point
│   ├── requirements.txt               # Python dependencies
│   ├── gui/                          # GUI components & applications
│   ├── messagebox/                   # Message box utilities
│   └── textures/                     # Image assets
│
├── RoshanOS-Cpp-version/             # 10.8% C++, 3% CMake
│   ├── CMakeLists.txt               # Build configuration
│   ├── main.cpp                     # Application entry point
│   ├── mainwindow.h/cpp             # Main window implementation
│   ├── mainwindow.ui                # Qt UI definition
│   ├── calculator.h/cpp             # Calculator application
│   ├── calculator.ui                # Calculator UI
│   ├── resources.qrc                # Qt resource file
│   └── textures/                    # Image resources
│
└── Project governance files
    ├── LICENSE                      # MIT License
    ├── CONTRIBUTING.md              # Contribution guidelines
    ├── CODE_OF_CONDUCT.md          # Community standards
    └── ISSUE_TEMPLATE.md            # Issue reporting template
```

## 🐍 Python Version (Primary Implementation)

A feature-rich desktop environment built with **CustomTkinter** and **Pillow**.

### Features

- **Desktop Environment**: Full-window GUI with background imagery and resizable layouts
- **Taskbar**: Application launcher with quick-access buttons
- **File Explorer**: Browse user files with directory navigation and file type handling
- **Notepad**: Text editor with create, load, and save functionality
- **Image Viewer**: Display images from the file system
- **Window Management**: Drag, resize, and close window controls
- **Modular Architecture**: Easy-to-extend application framework

### Requirements

- **Python 3.8+** (3.10+ recommended)
- **pip** (Python package manager)

### Dependencies

```
customtkinter==5.2.2
Pillow==12.2.0
```

### Installation & Setup

1. **Install dependencies**:
   ```bash
   python -m pip install -r "Roshan System - Python Version/requirements.txt"
   ```

2. **Run the application**:
   
   Option A — From repository root:
   ```bash
   python "Roshan System - Python Version/main.py"
   ```
   
   Option B — From the Python Version directory:
   ```bash
   cd "Roshan System - Python Version"
   python main.py
   ```

### Key Files

| File/Folder | Purpose |
|---|---|
| `main.py` | Application entry point; sets up desktop, taskbar, and app launchers |
| `gui/window.py` | Window management classes (pack/grid managers, drag/close behavior) |
| `gui/taskbar.py` | Taskbar container and layout |
| `gui/startmenu.py` | Start menu frame |
| `gui/notepad.py` | Notepad application with save/load |
| `gui/fileexplorer.py` | File browser with SaveAs dialog |
| `gui/imageviewer.py` | Image display helper |
| `textures/` | Background images and icons |
| `messagebox/` | Message box utilities |
| `user_dir/` | User data directory (created at runtime) |

### Python Version: Development

To extend the Python implementation:

1. **Add new applications**: Create a new module in `gui/` and inherit from `WindowPackManager` or `WindowGridManager`
2. **Register launchers**: Add buttons to the taskbar in `main.py`
3. **Update assets**: Replace images in `textures/` as needed
4. **Keep modular**: Each application should have its own module file

### Python Version: Troubleshooting

| Issue | Solution |
|---|---|
| Import errors | Activate virtual environment; verify requirements are installed |
| UI appearance issues | Use pinned customtkinter version from `requirements.txt` |
| Texture loading failures | Verify image files exist in `textures/`; check working directory paths |
| File save issues | Ensure `user_dir/` exists and has write permissions |

---

## ⚙️ C++ Version (Qt Implementation)

A cross-platform implementation using **Qt** framework and **CMake** build system.

### Features

- **Qt Framework**: Native cross-platform GUI capabilities
- **Calculator Application**: Functional calculator utility
- **Modular UI**: Separate UI definitions and logic
- **Resource Management**: Qt resource system for assets

### Build Requirements

- **C++ 11 or higher**
- **Qt 5.x or later** (Qt Creator recommended)
- **CMake 3.0+**
- **C++ compiler** (g++, clang, MSVC, etc.)

### Build & Run

```bash
mkdir build && cd build
cmake ..
cmake --build .
./RoshanOS
```

### Key Files

| File | Purpose |
|---|---|
| `CMakeLists.txt` | CMake build configuration |
| `main.cpp` | Application entry point |
| `mainwindow.h/cpp` | Main window class |
| `mainwindow.ui` | Main window UI definition (Qt Designer) |
| `calculator.h/cpp` | Calculator application logic |
| `calculator.ui` | Calculator UI definition |
| `resources.qrc` | Qt resource file (textures, icons) |
| `textures/` | Image assets |

### C++ Version: Development

To extend the C++ implementation:

1. **Add new applications**: Create `.h/cpp` and `.ui` files following the calculator pattern
2. **Update CMakeLists.txt**: Add new source files to the build configuration
3. **Use Qt Designer**: Edit `.ui` files for visual layout design
4. **Add resources**: Include new assets in `resources.qrc`

---

## 🚀 Quick Start

### For Python Users
```bash
# Install and run in 2 commands
python -m pip install -r "Roshan System - Python Version/requirements.txt"
python "Roshan System - Python Version/main.py"
```

### For C++ Developers
```bash
# Build and run in 3 commands
cmake -B build && cmake --build build
cd build
./RoshanOS
```

---

## 📋 Platform Considerations

**Python Version:**
- ✅ Windows: Fully supported
- ✅ macOS: Generally supported (some platform differences in file handlers)
- ✅ Linux: Supported (file opening uses OS defaults; may need adjustments)

**C++ Version:**
- ✅ Cross-platform via Qt
- Requires Qt development libraries installed

---

## 🤝 Contributing

This project welcomes contributions! Please see `CONTRIBUTING.md` for guidelines and `CODE_OF_CONDUCT.md` for community standards.

### How to contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

---

## 📝 License

This project is licensed under the **MIT License** — see the [`LICENSE`](LICENSE) file for details.

---

## 📞 Support & Issues

Found a bug or have a feature request? Please open an issue using the [`ISSUE_TEMPLATE.md`](ISSUE_TEMPLATE.md) format.

---

## 🎯 Project Status

**Status**: Experimental

This is an ongoing experimental project showcasing OS-like GUI design in both Python and C++. Features and architecture may change as development progresses.

---

**Last Updated**: 2026 | **Language Composition**: 86.2% Python, 10.8% C++, 3% CMake
