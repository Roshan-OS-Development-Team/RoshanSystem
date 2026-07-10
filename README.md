# RoshanSystem

> A fully-featured experimental operating system simulation with a professional desktop environment, complete application suite, system settings, and modern GUI.

[![Python](https://img.shields.io/badge/Python-100%25-3776ab?logo=python&logoColor=white)](https://github.com/RoshanGamer7791/RoshanSystem/tree/main/Roshan%20System%20-%20Python%20Version)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-experimental-orange)]()

RoshanSystem is an experimental project that creates a complete OS-like desktop environment in pure Python. The **Python implementation** is a fully-functional desktop system with a professional taskbar, window management, persistent settings, and 7 built-in applications.

---

## 🐍 Python Version (Primary Implementation)

### 🌟 Overview

A complete, production-ready desktop environment featuring a **modern dark-themed GUI** built with CustomTkinter and Pillow. The system includes window management, personalization settings, appearance modes, background customization, persistent settings storage, and a comprehensive suite of integrated applications—all designed to feel like a real operating system.

### ✨ Core Features

#### 🖥️ Professional Desktop System
- **Full-screen immersive environment** with high-quality background imagery
- **Fullscreen toggle** - switch between fullscreen and windowed mode for flexibility
- **Modern dark theme** with smooth animations and professional styling
- **Responsive window scaling** that adapts to any screen resolution
- **Persistent application state** - windows remember their positions between sessions
- **Smart taskbar** with icon display showing all running applications
- **Window layering** - bring any window to the front with a single click
- **Unified styling** across all applications using CustomTkinter dark-blue theme

#### ⚙️ Control Panel - System Settings & Personalization
- **Tabbed settings interface** (960x480 fixed size) with organized categories
- **Scrollable content panels** for each tab to handle multiple options gracefully
- **Persistent settings storage** - all preferences saved to `settings.json` and restored on startup
- **Protected configuration** - settings file protected from unintended overwrites during testing
- **Personalization tab** for appearance and visual customization:
  - **Appearance mode toggle** - seamlessly switch between Dark and Light themes
  - **Dynamic theme application** - instantly applies to all taskbar buttons and UI elements
  - **Background customization** - browse and select from multiple background images (5+ presets)
  - **Background thumbnail previews** - 100x100 pixel preview grid for easy selection
  - **Real-time background switching** - changes apply immediately without restart
  - **Responsive grid layout** - backgrounds displayed in 5-column grid automatically wrapping
- **Preferences tab** for system behavior:
  - **Messagebox Shutdown toggle** - choose between confirmation dialog or direct shutdown
  - **Fullscreen mode toggle** - switch between fullscreen and windowed mode on demand
  - **Dynamic command switching** - toggle between safe shutdown (with confirmation) and instant exit
  - **Protocol management** - control Alt+F4 behavior through settings
  - **Boolean variable persistence** - settings state management with file-based storage
- **Icon-based interface** - Control Panel has dedicated taskbar icon

#### 🎯 Advanced Window Management
- **Drag-and-drop window positioning** - click and drag the title bar to move windows anywhere
- **Fixed window dimensions** - each application has a preset window size:
  - Calculator: 250x337
  - Notepad: 640x360
  - File Explorer: 600x400
  - Image Viewer: 600x400
  - Paint: 960x480
  - Control Panel: 960x480
- **Window title bars** with application icons and close buttons
- **Position memory** - the system saves where each window was last placed via `settings.json`
- **Z-order management** - windows automatically come to the front when opened
- **Graceful close handling** - Alt+F4 protection prevents accidental exits
- **Shutdown confirmation** - safe system exit with Yes/No confirmation dialog (toggleable)

#### 📋 Integrated Taskbar & Application Launcher
- **Professional taskbar** positioned at the bottom of the screen
- **Application icons** for quick visual identification and launching:
  - Start Menu, Notepad, Calculator, File Explorer, Image Viewer, Paint, Control Panel, Shutdown
- **Start menu button** with system options
- **Persistent taskbar** that stays accessible at all times
- **Smooth button hover effects** with color transitions
- **Seven application launchers** for fast access to all system tools

#### 📁 File Explorer - Complete File Management
- **Full directory navigation** with back/forward controls
- **Visual file type detection** - folders, documents, and images display with emoji indicators:
  - 📁 Folders with nested directory support
  - 📄 Text files (.txt)
  - 🖼️ Image files (.png, .jpg, .jpeg, .ico, .gif, .bmp)
- **Direct file opening** - double-click files to open them in the appropriate application
- **Scrollable file list** for large directories
- **Address bar** with manual path entry and "Go" navigation
- **Automatic file association**:
  - Text files → Opens in Notepad
  - Image files → Opens in Image Viewer
- **User directory management** with automatic `user_dir` creation
- **Cross-platform file path handling** using `os.path.join()`

#### 📝 Full-Featured Notepad Application
- **Rich text editing** with word wrap support
- **Save functionality** with custom filename selection
- **Load functionality** with file browser dialog
- **Syntax-aware file operations** - automatically appends .txt extension
- **SaveAsFilename dialog** for choosing save locations and filenames
- **OpenAsFilename dialog** for browsing and opening existing files
- **Real-time text manipulation** with cursor position support
- **Integration with File Explorer** - open text files directly from the file system
- **Professional text editing interface** with smooth scrolling

#### 🖼️ Integrated Image Viewer
- **Support for 6 image formats** - PNG, JPG, JPEG, ICO, GIF, BMP
- **Automatic image scaling** - images fit within the 600x400 viewport
- **Smooth image rendering** via Pillow with CustomTkinter display
- **Open Image dialog** - browse and open images from the file system
- **Integration with File Explorer** - click image files to view them
- **Professional image display** with centered layout
- **Smart thumbnail generation** to prevent oversized images

#### 🧮 Functional Calculator Application
- **Full arithmetic operations** - addition, subtraction, multiplication, division
- **Decimal support** for precise calculations
- **Real-time expression display** - see your calculation as you build it
- **Space-separated operators** for clear operator visibility
- **Equals functionality** - evaluate expressions with Python's `eval()`
- **Grid-based button layout** with numeric keypad (0-9, .)
- **Operation buttons** (+, -, *, /)
- **Professional calculator UI** mimicking real desktop calculators
- **Clean, intuitive interface** suitable for quick calculations

#### 🎨 Professional Paint Application
- **Canvas-based drawing system** with smooth pixel placement
- **10 built-in colors** - Red, Orange, Yellow, Green, Blue, Purple, Violet, Black, White, Gray
- **Color selection buttons** with visual color representation
- **Brush tool** with 6-pixel diameter for balanced drawing
- **Dual rendering** - real-time canvas display + persistent image layer
- **Memory-backed drawing** using PIL's ImageDraw for saved artwork
- **Full-window canvas** (960x480) for comfortable drawing
- **Real-time drawing feedback** with no lag
- **Integration with File Explorer** for future save/load capabilities
- **Professional drawing interface** that responds to click-and-drag motions

#### 💬 Custom Message Box System
- **Multiple message box types**:
  - **MessageBoxYesNo** - Yes/No confirmation dialogs with custom callbacks
  - **MessageBoxOkCancel** - OK/Cancel dialogs for confirmations
- **Icon support** with 3 built-in icon types:
  - ℹ️ Information icon (blue) for general messages
  - ⚠️ Warning icon (yellow) for caution messages
  - ❌ Error icon (red) for error messages
- **Custom callback system** - define specific actions for each button
- **Default behavior** - buttons default to closing the dialog if no callback specified
- **Consistent styling** - all message boxes match the application theme
- **Professional appearance** with icons displayed inline with text
- **Used throughout the system** for important confirmations and alerts
- **Toggleable via Control Panel** - choose whether shutdown shows confirmation

#### 🏗️ Extensible Application Architecture
- **Base window class** (`WindowPackManager`) providing standard window functionality
- **Icon support** for all windows - display 20x20 icons in title bars
- **Reusable component library** for consistent UI elements
- **Modular plugin system** - each application is a self-contained module
- **Standard initialization pattern** - all apps inherit from WindowPackManager
- **Cross-platform compatibility** - Windows, macOS, and Linux support
- **Tab-based UI support** - Control Panel demonstrates CTkTabview for multi-section interfaces
- **Fixed sizing with `pack_propagate(False)`** - precise window dimension control
- **Scrollable frames** - handle content larger than fixed window with CTkScrollableFrame

### 📦 Technical Stack

- **GUI Framework**: CustomTkinter 5.2.2 (modern Tkinter with dark theme support)
- **Image Processing**: Pillow 12.2.0 (image loading, manipulation, and display)
- **Language**: Python 3.8+ (3.10+ recommended)
- **Theme**: Dark blue with professional styling
- **Configuration**: JSON-based settings persistence

### 📚 Dependencies

```
customtkinter==5.2.2
Pillow==12.2.0
```

### 🚀 Quick Start

#### Installation (One Command)
```bash
python -m pip install -r "Roshan System - Python Version/requirements.txt"
```

#### Run the System (One Command)
```bash
python "Roshan System - Python Version/main.py"
```

#### Or from the Python Directory
```bash
cd "Roshan System - Python Version"
python main.py
```

### 📂 Project Architecture

```
Roshan System - Python Version/
├── main.py                              # Desktop initialization & application launcher
├── requirements.txt                     # Python dependencies (5.2.2, 12.2.0)
├── settings.json                        # Persistent user settings (auto-created)
│
├── gui/                                 # Application components
│   ├── window.py                       # WindowPackManager - base window class
│   ├── taskbar.py                      # Taskbar UI container
│   ├── startmenu.py                    # Start menu launcher
│   ├── calculator.py                   # Calculator application (4x4 grid layout)
│   ├── notepad.py                      # Text editor with file I/O
│   ├── fileexplorer.py                 # File browser + SaveAs/Open dialogs
│   ├── imageviewer.py                  # Image display with format support
│   └── paint.py                        # Drawing canvas with color palette
│
├── messagebox/                          # Dialog system
│   ├── __init__.py                     # Module exports
│   ├── MessageboxYesNo.py              # Yes/No confirmation dialogs
│   └── MessageboxOkCancel.py           # OK/Cancel confirmation dialogs
│
├── textures/                            # UI assets and icons
│   ├── background7.png                 # Primary desktop background
│   ├── background*.png                 # Additional background options (5+ variants)
│   ├── startmenu.png                   # Start button icon
│   ├── notepad.png                     # Notepad app icon
│   ├── calculator.png                  # Calculator app icon
│   ├── filexplorer.png                 # File Explorer app icon
│   ├── imageviewer.png                 # Image Viewer app icon
│   ├── Paint.png                       # Paint app icon
│   ├── ctrlpanel.png                   # Control Panel app icon
│   ├── closeicon.png                   # Shutdown/close icon
│   ├── information.png                 # Information dialog icon
│   ├── warning.png                     # Warning dialog icon
│   └── error.png                       # Error dialog icon
│
└── user_dir/                            # User data storage (auto-created)
    ├── (user-created documents)
    └── (saved files from applications)
```

### 🔧 Application Window Sizes

Each application has a fixed, optimized window size set at initialization:

| Application | Dimensions | Notes |
|---|---|---|
| Calculator | 250x337 | Compact calculator layout with 4x4 button grid |
| Notepad | 640x360 | Comfortable text editing with Save/Load buttons |
| File Explorer | 600x400 | Directory browsing with scrollable file list |
| Image Viewer | 600x400 | Image display with toolbar |
| Paint | 960x480 | Large canvas for drawing with color palette |
| Control Panel | 960x480 | Tabbed settings with scrollable content panels |

### 🔧 File Reference

| Component | File | Responsibility |
|---|---|---|
| **Desktop** | `main.py` | Initializes fullscreen app, creates taskbar, registers all application launchers, manages Control Panel, loads/saves settings, handles shutdown with toggle |
| **Window System** | `gui/window.py` | `WindowPackManager` class - provides dragging, fixed sizing (pack_propagate), close buttons, icon support, position memory |
| **Taskbar** | `gui/taskbar.py` | Taskbar UI container at screen bottom (height: 70px) |
| **Start Menu** | `gui/startmenu.py` | Toggleable start menu launcher frame |
| **Control Panel** | `main.py` | Settings management with two tabbed sections using CTkScrollableFrame for content overflow, persists to settings.json |
| **Calculator** | `gui/calculator.py` | Full calculator with 16 buttons, real-time display, arithmetic evaluation, 250x337 fixed size |
| **Notepad** | `gui/notepad.py` | Text editor with Save/Load, integrates SaveAsFilename & OpenAsFilename dialogs, 640x360 fixed size |
| **File Explorer** | `gui/fileexplorer.py` | Main browser + SaveAsFilename (file save dialog) + OpenAsFilename (file open dialog), 600x400 fixed size |
| **Image Viewer** | `gui/imageviewer.py` | Image display with OpenAsFilename for selecting images, supports 6 formats, 600x400 fixed size |
| **Paint** | `gui/paint.py` | Drawing canvas with 10 colors, dual-layer rendering (visual + persistent), 960x480 fixed size |
| **Dialogs** | `messagebox/` | MessageBoxYesNo, MessageBoxOkCancel with icon support |
| **Settings** | `settings.json` | JSON file storing appearance mode, background selection, shutdown behavior, fullscreen toggle, and window positions |

### 🎮 How to Use

#### Launch Applications
- Click taskbar buttons to open applications
- Applications appear in their last saved position
- Click the Start button for additional options
- Click the Control Panel icon to access system settings

#### Access Settings
- Open **Control Panel** from the taskbar (960x480 window)
- **Personalization Tab**:
  - Switch between Dark and Light themes
  - Select different desktop backgrounds from the grid
  - See real-time preview thumbnails (100x100 pixels)
  - Scroll within the tab if needed
- **Preferences Tab**:
  - Toggle messagebox shutdown behavior
  - Toggle fullscreen mode on/off
  - Choose between safe shutdown (with confirmation) or direct exit
  - All settings persist when you restart the application

#### File Operations
- Use **File Explorer** to browse directories
- Double-click files to open them
- Use **Save File** in Notepad to save text with a custom filename
- Use **Load File** in Notepad to open existing text files

#### Drawing & Editing
- Open **Paint** and select a color, then click-and-drag to draw
- Edit text in **Notepad** with full word wrapping support
- View images in **Image Viewer** by selecting them from File Explorer

#### Window Management
- Drag any window by its title bar to reposition
- Click the **X** button to close applications
- Click the **Shutdown** button to exit the system (with confirmation, unless disabled)
- Toggle fullscreen mode from Control Panel > Preferences to adapt to your workspace

### 🐛 Troubleshooting

| Issue | Solution |
|---|---|
| Import errors for customtkinter | Install requirements: `pip install -r requirements.txt` |
| UI rendering problems | Verify CustomTkinter 5.2.2 is installed (exact version in requirements.txt) |
| Images not loading | Check all image files exist in `textures/` folder, including background variants |
| File operations fail | Ensure `user_dir/` has write permissions; the system auto-creates it |
| Application not launching | Run with `python -u` for unbuffered output to see error messages |
| Colors appear different | Verify dark-blue theme is applied; clear any conflicting system themes |
| Paint not responding | Ensure Paint.png exists in textures folder |
| Notepad won't save | Check that user_dir directory exists and is writable |
| Alt+F4 doesn't close app | This is intentional - use the Shutdown button or Control Panel preferences |
| Control Panel won't open | Ensure ctrlpanel.png exists in textures folder |
| Background change doesn't work | Verify multiple background*.png files exist in textures folder (background0.png, background1.png, etc.) |
| Theme switching not working | Check CTkOptionMenu is properly configured in Control Panel |
| Windows not remembering position | Position is saved when window closes; ensure proper shutdown. Check settings.json exists and is writable. |
| Window size can't be changed | Window sizes are fixed by design using `pack_propagate(False)` - modify application code to change dimensions |
| Control Panel content overflows | Use the scrollbar in each tab's scrollable frame to view hidden content |
| Settings not persisting | Ensure settings.json can be written to; check file permissions in the application directory |
| Fullscreen toggle not working | Verify fullscreen preference is properly saved in settings.json |

### 🖥️ Platform Support

| Platform | Status | Notes |
|---|---|---|
| **Windows** | ✅ Fully Supported | Primary development platform, fully tested |
| **macOS** | ✅ Supported | Works with native file handlers, minor UI differences possible |
| **Linux** | ✅ Supported | File operations use system defaults, may require adjustments |

### 📊 Statistics

- **Total Python Code**: ~900+ lines across all components
- **Applications Included**: 7 (Calculator, Notepad, File Explorer, Image Viewer, Paint, Control Panel, Start Menu)
- **Settings Categories**: 2 (Personalization, Preferences)
- **Persisted Settings**: 4 (appearance mode, background selection, shutdown behavior, fullscreen toggle)
- **Message Box Types**: 2 (Yes/No, OK/Cancel)
- **Supported Image Formats**: 6 (PNG, JPG, JPEG, ICO, GIF, BMP)
- **Built-in Colors**: 10 (Red, Orange, Yellow, Green, Blue, Purple, Violet, Black, White, Gray)
- **Dialog Types**: 3 (Information, Warning, Error)
- **Background Presets**: 5+
- **UI Themes**: 2 (Dark, Light)

### 🎯 Recent Improvements
- ✅ **Python-only focus** - pure Python codebase
- ✅ **Fullscreen toggle** - switch between fullscreen and windowed modes
- ✅ **Settings persistence** - all preferences saved to settings.json
- ✅ **Protected settings** - configuration file protected during testing
- ✅ Control Panel with tabbed interface and scrollable content
- ✅ Appearance mode toggle (Dark/Light themes)
- ✅ Background customization with preview grid
- ✅ Real-time theme application to all UI elements
- ✅ Shutdown behavior toggle (confirmation on/off)
- ✅ Dynamic command switching for graceful/direct exit
- ✅ Window icon support in title bars
- ✅ Window position persistence across sessions
- ✅ Paint application with real-time drawing
- ✅ Alt+F4 protection against accidental exits
- ✅ Graceful shutdown with confirmation
- ✅ Cross-platform file handling
- ✅ Enhanced message boxes with icon support
- ✅ Improved calculator functionality

### 📖 Development & Customization

For detailed guides on extending the Python version and adding new applications, please refer to the [project wiki](https://github.com/RoshanGamer7791/RoshanSystem/wiki).

---

## 📊 Repository Overview

- **Primary Language**: Python (100%)
- **Status**: Experimental & Actively Developed
- **License**: MIT
- **Total Size**: ~18 KB

### Key Achievements
- ✅ Fully functional desktop environment in pure Python
- ✅ 7 integrated applications with system settings
- ✅ Professional window management system
- ✅ Cross-platform compatibility
- ✅ Custom dialog and message box system
- ✅ Persistent application state with JSON storage
- ✅ Theme customization (Dark/Light modes)
- ✅ Desktop background customization
- ✅ Scrollable UI panels for content overflow
- ✅ Fullscreen/windowed mode toggle
- ✅ Settings protection for safe testing
- ✅ Ready for ISO distribution

---

## 🤝 Contributing

We welcome contributions! Please see `CONTRIBUTING.md` for guidelines and `CODE_OF_CONDUCT.md` for community standards.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

---

## 📝 License

Licensed under the **MIT License** — see [`LICENSE`](LICENSE) for details.

---

## 📞 Support

Found an issue or have a feature suggestion? Please open an issue using the [`ISSUE_TEMPLATE.md`](ISSUE_TEMPLATE.md) format.

---

## 🎯 Project Status

**Status**: Experimental & Production-Ready

RoshanSystem is a complete, functional OS simulation showcasing professional GUI development in Python. The Python version is feature-complete with a full application suite, robust window management, persistent settings, system preferences, and cross-platform support. The system is suitable for educational purposes, desktop simulation projects, or as a foundation for custom GUI applications.

Future roadmap includes ISO distribution, additional applications, advanced system utilities, and more customization options.

---

**Crafted with ❤️ by Roshan | Advanced OS Simulation in Python**
