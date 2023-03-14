import sys
from PyQt6.QtCore import QMessageAuthenticationCode

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon, QAction


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self._display()

    def _display(self):
        self._bar = self.statusBar()
        self._bar.showMessage("Ready")

        exitAct = QAction(QIcon('../imgs/acorn.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(QApplication.instance().quit)


        showAct = QAction(QIcon("../imgs/balloon-ellipsis.png"), "Show", self)
        showAct.triggered.connect(self.show_msg)
        

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.toolbar.addAction(showAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Tool bar")

    def show_msg(self, stat):
        print(stat)
        if stat:
            self._bar.show()
        else:
            self._bar.hide()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()



        

