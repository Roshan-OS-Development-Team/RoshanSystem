import hashlib
import json
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QResizeEvent
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
)


class LoginPage(QWidget):
    def __init__(self, master: QWidget):
        super().__init__(master)
        self.setGeometry(0, 0, master.width(), master.height())
        self.background = QWidget(self)
        self.background.setGeometry(0, 0, self.width(), self.height())
        self.background.setStyleSheet(
            "QWidget {"
            "   background-color: rgba(30, 30, 30, 230);"
            "   border-radius: 10px;"
            "   border: 2px solid white;"
            "}"
        )
        self.userico = QPixmap("textures/user.png").scaled(
            100,
            100,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        self.usericolabel = QLabel(self)
        self.usericolabel.setPixmap(self.userico)
        self.usericolabel.setStyleSheet("background-color: transparent;")
        self.usericolabel.move(self.width() // 2 - 100, 50)

        self.errorLabel = QLabel(self)
        self.errorLabel.setStyleSheet(
            "QLabel {"
            "   background-color: transparent;"
            "   font-size: 20px;"
            "}"
        )
        self.errorLabel.move(self.width() // 2, 160)

        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText("Username: ")
        self.usernameLabel.setStyleSheet(
            "QLabel {"
            "   background-color: transparent;"
            "   font-size: 20px;"
            "}"
        )
        self.usernameLabel.move(self.width() // 2 - 20 * len("Username: "), 190)
        self.usernameEntry = QLineEdit(self)
        self.usernameEntry.setStyleSheet(
            "QLineEdit {"
            "   background-color: transparent;"
            "   font-size: 20px;"
            "}"
        )
        self.usernameEntry.returnPressed.connect(self.handleLoginOrSignup)
        self.usernameEntry.move(self.width() // 2 - 10 * len("Username: "), 190)

        self.passwordLabel = QLabel(self)
        self.passwordLabel.setText("Password: ")
        self.passwordLabel.setStyleSheet(
            "QLabel {"
            "   background-color: transparent;"
            "   font-size: 20px;"
            "}"
        )
        self.passwordLabel.move(self.width() // 2 - 20 * len("Password: "), 230)
        self.passwordEntry = QLineEdit(self)
        self.passwordEntry.setStyleSheet(
            "QLineEdit {"
            "   background-color: transparent;"
            "   font-size: 20px;"
            "}"
        )
        self.passwordEntry.returnPressed.connect(self.handleLoginOrSignup)
        self.passwordEntry.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEntry.move(self.width() // 2 - 10 * len("Password: "), 230)

    def resizeEvent(self, event: QResizeEvent, /) -> None:
        super().resizeEvent(event)
        self.background.setGeometry(0, 0, self.width(), self.height())
        self.usernameLabel.move(self.width() // 2 - 20 * len("Username: "), 190)
        self.usernameEntry.move(self.width() // 2 - 10 * len("Username: "), 190)
        self.passwordLabel.move(self.width() // 2 - 20 * len("Password: "), 230)
        self.passwordEntry.move(self.width() // 2 - 10 * len("Password: "), 230)

    def handleLoginOrSignup(self):
        if (
            os.path.exists("login_details.json")
            and os.path.getsize("login_details.json") > 2
        ):
            with open("login_details.json", "r") as f:
                loginDetails = json.load(f)

            if self.checkSHA3512(
                self.usernameEntry.text(), loginDetails["username"]
            ) and self.checkSHA3512(
                self.passwordEntry.text(), loginDetails["password"]
            ):
                self.deleteLater()
            else:
                self.errorLabel.setText("Username or password is wrong")
                self.errorLabel.move(
                    self.width() // 2 - 10 * len("Username or password is wrong"), 160
                )
                self.errorLabel.setFixedWidth(10 * len("Username or password is wrong"))

        else:
            loginDetails = {
                "username": hashlib.sha3_512(
                    self.usernameEntry.text().encode()
                ).hexdigest(),
                "password": hashlib.sha3_512(
                    self.passwordEntry.text().encode()
                ).hexdigest(),
            }

            with open("login_details.json", "w") as f:
                json.dump(loginDetails, f, indent=4)

            self.deleteLater()

    def checkSHA3512(self, guess: str, sha3512: str):
        _sha3512 = hashlib.sha3_512(guess.encode()).hexdigest()
        return sha3512 == _sha3512

if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.resize(960, 480)
    win.setWindowTitle("Login Page -- TESTING ENVIROMENT NOT FOR END USER --")
    loginPage = LoginPage(win)
    win.show()
    app.exec()
