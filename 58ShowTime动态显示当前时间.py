'''
动态显示当前时间
QTimer类提供了重复和单次触发信号的定时器
QThread类提供了一个与平台无关的管理线程的方法。
一个QThread对象管理一个线程。
多线程：用于同时完成多个任务
'''

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime
import sys


class ShowTime(QWidget):

    def __init__(self, parent=None):
        super(ShowTime, self).__init__(parent)
        self.setWindowTitle("动态显示当前时间")

        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        # 网格布局
        layout= QGridLayout()
        # 创建定时器
        self.timer = QTimer()
        # timeout显示事件
        self.timer.timeout.connect(self.showTime)

        # 0,0,1,2 ： 在第0行第0列 占用1行，2列的 位置
        layout.addWidget(self.label,0,0,1,2)
        # 位置在第1行 第0列
        layout.addWidget(self.startBtn,1,0)
        layout.addWidget(self.endBtn,1,1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def showTime(self):
        # 获取当前事件
        time = QDateTime.currentDateTime()
        print(time)
        # 设置时间显示风格
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        # 风格加载到标签
        self.label.setText(timeDisplay)

    def startTimer(self):
        # timer.start(毫秒) 开始定时器 每隔多少毫秒 显示一次
        self.timer.start(1000)
        # 开始按钮设置为不可选
        self.startBtn.setEnabled(False)
        # 结束按钮设置为可选
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ShowTime()
    form.show()
    sys.exit(app.exec_())