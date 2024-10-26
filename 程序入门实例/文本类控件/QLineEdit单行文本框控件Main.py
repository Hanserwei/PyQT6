import sys

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit

if __name__ == '__main__':
    # 初始化 QApplication 应用程序
    app = QApplication(sys.argv)
    # 加载 UI 文件
    ui = uic.loadUi('QLineEdit单行文本框控件.ui')
    mylineEdit = ui.lineEdit
    mylineEdit.setPlaceholderText("请输入内容")
    mylineEdit.setMaxLength(10)
    mylineEdit.setClearButtonEnabled(True)


    ui.show()
    sys.exit(app.exec())
