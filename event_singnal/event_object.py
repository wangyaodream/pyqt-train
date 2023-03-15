import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QGridLayout,
    QLabel
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self._display()

    def _display(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = f'x: {x}, y: {y}'

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignmentFlag.AlignTop)

        self.setMouseTracking(True)
        self.setLayout(grid)

        self.setGeometry(300, 300, 450, 300)
    
    def mouseMoveEvent(self, a0) -> None:
        x = int(a0.position().x())
        y = int(a0.position().y())

        text = f'x: {x}, y: {y}'
        self.label.setText(text)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

