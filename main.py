from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit, QVBoxLayout
win_width, win_height = 800, 500
win_x, win_y = 200, 200
txt_title = "Отправка текста"
txt_send = "Результат"
txt_line1 = "Поле ввода"
txt_line2 = "Поле ввода"
txt_line3 = "Поле ввода"
txt_line4 = "Поле ввода"
txt_label1 = "1 Поле ввода"
txt_label2 = "2 Поле ввода"
txt_label3 = "3 Поле ввода"
txt_label4 = "4 Поле ввода"
class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.lable_1 = QLabel(txt_label1)
        self.btn_send = QPushButton(txt_send, self)
        self.line1 = QLineEdit(txt_line1)
        self.line2 = QLineEdit(txt_line2)
        self.line3 = QLineEdit(txt_line3)
        self.line4 = QLineEdit(txt_line3)
        self.lable_finish = QLabel()
        self.layout_lineH1 = QHBoxLayout()
        self.layout_lineH2 = QHBoxLayout()
        self.layout_lineV = QVBoxLayout()
        self.layout_lineH1.addWidget(self.line1, alignment = Qt.AlignLeft)
        self.layout_lineH1.addWidget(self.line2, alignment = Qt.AlignRight)
        self.layout_lineH2.addWidget(self.line3, alignment = Qt.AlignLeft)
        self.layout_lineH2.addWidget(self.line4, alignment = Qt.AlignRight)
        self.layout_lineH1.addWidget(self.lable_finish, alignment = Qt.AlignCenter)
        self.layout_lineV.addLayout(self.layout_lineH1)
        self.layout_lineV.addLayout(self.layout_lineH2)
        self.setLayout(self.layout_lineV)
    def next_click(self):
        self.lable_finish.setText(self.line.text())
    def connects(self):
        self.btn_send.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
main()
