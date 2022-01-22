'''
装载本地Web页面
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
class WebEngineView(QMainWindow):

    def __init__(self ):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('装载本地Web页面')
        self.setGeometry(300, 300, 1355, 730)
        # os.getcwd() 获取当前目录  最终得出完整路径
        url = os.getcwd() + '/test.html'
        print(os.getcwd())
        # 创建web控件
        self.browser = QWebEngineView()
        # 加载网页到控件
        self.browser.load(QUrl.fromLocalFile(url))

        self.setCentralWidget(self.browser)



if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = WebEngineView()
	win.show()
	sys.exit(app.exec_())