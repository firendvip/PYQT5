'''
表单布局（QFormLayout）
'''

import sys,math
from PyQt5.QtWidgets import *


class FormForm(QWidget) :
    def __init__(self):
        super(FormForm,self).__init__()
        self.setWindowTitle("表单布局")
        self.resize(750, 850)

        formLayout = QFormLayout()

        titleLabel = QLabel('标题')
        authorLabel = QLabel('作者')
        contentLabel = QLabel('内容')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        contentEdit = QTextEdit()

        formLayout.addRow(titleEdit,titleLabel)
        formLayout.addRow(authorLabel,authorEdit)
        formLayout.addRow(contentLabel,contentEdit)

        self.setLayout(formLayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FormForm()
    main.show()
    sys.exit(app.exec_())