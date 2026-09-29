from collections.abc import Callable

from base_messagebox import MessageBoxYesNo, MessageBoxYesNoCancel


class WarningMessageBoxYesNo(MessageBoxYesNo):
    def __init__(
        self,
        master,
        title: str = "Messagebox Yes No",
        message: str = "A yes or no messagebox",
        callbackFunction: Callable[[bool], None] = print,
    ):
        super().__init__(
            master, title, message, "textures/warning.png", callbackFunction
        )


class WarningMessageBoxYesNoCancel(MessageBoxYesNoCancel):
    def __init__(
        self,
        master,
        title: str = "Messagebox Yes No Cancel",
        message: str = "A yes or no or cancel \nmessagebox",
        callbackFunction: Callable[[bool], None] = print,
    ):
        super().__init__(master, title, message, "textures/warning.png", callbackFunction)
