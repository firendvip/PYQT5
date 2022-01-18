'''
显示列表数据（QListView控件）
'''

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import sys


class ListViewDemo(QWidget):
    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView 例子")
        self.resize(300, 270)
        layout = QVBoxLayout()
        # 创建查看器 和 数据模型
        listview = QListView()
        listModel = QStringListModel()
        self.list = ["列表项1","列表项2", "列表项3"]

        # 数据放入模型  # 模型放入查看器
        listModel.setStringList(self.list)
        listview.setModel(listModel)

        # 信号链到槽
        listview.clicked.connect(self.clicked)

        layout.addWidget(listview)
        self.setLayout(layout)

    def clicked(self,item):
        # QMessageBox.information(self,"QListView","您选择了：" + self.list[item.row()])
        print("您选择了：" + self.list[item.row()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())