import sys

from PyQt6.QtWidgets import (
    QWidget,
    QToolTip,
    QPushButton,
    QApplication
)
from PyQt6.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>Qwidget Test</b> widget')

        btn = QPushButton('Click', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

""" 最终呈现的是一个鼠标指上的悬浮提示效果"""

