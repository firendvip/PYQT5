'''
单选按钮控件（QRadioButton）
'''

import sys
from PyQt5.QtWidgets import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        # 所有单项框放在一个容器里，实现单项（内部定义好的）
        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        # 按钮1状态设置为选中状态
        self.button1.setChecked(True)
        # 对象.toggled.connect(函数) ：对象.状态被切换的时候触发函数
        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        # 同上
        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)

        layout.addWidget(self.button2)

        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()

        if radioButton.isChecked() == True:
            print('<' + radioButton.text() + '> 被选中')
        else:
            print('<' + radioButton.text() + '> 被取消选中状态')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())
