import sys

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, Qpen
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Pen styles')

