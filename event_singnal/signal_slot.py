import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLCDNumber,
    QSlider,
    QVBoxLayout,
    QApplication
) 



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self._display()

    def _display(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Orientation.Horizontal, self)


        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Signal and slot")



def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

