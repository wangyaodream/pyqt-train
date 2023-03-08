import sys

from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self._initUI()

    def _initUI(self):
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Message box')

    def closeEvent(self, event):

        reply = QMessageBox.question(self, "Message",
                                     "Are you sure to quit?",
                                     QMessageBox.StandardButton.No | QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Open, QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()




