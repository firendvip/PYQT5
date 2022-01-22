'''
自定义信号
pyqtSignal()
'''

from PyQt5.QtCore import *
# 创建一个信号的类 继承自 QObject 类
class MyTypeSignal(QObject):
    # 定义一个能发送对象的信号
    sendmsg = pyqtSignal(object)

    # 定义一个能发送3个参数的信号
    sendmsg1 = pyqtSignal(str,int,int)
    # emit 用来发射信号，传递参数
    # 把参数 'Hello PyQt5' 发送到和他绑定的槽函数上，成为槽函数的参数
    # 事件触发条件，对象.run()
    def run(self):
        self.sendmsg.emit('Hello PyQt5')

    def run1(self):
        self.sendmsg1.emit("hello1111",3,4)

# 创建一个槽的类
class MySlot(QObject):
    # msg：用来接收传递过来的参数
    def get(self,msg):
        print("信息：" + msg)
        #
    def get1(self,msg,a,b):
        print(msg,a+b)


if __name__ == '__main__':
    # 实例化信号
    send = MyTypeSignal()
    # 实例化槽
    slot = MySlot()

    send.sendmsg.connect(slot.get)
    send.sendmsg1.connect(slot.get1)

    # 断开信号与槽的链接
    # send.sendmsg.disconnect(slot.get)

    send.run()
    send.run1()
