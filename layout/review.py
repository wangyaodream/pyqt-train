import sys

from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QGridLayout,
    QApplication
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("review")

        self._display()

    def _display(self):
        title = QLabel("Title")
        author = QLabel('Author')
        review = QLabel('Review')


        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

