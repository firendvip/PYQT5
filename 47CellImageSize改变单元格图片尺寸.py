'''
改变单元格中图片的最大尺寸  （老师写成图片了）
setIconSize(QSize(width,height))
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class CellImageSize(QWidget):
    def __init__(self):
        super(CellImageSize,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("改变单元格中图片的尺寸")
        self.resize(1200, 1400);
        layout = QHBoxLayout()

        tablewidget = QTableWidget()
        # 设置加载的图片最大值
        tablewidget.setIconSize(QSize(300,200))
        tablewidget.setColumnCount(3)
        tablewidget.setRowCount(5)

        tablewidget.setHorizontalHeaderLabels(['图片1', '图片2', '图片3'])

        # 让列的宽度和图片的宽度相同 (设置单元格大小)
        for i in range(3):
            tablewidget.setColumnWidth(i,300)

        # 让行的高度和图片的高度相同  (设置单元格大小)
        for i in range(5):
            tablewidget.setRowHeight(i,200)

        # 有点看不懂？ 更愿意用两个for
        # for k in range(15):
        #     i = k / 3   # 行
        #     j = k % 3   # 列
        #     print(i,j)
        #     print()

        for i in range(5):
            for j in range(3):
                print(i,j)

                # 实例化item（cell单元格）
                item = QTableWidgetItem()
                # 往item里加载图片
                item.setIcon(QIcon('./03.png'))
                # 往表格里加载图片
                tablewidget.setItem(i,j,item)


        layout.addWidget(tablewidget)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellImageSize()
    example.show()
    sys.exit(app.exec_())