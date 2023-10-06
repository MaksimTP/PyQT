from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
# import sys

app = QApplication([])

# window = QWidget() 1
# window = QPushButton("Push me!")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("This is my app")
        button = QPushButton("Press Me")

        self.setCentralWidget(button)

window = MainWindow()
window.show()

app.exec()
