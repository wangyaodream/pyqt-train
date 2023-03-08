import sys
from functools import partial

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self._display()

    def _display(self):
        change_text = sys.argv[-1] 
        
        self.statusBar().showMessage("Ready")

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Statusbar")
        btn = QPushButton('click me', self)
        btn.move(50, 50)
        btn.clicked.connect(partial(self._change_status, change_text))

    def _change_status(self, text):
        print("text: ", text)
        if text:
            self.statusBar().showMessage(text)
        else:
            self.statusBar().showMessage("Shit!!!")


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


