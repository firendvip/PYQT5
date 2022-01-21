'''
容纳多文档的窗口
QMdiArea
QMdiSubWindow  子窗口
'''

import sys
from PyQt5.QtWidgets import *


class MultiWindows(QMainWindow):
    # 用到函数里的，计数用
    count = 0

    def __init__(self, parent=None):
        super(MultiWindows, self).__init__(parent)
        self.resize(750, 850)
        self.setWindowTitle("容纳多文档的窗口")
        # 创建容纳多文档窗口 并 设置为中心控件
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # 创建菜单和给菜单加入动作
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        # 菜单链接到槽
        file.triggered.connect(self.windowaction1)

    # q自动传入，当前的菜单项
    def windowaction1(self, q):
        # print(q.text())

        if q.text() == "New":
            # 统计当前窗口数
            MultiWindows.count = MultiWindows.count + 1
            print(MultiWindows.count,type(MultiWindows.count))
            # 创建子窗口
            sub = QMdiSubWindow()
            # 在子窗口里添加多行输入框
            sub.setWidget(QTextEdit())
            # 设置子窗口标题
            sub.setWindowTitle("子窗口" + str(MultiWindows.count))
            # 子窗口添加到多窗口控件
            self.mdi.addSubWindow(sub)
            sub.show()
        elif q.text() == "cascade":
            # cascade /kaˈskād / 小瀑布,级联
            self.mdi.cascadeSubWindows()
        elif q.text() == "Tiled":
            # tile /tīl/ 瓦,砖瓦
            self.mdi.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MultiWindows()
    demo.show()
    sys.exit(app.exec_())
