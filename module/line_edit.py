import sys
import random
from functools import partial

from PyQt6.QtWidgets import (
    QWidget,
    QLineEdit,
    QLabel,
    QApplication
)


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Line edit")
        self._display()

    def _display(self):
        self.lab = QLabel(self)
        qle = QLineEdit(self)

        self.lab.move(60, 40)
        qle.move(60, 100)
        
        # 目前没有发现有任何区别，可能是作为默认值，猜测会自动传递一个参数
        # qle.textChanged[str].connect(self._onChanged)
        qle.textChanged.connect(self._onChanged)

    def _onChanged(self):
        self.lab.setText(random.choice("aeiou"))
        self.lab.adjustSize()


def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

