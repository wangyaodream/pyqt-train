import sys
from functools import partial

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,300,350,250)
        self.setWindowTitle("CheckMenu")
        self._display()

    def _display(self):
        self.statu = self.statusBar()
        self.statu.showMessage('Ready')

        menubar = self.menuBar()
        if sys.platform == "darwin":
            menubar.setNativeMenuBar(False)

        viewMenu = menubar.addMenu('View')


        # 创建一个支持勾选的菜单
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(partial(self._toggleMenu))

        viewMenu.addAction(viewStatAct)

    def _toggleMenu(self, foo, eoo):
        print(foo)
        print(eoo)
        if foo:
            self.statu.show()
        else:
            self.statu.hide()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()




