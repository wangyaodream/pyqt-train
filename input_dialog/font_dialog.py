import sys

from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QSizePolicy,
    QLabel,
    QFontDialog,
    QApplication
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle("font dialog")
        self._display()

    def _display(self):
        
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lab = QLabel("Knowledge only matters", self)
        self.lab.move(130, 20)

        vbox.addWidget(self.lab)
        self.setLayout(vbox)


    def showDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.lab.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

