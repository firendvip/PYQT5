'''
为树节点添加响应事件
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class TreeEvent(QMainWindow):
    def __init__(self, parent=None):
        super(TreeEvent, self).__init__(parent)
        self.setWindowTitle('为树节点添加响应事件')
        self.resize(750, 850)

        # 创建树控件框架及加入节点和数据
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])
        # QTreeWidgetItem() 
        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        self.tree.clicked.connect(self.onTreeClicked)

        # 添加到中心控件
        self.setCentralWidget(self.tree)

    def onTreeClicked(self):
        # 获得当前的单击项  current：当前
        item = self.tree.currentItem()
        # item.text(0)： item第0列的值
        print('key=%s,value=%s' % (item.text(0), item.text(1)))



    # # index 自动传入？当前行的索引号？
    # def onTreeClicked(self,index):
    #     # 获得当前的单击项  current：当前
    #     item = self.tree.currentItem()
    #     print(index.row())
    #     # item.text(0)： item第0列的值
    #     print('key=%s,value=%s' % (item.text(0), item.text(1)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = TreeEvent()
    tree.show()
    sys.exit(app.exec_())
