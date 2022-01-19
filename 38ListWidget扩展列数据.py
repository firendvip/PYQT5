'''
扩展的列表控件（QListWidget） # 继承QListView,在其基础上添加了更多的方法
QListView
'''
from PyQt5.QtWidgets import *
import sys

class ListWidgetDemo(QMainWindow):
	def __init__(self, parent=None):
		super(ListWidgetDemo, self).__init__(parent)
		self.setWindowTitle("QListWidget 例子")
		self.resize(300, 270)
		# 创建一个扩展列表控件
		self.listwidget = QListWidget()
		# 加载数据单个和多个数据
		self.listwidget.addItem("item1")
		self.listwidget.addItems(["item2","item3","item4"])

		# 设置为中心控件
		self.setCentralWidget(self.listwidget)

		# 信号与槽
		self.listwidget.itemClicked.connect(self.clicked)

	def clicked(self,Index):
		QMessageBox.information(self,"QListWidget","您选择了：" + self.listwidget.item(self.listwidget.row(Index)).text())



if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = ListWidgetDemo()
	win.show()
	sys.exit(app.exec_())