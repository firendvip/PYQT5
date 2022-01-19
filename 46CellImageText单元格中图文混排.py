'''
在单元格中实现图文混排的效果
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class CellImageText(QWidget):

    def __init__(self):
        super(CellImageText,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("在单元格中实现图文混排的效果")
        self.resize(900, 850)
        layout = QHBoxLayout()
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)


        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重', '显示图片'])

        newItem = QTableWidgetItem('李宁')
        self.tableWidget.setItem(0,0,newItem)

        newItem = QTableWidgetItem('男')
        self.tableWidget.setItem(0,1,newItem)
        newItem = QTableWidgetItem('160')
        self.tableWidget.setItem(0,2,newItem)

        # 通过label防止图片
        label1 = QLabel()
        label1.setPixmap(QPixmap('./02.png'))
        # label1.setText('哈哈没有图片？')
        self.tableWidget.setCellWidget(2, 2, label1)
        # 在表格中添加图片
        newItem = QTableWidgetItem(QIcon('./01.png'),'')
        self.tableWidget.setItem(0,3,newItem)

        layout.addWidget(self.tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = CellImageText()
    example.show()
    sys.exit(app.exec_())