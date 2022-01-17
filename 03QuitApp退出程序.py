import sys

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, \
    QApplication, QPushButton, QWidget, QToolTip


class QuitAPP(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.setWindowTitle('退出程序')

        # 添加按钮
        self.button1 = QPushButton('退出程序的按钮')
        # 设置按钮字体和大小
        self.button1.setFont(QFont('SansSerif', 16))
        # 添加按钮提示信息
        self.button1.setToolTip('这是按钮的提示信息')
        # 设置提示信息字体和大小
        QToolTip.setFont(QFont('SansSerif', 24))
        # 将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)
        # 创建一个水平布局
        layout = QHBoxLayout()
        # 把按钮添加到布局里
        layout.addWidget(self.button1)
        # 主框架Widget，所有组件的根。将按钮添加到主框架中
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        # 把主框架放到窗口上且居中
        self.setCentralWidget(mainFrame)

    # 按钮单机事件的方法
    def onClick_Button(self):
        # sender()  返回发送信号的对象，即按钮对象
        sender = self.sender()
        # sender.text() 获取信号对象文本
        print(sender.text() + '被按下')
        # 获取instance() 获取单例对象(获取当前窗口)，单例：
        app = QuitAPP.instance()
        app.quit()


if __name__ == '__main__':
    # 创建程序
    app = QApplication(sys.argv)

    # 窗口实例化
    main = QuitAPP()

    # 设置图标
    app.setWindowIcon(QIcon('./01.png'))

    # 展示窗口
    main.show()

    # 持续监听
    sys.exit(app.exec_())

# 以上这些都是理解designer模块后面的原理，实际上关闭可以通过designer实现
