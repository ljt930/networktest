#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from UI.UI_Diaog_conninfo import Ui_Dialog_conninfo
# 修改默认编码为"utf-8"
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)



class Dialog_conninfo(QtGui.QDialog, Ui_Dialog_conninfo):
    """b
    #方法二：先把ui文件转换成py文件。
    再通过继承 ui中的类Ui_MainWindow，直接初始化
    """

    def __init__(self):
        super(Dialog_conninfo, self).__init__()
        self.setupUi(self)

        self.rCI = None
        self.__init_signal()

    def __init_signal(self):
        # self.pushButton_ok.clicked.connect(self.clickOK)
        self.connect(self.pushButton_cancel, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("__clickCancel()"))

        self.connect(self.pushButton_ok, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT("__clickOK()"))

        # self.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),self, QtCore.SLOT("accept()"))

    @QtCore.pyqtSlot()
    def __clickOK(self):
        self.emit(QtCore.SIGNAL("setting_clickOK(PyQt_PyObject)"), self.sendredisConnInfo())
        self.close()

    def sendredisConnInfo(self):
        if self.rCI == None:
            return None
        return self.rCI
        # self.close()

    @QtCore.pyqtSlot()
    def __clickCancel(self):
        # if self.rCI == None:
        #     self.close()
        # print self.rCI.getdInfo()
        self.close()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Dialog_conninfo()
    window.show()
    sys.exit(app.exec_())