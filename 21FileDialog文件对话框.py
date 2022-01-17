'''
文件对话框：QFileDialog
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文件对话框演示 ')

        # 创建控件
        self.imageLabel = QLabel()
        self.contents = QTextEdit()
        self.button1 = QPushButton('加载图片')
        self.button2 = QPushButton('加载文本文件')

        # 设置控件

        # 控件加入布局，布局放入框架
        layout = QVBoxLayout()
        layout.addWidget(self.contents)
        layout.addWidget(self.imageLabel)
        layout.addWidget(self.button2)
        layout.addWidget(self.button1)
        self.setLayout(layout)

        # 信号与槽绑定
        self.button1.clicked.connect(self.loadImage)
        self.button2.clicked.connect(self.loadText)

        # 定义槽(函数)
    def loadImage(self):
        # getOpenFileName(对象，对话框标题，默认路径，可选类型)
        # 返回一个被用户选中的文件的路径，前提是这个文件是存在的 . 和设置的可选类型
        # _ : 分配了一个特定的名称（变量），但是并不会在后面再次用到该名称
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件1', '.', '图像文件(*.jpg *.png)')
        print(fname, _)
        self.imageLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        # 创建一个可以打开窗口的实例
        dialog = QFileDialog()
        # 设置模式为可以打开任何文件模式
        dialog.setFileMode(QFileDialog.AnyFile)
        # setFilter()设置过滤器，只显示过滤器允许的文件类型
        # QDir.Files:  (文件？非文件夹)
        dialog.setFilter(QDir.Files)
         # 如果打开成功
        if dialog.exec():
            # 获取文件路径   selectedFiles()返回列表
            filenames = dialog.selectedFiles()
            print(filenames,filenames[0])
            with open(filenames[0], encoding='utf-8',mode='r') as f:
                data = f.read()
                self.contents.setText(data)

            # f = open(filenames[0], encoding='utf-8', mode='r')
            # with f:
            #     data = f.read()
            #     self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
