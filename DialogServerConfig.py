#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 23:51
# @Author  : Aries
# @Site    : 
# @File    : DialogServerConfig.py
# @Software: PyCharm

import sys
from PyQt4 import QtCore, QtGui
from UI.UI_DialogServerArgs import Ui_DialogServerArgs
# 修改默认编码为"utf-8"
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)



class DialogServerArgs(QtGui.QDialog, Ui_DialogServerArgs):
    """b
    #方法二：先把ui文件转换成py文件。
    再通过继承 ui中的类Ui_MainWindow，直接初始化
    """

    def __init__(self):
        super(DialogServerArgs, self).__init__()
        self.setupUi(self)
        ###最后一行自适应
        self.tableWidgetCfgNode.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetCfgArg.horizontalHeader().setStretchLastSection(True)

        self.params=""
    def StoredParams(self):
        print self.params


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = DialogServerArgs()
    window.show()
    sys.exit(app.exec_())