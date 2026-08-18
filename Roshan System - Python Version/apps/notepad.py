import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QWidget,
)

import core

style = core.get_qss_styles("styling/notepad")


class Notepad(core.Window):
    def __init__(self, master):
        super().__init__(master, "Notepad", (960, 480), "textures/notepad.png")

        self.master = master

        self.toolbar = QWidget(self)
        self.toolbar.setGeometry(0, 40, self.width(), 50)
        self.toolbar.setStyleSheet(style["toolbar"])

        self.toolbar_layout = QHBoxLayout(self.toolbar)
        self.toolbar_layout.setContentsMargins(10, 10, 10, 10)

        self.save_btn = QPushButton("Save", self.toolbar)
        self.save_btn.setAutoFillBackground(True)
        self.save_btn.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.save_btn.setStyleSheet(style["button"])
        self.save_btn.clicked.connect(self.handle_save)
        self.save_btn.setShortcut("Ctrl+S")

        self.open_btn = QPushButton("Open", self.toolbar)
        self.open_btn.setAutoFillBackground(True)
        self.open_btn.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.open_btn.setStyleSheet(style["button"])
        self.open_btn.clicked.connect(self.handle_open)
        self.open_btn.setShortcut("Ctrl+O")

        self.toolbar_layout.addWidget(self.save_btn)
        self.toolbar_layout.addWidget(self.open_btn)

        self.textbox = QTextEdit(self)
        self.textbox.setGeometry(0, 110, self.width(), self.height() - 110)

    def handle_save(self) -> None:
        def _handle_save(filepath: str):
            if not filepath.endswith(".txt"):
                filepath = f"{filepath}txt"
            with open(filepath, "w") as f:
                f.write(self.textbox.toPlainText())

        file_dialog = core.SaveFileDialog(self.master, ".txt", _handle_save)
        file_dialog.show()
        file_dialog.move(0, 0)

    def handle_open(self):
        def _handle_open(filepath: str):
            if not filepath.endswith(".txt"):
                filepath = f"{filepath}txt"
            with open(filepath, "r") as f:
                self.textbox.setText(f.read())

        file_dialog = core.OpenFileDialog(self.master, ".txt", _handle_open)
        file_dialog.show()
        file_dialog.move(0, 0)

    def load_file(self, filepath: str):
        with open(filepath, "r") as f:
            self.textbox.setText(f.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("Notepad -- Testing Enviroment NOT FOR END USER --")
    window.resize(1200, 800)
    Notepad(window).move(0, 0)
    window.show()
    sys.exit(app.exec())
