from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QWidget,
)

import core

style = core.get_qss_styles("styling/imageviewer")


class ImageViewer(core.Window):
    def __init__(self, master):
        super().__init__(master, "Image Viewer", (960, 480), "textures/imageviewer.png")

        self.master = master

        self.toolbar = QWidget(self)
        self.toolbar.setStyleSheet(style["toolbar"])
        self.toolbar.setGeometry(10, 50, self.width() - 20, 50)

        self.toolbar_layout = QHBoxLayout(self.toolbar)
        self.toolbar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.open_file_btn = QPushButton("Open an image")
        self.open_file_btn.setStyleSheet(style["button"])
        self.open_file_btn.clicked.connect(self.load_image)

        self.toolbar_layout.addWidget(self.open_file_btn)

        self.img = QPixmap("textures/background7.png").scaled(
            self.width() - 20,
            self.height() - 120,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.img_label = QLabel(self)
        self.img_label.setPixmap(self.img)
        self.img_label.setGeometry(10, 110, self.width() - 20, self.height() - 120)

    def load_image(self):
        def _load_image(filepath: str):
            self.img = QPixmap(filepath).scaled(
                self.width() - 20,
                self.height() - 120,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            self.img_label.setPixmap(self.img)

        self.filedialog = core.OpenFileDialog(
            self.master,
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
            ),
            _load_image,
        )
        self.filedialog.show()

    def open_image(self, filepath: str):
        self.img.load(filepath)
        self.img_label.setPixmap(self.img)


if __name__ == "__main__":
    import sys

    sys.argv.append("--style=fusion")
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Image Viewer -- Testing Enviroment NOT FOR END USER --")
    win.resize(960, 480)
    ImageViewer(win).move(0, 0)
    win.show()
    sys.exit(app.exec())
