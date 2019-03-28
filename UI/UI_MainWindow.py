# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
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

class Ui_MainWindowTool(object):
    def setupUi(self, MainWindowTool):
        MainWindowTool.setObjectName(_fromUtf8("MainWindowTool"))
        MainWindowTool.resize(733, 381)
        self.centralwidget = QtGui.QWidget(MainWindowTool)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidgetConfig = QtGui.QTabWidget(self.centralwidget)
        self.tabWidgetConfig.setObjectName(_fromUtf8("tabWidgetConfig"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayout = QtGui.QFormLayout(self.tab)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.tabWidgetConfig.addTab(self.tab, _fromUtf8(""))
        self.Servers = QtGui.QWidget()
        self.Servers.setObjectName(_fromUtf8("Servers"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.Servers)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tableWidgetServers = QtGui.QTableWidget(self.Servers)
        self.tableWidgetServers.setObjectName(_fromUtf8("tableWidgetServers"))
        self.tableWidgetServers.setColumnCount(10)
        self.tableWidgetServers.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetServers.setHorizontalHeaderItem(9, item)
        self.verticalLayout_2.addWidget(self.tableWidgetServers)
        self.tabWidgetConfig.addTab(self.Servers, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidgetConfig)
        MainWindowTool.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowTool)
        self.tabWidgetConfig.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowTool)

    def retranslateUi(self, MainWindowTool):
        MainWindowTool.setWindowTitle(_translate("MainWindowTool", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindowTool", "PushButton", None))
        self.tabWidgetConfig.setTabText(self.tabWidgetConfig.indexOf(self.tab), _translate("MainWindowTool", "Tab 1", None))
        item = self.tableWidgetServers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowTool", "服务类型", None))
        item = self.tableWidgetServers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowTool", "服务名称", None))
        item = self.tableWidgetServers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowTool", "程序路径", None))
        item = self.tableWidgetServers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowTool", "工作目录", None))
        item = self.tableWidgetServers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowTool", "环境变量", None))
        item = self.tableWidgetServers.horizontalHeaderItem(5)
        item.setText(_translate("MainWindowTool", "服务参数", None))
        item = self.tableWidgetServers.horizontalHeaderItem(6)
        item.setText(_translate("MainWindowTool", "启动", None))
        item = self.tableWidgetServers.horizontalHeaderItem(7)
        item.setText(_translate("MainWindowTool", "自动启动", None))
        item = self.tableWidgetServers.horizontalHeaderItem(8)
        item.setText(_translate("MainWindowTool", "不重复启动", None))
        item = self.tableWidgetServers.horizontalHeaderItem(9)
        item.setText(_translate("MainWindowTool", "启动后延时", None))
        self.tabWidgetConfig.setTabText(self.tabWidgetConfig.indexOf(self.Servers), _translate("MainWindowTool", "Servers", None))

