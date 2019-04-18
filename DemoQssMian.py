#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 22:34
# @Author  : Aries
# @Site    : 
# @File    : DemoQssMian.py
# @Software: PyCharm
import MainWindowTool
from PyQt4 import QtGui, QtCore


class Demo(QtGui.QMainWindow, MainWindowTool):
    """qt stylesheet demo"""

    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setupUi(self)
        # 开始装载样式表
        qss_file = open('style.qss').read()
        self.setStyleSheet(qss_file)


import sys

if __name__ == '__main__':
    a = QtGui.QApplication(sys.argv)
    app = Demo()
    app.show()
    a.exec_()