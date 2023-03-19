import sys

from PyQt6.QtWidgets import (
    QWidget,
    QComboBox,
    QLabel,
    QApplication
)


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle("QComboBox")
        self._display()

    def _display(self):
        self.lab = QLabel('Ubuntu', self)

        combo = QComboBox(self)

        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("asfkljalfjlakdjflakjGentoo")

        combo.move(50, 50)
        self.lab.move(50, 150)

        combo.textActivated.connect(self.onActivated)

    def onActivated(self, index):
        self.lab.setText(index)
        self.lab.adjustSize()

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

