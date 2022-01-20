import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 系统模式
    modle = QDirModel()
    tree = QTreeView()
    tree.setModel(modle)
    tree.show()
    sys.exit(app.exec_())