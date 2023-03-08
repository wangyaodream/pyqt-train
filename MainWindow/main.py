import sys

from PyQt6.QtWidgets import QMainWindow, QMenu, QApplication
from PyQt6.QtGui import QAction


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # 相当于初始化statusBar,在不初始化的情况下不知道为啥下面的QAction就不会改变bar的内容·
        self.statusBar().showMessage("Ready")
        self._display()

    def _display(self):
        menubar = self.menuBar()
        # for macos
        menubar.setNativeMenuBar(False)

        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        impAct.setStatusTip("Import mail")
        impMenu.addAction(impAct)

        newAct = QAction('New', self)
        newAct.setStatusTip("Create a new file")

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Submenu')


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

