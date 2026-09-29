from collections.abc import Callable

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QPushButton, QApplication, QMainWindow

import core

style = core.get_qss_styles("styling/base_messagebox")

class MessageBoxYesNo(core.Window):
    """
    Title: sets the title of the messagebox
    Message: sets the message of the messagebox
    Callback Function: passes in True to the function if true else it will be false
    """
    def __init__(
            self,
            master, 
            title: str = "Messagebox Yes No", 
            message: str = "A yes or no messagebox", 
            messageboxTexture: str = "textures/confirm.png",
            callbackFunction: Callable[[bool], None] = print
        ):
        super().__init__(master, title, (640, 360), messageboxTexture)
        self.textureLabel = QLabel(self)
        self.textureLabel.setGeometry(50, 100, 100, 100)
        self.textureLabel.setPixmap(
            QPixmap(messageboxTexture).scaled(
                100,
                100,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        self.messageLabel = QLabel(message, self)
        self.messageLabel.move(200, 125)

        self.messageLabel.setStyleSheet(style["messageLabel"])

        self.yesBtn = QPushButton("Yes", self)
        self.yesBtn.clicked.connect(lambda checked: callbackFunction(True))
        self.yesBtn.move(500, 250)
        self.yesBtn.setStyleSheet(style["button"])

        self.noBtn = QPushButton("No", self)
        self.noBtn.clicked.connect(lambda checked: callbackFunction(False))
        self.noBtn.move(425, 250)
        self.noBtn.setStyleSheet(style["button"])

def main():
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.setWindowTitle("Message box yes no")
    win.resize(640, 360)
    MessageBoxYesNo(win)
    win.show()
    app.exec()

if __name__ == "__main__":
    main()