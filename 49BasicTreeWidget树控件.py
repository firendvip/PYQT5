'''
树控件（QTreeWidget）的基本用法
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt


class BasicTreeWidget(QMainWindow):
    def __init__(self, parent=None):
        super(BasicTreeWidget, self).__init__(parent)
        self.setWindowTitle('树控件（QTreeWidget）的基本用法')
        self.resize(750, 850)
        # 创建树控件框架
        self.tree = QTreeWidget()
        # 为树控件指定列数
        self.tree.setColumnCount(2)

        # 设置列标签文案
        self.tree.setHeaderLabels(['Key','Value'])
        # 实例化根节点,参数为 属于哪一个树
        root = QTreeWidgetItem(self.tree)
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('./01.png'))
        # 设置列的宽度
        self.tree.setColumnWidth(0,500)

        # root: 参数为 实例化对象的 上级节点
        child1 = QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1,'子节点1的数据')
        child1.setIcon(0,QIcon('./03.png'))
        # 设置为可选状态
        child1.setCheckState(0,Qt.Checked)

        # 同上
        child2 = QTreeWidgetItem(root)
        child2.setText(0,'子节点2')
        child2.setIcon(0,QIcon('./03.png'))

        # 为child2添加一个子节点
        child3 = QTreeWidgetItem(child2)
        child3.setText(0,'子节点3')
        child3.setText(1,'新的值')
        child3.setIcon(0,QIcon('./01.png'))

        # 让所有节点默认为展开状态
        self.tree.expandAll()
        # 设置为中心控件
        self.setCentralWidget(self.tree)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = BasicTreeWidget()
    tree.show()
    sys.exit(app.exec_())