import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self._display

    def _display(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Event handler")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
