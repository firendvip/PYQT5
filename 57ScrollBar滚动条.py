'''
滚动条控件（QScrollBar）
QScrollBar的作用
1. 通过滚动条值的变化控制其他控件状态的变化
2. 通过滚动条值的变化控制控件位置的变化
'''

import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ScrollBar(QWidget):
    def __init__(self):
        super(ScrollBar, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        # 创建标签并加入水平布局
        self.label = QLabel('拖动滚动条去改变文字颜色')
        hbox.addWidget(self.label)

        # 创建滑块和设置最大值
        self.scrollbar1 = QScrollBar()
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.sliderMoved.connect(self.sliderMoved)

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.sliderMoved.connect(self.sliderMoved)

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.sliderMoved.connect(self.sliderMoved)

        self.scrollbar4 = QScrollBar()
        self.scrollbar4.setMaximum(255)
        self.scrollbar4.sliderMoved.connect(self.sliderMoved1)

        # 滚动条加入水平布局
        hbox.addWidget(self.scrollbar1)
        hbox.addWidget(self.scrollbar2)
        hbox.addWidget(self.scrollbar3)
        hbox.addWidget(self.scrollbar4)
        # 设置窗口初始坐标和大小
        self.setGeometry(600, 600, 750, 850)
        self.setLayout(hbox)

        # 获取当前标签坐标y的值
        self.y = self.label.pos().y()

    def sliderMoved(self):
        print(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value())
        # 调色板
        palette = QPalette()
        # QColor(R,G,B,透明度)
        c = QColor(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value(), 255)
        # Foreground ： 前景色，即 字体颜色
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)

    def sliderMoved1(self):
        # label.move(x,y)
        self.label.move(self.label.x(), self.y + self.scrollbar4.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ScrollBar()
    demo.show()
    sys.exit(app.exec_())
