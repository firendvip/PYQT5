'''
让程序定时关闭
QTimer.singleShot(t，f(x)) : 在一定t毫秒后 执行一次 f(x)
'''

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    label = QLabel('<font color=red size=140><b>Hello World，窗口在3秒后自动关闭!</b></font>')
    # setWindowFlags():设置窗口属性
    # Qt.SplashScreen: 闪屏效果
    # Qt.FramelessWindowHint: 隐藏标题栏
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()
    # QTimer.singleShot(t，f(x)): 在一定t毫秒后执行一次f(x)
    QTimer.singleShot(3000, app.quit)

    sys.exit(app.exec_())
