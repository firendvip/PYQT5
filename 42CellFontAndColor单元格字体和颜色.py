'''
设置单元格字体和颜色
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtGui import QBrush, QColor, QFont


class CellFontAndColor(QWidget):
    def __init__(self):
        super(CellFontAndColor,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("设置单元格字体和颜色")
        self.resize(750, 550);

        # 创建扩展性表格 和 设置信息
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        # 设置单元格内容和样式
        newItem1 = QTableWidgetItem('雷神')
        # newItem1.setFont(QFont('文本信息', 字号, QFont.字体颜色))
        newItem1.setFont(QFont('Times',14,QFont.Black))
        newItem1.setForeground(QBrush(QColor(255,0,0)))
        tableWidget.setItem(0,0,newItem1)

        newItem2 = QTableWidgetItem('女')
        newItem2.setForeground(QBrush(QColor(255,255,0)))
        newItem2.setBackground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0,1,newItem2)

        newItem3 = QTableWidgetItem('160')
        newItem3.setFont(QFont('Times',20,QFont.Black))
        newItem3.setForeground(QBrush(QColor(0,0,255)))
        tableWidget.setItem(0,2,newItem3)

        layout = QHBoxLayout()
        layout.addWidget(tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellFontAndColor()
    example.show()
    sys.exit(app.exec_())