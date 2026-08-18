import os  # imports os for looping through directories

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

import core  # Imports File Dialog and Windows :)

style = core.get_qss_styles("styling/fileexplorer")


class FileExplorer(core.Window):
    def __init__(self, master):
        super().__init__(master, "File Explorer", (960, 480), "textures/explorer.png")
        self.master = master
        self.toolbar = QWidget(self)
        self.toolbar.setStyleSheet(style["toolbar"])
        self.toolbar.setGeometry(0, 50, self.width(), 50)
        self.toolbar_layout = QHBoxLayout(self.toolbar)

        self.filepath_entry = QLineEdit(self.toolbar)
        self.filepath_entry.setPlaceholderText("Enter a filepath")
        self.filepath_entry.returnPressed.connect(
            lambda checked=False: self.load_dir(self.filepath_entry.text())
        )
        self.toolbar_layout.addWidget(self.filepath_entry)

        self.go_btn = QPushButton("Go ->", self.toolbar)
        self.go_btn.clicked.connect(
            lambda checked=False: self.load_dir(self.filepath_entry.text())
        )
        self.go_btn.setStyleSheet(style["button"])
        self.toolbar_layout.addWidget(self.go_btn)

        self.file_viewport = QScrollArea(self)
        self.file_viewport.setWidgetResizable(True)
        self.file_viewport.setGeometry(0, 120, self.width(), self.height() - 120)
        self.file_viewport.setStyleSheet(style["scrollbar"])

        self.files = QWidget()
        self.files.setStyleSheet(style["file_contents_container"])
        self.files_layout = QVBoxLayout(self.files)
        self.files_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.file_viewport.setWidget(self.files)

        self.load_dir("user_dir")

    def load_dir(self, filepath: str):

        self.filepath_entry.setText(filepath)

        for btn in self.files.findChildren(QPushButton):
            btn.deleteLater()

        with os.scandir(filepath) as files:
            for file in files:
                if file.is_dir():
                    self.folder_btn = QPushButton(file.name)
                    self.folder_btn.clicked.connect(
                        lambda checked=False, filepath=file.path: self.load_dir(
                            filepath
                        )
                    )
                    self.folder_btn.setStyleSheet(style["button"])
                    self.files_layout.addWidget(self.folder_btn)
                elif file.is_file():
                    self.file_btn = QPushButton(file.name)
                    self.file_btn.clicked.connect(
                        lambda checked=False, filepath=file.path: self.open_file(
                            filepath
                        )
                    )
                    self.file_btn.setStyleSheet(style["button"])
                    self.files_layout.addWidget(self.file_btn)

    def open_file(self, filepath: str):
        if filepath.endswith(".txt"):
            from apps.notepad import Notepad

            notepad = Notepad(self.master)
            notepad.load_file(filepath)
            notepad.show()

        elif filepath.endswith(
            (
                ".jpeg",
                ".png",
                ".jpg",
                ".bmp",
                ".ico",
                ".svg",
                ".tiff",
                ".ppm",
                ".xbm",
                ".xpm",
                ".webp",
            )
        ):
            from apps.imageviewer import ImageViewer

            imageviewer = ImageViewer(self.master)
            imageviewer.open_image(filepath)
            imageviewer.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = QMainWindow()
    win.resize(960, 480)
    win.setWindowTitle("File Explorer -- TESTING ENVIROMENT NOT FOR END USER --")
    FileExplorer(win).move(0, 0)
    win.show()
    sys.exit(app.exec())
