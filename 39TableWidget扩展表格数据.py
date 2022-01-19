'''
扩展的表格控件（QTableWidget） 继承 QTableView ,在其基础上添加了更多的方法
每一个Cell（单元格）是一个QTableWidgetItem
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView)


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget演示")
        self.resize(430, 230);
        # 创建水平布局
        layout = QHBoxLayout()
        # 创建扩展型的表格
        tablewidget = QTableWidget()
        # 设置行列
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)
        # 控件放入布局
        layout.addWidget(tablewidget)

        # 设置水平的列表头字段
        tablewidget.setHorizontalHeaderLabels(['姓名','年龄','籍贯'])
        # 每一个Cell（单元格）都是一个QTableWidgetItem对象
        nameItem = QTableWidgetItem("小明")
        # 放在在第0行第0列
        tablewidget.setItem(0,0,nameItem)

        ageItem = QTableWidgetItem("24")
        tablewidget.setItem(0,1,ageItem)

        jgItem = QTableWidgetItem("北京")
        tablewidget.setItem(0,2,jgItem)

        # 禁止编辑
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 调整列和行的宽高，  默认输入值大小的期望快高。
        tablewidget.resizeColumnsToContents()
        tablewidget.resizeRowsToContents()

        # tablewidget.horizontalHeader().setVisible(False)
        # tablewidget.verticalHeader().setVisible(False)
        # 设置垂直头的文案
        tablewidget.setVerticalHeaderLabels(["a","b"])

        # 隐藏表格线
        tablewidget.setShowGrid(False)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = TableWidgetDemo()
    example.show()
    sys.exit(app.exec_())