import sys


from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        self._display()

    def _display(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle("Event sender")

    def buttonClicked(self):
        # 
        sender = self.sender()

        msg = f'{sender.text()} was pressed'
        self.statusBar().showMessage(msg)


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

        
