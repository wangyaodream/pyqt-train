import sys


from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QFrame,
    QLabel,
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
        self.label = QLabel("malilalihong!", self)
        self.label.setLineWidth(100)
        self.label.move(300, 10) 


        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s}"
                                   % self.col.name())
    
    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        # change frame style
        self.square.setStyleSheet("QFrame { background-color: %s }"
                                   % self.col.name())
        self.label.setText(str(self.col.name()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

    
