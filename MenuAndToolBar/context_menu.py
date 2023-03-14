import sys


from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self._display()
    
    def _display(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Context menu")

        self.context_menu = QMenu(self)
        action1 = self.context_menu.addAction("Action 1")
        action2 = self.context_menu.addAction("Action 2")
        action3 = self.context_menu.addAction("Action 3")

        # Connect the actions to methods
        action1.triggered.connect(self.action1_triggered)
        action2.triggered.connect(self.action2_triggered)
        action3.triggered.connect(self.action3_triggered)

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        return super().contextMenuEvent(event)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()



        
