'''
日历控件
QCalendarWidget
'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar, self).__init__()
        self.initUI()

    def initUI(self):
        # 创建窗体标题
        self.setWindowTitle("日历演示")
        # 设置窗体大小
        self.resize(600, 500)

        # 实例化日期控件
        self.cal = QCalendarWidget(self)
        # 设置日期最大最小值
        self.cal.setMinimumDate(QDate(1988, 1, 1))
        self.cal.setMaximumDate(QDate(2088, 1, 1))
        # 日期数字之间加入网格
        self.cal.setGridVisible(True)
        # 移动控件位置
        self.cal.move(20, 20)

        # 创建标签
        self.label = QLabel(self)
        # 移动标签位置
        self.label.move(50, 400)
        # 获取日历控件数据(当前所选的日期)
        date = self.cal.selectedDate()
        # label文本设置为选中的日期  #初始化的日期
        self.label.setText(date.toString("yyyy-MM-dd dddd"))

        # 链接到槽
        self.cal.clicked.connect(self.showDate)

    def showDate(self, date):
        # label文本设置为选中的日期 # 点击事件选中后的日期
        self.label.setText((self.cal.selectedDate().toString("yyyy-MM-dd dddd")))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyCalendar()
    main.show()
    sys.exit(app.exec_())
