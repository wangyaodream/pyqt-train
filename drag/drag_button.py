import sys

from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QApplication
)
from PyQt6.QtCore import QMimeData, Qt
from PyQt6.QtGui import QDrag


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e) -> None:
        if e.buttons() != Qt.MouseButton.LeftButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)

        drag.setHotSpot(e.position().toPoint() - self.rect().topLeft())

        dropAction = drag.exec(Qt.DropAction.MoveAction)

    def mousePressEvent(self, e) -> None:
        super().mousePressEvent(e)
        if e.button() == Qt.MouseButton.RightButton:
            print('press')


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Simple drag and drop")

        self._display()
    
    def _display(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.position()
        self.button.move(position.toPoint())

        e.setDropAction(Qt.DropAction.MoveAction)
        e.accept()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


