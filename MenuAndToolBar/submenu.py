import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu
from PyQt6.QtGui import QAction


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("sub")

        self._display()

    def _display(self):
        menubar = self.menuBar()
        # for mac
        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu('File')
        subMenu = QMenu("Import", parent=self)
        subAct = QAction('Import mail', self)
        subMenu.addAction(subAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(subMenu)

        editMenu = menubar.addMenu('Edit')
        cutAct = QAction("Cut", self)
        editMenu.addAction(cutAct)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()



