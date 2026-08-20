import json  # Helps load and save settings.json
import os  # Imports OS to check if a path exists and to check if settings.json is valid
import subprocess  # Handles dependency handling
import sys  # Handles command-line arguments arguments for the interal QApplication

# === Start of PySide6 imports ===
try:
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QCloseEvent, QIcon, QPixmap, QResizeEvent
    from PySide6.QtWidgets import (
        QApplication,
        QGridLayout,
        QHBoxLayout,
        QLabel,
        QMainWindow,
        QPushButton,
        QScrollArea,
        QTabWidget,
        QVBoxLayout,
        QWidget,
    )
except ModuleNotFoundError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=False)
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QCloseEvent, QIcon, QPixmap, QResizeEvent
    from PySide6.QtWidgets import (
        QApplication,
        QGridLayout,
        QHBoxLayout,
        QLabel,
        QMainWindow,
        QPushButton,
        QScrollArea,
        QTabWidget,
        QVBoxLayout,
        QWidget,
    )

# === End of PySide6 imports ===
import core  # Imports the window class for type annotation and for settings and dynamic styling
from login_page import LoginPage  # Imports the Login Page for ROS

os.chdir(
    os.path.dirname(os.path.abspath(__file__))
)  # Makes the working directory to this folder

# Checks if the settings file exists and if it isnt empty
if os.path.exists("settings.json") and os.path.getsize("settings.json") > 0:
    with open("settings.json", "r") as f:
        settings = json.load(f)
# This is an else case of the settings.json file not existing
else:
    settings = {
        "background": "textures/background7.png",
        "fullscreen": True,
        "maximized": True,
        "taskbar_alignment": "center",
        "messagebox_shutdown": True
    }

if not os.path.exists("packages"):
    os.mkdir("packages")

# Gets all the styling for the window
style = core.get_qss_styles("styling/main")

