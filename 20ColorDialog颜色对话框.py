'''
字体对话框：QFontDialog
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Dialog例子')

        self.colorLabel = QLabel('Hello，测试颜色例子')
        self.colorButton = QPushButton('设置字体颜色')
        self.colorButton1 = QPushButton('设置背景颜色')

        layout = QVBoxLayout()
        layout.addWidget(self.colorButton)
        layout.addWidget(self.colorButton1)
        layout.addWidget(self.colorLabel)
        self.setLayout(layout)

        self.colorButton.clicked.connect(self.getColor)
        self.colorButton1.clicked.connect(self.getBGColor)

    def getColor(self):
        # 获取窗体所选中的颜色样式
        color = QColorDialog.getColor()
        # 创建一个调色板
        # QPalettet(palette, 调色板)类相当于窗口或空间的调色板，
        # 它管理着控件或者窗口的颜色信息，
        # 每个部件(widget)都包含一个QPalette对象，并使用该调色板进行绘制
        p = QPalette()
        # QPalette.WindowText：窗体部件文本
        p.setColor(QPalette.WindowText, color)
        self.colorLabel.setPalette(p)

    def getBGColor(self):
        # 同上
        color = QColorDialog.getColor()

        p = QPalette()
        # QPalette.Window：窗体部件的背景色
        p.setColor(QPalette.Window, color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)

        # 二选一，问题未解决

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())
