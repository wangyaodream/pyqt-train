import sys

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import (
    QColorDialog,
    QWidget,
    QApplication,
    QPushButton,
    QFrame,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 450, 350) 
        self.setWindowTitle('Input dialog')
        self._display()

    def _display(self):

        col = QColor(0, 0, 0)

        self.btn = QPushButton("Dialog", self)
        self.btn.clicked.connect(self.showDialog)
        self.btn.move(20, 20)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s}" % col.name())

        self.frm.setGeometry(130, 22, 200, 200)

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            # setStyleSheet中的字符串大小写敏感，需要准确设定
            self.frm.setStyleSheet("QWidget { background-color: %s}" % col.name())


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

