from PySide6.QtWidgets import QApplication, QMainWindow

import core

with open("apps/paint.html", "r") as f:
    htmlCode = f.read()


class Paint(core.WebWindow):
    def __init__(self, master):
        super().__init__(master, "Pain(t)", htmlCode, (960, 480), "textures/paint.png")


if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.setWindowTitle("Paint -- Testing Enviroment NOT FOR END USER --")
    win.resize(960, 480)
    Paint(win).move(0, 0)
    win.show()
    app.exec()
