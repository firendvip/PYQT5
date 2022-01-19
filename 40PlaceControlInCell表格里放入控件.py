'''
在单元格中放置控件
setItem：将文本放到单元格中
setCellWidget：将控件放到单元格中
setStyleSheet：设置控件的样式（QSS）
'''

import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem, QAbstractItemView,
                              QComboBox, QPushButton)


class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中放置控件")
        self.resize(750, 400);

        # 创建水平布局
        layout = QHBoxLayout()
        # 创建扩展型列表控件
        tableWidget = QTableWidget()
        # 设置行列
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        # 控件加入布局
        layout.addWidget(tableWidget)
        # 设置行列首字段
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重（kg）'])
        # 填入信息小明到 0行0列
        textItem = QTableWidgetItem('小明')
        tableWidget.setItem(0,0,textItem)

        # 创建下拉框
        combox = QComboBox()
        combox.addItem('男')
        combox.addItem('女')
        # QSS Qt StyleSheet
        # combox.setStyleSheet() 设置下拉框样式 类似CSS
        # margin:3px:编距像素为3px,  QComboBox{}：设置所有的下拉框
        combox.setStyleSheet('QComboBox{margin:3px};')
        # 下拉框放进 0，1 位置
        tableWidget.setCellWidget(0,1,combox)

        # 创建按钮并放入表格
        modifyButton = QPushButton('修改')
        # modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px};')
        tableWidget.setCellWidget(0,2,modifyButton)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = PlaceControlInCell()
    example.show()
    sys.exit(app.exec_())