# The main application class
class App(QMainWindow):
    def __init__(self) -> None:
        self.ready: bool = (
            False  # Lets the interpreter know it isnt ready to be messed with
        )
        super().__init__()  # Calles the init method of the parent class
        self.setWindowTitle("Roshan OS")  # Sets the Window title to Roshan OS

        app_ico = QIcon("textures/Logo.png")  # It gets the icon for the window

        self.setWindowIcon(app_ico)  # It sets the icon of the window

        self.container = QWidget()  # This contains all the apps, start menu and taskbar

        # This gets the background based on the setttings background
        self.background = QPixmap(settings["background"]).scaled(
            self.width(),
            self.height(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        # This makes a label to show the background
        self.backgroundlabel = QLabel(self.container)
        self.backgroundlabel.setPixmap(self.background)
        self.backgroundlabel.setGeometry(0, 0, self.width(), self.height())
        self.backgroundlabel.lower()

        # This sets the central widget of the window to the container
        self.setCentralWidget(self.container)

        self.taskbar = QWidget(self.container)  # This initalizes the taskbar

        self.taskbar.setStyleSheet(style["taskbar"])  # This sets the taskbar's style

        self.taskbar.setGeometry(
            0, self.height() - 70, self.width(), 70
        )  # This sets the position and size

        self.taskbar_layout = QHBoxLayout(self.taskbar)  # This is the start menu layout

        self.startmenu_opened: bool = (
            False  # It stores if the start menu is open or not
        )
        self.startmenu = QWidget(self.container)
        if settings["taskbar_alignment"] == "center":
            self.taskbar_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            self.startmenu.setGeometry(
                self.width() // 2 - 200, self.height() - 480, 400, 400
            )
        elif settings["taskbar_alignment"] == "left":
            self.taskbar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.startmenu.setGeometry(10, self.height() - 480, 400, 400)

        startmenu_size_policy = self.startmenu.sizePolicy()
        startmenu_size_policy.setRetainSizeWhenHidden(True)

        self.startmenu.setSizePolicy(startmenu_size_policy)
        self.startmenu.setVisible(False)
        self.startmenu.setStyleSheet(style["startmenu"])

        self.startmenu_scroll = QScrollArea(self.startmenu)
        self.startmenu_scroll.setGeometry(50, 0, 350, 400)
        self.startmenu_container = QWidget()
        self.startmenu_container.setStyleSheet(style["startmenu_container"])
        self.startmenu_scroll.setWidget(self.startmenu_container)
        self.startmenu_scroll.setStyleSheet(style["scrollbar"])
        self.startmenu_layout = QVBoxLayout(self.startmenu_container)
        self.startmenu_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.startmenu_scroll.setWidgetResizable(True)

        self.startmenu_btn = QPushButton(self.taskbar)
        self.startmenu_ico = QPixmap("textures/Start.png").scaled(
            50,
            50,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.startmenu_btn.setIcon(self.startmenu_ico)
        self.startmenu_btn.setFixedSize(60, 60)
        self.startmenu_btn.setIconSize(self.startmenu_ico.size())
        self.startmenu_btn.clicked.connect(self.toggle_startmenu)
        self.startmenu_btn.setStyleSheet(style["button"])

        self.taskbar_layout.addWidget(self.startmenu_btn)

        with open("apps.json", "r") as f:
            self.apps = json.load(f)

        for app in self.apps:
            starter = self.apps[app]
            app_module = __import__(starter["module"])
            app_class = getattr(app_module, starter["class_or_func"])
            app_instance = app_class(self)
            app_instance.hide()
            app_img = QPixmap(starter["icon"]).scaled(
                50,
                50,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )

            self.apps[app] = {
                "instance": app_instance,
                "ico": app_img
            }

            if starter["taskbar_btn"]:
                self.app_taskbar_btn = QPushButton()
                self.app_taskbar_btn.setFixedSize(60, 60)
                self.app_taskbar_btn.setIcon(app_img)
                self.app_taskbar_btn.setIconSize(app_img.size())
                self.app_taskbar_btn.clicked.connect(
                    lambda checked=False, app=app_instance: self.openApp(app)
                )
                self.app_taskbar_btn.setStyleSheet(style["button"])
                self.taskbar_layout.addWidget(self.app_taskbar_btn)

            if starter["startmenu_btn"]:
                self.app_startmenu_btn = QPushButton(app)
                self.app_startmenu_btn.setStyleSheet(style["button"])
                self.app_startmenu_btn.setIcon(app_img)
                self.app_startmenu_btn.setIconSize(app_img.size())
                self.app_startmenu_btn.clicked.connect(
                    lambda checked=False, app=app_instance: self.openApp(app)
                )
                self.startmenu_layout.addWidget(self.app_startmenu_btn)

        settings_ico = QPixmap("textures/settings.png").scaled(
            50,
            50,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.apps["settings"] = {
            "instance": self.settings(),
            "ico": settings_ico
        }
        self.loginPage = LoginPage(self)
        self.ready = True

    def resizeEvent(self, event: QResizeEvent, /) -> None:
        super().resizeEvent(event)
        if self.ready:
            self.taskbar.setGeometry(0, self.height() - 70, self.width(), 70)
            self.background = QPixmap(settings["background"]).scaled(
                self.width(),
                self.height(),
                Qt.AspectRatioMode.IgnoreAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            self.backgroundlabel.setPixmap(self.background)
            self.backgroundlabel.setGeometry(0, 0, self.width(), self.height())
            self.backgroundlabel.lower()
            if settings["taskbar_alignment"] == "left":
                self.startmenu.setGeometry(10, self.height() - 480, 400, 400)
            elif settings["taskbar_alignment"] == "center":
                self.startmenu.setGeometry(
                    self.width() // 2 - 200, self.height() - 480, 400, 400
                )

            self.loginPage.setGeometry(0, 0, self.width(), self.height())
            self.loginPage.resizeEvent(event)

    def closeEvent(self, event: QCloseEvent, /) -> None:
        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=4)

        event.accept()

    def openApp(self, app: core.Window):
        app.move(app.position["x"], app.position["y"])
        app.show()

    def toggle_startmenu(self):
        if self.startmenu_opened:
            self.startmenu.setVisible(False)
            self.startmenu_opened = False
        else:
            self.startmenu.setVisible(True)
            self.startmenu_opened = True
            self.startmenu.raise_()

    def changeBackground(self, filePath: str):
        self.background = QPixmap(filePath).scaled(
            self.width(),
            self.height(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.backgroundlabel.setPixmap(self.background)
        settings["background"] = filePath

    def settings(self) -> core.Window:
        settings_win = core.Window(
            self, "Settings", (960, 480), "textures/settings.png"
        )

        backgrounds: list[str] = [
            os.path.join("textures", file)
            for file in os.listdir("textures")
            if "background" in file
        ]

        ctrlPanelStyles = core.get_qss_styles("styling/settings")

        contents = QTabWidget(settings_win)
        contents.setGeometry(0, 50, settings_win.width(), settings_win.height() - 50)
        contents.setStyleSheet(ctrlPanelStyles["contents"])

        personalization_tab = QScrollArea()
        personalization_tab_container = QWidget()
        personalization_tab.setWidget(personalization_tab_container)
        personalization_tab_layout = QVBoxLayout(personalization_tab)
        personalization_tab.viewport().setAutoFillBackground(False)

        background_buttons = QWidget(personalization_tab_container)
        background_buttons_layout = QGridLayout(background_buttons)

        row: int = 0
        column: int = 0
        for background in backgrounds:
            background_ico = QPixmap(background).scaled(
                100,
                100,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            background_btn = QPushButton(background_buttons)
            background_btn.setIcon(background_ico)
            background_btn.setIconSize(background_ico.size())
            background_btn.clicked.connect(
                lambda checked=1, bg=background: self.changeBackground(bg)
            )
            background_btn.setStyleSheet(ctrlPanelStyles["bg_button"])
            background_buttons_layout.addWidget(background_btn, row, column)
            if column == 5:
                row += 1
                column = 0
            else:
                column += 1

        personalization_tab_layout.addWidget(background_buttons)

        contents.addTab(personalization_tab, "Personalization")


        return settings_win


if __name__ == "__main__":
    if not "--style=fusion" in sys.argv:
        sys.argv.append("--style=fusion")
    app = QApplication(sys.argv)
    win = App()
    if settings["fullscreen"]:
        win.showFullScreen()
    elif not settings["fullscreen"] and settings["maxmimized"]:
        win.showMaximized()
    else:
        win.resize(1200, 800)
        win.show()
    sys.exit(app.exec())
