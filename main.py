from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QLineEdit
win_width, win_height = 800, 300
win_x, win_y = 200, 200
txt_title = "Отправка текста"
txt_send = "Отправить"
txt_line = "Поле ввода"
class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
        def initUI(self):
            self.btn_send = QPushButton(txt_send, self)
            self.line = QLineEdit(txt_line)
            self.lable_finish = QLabel()
            self.layout_line = QHBoxLayout()
            self.layout_line.addWidget(self.line, alignment = Qt.AlignLeft)
            self.layout_line.addWidget(self.btn_send, alignment = Qt.AlignLeft)
            self.layout_line.addWidget(self.lable_finish, alignment = Qt.AlignCenter)
            self.setLayout(self.layout_line)
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
        mw = MainWindow()
        app.exec_()

