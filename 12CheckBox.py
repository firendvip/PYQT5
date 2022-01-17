'''
复选框控件（QCheckBox）
3种状态
未选中：0
半选中：1
选中：2
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框控件演示')

        layout = QHBoxLayout()

        self.checkBox1 = QCheckBox('复选框控件1')
        # 设置为选中状态
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda:self.checkboxState(self.checkBox1))
        layout.addWidget(self.checkBox1)

        # 同上
        self.checkBox2 = QCheckBox('复选框控件2')
        self.checkBox2.stateChanged.connect(lambda:self.checkboxState(self.checkBox2))
        layout.addWidget(self.checkBox2)

        # 同上
        self.checkBox3 = QCheckBox('半选中')
        self.checkBox3.stateChanged.connect(lambda:self.checkboxState(self.checkBox3))
        # .setTristate(True) 设置为可以是半选中状态
        self.checkBox3.setTristate(True)
        # 设置为半选中状态  上面的setChecked() 只能设置选中或未选中
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)

    def checkboxState(self,cb):
        # .text()文本信息  / .isChecked() bool值，是否被选中  / .checkState() 返回0或1或2（未选中，半选中，选中）
        check1Status = self.checkBox1.text() + ', isChecked=' + str(self.checkBox1.isChecked()) + ',checkState=' + str(self.checkBox1.checkState()) + '\n'
        check2Status = self.checkBox2.text() + ', isChecked=' + str(self.checkBox2.isChecked()) + ',checkState=' + str(self.checkBox2.checkState()) + '\n'
        check3Status = self.checkBox3.text() + ', isChecked=' + str(self.checkBox3.isChecked()) + ',checkState=' + str(self.checkBox3.checkState()) + '\n'
        print(check1Status + check2Status + check3Status)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())