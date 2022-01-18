'''
创建和使用菜单
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Menu(QMainWindow) :
    def __init__(self):
        super(Menu,self).__init__()
        # 获取菜单栏
        bar = self.menuBar()
        # 创建菜单
        file = bar.addMenu("文件")
        file.addAction("新建")
        # 创建动作
        # QAction类是来封装用户需要执行的动作
        # self:在当前窗口创建
        save = QAction("保存", self)
        # 设置快捷键
        save.setShortcut("Ctrl + S")
        # 把动作添加到菜单
        file.addAction(save)


        edit = bar.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction("退出",self)
        file.addAction(quit)
        # triggered: 菜单的触发事件连接槽
        save.triggered.connect(self.process)

    def process(self):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())