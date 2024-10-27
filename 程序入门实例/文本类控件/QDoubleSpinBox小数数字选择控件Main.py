import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi('QDoubleSpinBox小数数字选择控件.ui')

    ui.show()
    sys.exit(app.exec())