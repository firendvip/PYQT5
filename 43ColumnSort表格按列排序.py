'''
按列排序
1. 按哪一列排序
2. 排序类型：升序或降序
sortItems(columnIndex，orderType）
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class ColumnSort(QWidget):
    def __init__(self):
        super(ColumnSort,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("按列排序")
        self.resize(750,850);
        layout = QVBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(3)
        layout.addWidget(self.tableWidget)

        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        newItem = QTableWidgetItem('张三')
        self.tableWidget.setItem(0,0,newItem)

        newItem=QTableWidgetItem('男')
        self.tableWidget.setItem(0,1,newItem)

        newItem=QTableWidgetItem('165')
        self.tableWidget.setItem(0,2,newItem)

        newItem = QTableWidgetItem('李四')
        self.tableWidget.setItem(1, 0, newItem)

        newItem = QTableWidgetItem('女')
        self.tableWidget.setItem(1, 1, newItem)

        newItem = QTableWidgetItem('160')
        self.tableWidget.setItem(1, 2, newItem)

        newItem = QTableWidgetItem('王五')
        self.tableWidget.setItem(2, 0, newItem)

        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(2, 1, newItem)

        newItem = QTableWidgetItem('170')
        self.tableWidget.setItem(2, 2, newItem)


        self.button = QPushButton('排序')
        self.button.clicked.connect(self.order)

        #  设置排序初始的初始值
        self.orderType = Qt.DescendingOrder

        layout.addWidget(self.button)
        self.setLayout(layout)


    def order(self):
        if self.orderType == Qt.DescendingOrder: # 判断是否降序
            self.orderType = Qt.AscendingOrder  # 是则改为升序
        else:
            self.orderType = Qt.DescendingOrder  # 否则 改为降序
            # 2：第2列作为排序列  self.orderType：排序的类型
        self.tableWidget.sortItems(2,self.orderType)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ColumnSort()
    example.show()
    sys.exit(app.exec_())