'''
滑块控件（QSlider）
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('滑块控件演示')
        self.resize(300,700)
        self.label = QLabel('你好 PyQt5')
        self.label.setAlignment(Qt.AlignCenter)

        # 创建横向滑块控件
        self.slider = QSlider(Qt.Horizontal)
        # 设置最小值
        self.slider.setMinimum(12)
        # 设置最大值
        self.slider.setMaximum(48)
        # 步长
        self.slider.setSingleStep(3)
        # 设置当前值
        self.slider.setValue(18)
        # 设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        # 设置刻度的间隔
        self.slider.setTickInterval(6)

        # 设置一个竖滑块
        self.slider1 = QSlider(Qt.Vertical)
        # 设置最小值
        self.slider1.setMinimum(10)
        # 设置最大值
        self.slider1.setMaximum(60)
        # 步长
        self.slider1.setSingleStep(5)
        # 设置当前值
        self.slider1.setValue(30)
        # 设置刻度的位置，刻度在下方
        self.slider1.setTickPosition(QSlider.TicksLeft)
        # 设置刻度的间隔
        self.slider1.setTickInterval(2)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.slider1)
        self.setLayout(layout)

        # 值发生变化的时候触发
        self.slider.valueChanged.connect(self.valueChange)
        self.slider1.valueChanged.connect(self.valueChange)


    def valueChange(self):
        # 获取发送信号对象的值（触发事件就发送信号）
        size = self.sender().value()
        # 输出当前值
        print('当前值：%s' % size)
        # 把当前值设置为字体大小
        self.label.setFont(QFont('Arial',size))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())