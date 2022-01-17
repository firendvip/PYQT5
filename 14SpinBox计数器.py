'''
计数器控件（QSpinBox）
'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QSpinBox演示')
        self.resize(300,100)

        layout = QVBoxLayout()
        self.label = QLabel('当前值')
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        # 创建计数器
        self.sb = QSpinBox()
        # 设置计数器初始值
        self.sb.setValue(18)
        # 设置计数器取值范围
        self.sb.setRange(10,38)
        # 设置计数器步长
        self.sb.setSingleStep(3)
        # *事件值发生变化时发出信号
        self.sb.valueChanged.connect(self.valueChange)

        layout.addWidget(self.sb)
        self.setLayout(layout)

    def valueChange(self):
        self.label.setText('当前值：' + str(self.sb.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSpinBoxDemo()
    main.show()
    sys.exit(app.exec_())