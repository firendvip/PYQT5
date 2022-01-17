'''
按钮控件（QPushButton）
QAbstractButton
QPushButton
AToolButton
QRadioButton
QCheckBox
'''


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QPushButtonDemo(QDialog) :
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')

        layout = QVBoxLayout()

        # 创建按钮
        self.button1 = QPushButton('第1个按钮')
        # 按钮文本
        self.button1.setText('First Button1')
        # 设置按钮为可核对的状态（可按下状态），默认按下状态
        self.button1.setCheckable(True)
        # 获取切换的功能(设置了开关)  应用场景：比如播放器按钮
        self.button1.toggle()
        # 链接到按钮状态，每次单击都会切换状态
        self.button1.clicked.connect(self.buttonState)
        # 1.lambda语法 2.为啥用lambda, 为了好传参数
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))

        layout.addWidget(self.button1)

        # 在文本前面显示图像
        # 同上
        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./01.png')))
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('不可用的按钮')
        # setEnabled(False) 不可选
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        self.button4 = QPushButton('&MyButton')  # atl + 第一个字母
        # .setDefault(True) 设置为默认按钮，按回车之间点击该按钮
        # 默认按钮一个窗口只能有一个
        self.button4.setDefault(True)

        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(600,400)

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')

    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())