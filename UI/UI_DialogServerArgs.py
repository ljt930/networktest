# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogServerArgs.ui'
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

class Ui_DialogServerArgs(object):
    def setupUi(self, DialogServerArgs):
        DialogServerArgs.setObjectName(_fromUtf8("DialogServerArgs"))
        DialogServerArgs.resize(483, 383)
        self.verticalLayout = QtGui.QVBoxLayout(DialogServerArgs)
        self.verticalLayout.setMargin(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(DialogServerArgs)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(1)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tableWidgetCfgNode = QtGui.QTableWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetCfgNode.sizePolicy().hasHeightForWidth())
        self.tableWidgetCfgNode.setSizePolicy(sizePolicy)
        self.tableWidgetCfgNode.setMinimumSize(QtCore.QSize(200, 0))
        self.tableWidgetCfgNode.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidgetCfgNode.setObjectName(_fromUtf8("tableWidgetCfgNode"))
        self.tableWidgetCfgNode.setColumnCount(1)
        self.tableWidgetCfgNode.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetCfgNode.setHorizontalHeaderItem(0, item)
        self.tableWidgetCfgArg = QtGui.QTableWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetCfgArg.sizePolicy().hasHeightForWidth())
        self.tableWidgetCfgArg.setSizePolicy(sizePolicy)
        self.tableWidgetCfgArg.setObjectName(_fromUtf8("tableWidgetCfgArg"))
        self.tableWidgetCfgArg.setColumnCount(2)
        self.tableWidgetCfgArg.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetCfgArg.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetCfgArg.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_save = QtGui.QPushButton(DialogServerArgs)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.horizontalLayout.addWidget(self.pushButton_save)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(DialogServerArgs)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogServerArgs)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogServerArgs.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogServerArgs.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogServerArgs)

    def retranslateUi(self, DialogServerArgs):
        DialogServerArgs.setWindowTitle(_translate("DialogServerArgs", "Dialog", None))
        item = self.tableWidgetCfgNode.horizontalHeaderItem(0)
        item.setText(_translate("DialogServerArgs", "配置节点名称", None))
        item = self.tableWidgetCfgArg.horizontalHeaderItem(0)
        item.setText(_translate("DialogServerArgs", "参数名称", None))
        item = self.tableWidgetCfgArg.horizontalHeaderItem(1)
        item.setText(_translate("DialogServerArgs", "参数值", None))
        self.pushButton_save.setText(_translate("DialogServerArgs", "保存", None))

