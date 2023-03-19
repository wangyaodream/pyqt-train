import sys

from PyQt6.QtWidgets import (
    QWidget,
    QHBoxLayout,
    QFrame,
    QSplitter,
    QApplication
)
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Splitter")
        self.setGeometry(300, 300, 450, 400)
        self._display()

    def _display(self):
        
        hbox = QHBoxLayout(self)
        
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.Shape.StyledPanel)

        topright = QFrame(self)
        topright.setFrameShape(QFrame.Shape.StyledPanel)
        
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.Shape.StyledPanel)

        splitter1 = QSplitter(Qt.Orientation.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Orientation.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

