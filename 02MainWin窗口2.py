import sys  # 系统库
from PyQt5.QtWidgets import QMainWindow, QApplication  # 创建窗口和程序
from PyQt5.QtGui import QIcon  # 设置图标




class MainWin(QMainWindow):
    # https: // blog.csdn.net / thumb3344 / article / details / 5644789
    # 没有parent的QWidget类被认为是最上层的窗体（通常是MainWindow）
    # mainWindow = QMainWindow
    def __init__(self, parent=None):
        # 初始化继承的父类
        super().__init__(parent)

        # 设置窗口标题
        self.setWindowTitle('这是一个窗口标题')

        # 设置窗口尺寸
        self.resize(400, 300)

        # 创建状态栏
        self.status = self.statusBar()
        # 在状态栏上显示信息
        self.status.showMessage('存在3秒的消息', 3000)


if __name__ == '__main__':
    #创建程序
    app = QApplication(sys.argv)

    # 设置图标
    app.setWindowIcon(QIcon('./01.png'))

    # 窗口实例化
    main = MainWin()

    # 展示窗口
    main.show()

    # 持续监听
    sys.exit(app.exec_())
