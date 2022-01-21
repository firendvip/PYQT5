'''
使用线程类（QThread）编写计数器
QThread
def run(self):
   while True:
       self.sleep(1)
       if sec == 5:
           break;


QLCDNumber控件用于显示一个LCD数字

在主线程里更新控件
用到自定义信号，之前用的都是系统内置的信号方法
WorkThread(QThread)
'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *




sec = 0


class WorkThread(QThread):
    # 定义两个无参数的信号
    timer = pyqtSignal()  # 用来每隔1秒发送一次信号
    end = pyqtSignal()  # 用来计数完成后发送一次信号

    def run(self):
        while True:
            self.sleep(1)  # 休眠1秒
            if sec == 5:
                # 每隔1秒发送一次信号
                self.end.emit()  # 发送end信号
                break
            # 计数完成后发送一次信号
            self.timer.emit()  # 发送timer信号


class Counter(QWidget):

    def __init__(self, parent=None):
        super(Counter, self).__init__(parent)

        self.setWindowTitle("使用线程类（QThread）编写计数器")
        self.resize(750, 850)

        layout = QVBoxLayout()
        # QLCDNumber控件用于显示一个LCD数字 计算器那样的数字
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)

        button = QPushButton('开始计数')
        layout.addWidget(button)
        # 创建多线程任务
        self.workThread = WorkThread()
        # 信号关联到槽 （两个自定义的信号 timer 和 end）
        # 每隔一秒发送一次信号，每次发送信号都执行 self.countTime
        self.workThread.timer.connect(self.countTime)
        self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)

        self.setLayout(layout)

    def countTime(self):
        global sec
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self, '消息', '计数结束', QMessageBox.Ok)

    # 按钮对应的函数，直接启动多线程
    def work(self):
        self.workThread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Counter()
    form.show()
    sys.exit(app.exec_())
