import sys

from PyQt6.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.resize(250, 200)
    # .move方法将部件移动到屏幕的制定坐标
    window.move(600, 200)

    window.setWindowTitle("Simple")
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

