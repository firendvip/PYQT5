'''
Override（覆盖）槽函数
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class OverrideSlot(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Override（覆盖）槽函数")

    # 系统定义好的，这里进行重写（覆盖），e ：键盘事件   e.key():键盘按键值
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            print(e.key())
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle("按下Alt键")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = OverrideSlot()
    form.show()
    sys.exit(app.exec_())
