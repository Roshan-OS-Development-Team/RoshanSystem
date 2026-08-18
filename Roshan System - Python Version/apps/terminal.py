import subprocess

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QPlainTextEdit, QApplication, QMainWindow

import core

style = core.get_qss_styles("styling/terminal")

class TerminalText(QPlainTextEdit):
    def __init__(self, master):
        super().__init__(master)
        self.setStyleSheet(style["text_area"])
        self.appendPlainText("> ")

    def keyPressEvent(self, e: QKeyEvent, /) -> None:
        if e.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.run_cmd()
            return
        super().keyPressEvent(e)

    def run_cmd(self):

        cursor = self.textCursor()
        current_line_text = cursor.block().text()

        cmd = current_line_text.removeprefix("> ").strip()
        if cmd:
            try:
                output = subprocess.run(cmd, capture_output=True, shell=True, text=True, timeout=5, check=False)
                result = output.stdout + output.stderr
            except subprocess.TimeoutExpired:
                result = "\nError: Command Timed out"
            except Exception as ex: # NOQA
                result = f"\nError: {str(ex)}" # NOQA
        else:
            result = ""

        if result:
            self.appendPlainText(result.strip())
        self.appendPlainText("> ")
        self.ensureCursorVisible()

class Terminal(core.Window):
    def __init__(self, master):
        super().__init__(master, "Terminal", (960, 480), "textures/terminal.png")
        TerminalText(self).setGeometry(0, 50, self.width(), self.height() - 50)


if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.setWindowTitle("Terminal -- Testing Enviroment NOT FOR END USER --")
    win.resize(960, 480)
    Terminal(win).move(0, 0)
    win.show()
    app.exec()
