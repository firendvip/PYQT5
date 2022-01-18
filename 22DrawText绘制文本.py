'''
绘图API：绘制文本
可以绘制这些
1. 文本
2. 各种图形（直线，点，椭圆，弧，扇形，多边形等）
3. 图像

绘制过程
QPainter
painter = QPainter() 实例化
painter.begin()  # 初始化
painter.drawText(...)  # 绘制内容
painter.end()  # 结束
必须在paintEvent事件方法中绘制各种元素
比如移动窗口时候 卡的时候，就会出现多个绘制窗口
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300, 200)
        self.text = "Python从菜鸟到高手"

    # matplotlib库  pip install matplotlib  画图用这个库
    # 函数名必须是paintEvent(),  event绘制区域
    def paintEvent(self, event):
        painter = QPainter(self)
        # 初始化，开始绘图
        painter.begin(self)
        # 设置画笔颜色 RGB
        painter.setPen(QColor(0, 255, 0))
        # 设置字体和大小
        painter.setFont(QFont('SimSun', 25))
        # 填入颜色方案 painter.drawText(绘图区域，对齐方式，绘制对象)
        # event.rect()：当前窗口，Qt.AlignCenter：居中对齐
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        # 结束绘图
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawText()
    main.show()
    sys.exit(app.exec_())
