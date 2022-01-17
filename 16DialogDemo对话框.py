'''
对话框：QDialog
QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog
QMainWindow
QWidget
QDialog
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)
        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50,50) # 相对坐标
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        # 创建一个对话框实例
        dialog = QDialog()
        # 创建一个按钮
        button = QPushButton('确定',dialog)

        button.move(50,50)
        dialog.setWindowTitle('对话框')
        # 让对话框处于 模式 状态下
        # dialog.setWindowModality(Qt.ApplicationModal)

        # 链接到槽，关闭对话框
        button.clicked.connect(dialog.close)
        # show():非模式 exec()模式，模式下关闭当前对话框才能进行其他非该窗口操作
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())