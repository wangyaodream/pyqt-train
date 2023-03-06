import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QPushButton, QHBoxLayout


def show():
    if display.text():
        display.setText("")
    else:
        display.setText("Hello world!")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Test")
generalLaytou = QVBoxLayout()
display = QLineEdit()
# 让editLine的cursor 从右边开始
display.setAlignment(Qt.AlignmentFlag.AlignRight)
display.setText("Hello world")
display.setReadOnly(True)
generalLaytou.addWidget(display)

buttonLayout = QHBoxLayout()
btn = QPushButton("click!")
btn.clicked.connect(show)

buttonLayout.addWidget(btn)

generalLaytou.addLayout(buttonLayout)
window.setLayout(generalLaytou)


window.show()
sys.exit(app.exec())


