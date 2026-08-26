from PySide6.QtWidgets import QApplication, QMainWindow

import core


class Paint(core.WebWindow):
    def __init__(self, master):
        super().__init__(master, "Pain(t)", size=(960, 480), icon="textures/paint.png")
        self.webview.load("https://roshan-os-development-team.github.io/ROS-Paint-App/")


if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.setWindowTitle("Paint -- Testing Enviroment NOT FOR END USER --")
    win.resize(960, 480)
    Paint(win).move(0, 0)
    win.show()
    app.exec()
