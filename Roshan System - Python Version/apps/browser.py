from PySide6.QtCore import QUrl
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
)

import core

style = core.get_qss_styles("styling/browser")

class BrowserPage(QWebEnginePage):
    def javaScriptConsoleMessage(self, level: QWebEnginePage.JavaScriptConsoleMessageLevel, message: str, lineNumber: int, sourceID: str, /) -> None:
        if level == QWebEnginePage.JavaScriptConsoleMessageLevel.ErrorMessageLevel:
            print(f"[ERROR]: {message}")
        elif level == QWebEnginePage.JavaScriptConsoleMessageLevel.WarningMessageLevel:
            print(f"[WARNING]: {message}")
        else:
            print(f"[INFO]: {message}")

class Browser(core.Window):
    def __init__(self, master) -> None:
        super().__init__(master, "Browser", (1200, 800), "textures/browser.png")
        self.toolbar = QWidget(self)
        self.toolbar.setStyleSheet(style["toolbar"])
        self.toolbar.setGeometry(10, 50, self.width() - 20, 50)
        self.toolbarLayout = QHBoxLayout(self.toolbar)

        self.webview = QWebEngineView(self)
        self.webviewPage = BrowserPage()
        self.webview.setPage(self.webviewPage)
        self.webview.setGeometry(10, 110, self.width() - 20, self.height() - 130)
        self.webview.load("https://google.com")

        self.backBtn = QPushButton(self)
        self.backBtn.setText("<-")
        self.backBtn.clicked.connect(lambda checked: self.handleBackOrForwards("backwards"))
        self.backBtn.setStyleSheet(style["button"])

        self.forwardsBtn = QPushButton(self)
        self.forwardsBtn.setText("->")
        self.forwardsBtn.clicked.connect(lambda checked: self.handleBackOrForwards("forwards"))
        self.forwardsBtn.setStyleSheet(style["button"])

        self.toolbarLayout.addWidget(self.backBtn)
        self.toolbarLayout.addWidget(self.forwardsBtn)

        self.urlInput = QLineEdit(self)
        self.urlInput.setText("https://google.com")
        self.urlInput.returnPressed.connect(self.handleURLChange)
        self.urlInput.setStyleSheet(style["urlInput"])

        self.toolbarLayout.addWidget(self.urlInput)

    def handleBackOrForwards(self, state: str) -> None:
        if state == "backwards" and self.webview.history().canGoBack():
            self.webview.back()
            self.urlInput.setText(self.webview.url().toString())
        elif state == "forwards" and self.webview.history().canGoForward():
            self.webview.forward()
            self.urlInput.setText(self.webview.url().toString())

    def handleURLChange(self) -> None:
        url = self.urlInput.text()
        if not url.startswith("http"):
            url = "https://" + url

        self.webview.load(QUrl(url))

if __name__ == "__main__":
    app = QApplication(["--style=fusion"])
    win = QMainWindow()
    win.setWindowTitle("Browser -- TESTING ENVIROMENT NOT FOR END USER --")
    win.resize(1200, 800)
    Browser(win).show()
    win.show()
    app.exec()
