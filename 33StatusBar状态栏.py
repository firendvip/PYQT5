'''
创建和使用状态栏
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class StatusBar(QMainWindow) :
    def __init__(self):
        super(StatusBar,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("状态栏演示")
        self.resize(300,200)

        # 创建菜单栏
        bar = self.menuBar()
        # 添加子菜单
        file = bar.addMenu("File")
        # 添加动作
        file.addAction("show")

        file.triggered.connect(self.processTrigger)

        # 在窗体中间添加多行输入框
        # self.setCentralWidget(QTextEdit())

        # 创建状态栏
        self.statusBar = QStatusBar()
        # 设置状态栏
        self.setStatusBar(self.statusBar)


    def processTrigger(self,q):
        if q.text() == "show" :
            self.statusBar.showMessage(q.text() + " 菜单被点击了",5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBar()
    main.show()
    sys.exit(app.exec_())