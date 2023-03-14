import sys

from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)


class Window(QWidget):
    def __init__(self):
        super().__init__(parent=None)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Buttons") 
        self._display()

    def _display(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        # hbox.addStretch(4)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)


        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

