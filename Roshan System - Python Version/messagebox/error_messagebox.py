from collections.abc import Callable

from base_messagebox import MessageBoxYesNo, MessageBoxYesNoCancel


class ErrorMessageBoxYesNo(MessageBoxYesNo):
    def __init__(
        self,
        master,
        title: str = "Messagebox Yes No",
        message: str = "A yes or no messagebox",
        callbackFunction: Callable[[bool], None] = print,
    ):
        super().__init__(master, title, message, "textures/error.png", callbackFunction)


class ErrorMessageBoxYesNoCancel(MessageBoxYesNoCancel):
    def __init__(
        self,
        master,
        title: str = "Messagebox Yes No Cancel",
        message: str = "A yes or no or cancel \nmessagebox",
        callbackFunction: Callable[[bool], None] = print,
    ):
        super().__init__(master, title, message, "textures/error.png", callbackFunction)
