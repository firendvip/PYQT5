'''
信号槽N对N连接与断开连接
'''

from PyQt5.QtCore import *

class NNSignal(QObject):

    signal1 = pyqtSignal()
    signal2 = pyqtSignal()
    signal3 = pyqtSignal(int)

    def __init__(self):
        super(NNSignal,self).__init__()

        self.signal1.connect(self.call1)
        self.signal1.connect(self.call2)

        self.signal2.connect(self.call1)

        self.signal3.connect(self.call1)
        self.signal3.connect(self.call3)

        self.signal1.emit()
        self.signal2.emit()
        self.signal3.emit(3)

    def call1(self):
        print("call1 emit")

    def call2(self):
        print("call2 emit")

    def call3(self,val):
        print("call3 emit:",val)
if __name__ == '__main__':
    nnSignal = NNSignal()