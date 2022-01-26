# setAlignment():设置文本的对齐方式
# setIndent():设置文本缩进
# text():获取文本内容
# setBuddy():设置伙伴关系
# setText():设置文本内容
# selectedText():返回所选择的字符
# setWordWrap():设置是否允许换行
# QLabel常用的信号(事件) :
# 1.当鼠标滑过QL abel控件时触发: linkHovered
# 2.当鼠标单击QL abel控件时触发: linkActivated

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout,\
    QMainWindow, QApplication, QLabel, QWidget
from PyQt5.QtGui import QPalette, QPixmap, QIcon  # 调色板，设置本背景颜色


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        # 设置窗口大小
        self.resize(600, 400)
        # 继承initUI
        self.initUI()

    # 定义主体窗口
    def initUI(self):
        # 创建label控件
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # 设置文本信息字体颜色和内容
        label1.setText("<font color=yellow>这是一个文本标题</font>")
        # 填充背景
        label1.setAutoFillBackground(True)
        # 实例化调色板
        palette = QPalette()
        # 设置颜色对象及颜色
        palette.setColor(QPalette.Window, Qt.blue)
        # 设置label1调色样式为 palette
        label1.setPalette(palette)
        # 设置对齐方式为，居中显示
        label1.setAlignment(Qt.AlignCenter)

        # 设置为富文本及文本信息
        label2.setText("<a href='#'>这是label2</a>")

        # 设置对齐方式为，居中显示 和 提示信息
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        # QPixmap类用于绘图设备的图像显示，
        # 它即可以作为一个绘图对象，也可以加载到一个控件中
        label3.setPixmap(QPixmap('./01.png'))

        # 设置打开外部链接为True，打开浏览器链接
        # 如为False,调用槽函数 二选一
        label4.setOpenExternalLinks(True)
        # 设置为富文本及文本信息
        label4.setText("<a href='https://baidu.com'>百度链接</a>")
        # 对齐方式为靠右
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        # ctrl+D
        # 实例化垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        # 信号与槽绑定
        label2.linkHovered.connect(self.link_Hovered)
        label4.linkActivated.connect(self.linkClicked)

        # 把布局添加到框架
        self.setLayout(vbox)
        self.setWindowTitle('Qlabel控件演示')

    def link_Hovered(self):
        print('当鼠标滑过label2控件时触发')

    def linkClicked(self):
        print('当鼠单击label4控件时触发')

if __name__ == '__main__':
    # 创建程序
    app = QApplication(sys.argv)
    # 窗口实例化
    main = QLabelDemo()
    # 设置图标
    app.setWindowIcon(QIcon('./HTicon'))
    # 展示窗口
    main.show()
    # 持续监听
    sys.exit(app.exec_())