'''
QTextEdit控件
'''

from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget) :
    def __init__(self):
        super(QTextEditDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit控件演示')

        self.resize(800,620)

        # 创建一个多行输入框
        self.textEdit = QTextEdit()
        # 创建按钮
        self.buttonText = QPushButton('显示文本')
        self.buttonHTML = QPushButton('显示HTML')

        self.buttonToText = QPushButton('获取文本')
        self.buttonToHTML = QPushButton('获取HTML')

        # 创建垂直布局 并添加前面所有控件
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToHTML)

        # 布局添加到框架
        self.setLayout(layout)

        # 按钮单击信号链接到槽
        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHTML.clicked.connect(self.onClick_ButtonHTML)

        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHTML.clicked.connect(self.onClick_ButtonToHTML)

    def onClick_ButtonText(self):
        # self.textEdit 多行输入框对象  .setPlainText() 在输入框内显示文本
        self.textEdit.setPlainText('Hello World，世界你好吗？')

    def onClick_ButtonToText(self):
        # 获取输入框内的文本
        print(self.textEdit.toPlainText())

    def onClick_ButtonHTML(self):
        # 显示HTML
        self.textEdit.setHtml('<font color="blue" size="5">Hello World</font>')
    def onClick_ButtonToHTML(self):
        # 获取HTML格式的文本
        print(self.textEdit.toHtml())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())