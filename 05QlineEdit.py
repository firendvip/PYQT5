from PyQt5.QtWidgets import *
import sys

class LineEdit_Echo(QWidget):

    def __init__(self):
        super(LineEdit_Echo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框回显模式')

        # 创建表单布局
        formLayou = QFormLayout()

        # 创建输入框
        normal_Edit = QLineEdit()
        noEcho_Edit = QLineEdit()
        password_Edit = QLineEdit()
        passwordEcho_Edit = QLineEdit()

        # 文本框加到框架
        formLayou.addRow('Normal',normal_Edit)
        formLayou.addRow('NoEcho',noEcho_Edit)
        formLayou.addRow('password',password_Edit)
        formLayou.addRow('passwordEcho',passwordEcho_Edit)

        # 设置框内的内容
        normal_Edit.setPlaceholderText('Normal')
        noEcho_Edit.setPlaceholderText('NoEcho')
        password_Edit.setPlaceholderText('password')
        passwordEcho_Edit.setPlaceholderText('passwordEcho')

        # 设置回显模式
        normal_Edit.setEchoMode(QLineEdit.Normal)
        noEcho_Edit.setEchoMode(QLineEdit.NoEcho)
        password_Edit.setEchoMode(QLineEdit.Password)
        passwordEcho_Edit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayou)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = LineEdit_Echo()
    main.show()
    sys.exit(app.exec_())