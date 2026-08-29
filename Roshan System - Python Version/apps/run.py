import importlib
import json

from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QPushButton

import core

style = core.get_qss_styles("styling/run")


class Run(core.Window):
    def __init__(self, master):
        super().__init__(master, "Run", (600, 300), "textures/run.png")

        with open("run_apps/run_apps.json", "r") as f:
            apps = json.load(f)

        self.apps: dict[str, core.Window] = {}

        for app in apps:
            app_module = importlib.import_module(apps[app]["module"])
            app_class = getattr(app_module, apps[app]["class_or_func"])
            app_instance = app_class(master)
            app_instance.hide()

            self.apps[app.lower()] = app_instance

        self.app_entry = QLineEdit(self)
        self.app_entry.setStyleSheet(style["app_entry"])
        self.app_entry.returnPressed.connect(
            lambda checked=False: self.openApp(self.app_entry.text())
        )
        self.app_entry.setGeometry(10, 50, self.width() - 20, 50)

        self.cancel_btn = QPushButton(self)
        self.cancel_btn.setText("Cancel")
        self.cancel_btn.setStyleSheet(style["button"])
        self.cancel_btn.clicked.connect(self.hide)
        self.cancel_btn.move(200, 150)

        self.ok_btn = QPushButton(self)
        self.ok_btn.setText("Ok")
        self.ok_btn.setStyleSheet(style["button"])
        self.ok_btn.clicked.connect(
            lambda checked=False: self.openApp(self.app_entry.text())
        )
        self.ok_btn.move(300, 150)

    def openApp(self, app: str):
        _app = self.apps.get(app.lower())
        if _app:
            _app.show()
        else:
            self.app_entry.setText("App does not exist")


if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.resize(600, 300)
    win.setWindowTitle("Run -- Testing Enviroment NOT FOR END USER --")
    Run(win).show()
    win.show()
    app.exec()
