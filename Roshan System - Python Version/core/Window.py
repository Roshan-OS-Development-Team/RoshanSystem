from PySide6.QtCore import QRectF, Qt, QUrl
from PySide6.QtGui import (
    QColor,
    QImage,
    QMouseEvent,
    QPainter,
    QPainterPath,
    QPaintEvent,
    QPixmap,
)
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineSettings
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QGraphicsBlurEffect,
    QGraphicsPixmapItem,
    QGraphicsScene,
    QLabel,
    QPushButton,
    QWidget,
)

with open("styling/window/window.qss", "r") as f:
    window_style = f.read()

with open("styling/window/window_close_btn.qss", "r") as f:
    close_btn_style = f.read()


class Window(QWidget):
    def __init__(
        self,
        master,
        title: str = "ROSW",
        size: tuple[int, int] | None = None,
        icon: str = "textures/generic app.png",
    ):
        super().__init__(master)
        if type(size) == tuple:
            self.resize(size[0], size[1])


        self.background = QWidget(self)
        self.background.setGeometry(0, 0, self.width(), self.height())
        self.background.setStyleSheet(
            "QWidget {"
            "   border: 2px solid white;"
            "   border-radius: 10px;"
            "}"
        )

        self.background.lower()

        self.titlebar = QWidget(self)
        self.titlebar.setGeometry(0, 0, self.width(), 35)
        self.titlebar.setStyleSheet(window_style)

        self.win_ico = QPixmap(icon).scaled(
            20,
            20,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.icolabel = QLabel(self)
        self.icolabel.setPixmap(self.win_ico)
        self.icolabel.move(10, 10)

        self.titlelabel = QLabel(self)
        self.titlelabel.setText(title)
        self.titlelabel.move(60, 10)

        self.close_btn = QPushButton(self)
        self.close_btn.setStyleSheet(close_btn_style)
        self.close_btn.setText("X")
        self.close_btn.clicked.connect(self.hide)
        self.close_btn.setGeometry(self.width() - 30, 10, 20, 20)

        self.position: dict[str, int] = {"x": 0, "y": 0}

        self.setMouseTracking(True)

        self.startX: int = 0
        self.startY: int = 0

        self._blurDirty = True
        self._blurredBg = None

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.startX = int(event.position().x())
        self.startY = int(event.position().y())
        self.raise_()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() & Qt.MouseButton.LeftButton:
            x = self.x() + int(event.position().x()) - self.startX
            y = self.y() + int(event.position().y()) - self.startY
            self.position["x"] = x
            self.position["y"] = y
            self.move(x, y)
            self._blurDirty = True
        super().mouseMoveEvent(event)

    def paintEvent(self, event: QPaintEvent):
        painter: QPainter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        clipPath: QPainterPath = QPainterPath()
        clipPath.addRoundedRect(self.rect(), 10, 10)
        painter.setClipPath(clipPath)

        if self.parentWidget():

            if self._blurDirty or self._blurredBg is None:

                self.hide()

                background: QPixmap = self.parentWidget().grab(self.geometry())

                self.show()

                blur: QGraphicsBlurEffect = QGraphicsBlurEffect(self)
                blur.setBlurRadius(15)
                blur.setBlurHints(QGraphicsBlurEffect.BlurHint.PerformanceHint)

                scene: QGraphicsScene = QGraphicsScene()
                item: QGraphicsPixmapItem = QGraphicsPixmapItem()
                item.setPixmap(background)
                item.setGraphicsEffect(blur)
                scene.addItem(item)

                self._blurredBg: QImage = QImage(self.size(), QImage.Format.Format_ARGB32_Premultiplied)
                self._blurredBg.fill(Qt.GlobalColor.transparent)

                imagePainter: QPainter = QPainter(self._blurredBg)

                scene.render(imagePainter, QRectF(), QRectF(0, 0, self.width(), self.height()))

                imagePainter.end()

                self._blurDirty = False

            painter.drawImage(0, 0, self._blurredBg)

        painter.setBrush(QColor(0, 0, 0, 140))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(self.rect())

        super().paintEvent(event)

class WebEnginePage(QWebEnginePage):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
    def javaScriptConsoleMessage(self, level: QWebEnginePage.JavaScriptConsoleMessageLevel, message: str, lineNumber: int, sourceID: str, /) -> None:
        if level == QWebEnginePage.JavaScriptConsoleMessageLevel.ErrorMessageLevel:
            print(f"[ERROR]: {message}")
        elif level == QWebEnginePage.JavaScriptConsoleMessageLevel.WarningMessageLevel:
            print(f"[WARNING]: {message}")
        else:
            print(f"[LOG]: {message}")

class WebWindow(QWidget):
    def __init__(
        self,
        master,
        title: str = "ROSW",
        html_str: str = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roshan OS Website</title>
    <style>
        html, body {
            background-color: rgb(50, 50, 50);
        }
        h1 {
            color: white;
            font-family: "Jetbrains Mono";
        }
    </style>
</head>
<body>
    <h1>This is the default website for Roshan OS</h1>
</body>
</html>""",
        size: tuple[int, int] | None = None,
        icon: str = "textures/generic app.png",
    ):
        super().__init__(master)
        if type(size) == tuple:
            self.resize(size[0], size[1])

        self.background = QWidget(self)
        self.background.setGeometry(0, 0, self.width(), self.height())
        self.background.setStyleSheet(
            "QWidget {"
            "   border: 2px solid white;"
            "   border-radius: 10px;"
            "}"
        )

        self.background.lower()

        self.titlebar = QWidget(self)
        self.titlebar.setGeometry(0, 0, self.width(), 35)
        self.titlebar.setStyleSheet(window_style)

        self.win_ico = QPixmap(icon).scaled(
            20,
            20,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

        self.icolabel = QLabel(self)
        self.icolabel.setPixmap(self.win_ico)
        self.icolabel.move(10, 10)

        self.titlelabel = QLabel(self)
        self.titlelabel.setText(title)
        self.titlelabel.move(60, 10)

        self.webview = QWebEngineView(self)
        self.webview.settings().setAttribute(
            QWebEngineSettings.WebAttribute.PlaybackRequiresUserGesture, False
        )
        self.page = WebEnginePage(master)
        self.webview.setPage(self.page)
        self.webview.setHtml(html_str, QUrl("about:blank"))
        self.webview.setGeometry(0, 40, self.width(), self.height() - 40)

        self.close_btn = QPushButton(self)
        self.close_btn.setStyleSheet(close_btn_style)
        self.close_btn.setText("X")
        self.close_btn.clicked.connect(self.hide)
        self.close_btn.setGeometry(self.width() - 30, 10, 20, 20)

        self.position: dict[str, int] = {"x": 0, "y": 0}

        self.setMouseTracking(True)

        self.startX: int = 0
        self.startY: int = 0

        self._blurDirty = True
        self._blurredBg: QImage | None = None

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.startX = int(event.position().x())
        self.startY = int(event.position().y())
        self.raise_()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() & Qt.MouseButton.LeftButton:
            x = self.x() + int(event.position().x()) - self.startX
            y = self.y() + int(event.position().y()) - self.startY
            self.position["x"] = x
            self.position["y"] = y
            self.move(x, y)
            self._blurDirty = True
        super().mouseMoveEvent(event)

    def paintEvent(self, event: QPaintEvent):
        painter: QPainter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        clipPath: QPainterPath = QPainterPath()
        clipPath.addRoundedRect(self.rect(), 10, 10)
        painter.setClipPath(clipPath)

        if self.parentWidget():

            if self._blurDirty or self._blurredBg is None:

                self.hide()

                background: QPixmap = self.parentWidget().grab(self.geometry())

                self.show()

                blur: QGraphicsBlurEffect = QGraphicsBlurEffect(self)
                blur.setBlurRadius(15)
                blur.setBlurHints(QGraphicsBlurEffect.BlurHint.PerformanceHint)

                scene: QGraphicsScene = QGraphicsScene()
                item: QGraphicsPixmapItem = QGraphicsPixmapItem()
                item.setPixmap(background)
                item.setGraphicsEffect(blur)
                scene.addItem(item)

                self._blurredBg = QImage(self.size(), QImage.Format.Format_ARGB32_Premultiplied)
                self._blurredBg.fill(Qt.GlobalColor.transparent)

                imagePainter: QPainter = QPainter(self._blurredBg)

                scene.render(imagePainter, QRectF(), QRectF(0, 0, self.width(), self.height()))

                imagePainter.end()

                self._blurDirty = False

            painter.drawImage(0, 0, self._blurredBg)

        painter.setBrush(QColor(0, 0, 0, 140))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(self.rect())

        super().paintEvent(event)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(960, 480)
    WebWindow(window, size=(960, 480)).move(0, 0)
    window.show()
    sys.exit(app.exec())
