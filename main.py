from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize, QPoint
import sys
from currency_converter import CurrencyConverter
from datetime import date


class MainWindow(QMainWindow):
    flag1 = False
    flag2 = False
    val = ['USD', 'EUR', 'RUB', 'GBP', 'JPY', 'CHF']
    row1 = 0
    row2 = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('mainWin.ui', self)
        self.convert_btn.clicked.connect(self.conv)
        self.cur_line_in.clicked.connect(self.list1_)
        self.cur_line_out.clicked.connect(self.list2_)
        self.cur_line_in.currentRowChanged.connect(self.change1)
        self.cur_line_out.currentRowChanged.connect(self.change2)

        self.btnpos_anim = QPropertyAnimation(self.convert_btn, b'pos')
        self.btn_anim = QPropertyAnimation(self.convert_btn, b'size')
        self.animation = QPropertyAnimation(self.cur_line_in, b'size')
        self.animation1 = QPropertyAnimation(self.cur_line_out, b'size')
        self.btnpos_anim.setDuration(150)
        self.btn_anim.setDuration(150)
        self.animation.setDuration(200)
        self.animation1.setDuration(200)

    def conv(self):
        self.btnpos_anim.stop()
        self.btn_anim.stop()
        self.btn_anim.setEasingCurve(QEasingCurve.SineCurve)
        self.btnpos_anim.setEasingCurve(QEasingCurve.SineCurve)
        self.btn_anim.setStartValue(QSize(81, 61))
        self.btn_anim.setEndValue(QSize(71, 51))
        self.btnpos_anim.setStartValue(QPoint(180, 260))
        self.btnpos_anim.setEndValue(QPoint(185, 265))
        self.btnpos_anim.start()
        self.btn_anim.start()
        try:
            amount = int(self.amount_line_in.text())
            oldcur = self.val[self.row1]
            newcur = self.val[self.row2]
            c = CurrencyConverter()
            d = c.convert(amount, oldcur, newcur, date(2022, 3, 1))
            if str(round(d, 3))[0] == '0':
                self.amount_line_out.setText(str(round(d, 3)))
            else:
                self.amount_line_out.setText(str(round(d)))
        except:
            self.amount_line_out.setText('ERROR')

    def list1_(self):
        if not self.flag1:
            self.animation.stop()
            self.animation.setEasingCurve(QEasingCurve.BezierSpline)
            self.animation.setStartValue(QSize(101, 41))
            self.animation.setEndValue(QSize(101, 231))
            self.animation.start()
            self.flag1 = True
            self.cur_line_in.setCurrentRow(0)
        else:
            self.animation.stop()
            self.animation.setEasingCurve(QEasingCurve.InBack)
            self.animation.setStartValue(QSize(101, 231))
            self.animation.setEndValue(QSize(101, 41))
            self.animation.start()
            self.flag1 = False

    def list2_(self):
        if not self.flag2:
            self.animation1.stop()
            self.animation1.setEasingCurve(QEasingCurve.BezierSpline)
            self.animation1.setStartValue(QSize(101, 41))
            self.animation1.setEndValue(QSize(101, 231))
            self.animation1.start()
            self.flag2 = True
            self.cur_line_out.setCurrentRow(0)
        else:
            self.animation1.stop()
            self.animation1.setEasingCurve(QEasingCurve.InBack)
            self.animation1.setStartValue(QSize(101, 231))
            self.animation1.setEndValue(QSize(101, 41))
            self.animation1.start()
            self.flag2 = False

    def change1(self, x):
        self.row1 = x

    def change2(self, x):
        self.row2 = x


def application():
    app = QApplication(sys.argv)
    global mainWin
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
