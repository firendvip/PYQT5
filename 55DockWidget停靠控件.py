'''
停靠控件（QDockWidget）
'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DockDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DockDemo, self).__init__(parent)
        self.resize(750, 850)
        self.setWindowTitle("停靠控件（QDockWidget）")

        layout = QHBoxLayout()
        # 创建悬停控件
        self.items = QDockWidget('Dockable',self)
        # 创建列表控件
        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')
        # 列表放到悬停控件里
        self.items.setWidget(self.listWidget)
        # 设置单行输入框为中心控件
        self.setCentralWidget(QLineEdit())
        # 默认悬浮状态  如为真，默认悬靠位置则不起作用
        # self.items.setFloating(True)
        # Qt.RightDockWidgetArea ： 停靠区域为右侧
        self.addDockWidget(Qt.LeftDockWidgetArea,self.items)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockDemo()
    demo.show()
    sys.exit(app.exec_())