import sys

from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QLineEdit,
    QInputDialog
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 450, 350) 
        self.setWindowTitle('Input dialog')
        self._display()

    def _display(self):
        self.btn = QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

    def showDialog(self):
        # 会弹出一个对话框
        text, ok = QInputDialog.getText(self, 'Input Dialog',
                                        'Enter your name:')
        if ok:
            self.le.setText(str(text))

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

