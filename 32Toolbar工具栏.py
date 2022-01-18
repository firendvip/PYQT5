'''
创建和使用工具栏
工具栏默认按钮：只显示图标，将文本作为悬停提示展示
工具栏按钮有3中显示状态
1.  只显示图标
2.  只显示文本
3.  同时显示文本和图标
'''
#

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Toolbar(QMainWindow) :
    def __init__(self):
        super(Toolbar,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("工具栏例子")
        self.resize(300,200)
        # 实例化工具栏
        tb1 = self.addToolBar("图片按钮")
        # 创建并添加new
        new = QAction(QIcon('./01.png'),"new",self)
        tb1.addAction(new)
        # 同上
        open = QAction(QIcon('./01.png'),"open",self)
        tb1.addAction(open)
        # 同上
        save = QAction(QIcon('./01.png'),"save",self)
        tb1.addAction(save)
        # 显示工具栏风格为文本显示在图标下方
        tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


        # 创建工具栏tb2
        tb2 = self.addToolBar("新建按钮")
        # 同上
        new1 = QAction(QIcon('.01.png'),"新建",self)
        tb2.addAction(new1)
        # 1 : ToolButtonTextOnly
        # tb2.setToolButtonStyle(1)
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb1.actionTriggered.connect(self.toolbtnpressed)
        tb2.actionTriggered.connect(self.toolbtnpressed)

    # a:actionTriggered 动作被触发后 传入,指代被点击的菜单
    # a 自动传入
    def toolbtnpressed(self,a):
        print(a)
        print(type(a))
        print("按下的工具栏按钮是",a.text())

    # 下面这样写不行:
    # def toolbtnpressed(self):
    #     sender = self.sender()
    #     print("按下的工具栏按钮是",sender.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Toolbar()
    main.show()
    sys.exit(app.exec_())