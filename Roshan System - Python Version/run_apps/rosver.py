from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton

import core

style = core.get_qss_styles("styling/rosver")


class Rosver(core.Window):
    def __init__(self, master):
        super().__init__(master, "Rosver", (300, 700))
        self.os_logo_lbl = QLabel(self)
        self.os_logo_lbl.setPixmap(
            QPixmap("textures/Logo.png").scaled(
                50,
                50,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )
        self.os_logo_lbl.move(30, 50)

        self.os_name_lbl = QLabel(self)
        self.os_name_lbl.setStyleSheet(style["os_name_lbl"])
        self.os_name_lbl.setText("Roshan OS")
        self.os_name_lbl.move(100, 50)

        self.version_label = QLabel(self)
        self.version_label.setText("Version 19 | 19.290726")
        self.version_label.setStyleSheet(style["text_lbl"])
        self.version_label.move(20, 120)

        self.text_lbl = QLabel(self)
        self.text_lbl.setText("""
Roshan OS and its GUI
is licensed under the MIT License
for anyone to use.
You can edit, alter and rewrite the
Roshan OS code and sell it for profit.
You can share the original or modified
code with anyone.
You can also change how downstream
users recieve this os.
You can run and modify the software
internally without making it public
but you must include the MIT License
text in all copies or substantial
portions of this os
""")
        self.text_lbl.setStyleSheet(style["text_lbl"])
        self.text_lbl.move(20, 160)

        self.contributors_label = QLabel(self)
        self.contributors_label.setText("""
Contributors:
* Roshan (Lead Developler)
* A cool black hole (Artist)
* Asier_Diamond (
     Making 3 backgrounds
  )
* Huopa (
     Skating in one of the backgrounds
  )
""")

        self.contributors_label.setStyleSheet(style["text_lbl"])
        self.contributors_label.move(20, 470)

        self.ok_btn = QPushButton(self)
        self.ok_btn.setText("Ok")
        self.ok_btn.setStyleSheet(style["btn"])
        self.ok_btn.clicked.connect(self.deleteLater)

        self.ok_btn.move((self.width() - self.ok_btn.width()) // 2, 660)


if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.setWindowTitle("Rosver -- Testing Enviroment NOT FOR END USERS --")
    win.resize(300, 600)
    Rosver(win).show()
    win.show()
    app.exec()
