import sys

from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QLabel,
    QApplication
)
from PyQt6.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self._display()

    def _display(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("back.gif")
        

        lab = QLabel(self)
        lab.setPixmap(pixmap)

        hbox.addWidget(lab)
        self.setLayout(hbox)

        self.move(900, 200)
        self.setWindowTitle("Sid")


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

