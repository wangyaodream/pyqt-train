import sys

from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QLineEdit,
    QApplication
)


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e) -> None:
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, a0) -> None:
        self.setText(a0.mimeData().text())


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle("Simple drag and drop")

        self._display()
    
    def _display(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


