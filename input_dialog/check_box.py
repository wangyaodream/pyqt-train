import sys


from PyQt6.QtWidgets import (
    QWidget,
    QCheckBox,
    QApplication
)
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setGeometry(300, 300, 450, 250)
        self.setWindowTitle("QCheckBox")

        self._display()

    def _display(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        # cb.toggle()
        cb.stateChanged.connect(self.changetitle)


    def changetitle(self, state):
        print(state)
        if state == Qt.CheckState.Checked.value:
            self.setWindowTitle("QCheckBox")
        else:
            self.setWindowTitle('')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

    
