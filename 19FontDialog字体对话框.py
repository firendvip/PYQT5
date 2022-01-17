'''
字体对话框：QFontDialog
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Font Dialog例子')
        self.fontLabel = QLabel('Hello，测试字体例子')
        self.fontButton = QPushButton('选择字体')

        layout = QVBoxLayout()
        layout.addWidget(self.fontButton)
        layout.addWidget(self.fontLabel)
        self.setLayout(layout)

        self.fontButton.clicked.connect(self.getFont)

    def getFont(self):
        # 获取字体弹窗返回值
        font, ok = QFontDialog.getFont()
        # 把字体样式设置到label
        if ok :
            self.fontLabel.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())