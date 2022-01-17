import sys
from PyQt5.QtWidgets import *


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300, 100)

        layout = QVBoxLayout()

        self.label = QLabel('请选择编程语言')

        # 创建下拉框
        self.cb = QComboBox()
        # 添加单个下拉框内容
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        # 添加多个下拉框内容
        self.cb.addItems(['Java', 'C#', 'Ruby'])
        # 当前的索引变化
        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)

    def selectionChange(self):
        # 获取发送信号的对象
        cb_item = self.sender()
        print('您当前选中的是' + cb_item.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())
