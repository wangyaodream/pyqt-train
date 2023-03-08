import sys


from PyQt6.QtWidgets import (
    QWidget, QPushButton, QApplication
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self._initUI()

    def _initUI(self):
        self.setWindowTitle("QuitButton")
        btn = QPushButton("Quit", parent=self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.move(80, 175)

        self.setGeometry(300, 300, 350, 250)



def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

    
