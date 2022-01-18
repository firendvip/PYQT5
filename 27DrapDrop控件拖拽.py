'''
让控件支持拖拽动作
A.setDragEnabled(True)
B.setAcceptDrops(True)
B需要两个事件
1. dragEnterEvent   将A拖到B触发
2. dropEvent        在B的区域放下A时触发
'''

import sys
from PyQt5.QtWidgets import *


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        self.setWindowTitle('拖拽案例')

        lable1 = QLabel("请将左边的文本拖拽到右边的下拉列表中")
        combo = MyComboBox()
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)  # 让QLineEdit控件可拖动

        formLayout = QFormLayout()
        formLayout.addRow(lable1)
        formLayout.addRow(lineEdit, combo)  # 表单布局支持放入两个控件
        self.setLayout(formLayout)

class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)  # 可接受拖进来的控件


    def dragEnterEvent(self, event):
        print(type(event))
        # event: 被拖拽的事件
        # event.mimeData().hasText() 判断触发事件中是否含有文本
        # 如果有，则event.accept()接收；如果没有，则event.ignore()不接收 (不写else那段也可以)
        if event.mimeData().hasText():
            event.accept() # 接收
        else:
            event.ignore() # 不接收

    # 鼠标松开，释放控件时dropEvent事件自动触发
    # 将事件中的文本内容添加到下拉列表中
    def dropEvent(self, event):
        self.addItem(event.mimeData().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrapDropDemo()
    main.show()
    sys.exit(app.exec_())
