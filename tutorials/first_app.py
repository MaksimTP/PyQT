from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import Qt ,QSize
# import sys

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(self.btn_was_clckd)

        self.setCentralWidget(button)

    def btn_was_clckd(self):
        print("Clicked!")


window = MainWindow()
window.show()

app.exec()
