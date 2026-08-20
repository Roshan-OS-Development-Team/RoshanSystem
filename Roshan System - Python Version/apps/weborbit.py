import core


class WebOrbit(core.WebWindow):
    def __init__(self, master):
        super().__init__(
            master, "WebOrbit", size=(1200, 800), icon="textures/Weborbit.png"
        )
        self.webview.load("https://sorabora.github.io/weborbit")
