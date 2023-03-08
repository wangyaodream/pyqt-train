import sys

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QAction


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self._display()

    def _display(self):
        # activate statusbar
        statusbar =  
