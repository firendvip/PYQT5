'''
多窗口交互（1）：不使用信号与槽
Win1
Win2
强耦合：win1控件直接访问win2并从win2提取数据到win1

一般尽量降低耦合度
比如：win2是数据库，win1上有个按钮能获取到win2里的某个字段数据。
'''

#  需要先创建 DateDialog的py文件 的类

import sys

from PyQt5.QtWidgets import *

from DateDialog import DateDialog


class MultiWindow1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("多窗口交互（1）：不使用信号与槽")

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Click)

        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)

        self.setLayout(gridLayout)

    def onButton1Click(self):
        dialog = DateDialog(self)
        result = dialog.exec()
        date = dialog.dateTime()
        if result == QDialog.Accepted:
            self.lineEdit.setText(date.date().toString())
            print('点击确定按钮')
        else:
            print('单击取消按钮')

        # ？
        dialog.destroy()

    def onButton2Click(self):
        # getDateTime 是我们自己定义的静态方法
        date,time,result = DateDialog.getDateTime()

        if result == QDialog.Accepted:
            self.lineEdit.setText(date.toString())
            print('点击确定按钮')
        else:
            print('单击取消按钮')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MultiWindow1()
    form.show()
    sys.exit(app.exec_())