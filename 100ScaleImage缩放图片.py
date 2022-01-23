'''
缩放图片
QImage.scaled
'''

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import sys


class ScaleImage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图片大小缩放例子")
        # filename = './02.png'
        img = QImage('./02.png')
        label1 = QLabel(self)
        label1.setFixedWidth(200)
        label1.setFixedHeight(200)
        # scaled(宽，高，)
        # QPixmap类是一种 off-screen 图像表示形式，
        # 可以用作绘画设备。使用QLabel或QAbstractButton的子类之一（例如QPushButton和QToolButton），
        # 可以轻松地在屏幕上显示QPixmap。QLabel具有pixmap属性，而QAbstractButton具有icon属性。
        # fromImage() 静态方法，可以直接调用
        # Qt.IgnoreAspectRatio ：忽略长宽比
        # Qt.SmoothTransformation : 平滑变换
        result = img.scaled(label1.width(),label1.height(),Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        label1.setPixmap(QPixmap.fromImage(result))

        vbox = QVBoxLayout()
        vbox.addWidget(label1)

        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ScaleImage()
    win.show()
    sys.exit(app.exec_())