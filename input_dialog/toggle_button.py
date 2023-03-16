import sys


from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QFrame,
    QApplication
)
from PyQt6.QtGui import QColor


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setGeometry(300, 300, 450, 250)
        self.setWindowTitle("QCheckBox")

        self._display()

    def _display(self):

        self.col = QColor(0,0,0)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        green





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

    
