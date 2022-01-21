'''
堆栈窗口控件（QStackedWidget）
'''

import sys

from PyQt5.QtWidgets import *


class StackedExample(QWidget):
    def __init__(self):
        super(StackedExample, self).__init__()
        # 从屏幕上（800，500）位置开始（即为最左上角的点坐标），
        # 显示一个1*1的界面（宽1，高1）
        self.setGeometry(800, 500, 1, 1)
        self.setWindowTitle('堆栈窗口')

        # 创建一个列控件
        self.list = QListWidget()
        self.list.insertItem(0,'联系方式')
        self.list.insertItem(1,'个人信息')
        self.list.insertItem(2,'教育程度')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        # 创建堆栈窗口控件
        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)

        self.list.currentRowChanged.connect(self.display)


    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())

        self.stack1.setLayout(layout)

    def tab2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow(QLabel('性别'),sex)
        layout.addRow('生日',QLineEdit())

        self.stack2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        self.stack3.setLayout(layout)
    # index自动传入，为当前堆栈控件页面索引
    def display(self,index):
        print(index)
        self.stack.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = StackedExample()
    demo.show()
    sys.exit(app.exec_())