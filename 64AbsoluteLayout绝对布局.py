'''
绝对布局
'''


import sys,math
from PyQt5.QtWidgets import *


class AbsoluteLayout(QWidget) :
    def __init__(self):
        super(AbsoluteLayout,self).__init__()
        self.setWindowTitle("绝对布局")
        # 直接通过坐标控制控件位置的布局形式 叫 绝对布局 。
        # 坐标是相对于窗体的坐标。菜单栏或工具栏下的窗体框架的左上为（0，0）
        self.label1 = QLabel('欢迎',self)
        self.label1.move(200,200)

        self.label2 = QLabel('学习',self)
        self.label2.move(350,400)

        self.label3 = QLabel('PyQt5',self)
        self.label3.move(550,800)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AbsoluteLayout()
    main.show()
    sys.exit(app.exec_())