import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QFileDialog,
    QTextEdit
)
from PyQt6.QtGui import QIcon, QAction
from pathlib import Path


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 450, 350) 
        self.setWindowTitle('Input dialog')
        self._display()

    def _display(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('../imgs/balloon-ellipsis.png'), 'Open', self)
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

    def showDialog(self):
        # 会弹出一个对话框
        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

