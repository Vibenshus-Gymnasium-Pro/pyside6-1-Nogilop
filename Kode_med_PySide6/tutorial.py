import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tutorial App")

        button = QPushButton("Press me bruh")

        self.setCentralWidget(button)

balls=QApplication(sys.argv)

window=MainWindow()
window.show()

balls.exec()