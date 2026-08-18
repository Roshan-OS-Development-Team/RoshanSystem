try:
    from core.Window import Window
except ImportError:
    from Window import Window

import os
from collections.abc import Callable, Sequence

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

with open("styling/filedialog/button.qss", "r") as f:
    button_style = f.read()

with open("styling/filedialog/entry.qss", "r") as f:
    entry_style = f.read()

with open("styling/filedialog/filebar.qss", "r") as f:
    filebar_style = f.read()

with open("styling/filedialog/fileoptionsbox.qss", "r") as f:
    file_options_box = f.read()

with open("styling/filedialog/scrollbar.qss", "r") as f:
    scrollbar_style = f.read()


class SaveFileDialog(Window):
    def __init__(
        self,
        master,
        filetype: str | Sequence[str],
        save_callback: Callable[[str], None],
    ):
        super().__init__(
            master,
            f"Save {filetype if type(filetype) == str else ''} files",
            (960, 480),
            "textures/explorer.png",
        )
        self.file_extensions = filetype if type(filetype) == str else tuple(filetype)

        self.toolbar = QWidget(self)
        self.toolbar.setGeometry(0, 60, self.width(), 50)
        self.toolbar_layout = QHBoxLayout(self.toolbar)
        self.toolbar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.files_viewport = QScrollArea(self)
        self.files_viewport.setStyleSheet(scrollbar_style)
        self.files_viewport.setGeometry(0, 120, self.width(), self.height() - 170)
        self.files_viewport.setWidgetResizable(True)

        self.files = QWidget()
        self.files_layout = QVBoxLayout(self.files)
        self.files_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.files_viewport.setWidget(self.files)

        self.filepath_entry = QLineEdit()
        self.filepath_entry.setText("user_dir")
        self.filepath_entry.returnPressed.connect(
            lambda: self.load_dir(self.filepath_entry.text())
        )
        self.filepath_entry.setStyleSheet(entry_style)
        self.toolbar_layout.addWidget(self.filepath_entry)

        self.go_btn = QPushButton("Go ->")
        self.go_btn.clicked.connect(lambda: self.load_dir(self.filepath_entry.text()))
        self.go_btn.setStyleSheet(button_style)
        self.toolbar_layout.addWidget(self.go_btn)

        self.filebar = QWidget(self)
        self.filebar.setGeometry(0, 430, self.width(), 50)
        self.filebar.setStyleSheet(filebar_style)

        self.filebar_layout = QHBoxLayout(self.filebar)
        self.filebar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.file_name_entry = QLineEdit()
        self.file_name_entry.setStyleSheet(entry_style)
        self.filebar_layout.addWidget(self.file_name_entry)

        self.extensions_box = QComboBox()
        self.extensions_box.setStyleSheet(file_options_box)

        if type(self.file_extensions) == str:
            self.extensions_box.addItem(self.file_extensions)
        else:
            self.extensions_box.addItems(self.file_extensions)

        self.extensions_box.currentTextChanged.connect(
            self.handle_file_extension_change
        )

        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.handle_save)
        self.save_btn.setStyleSheet(button_style)

        self.filebar_layout.addWidget(self.extensions_box)

        self.filebar_layout.addWidget(self.save_btn)

        self.save_callback = save_callback
        self.filepath = ""

        self.file_extension = self.file_extensions[0]

        self.load_dir(
            os.path.join(
                os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "user_dir"
            )
        )

    def handle_file_extension_change(self, text: str):
        self.file_extension = text

    def load_dir(self, filepath: str) -> None:

        self.filepath = filepath

        self.filepath_entry.setText(filepath)

        for btn in self.files.findChildren(QPushButton):
            btn.deleteLater()

        with os.scandir(filepath) as files:

            for file in files:
                if file.is_dir():
                    self.folder_btn = QPushButton()
                    self.folder_btn.setStyleSheet(button_style)
                    self.folder_btn.setText(file.name)
                    self.folder_btn.clicked.connect(
                        lambda checked=False, filepath=file.path: self.load_dir(filepath)
                    )
                    self.files_layout.addWidget(self.folder_btn)
                elif file.is_file():
                    self.file_btn = QPushButton()
                    self.file_btn.setStyleSheet(button_style)
                    self.file_btn.setText(file.name)
                    self.file_btn.clicked.connect(
                        lambda checked=False, filename=file.name: (
                            self.file_name_entry.setText(filename)
                        )
                    )
                    self.files_layout.addWidget(self.file_btn)

    def handle_save(self):
        filename = self.file_name_entry.text()
        if not filename.endswith(self.file_extensions):
            filename = f"{filename}{self.file_extension}"
        self.save_callback(os.path.join(self.filepath, filename))
        self.destroy()


