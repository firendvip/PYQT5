'''
拖动控件之间的边界（QSplitter）分裂器
'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        self.setWindowTitle('QSplitter 例子')
        self.setGeometry(300, 300, 750, 850)
        # QFrame()继承自 QWidget 的矩形框架 ， 可以实现阴影等各种样式
        topleft = QFrame()
        # QFrame.Shape枚举值
        # QFrame.NoFrame  # QFrame什么都没画
        # QFrame.Box  # QFrame围绕其内容绘制一个框
        # QFrame.Panel  # QFrame绘制一个面板，使内容显得凸起或凹陷
        # QFrame.VLine  # QFrame绘制一条无框架的垂直线（用作分隔符）
        # QFrame.StyledPanel  # 绘制一个矩形面板，其外观取决于当前的GUI样式。它可以升起或凹陷。
        # QFrame.HLine  # QFrame绘制一条没有框架的水平线（用作分隔符）
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        # 创建水平拖动控件
        splitter1 = QSplitter(Qt.Horizontal)
        # 多行输入框
        textedit = QTextEdit()
        # topleft放在 splitter1 的左边
        splitter1.addWidget(topleft)
        # textedit默认在右边
        splitter1.addWidget(textedit)
        splitter1.setSizes([200,100])

        # 创建垂直上下拖动的控件
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)


        hbox.addWidget(splitter2)
        self.setLayout(hbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Splitter()
    demo.show()
    sys.exit(app.exec_())