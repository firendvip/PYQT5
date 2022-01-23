'''
信号与槽自动连接
on_objectname_signalname
on_okButton_clicked
'''

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication ,QWidget ,QHBoxLayout , QPushButton
import sys

class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot,self).__init__()

        self.okButton = QPushButton("ok", self)
        # 设置okButton的 对象为 "okButton"  "okButton" 为控件内部引用的名字 指向 ok功能的按钮
        # 在QtDesigner指定对象名就可以自动生成下面这句代码
        self.okButton.setObjectName("okButton")


        self.okButton1 = QPushButton("cancel",self)
        self.okButton1.setObjectName("cancelButton")


        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        # Slots：插槽
        QtCore.QMetaObject.connectSlotsByName(self)
        # 以前非自动化信号与槽连接
        #self.okButton.clicked.connect(self.on_okButton_clicked)

    # @QtCore.pyqtSlot()：声明下面的函数是个槽函数
    # 命名规则：on_对象名_信号名(信号参数);
    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print("点击了ok按钮")

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print("点击了cancel按钮")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = AutoSignalSlot()
    example.show()
    sys.exit(app.exec_())