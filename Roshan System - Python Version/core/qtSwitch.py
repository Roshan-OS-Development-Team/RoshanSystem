from collections.abc import Callable
from typing import Any

from PySide6.QtWidgets import (  # Imports everything needed for the Switch
    QApplication,  # QApplication for the testing
    QHBoxLayout,  # QHBoxLayout for Horizontal Switch
    QPushButton,  # QPushButton for the buttons
    QVBoxLayout,  # QVBoxLayout for the Vertical Switch
    QWidget,  # QWidget for the switch container itself
)

style = {}
with open("styling/qtSwitch/selected_btn.qss", "r") as f:
    style["selected_btn"] = f.read()

with open("styling/qtSwitch/unselected_btn.qss", "r") as f:
    style["unselected_btn"] = f.read()

class QtSwitch(QWidget):
    def __init__(self, master, offLabel: str, onLabel: str, QLayout, onChangeCallback: Callable[[bool], Any]) -> None:
        super().__init__(master)
        self._layout: QVBoxLayout | QHBoxLayout = QLayout(self)
        self.onChangeCallback = onChangeCallback
        self.switchedOn: bool = False

        self.off_btn = QPushButton(self)
        self.off_btn.setStyleSheet(style["selected_btn"])
        self.off_btn.setText(offLabel)
        self.off_btn.clicked.connect(self.handleSwitch)
        self._layout.addWidget(self.off_btn)

        self.on_btn = QPushButton(self)
        self.on_btn.setStyleSheet(style["unselected_btn"])
        self.on_btn.setText(onLabel)
        self.on_btn.clicked.connect(self.handleSwitch)
        self._layout.addWidget(self.on_btn)

        self.selected: bool = False

    def handleSwitch(self):
        if self.selected:
            self.off_btn.setStyleSheet(style["selected_btn"])
            self.on_btn.setStyleSheet(style["unselected_btn"])
            self.onChangeCallback(False)
        else:
            self.off_btn.setStyleSheet(style["unselected_btn"])
            self.on_btn.setStyleSheet(style["selected_btn"])
            self.onChangeCallback(True)
        self.selected = not self.selected

class VerticalSwitch(QtSwitch):
    def __init__(self, master = None, offLabel: str = "Off", onLabel: str = "On", onChangeCallback: Callable[[bool], Any] = print) -> None:
        super().__init__(master, offLabel, onLabel, QVBoxLayout, onChangeCallback)

class HorizontalSwitch(QtSwitch):
    def __init__(self, master = None, offLabel: str = "Off", onLabel: str = "On", onChangeCallback: Callable[[bool], Any] = print) -> None:
        super().__init__(master, offLabel, onLabel, QHBoxLayout, onChangeCallback)

if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    test1 = VerticalSwitch()
    test1.resize(100, 50)
    test2 = HorizontalSwitch()
    test2.resize(100, 50)
    test1.show()
    test2.show()
    app.exec()
