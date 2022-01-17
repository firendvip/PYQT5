import sys  # 系统库
from PyQt5.QtWidgets import QMainWindow, QApplication  # 创建窗口和程序

# QtWidgets 是所有QT控件中的基类
# sys.argv 变量是一个字符串的列表。sys.argv包含了命令行参数的列表

print(sys.argv)

if __name__ == '__main__':
    # 创建程序，类的初始化
    app = QApplication(sys.argv)

    # 创建窗口
    mainWindow = QMainWindow()

    # 显示窗口
    mainWindow.show()

    # app.exec_() 点击关闭按钮，返回 0
    # sys.exit() 对事件进行无限循环监听
    # sys.exit(0)，Break退出循环，sys.exit(1)一直执行，死循环，无限循环
    sys.exit(app.exec_())