# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Diaog_conninfo.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_conninfo(object):
    def setupUi(self, Dialog_conninfo):
        Dialog_conninfo.setObjectName(_fromUtf8("Dialog_conninfo"))
        Dialog_conninfo.resize(363, 348)
        Dialog_conninfo.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog_conninfo)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Dialog_conninfo)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(35)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_name = QtGui.QLineEdit(self.tab)
        self.lineEdit_name.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.gridLayout.addWidget(self.lineEdit_name, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_host = QtGui.QLineEdit(self.tab)
        self.lineEdit_host.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_host.setObjectName(_fromUtf8("lineEdit_host"))
        self.gridLayout.addWidget(self.lineEdit_host, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.spinBox_port = QtGui.QSpinBox(self.tab)
        self.spinBox_port.setMinimumSize(QtCore.QSize(0, 25))
        self.spinBox_port.setMaximum(65535)
        self.spinBox_port.setProperty("value", 6379)
        self.spinBox_port.setObjectName(_fromUtf8("spinBox_port"))
        self.gridLayout.addWidget(self.spinBox_port, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_auth = QtGui.QLineEdit(self.tab)
        self.lineEdit_auth.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_auth.setObjectName(_fromUtf8("lineEdit_auth"))
        self.gridLayout.addWidget(self.lineEdit_auth, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_testconnection = QtGui.QPushButton(Dialog_conninfo)
        self.pushButton_testconnection.setObjectName(_fromUtf8("pushButton_testconnection"))
        self.horizontalLayout.addWidget(self.pushButton_testconnection)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_ok = QtGui.QPushButton(Dialog_conninfo)
        self.pushButton_ok.setObjectName(_fromUtf8("pushButton_ok"))
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtGui.QPushButton(Dialog_conninfo)
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_conninfo)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_conninfo)

    def retranslateUi(self, Dialog_conninfo):
        Dialog_conninfo.setWindowTitle(_translate("Dialog_conninfo", "Dialog", None))
        self.label.setText(_translate("Dialog_conninfo", "Name:", None))
        self.label_2.setText(_translate("Dialog_conninfo", "Host:", None))
        self.lineEdit_host.setText(_translate("Dialog_conninfo", "127.0.0.1", None))
        self.label_4.setText(_translate("Dialog_conninfo", "Port:", None))
        self.label_3.setText(_translate("Dialog_conninfo", "Auth:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog_conninfo", "Connection", None))
        self.pushButton_testconnection.setText(_translate("Dialog_conninfo", "Test Connection", None))
        self.pushButton_ok.setText(_translate("Dialog_conninfo", "OK", None))
        self.pushButton_cancel.setText(_translate("Dialog_conninfo", "Cancel", None))

