from collections.abc import Callable
from typing import Any

from PySide6.QtWidgets import (  # Imports everything needed for the Switch
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
        self.switchedOn: bool = False
