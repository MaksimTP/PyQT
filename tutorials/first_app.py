from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import Qt ,QSize
# import sys

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.btn_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.btn_was_clckd)
        # button.clicked.connect(self.btn_was_tgld)
        self.button.setChecked(self.btn_is_checked)
        self.setCentralWidget(self.button)

    def btn_was_clckd(self):
        print("Clicked!")
        self.btn_is_checked = self.button.isChecked()

        print(self.btn_is_checked)


        # if self.btn_is_checked:
        #     print('Wow!')

    # def btn_was_tgld(self, checked):
    #     print("Checked?", checked)


window = MainWindow()
window.show()

app.exec()
