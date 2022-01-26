'''
设置窗口样式（主要是窗口边框、标题栏以及窗口本身的样式）
'''

from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import *

class WindowPattern(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 200)
        self.setWindowTitle('设置窗口的样式')
        # Qt.WindowMaximizeButtonHint ：禁止选择 "最小化" 和 "关闭" 按钮。
        # Qt.WindowStaysOnTopHint ：窗口永远在最前端
        self.setWindowFlags(Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint )
        self.setObjectName("MainWindow")
        # 前面有贴过相关信息  这里跳过
        self.setStyleSheet("#MainWindow{border-image:url(images/python.jpg);}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = WindowPattern()
    form.show()
    sys.exit(app.exec_())