import sys


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGridLayout,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QWidget
)


WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35


class PyCalcWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        # create display area
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        # display area is a line editor
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment()



def main():
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    sys.exit(pycalcApp.exec())


if __name__ == "__main__":
    main()




