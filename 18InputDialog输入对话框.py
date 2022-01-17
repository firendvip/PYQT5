'''
输入对话框：QInputDialog
QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt
'''

import sys
from PyQt5.QtWidgets import *


class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('输入对话框')

        # 创建3按钮
        self.button1 = QPushButton('获取列表中的选项')
        self.button2 = QPushButton('获取字符串')
        self.button3 = QPushButton('获取整数')

        # 创建3标签
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()

        layout = QFormLayout()
        layout.addRow(self.lineEdit1, self.button1)
        layout.addRow(self.lineEdit2, self.button2)
        layout.addRow(self.lineEdit3, self.button3)
        self.setLayout(layout)

        self.button1.clicked.connect(self.getItem)
        self.button2.clicked.connect(self.getText)
        self.button3.clicked.connect(self.getInt)

    def getItem(self):
        items = ['C', 'C++', 'Ruby', 'Python', 'Java']
        #  QInputDialog.getItem()静态方法，不用创建实例就可以直接实用
        # QInputDialog.getItem(对象,窗口标题,提示内容,元组/列表)
        # 返回：被选中的item 和 Ture/False
        item, ok = QInputDialog.getItem(self, '请选择编程语言', '语言列表', items)
        print(item)
        print(ok)
        # 当用户选中ok键的时候则在对话框里输入item
        if ok and item:
            self.lineEdit1.setText(item)


    def getText(self):
        # getText() 弹出文本输入框
        text, ok = QInputDialog.getText(self, '文本输入框', '输入姓名')
        if ok and text:
            self.lineEdit2.setText(text)

    def getInt(self):
        # getInt() 弹出计数器
        num, ok = QInputDialog.getInt(self, '整数输入框', '输入数字')
        if ok and num:
            self.lineEdit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())
