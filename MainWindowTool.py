#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 22:29
# @Author  : Aries
# @Site    : 
# @File    : MainWindowTool.py
# @Software: PyCharm

import sys
from PyQt4 import QtCore, QtGui
from UI.UI_MainWindow import Ui_MainWindowTool


from DialogServerConfig import DialogServerArgs


# 修改默认编码为"utf-8"
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

class MainWindowTool(QtGui.QMainWindow, Ui_MainWindowTool):
    """b
    #方法二：先把ui文件转换成py文件。
    再通过继承 ui中的类Ui_MainWindow，直接初始化
    """

    def __init__(self):
        super(MainWindowTool, self).__init__()
        self.setupUi(self)

        self.ServersTableInit()
        #self.__showSettingDialog()
        self.connect(self.tableWidgetServers, QtCore.SIGNAL("cellDoubleClicked(int,int)"),
                 self, QtCore.SLOT("__ServerArgsDialog(int,int)"))




    def ServersTableInit(self):
        # self.tableWidgetServers.setColumnCount(11)


        self.tableWidgetServers.setRowCount(1)

        # self.csbutton = QtGui.QPushButton()
        # self.tableWidgetServers.setCellWidget(0,5,self.csbutton)
        for col in range(0,6):
            self.ItemInTable(col)

        self.ItemInTable(9)

        for col in range(6, 9):
            self.CheckBoxInTable(col)

    def ItemInTable(self,col,text=""):
        item = QtGui.QTableWidgetItem()
        item.setText("xxxxxxxxxx")
        self.tableWidgetServers.setItem(0,col,item)
        item.setSelected(False)

    # def NoEditItemInTable(self,col,text=""):
    #
    #     item = QtGui.QTableWidgetItem()
    #     item.setText("xxxxxxxxxx")
    #     # item.setFlags(QtCore.Qt.ItemIsEditable)
    #     self.tableWidgetServers.setItem(0,col,item)

    def CheckBoxInTable(self,col):
        chekboxwidget = QtGui.QWidget()
        isEnableChekBox = QtGui.QCheckBox()
        VLayout = QtGui.QVBoxLayout()
        VLayout.addWidget(isEnableChekBox)
        VLayout.setMargin(0)
        VLayout.setAlignment(QtCore.Qt.AlignCenter)
        chekboxwidget.setLayout(VLayout)
        self.tableWidgetServers.setCellWidget(0,col,chekboxwidget)


        pass

    @QtCore.pyqtSlot(int,int)  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __ServerArgsDialog(self,row,col):
        # 初始化显示控制台相关qdialog部件
        print row,col
        if col == 5:
            item = self.tableWidgetServers.currentItem()
            #self.tableWidgetServers.currentItem().setFlags(QtCore.Qt.ItemIsEditable)
            dlgargs = DialogServerArgs()
            dlgargs.params = item.text()
            dlgargs.StoredParams()
            self.connect(dlgargs.buttonBox, QtCore.SIGNAL("accepted()"), self,
                         QtCore.SLOT("__DialogAccept()"))  # 确认或者OK按钮
            self.connect(dlgargs.buttonBox, QtCore.SIGNAL("rejected()"), self,
                         QtCore.SLOT("__DialogReject()"))  # 取消或者Cancel按钮

            dlgargs.exec_()
        # rInfo = dlginfo.sendredisConnInfo()
            dlgargs.destroy()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)


    @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __DialogAccept(self):

        print "__DialogAccept()"

    @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __DialogReject(self):

        print "__DialogReject()"

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindowTool()
    window.show()
    sys.exit(app.exec_())