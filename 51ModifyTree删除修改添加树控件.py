'''
添加、修改和删除树控件中的节点
'''

import sys
from PyQt5.QtWidgets import *


class ModifyTree(QWidget):
    def __init__(self, parent=None):
        super(ModifyTree, self).__init__(parent)
        self.setWindowTitle('TreeWidget 例子')
        self.resize(750, 850)
        operatorLayout = QHBoxLayout()

        addBtn = QPushButton('添加节点')
        updateBtn = QPushButton('修改节点')
        deleteBtn = QPushButton('删除节点')

        operatorLayout.addWidget(addBtn)
        operatorLayout.addWidget(updateBtn)
        operatorLayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deleteNode)

        self.tree = QTreeWidget()

        self.tree.setColumnCount(2)

        self.tree.setHeaderLabels(['Key','Value'])

        root  = QTreeWidgetItem(self.tree)
        root.setText(0,'root')
        root.setText(1, '0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0,'child1')
        child1.setText(1,'1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0,'child2')
        child2.setText(1,'2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0,'child3')
        child3.setText(1,'3')

        self.tree.clicked.connect(self.onTreeClicked)

        # 创建垂直布局
        mainLayout = QVBoxLayout(self)
        # 水平布局放到垂直布局   按钮在水平布局  3个按钮与树控件形成 垂直布局
        mainLayout.addLayout(operatorLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)

    # 同前面一样
    def onTreeClicked(self,index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s' % (item.text(0),item.text(1)))

    # 添加节点
    def addNode(self):
        print('添加节点')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0,'新节点')
        node.setText(1,'新值')

    def updateNode(self):
        print('修改节点')
        item = self.tree.currentItem()
        # '修改节点'通常为变量，变量里装载 用户输入的值
        item.setText(0,'修改节点')
        item.setText(1, '值已经被修改')



    def deleteNode(self):
        print('删除节点')
        item = self.tree.currentItem()
        # #获得根节点root的不可见的父节点
        root = self.tree.invisibleRootItem()
        # tree.selectedItems()：当前选中的节点
        # for 没有必要写
        # for item in self.tree.selectedItems():
        (item.parent() or root).removeChild(item)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = ModifyTree()
    tree.show()
    sys.exit(app.exec_())