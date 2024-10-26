import sys

from PyQt6 import uic, QtGui
from PyQt6.QtWidgets import QApplication, QTextEdit

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi("QTextEdit多行富文本框控件.ui")
    my_text: QTextEdit = ui.textEdit
    my_text2: QTextEdit = ui.textEdit_2
    my_text.setText('ssssss')
    # my_text.setTextColor(QtGui.QColor(255,255,255))
    my_text.setTextBackgroundColor(QtGui.QColor(255,255,0))
    ui.show()
    sys.exit(app.exec())