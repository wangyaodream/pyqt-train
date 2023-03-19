import sys
import random

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import QtGui
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 450)
        self.setWindowTitle("Test for draw")
        self._display()

    def _display(self):
        self.setMinimumSize(50, 50)

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.GlobalColor.red)
        size = self.size()

        for _ in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

        
