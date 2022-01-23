'''
信号（Signal）与槽（Slot）
'''
from PyQt5.QtWidgets import *
import sys

class SigalSlotDemo(QWidget):
    def __init__(self):
        super().__init__()
        # 对initUI函数进行修改和添加功能
        self.initUI()

    # 创建窗体 和 按钮
    def initUI(self):
        self.setGeometry(300, 300, 500, 800)
        self.setWindowTitle('信号（Signal）与槽（Slot）')
        self.btn = QPushButton('我的按钮',self)

        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        self.btn.setText("22222")
        # setStyleSheet的用法： 设置样式的
        # https: // blog.csdn.net / qq_42250189 / article / details / 105199339
        self.btn.setStyleSheet("QPushButton(max-width:200px;min-width:200px")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SigalSlotDemo()
    gui.show()
    sys.exit(app.exec_())