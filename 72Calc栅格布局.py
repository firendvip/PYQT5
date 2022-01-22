'''
栅格布局：实现计算器UI
'''

import sys,math
from PyQt5.QtWidgets import *


class Calc(QWidget) :
    def __init__(self):
        super(Calc,self).__init__()
        self.setWindowTitle("栅格布局")
        # 栅格布局
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls','Back','','Close',
                 '7','8','9','/',
                 '4','5','6','*',
                 '1','2','3','-',
                 '0','.','=','+']
        # for i in range(5):0-4
        #     for j in range(4):0-3
        #         return (i,j)

        positions = [(i,j) for i in range(5) for j in range(4)]
        print(positions)
        # zip((0,0))
        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            # addWidget() z只接受int 和 QWidget Qt.XXX
           # *position ：把position元组打散成单值
           #  grid.addWidget(button,0,0)
            grid.addWidget(button,*position)










if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Calc()
    main.show()
    sys.exit(app.exec_())