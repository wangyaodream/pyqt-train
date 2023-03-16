import sys


from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()

class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self._display()

    def _display(self):
        
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle("Emit signal")

    def mousePressEvent(self, e) -> None:
        self.c.closeApp.emit()



def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

        
