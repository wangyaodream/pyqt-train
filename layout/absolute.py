import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self._display()

    def _display(self):

        label1 = QLabel('ZetCode', self)
        label1.move(15, 10)

        label2 = QLabel('tutorials', self)
        label2.move(35, 40)

        label2 = QLabel('for programmers', self)
        label2.move(55, 70)

        self.setGeometry(300, 300, 350, 720)
        self.setWindowTitle('Absolute layout')


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    # sys.exit(app.exec())
    app.exec()


if __name__ == "__main__":
    main()




