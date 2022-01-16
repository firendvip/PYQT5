from PyQt5.QtWidgets import *
import sys

# 整数校验，精度校验，正则表达式作为校验
from PyQt5.QtGui import QIntValidator,\
    QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp

class Edit_Validator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        # 创建表单布局
        formLayou = QFormLayout()

        # 创建输入框Edit
        int_Edit = QLineEdit()
        double_Edit = QLineEdit()
        re_Edit = QLineEdit()
        re_Edit_NoCh = QLineEdit()
        reg01_Edit = QLineEdit()

        # Edit添加到表单
        formLayou.addRow('整数类型',int_Edit)
        formLayou.addRow('浮点类型',double_Edit)
        formLayou.addRow('数字和字母',re_Edit)
        formLayou.addRow('非中文', re_Edit_NoCh)
        formLayou.addRow('0-1的小数', reg01_Edit)


        # 设置Edit的框内提示信息
        int_Edit.setPlaceholderText('请输入整数')
        double_Edit.setPlaceholderText('请输入数字')
        re_Edit.setPlaceholderText('请输入字母或数字')
        re_Edit_NoCh.setPlaceholderText('请输入非中文')
        reg01_Edit.setPlaceholderText('请输入0-1的小数')

        # 整数校验器
        intValidator = QIntValidator()
        intValidator.setRange(1,999) # 左闭右闭

        # 设置浮点数校验器
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(0.02,1) # 有BUG 上下限无效
        # 常规模式显示浮点数,小数点后两位
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        # 设置正则校验器 字符和数字
        # +:匹配1个或以上的字符，
        # ^ 匹配一行的开头位置 ，$匹配一行的结尾位置
        # 中括号：表示只能取中括号里的值
        # 字母或数字
        reg = QRegExp('^[a-zA-Z0-9]+$')
        re_validator = QRegExpValidator()
        re_validator.setRegExp(reg)

        # 非中文 图片地址
        reg_NoCh = QRegExp('^[^\u4e00-\u9fa5]+$')
        reNoch_validator = QRegExpValidator()
        reNoch_validator.setRegExp(reg_NoCh)

        # 0-1之间的小数,精确到后两位
        reg_01 = QRegExp('^1|(0\.[0-9]{1}[1-9]{1})$')
        reg01_validator = QRegExpValidator()
        reg01_validator.setRegExp(reg_01)


        # 设置校验器
        int_Edit.setValidator(intValidator)
        double_Edit.setValidator(doubleValidator)
        re_Edit.setValidator(re_validator)
        re_Edit_NoCh.setValidator(reNoch_validator)
        reg01_Edit.setValidator(reg01_validator)

        self.setLayout(formLayou)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Edit_Validator()
    main.show()
    sys.exit(app.exec_())
