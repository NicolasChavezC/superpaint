from PyQt6.QtGui import QColor

class MainController:
    def __init__(self, main_window, ui):
        self.main_window = main_window
        self.ui = ui
        self.canvas = ui.widget
        self.connect_signals()

    #Declaramos los eventos
    def connect_signals(self):
        self.ui.txtColor.textChanged.connect(self.update_color)
        self.ui.slider.valueChanged.connect(self.update_brush)
        self.ui.btnEraser.clicked.connect(self.set_eraser)
    def set_eraser(self):
        self.canvas.pen_color = QColor("#2d2d2d")
    def update_brush(self,width):
        #rint(width)
        self.canvas.pen_width = width

    def update_color(self):
        color = self.ui.txtColor.toPlainText().strip()
        print(color)
        background = QColor(color)
        self.canvas.pen_color = background
        if background.isValid():
            self.ui.txtColor.setStyleSheet(f"background-color: {color};color:{self.color_inverse(background).name()}")
    def color_inverse(self, color):
        inverse = QColor(255-color.red(), 255-color.green(), 255-color.blue())
        return inverse