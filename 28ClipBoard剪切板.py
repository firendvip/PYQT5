import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()
        textCopyButton = QPushButton("复制文本")
        textPasteButton = QPushButton("粘贴文本")

        htmlCopyButton = QPushButton("复制HTML")
        htmlPasteButton = QPushButton("粘贴HTML")

        imageCopyButton = QPushButton("复制图像")
        imagePasteButton = QPushButton("粘贴图像")

        # 增添显示文本和图片的QLabel控件
        self.textLabel = QLabel("默认文本")
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap("./image/pic2.png"))

        # 使用网格布局
        layout = QGridLayout()
        # 0, 0 ：第0行，第0列
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(htmlCopyButton, 0, 1)
        layout.addWidget(imageCopyButton, 0, 2)
        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(htmlPasteButton, 1, 1)
        layout.addWidget(imagePasteButton, 1, 2)

        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)

        self.setLayout(layout)
        self.setWindowTitle("剪贴板演示")

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)

        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)

        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

    def copyText(self):
        # 直接从QApplication中获得剪贴板对象
        clipboard = QApplication.clipboard()
        # 将系统剪贴板中的内容设为"hello world"
        clipboard.setText("hello world")

    def pasteText(self):
        clipboard = QApplication.clipboard()
        # clipboard.text()方法可以从剪贴板中获取内容
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        # 同QLabel对象一样，clipboard对象设置图像也是通过setPixmap方法
        clipboard.setPixmap(QPixmap('./01.png'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        # clipboard.pixmap()会返回一个代表复制的图像的QPixmap对象
        self.imageLabel.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())