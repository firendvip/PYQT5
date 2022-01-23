from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DateDialog(QDialog):
    def __init__(self,parent=None):
        super(DateDialog,self).__init__(parent)
        self.setWindowTitle("DateDialog")

        layout = QVBoxLayout(self)
        # QDateTimeEdit是一个允许用户编辑日期时间的控件，
        # 可以使用键盘上的上下键头按钮来增加或减少日期的时间值，
        # QDateTimeEdit通过setDisplayFormat（）函数来设置显示的日期时间格式
        self.datetime = QDateTimeEdit(self)
        # QDateEdit控件要显示日历，需要用下面的setCalendarPopup(true)
        self.datetime.setCalendarPopup(True)
        # 设置时间为当前时间
        self.datetime.setDateTime(QDateTime.currentDateTime())

        layout.addWidget(self.datetime)
        # QDialogButtongBox类是一个包含很多按钮的控件，
        # 在对话框中有多个按钮需要分组排列的按钮时，
        # 可以使用QDialogButtongBox类。
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal,self)
        # self.accept/accept（）函数和self.accept/reject（）函数
        # 这两个函数作用分别是：都能够隐藏QDialog，
        # 但是返回值不同，一个是Accepted，一个是Rejected，
        # 返回值不同的作用是：区分用户按下的OK按钮，还是Cancel按钮。
        #  ok 按钮和 cancel按钮 是系统内置的
        buttons.accepted.connect(self.accept) # accepted代表ok按钮的单击事件/信号
        buttons.rejected.connect(self.reject) # rejected代表cancel按钮的单击事件/信号

        layout.addWidget(buttons)

    def dateTime(self):
        return self.datetime.dateTime()


    @staticmethod # 声明下面的是个静态方法
    def getDateTime(parent = None):
        # 实例化日期时间的控件/对话框 对象
        dialog = DateDialog(parent)
        # 对话框
        result = dialog.exec()
        # 获取日期 调用上面自己定义的函数
        date = dialog.dateTime()
        # 返回 result == QDialog.Accepted  执行后会返回： Ture or false
        return (date.date(),date.time(),result == QDialog.Accepted)