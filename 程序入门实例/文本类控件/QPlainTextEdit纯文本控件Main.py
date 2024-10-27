import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QPlainTextEdit, QWidget
from PyQt6.uic.Compiler.qtproxies import QtWidgets

if __name__ == '__main__':
    # 初始化应用程序
    app = QApplication(sys.argv)
    # 加载UI文件
    ui = uic.loadUi("QPlainTextEdit纯文本控件.ui")
    # 获取QPlainTextEdit控件
    myplaintextEdit: QPlainTextEdit = ui.plainTextEdit
    # 向文本编辑器中添加文本
    myplaintextEdit.appendPlainText('bbbbbbbbbbbbbb')
    # 设置文本编辑器为只读状态
    myplaintextEdit.setReadOnly(True)
    # 打印文本编辑器是否为只读
    print(myplaintextEdit.isReadOnly())
    # 打印文本编辑器中的文本内容
    print(myplaintextEdit.toPlainText())


    ui.show()
    sys.exit(app.exec())