class OpenFileDialog(Window):
    def __init__(
        self,
        master,
        filetype: str | Sequence[str],
        open_callback: Callable[[str], None],
    ):
        super().__init__(
            master,
            f"Open {filetype if type(filetype) == str else ''} files",
            (960, 480),
            "textures/fileexplorer.png",
        )
        self.file_extensions = filetype if type(filetype) == str else tuple(filetype)

        self.toolbar = QWidget(self)
        self.toolbar.setGeometry(0, 60, self.width(), 50)
        self.toolbar_layout = QHBoxLayout(self.toolbar)
        self.toolbar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.files_viewport = QScrollArea(self)
        self.files_viewport.setStyleSheet(scrollbar_style)
        self.files_viewport.setGeometry(0, 120, self.width(), self.height() - 170)
        self.files_viewport.setWidgetResizable(True)

        self.files = QWidget()
        self.files_layout = QVBoxLayout(self.files)
        self.files_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.files_viewport.setWidget(self.files)

        self.filepath_entry = QLineEdit()
        self.filepath_entry.setText("user_dir")
        self.filepath_entry.returnPressed.connect(
            lambda: self.load_dir(self.filepath_entry.text())
        )
        self.filepath_entry.setStyleSheet(entry_style)
        self.toolbar_layout.addWidget(self.filepath_entry)

        self.go_btn = QPushButton("Go ->")
        self.go_btn.clicked.connect(lambda: self.load_dir(self.filepath_entry.text()))
        self.go_btn.setStyleSheet(button_style)
        self.toolbar_layout.addWidget(self.go_btn)

        self.filebar = QWidget(self)
        self.filebar.setGeometry(0, 430, self.width(), 50)
        self.filebar.setStyleSheet(filebar_style)

        self.filebar_layout = QHBoxLayout(self.filebar)
        self.filebar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.file_name_entry = QLineEdit()
        self.file_name_entry.setStyleSheet(entry_style)
        self.filebar_layout.addWidget(self.file_name_entry)

        self.extensions_box = QComboBox()
        self.extensions_box.setStyleSheet(file_options_box)

        if type(self.file_extensions) == str:
            self.extensions_box.addItem(self.file_extensions)
        else:
            self.extensions_box.addItems(self.file_extensions)

        self.extensions_box.currentTextChanged.connect(
            self.handle_file_extension_change
        )

        self.open_btn = QPushButton("Open")
        self.open_btn.clicked.connect(self.handle_open)
        self.open_btn.setStyleSheet(button_style)

        self.filebar_layout.addWidget(self.extensions_box)

        self.filebar_layout.addWidget(self.open_btn)

        self.open_callback = open_callback
        self.filepath = ""

        self.file_extension = self.file_extensions[0]

        self.load_dir(
            os.path.join(
                os.path.abspath(os.path.dirname(os.path.dirname(__file__))), "user_dir"
            )
        )

    def handle_file_extension_change(self, text: str):
        self.file_extension = text

    def load_dir(self, filepath: str) -> None:

        self.filepath = filepath

        self.filepath_entry.setText(filepath)

        for btn in self.files.findChildren(QPushButton):
            btn.deleteLater()

        for file in os.scandir(filepath):
            if file.is_dir():
                self.folder_btn = QPushButton()
                self.folder_btn.setStyleSheet(button_style)
                self.folder_btn.setText(file.name)
                self.folder_btn.clicked.connect(
                    lambda checked=False, filepath=file.path: self.load_dir(filepath)
                )
                self.files_layout.addWidget(self.folder_btn)
            elif file.is_file():
                self.file_btn = QPushButton()
                self.file_btn.setStyleSheet(button_style)
                self.file_btn.setText(file.name)
                self.file_btn.clicked.connect(
                    lambda checked=False, filename=file.name: (
                        self.file_name_entry.setText(filename)
                    )
                )
                self.files_layout.addWidget(self.file_btn)

    def handle_open(self):
        filename = self.file_name_entry.text()
        if not filename.endswith(self.file_extensions):
            filename = f"{filename}{self.file_extension}"
        self.open_callback(os.path.join(self.filepath, filename))
        self.destroy()


if __name__ == "__main__":
    import sys

    sys.argv.append("--style=fusion")
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.resize(960, 480)

    def handle_save(filepath: str) -> None:
        with open(filepath, "w") as f:
            f.write("Hello, World!")

    SaveFileDialog(window, (".txt", ".json", ".csv"), handle_save).move(0, 0)
    window.show()
    sys.exit(app.exec())
