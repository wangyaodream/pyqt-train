import sys

from PyQt6.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self._display()

    def _display(self):
        self.resize(350, 250)
        self._center()

        self.setWindowTitle('Center')
    
    def _center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        # print(cp)


        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()


