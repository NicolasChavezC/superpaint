from PyQt6.QtGui import QColor

class MainController:
    def __init__(self, main_window, ui):
        self.main_window = main_window
        self.ui = ui
        self.connect_signals()

    #Declaramos los eventos
    def connect_signals(self):
        self.ui.txtColor.textChanged.connect(self.update_color)
        self.ui.slider.valueChanged.connect(self.update_brush)
    def update_brush(self,width):
        print(width)

    def update_color(self):
        color = self.ui.txtColor.toPlainText().strip()
        print(color)
        background = QColor(color)
        if background.isValid():
            self.ui.txtColor.setStyleSheet(f"background-color: {color};color:{self.color_inverse(background).name()}")
    def color_inverse(self, color):
        inverse = QColor(255-color.red(), 255-color.green(), 255-color.blue())
        return inverse