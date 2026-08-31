from ast import expr

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QWidget,
)

import core

style = core.get_qss_styles("styling/calculator")


class Calculator(core.Window):
    def __init__(self, master):
        super().__init__(master, "Calculator", (450, 650), "textures/calculator.png")
        self.expression: str = ""

        self.expression_lbl = QLabel(self)
        self.expression_lbl.setStyleSheet(style["expression_lbl"])
        self.expression_lbl.setText(self.expression)
        self.expression_lbl.setGeometry(10, 40, self.width() - 20, 75)

        self.btns_container = QWidget(self)
        self.btns_container.setGeometry(0, 110, self.width(), self.height() - 110)

        self.btns_layout = QGridLayout(self.btns_container)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setStyleSheet(style["button"])
        self.clear_btn.clicked.connect(self.clear)
        self.clear_btn.setFixedHeight(100)
        self.btns_layout.addWidget(self.clear_btn, 0, 0, 1, 4)

        self.buttons: list[list[int | str]] = [
            [7, 8, 9],
            [4, 5, 6],
            [1, 2, 3],
            ["=", 0, "."],
        ]

        self.row = 1

        for row_idx, row_list in enumerate(self.buttons):
            for column_idx, num in enumerate(row_list):
                row = row_idx + self.row
                self.num_btn = QPushButton(str(num))
                self.num_btn.setFixedSize(100, 100)
                self.num_btn.setShortcut(str(num))
                if num == "=":
                    self.num_btn.clicked.connect(self.evaluate_expression)
                else:
                    self.num_btn.clicked.connect(
                        lambda checked=False, number=num: self.add_num_to_str(number)
                    )
                self.num_btn.setStyleSheet(style["button"])
                self.btns_layout.addWidget(self.num_btn, row, column_idx, 1, 1)

        self.operators = ["+", "-", "*", "/"]

        for row_idx, operator in enumerate(self.operators):
            row = row_idx + 1
            self.operator_btn = QPushButton(operator)
            self.operator_btn.setShortcut(operator)
            self.operator_btn.setFixedSize(100, 100)
            self.operator_btn.setStyleSheet(style["button"])
            self.operator_btn.clicked.connect(
                lambda checked=False, op=operator: self.add_num_to_str(f" {op} ")
            )
            self.btns_layout.addWidget(self.operator_btn, row, 3, 1, 1)

    def clear(self):
        self.expression = ""
        self.expression_lbl.setText(self.expression)

    def add_num_to_str(self, num: str | int):
        self.expression += str(num)
        self.expression_lbl.setText(self.expression)

    def evaluate_expression(self):

        for operator in self.operators:
            if operator in self.expression:
                expression = [float(item.strip()) for item in self.expression.split(operator)]
                result: float = 0.0
                for num in expression:
                    match operator:
                        case "+":
                            result += num
                        case "-":
                            result -= num
                        case "*":
                            result *= num
                        case "/":
                            if 0 in expression:
                                self.expression_lbl.setText("Error: Cannot Divide by 0")
                                return
                            result /= num
                self.changeLabelText(result)
                return

    def changeLabelText(self, result: float):
        if result % 1 == 0:
            self.expression = str(int(result))
        else:
            self.expression = str(result)
        self.expression_lbl.setText(self.expression)


if __name__ == "__main__":
    import sys

    sys.argv.append("--style=fusion")
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("Calcualator -- TESTING ENVIROMENT NOT FOR END USER --")
    win.resize(450, 650)
    Calculator(win).move(0, 0)
    win.show()
    sys.exit(app.exec())
