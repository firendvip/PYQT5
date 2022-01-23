'''
多线程更新UI数据（在两个线程中传递数据）
'''
# A线程处理数据，返回数据 到B线程(主线程)上
# 在分线程处理数据 处理完后显示在主线程的UI中
# 用信号与槽 进行数据传递与更新

# 1.子线程信号绑定到主线程的槽函数
# 2.子线程完成任务发送信号传递数据给到主线程的槽函数
# 3.槽函数更新主线程ui


from PyQt5.QtCore import QThread ,  pyqtSignal,  QDateTime
from PyQt5.QtWidgets import QApplication,  QDialog,  QLineEdit
import time
import sys

#
# QThread:线程类
class BackendThread(QThread):
    # 声明一个带字符串参数类型的信号
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            # 获取系统当前事件
            data = QDateTime.currentDateTime()
            # 设置事件样式
            currentTime = data.toString("yyyy-MM-dd hh:mm:ss")
            # 把时间当成参数发送
            self.update_date.emit(currentTime)
            time.sleep(1)
# QDialog 对话框
class ThreadUpdateUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('多线程更新UI数据')
        self.resize(600,300)
        self.input = QLineEdit(self)
        # 设置单行输入框的尺寸
        self.input.resize(600,300)
        # 执行 initUI() 函数
        self.initUI()

    def initUI(self):
        # 创建一个线程 BackendThread() ：上面我自己定义的线程类
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        # 让整个类运行起来
        self.backend.start()

    def handleDisplay(self,data):
        self.input.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = ThreadUpdateUI()
    example.show()
    sys.exit(app.exec_())


