#pip install pyqt6 pyqt6-tools

from PyQt6 import QtWidgets, uic
import sys
from controller import MainController


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./views/main_window.ui",self)
        self.controller = MainController(self,self)

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())