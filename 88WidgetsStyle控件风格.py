'''
窗口、绘图与特效：设置窗口风格
设置窗口中控件的风格
QApplication.setStyle(...)
'''

import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class WindowStyle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('设置窗口风格')
        horizontalLayout = QHBoxLayout()
        self.styleLabel = QLabel('设置窗口风格：')
        #  QComboBox() 下拉列表
        self.styleComboBox = QComboBox()
        self.styleComboBox.addItems(QStyleFactory.keys())

        # 获取当前窗口的风格
        # print(QApplication.style().objectName())
        # 获取下来框选项的索引
        # index = self.styleComboBox.findText(QApplication.style().objectName(),QtCore.Qt.MatchFixedString)
        # # 设置索引
        # self.styleComboBox.setCurrentIndex(index)
        #activated[str] 传送的是选中Item的ItemName
        self.styleComboBox.activated[str].connect(self.handleStyleChanged)

        horizontalLayout.addWidget(self.styleLabel)
        horizontalLayout.addWidget(self.styleComboBox)
        self.setLayout(horizontalLayout)

    # 设置样式
    def handleStyleChanged(self,style):
        QApplication.setStyle(style)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WindowStyle()
    form.show()
    sys.exit(app.exec_())