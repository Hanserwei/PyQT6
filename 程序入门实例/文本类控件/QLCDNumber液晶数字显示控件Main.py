import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLCDNumber

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = uic.loadUi('QLCDNumber液晶数字显示控件.ui')
    myLCD: QLCDNumber = ui.lcdNumber
    myLCD.display(8.111)
    myLCD.setDigitCount(8)
    print(myLCD.digitCount())
    print(myLCD.value())
    ui.show()
    sys.exit(app.exec())