import sys

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QLabel

if __name__ == '__main__':
    # 初始化 QApplication 应用程序
    app = QApplication(sys.argv)
    # 加载 UI 文件
    ui = uic.loadUi('QLabel标签控件.ui')
    # 获取 QLabel 控件
    myLabel: QLabel = ui.label
    myLabel2: QLabel = ui.label_2
    myLabel3: QLabel = ui.label_3
    # 打印 QLabel 的文本内容
    print(myLabel.text())
    print(myLabel2.text())
    myLabel3.setPixmap(QtGui.QPixmap('../icon/baolei.svg'))

    ui.show()
    sys.exit(app.exec())
