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
import FormatParams
import TableWidgetOpera
import ConfigFileParserOper

import jsonParserOper

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
        self.rc = ConfigFileParserOper.ReadConfig()
        self.ServersTableInit()
        #self.__showSettingDialog()
        self.connect(self.tableWidgetServers, QtCore.SIGNAL("cellDoubleClicked(int,int)"),
                 self, QtCore.SLOT("__ServerArgsDialog(int,int)"))


        # self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.customContextMenuRequested.connect(self.generateMenu)

    def generateMenu(self, pos):
        print pos

    def ServersTableInit(self):
        listServerCfg = self.getServerCfgDict()
        print "ServersTableInit:\n",listServerCfg
        row = len(listServerCfg)
        # row = self.rc.getServerSize()
        # self.rc.createopt()
        # row = 0
        # self.tableWidgetServers.setColumnCount(11)


        self.tableWidgetServers.setRowCount(row)
        r = 0
        for ServerCfg in listServerCfg :
            if ServerCfg.has_key("title"):
                self.ItemInTable(1, ServerCfg["title"],r) #服务名称
            else:
                return
            if ServerCfg.has_key("serviceType"):
                self.ItemInTable(0, ServerCfg["serviceType"], r)  # 服务类型
            else:
                self.ItemInTable(0, "", r)
            if ServerCfg.has_key("path"):
                self.ItemInTable(2, ServerCfg["path"], r)  # 服务路径
            else:
                self.ItemInTable(2, "", r)
            if ServerCfg.has_key("workDir"):
                self.ItemInTable(3, ServerCfg["workDir"], r)  # 工作目录
            else:
                self.ItemInTable(3, "", r)
            if ServerCfg.has_key("environment"):
                self.ItemInTable(4, ServerCfg["environment"], r)  # 环境变量
            else:
                self.ItemInTable(4, "", r)
            if ServerCfg.has_key("josnStartParam"):
                self.ItemInTable(5, ServerCfg["josnStartParam"], r)  # 参数
            else:
                self.ItemInTable(5, "", r)
            if ServerCfg.has_key("StartedDelay"):
                self.ItemInTable(6, ServerCfg["StartedDelay"], r)  # 启动延时
            else:
                self.ItemInTable(6, "", r)
            if ServerCfg.has_key("isEnable"):
                self.CheckBoxInTable(7,self.StrToBool(ServerCfg["isEnable"]),r) # 是否启用
            else:
                self.CheckBoxInTable(7,False,r)
            if ServerCfg.has_key("AutoRestart"):
                self.CheckBoxInTable(8,self.StrToBool(ServerCfg["AutoRestart"]),r) # 自动启动
            else:
                self.CheckBoxInTable(8, False, r)
            if ServerCfg.has_key("OnlyOne"):
                self.CheckBoxInTable(9, self.StrToBool(ServerCfg["OnlyOne"]), r)  # 不重复启动
            else:
                self.CheckBoxInTable(9, False, r)

            r +=1


        # self.csbutton = QtGui.QPushButton()
        # self.tableWidgetServers.setCellWidget(0,5,self.csbutton)
        # for col in range(0,6):
        #     self.ItemInTable(col)
        r = 0
        for key, values in self.rc.servers.items():
            self.ItemInTable(0,values["Title"],r) #服务类型
            self.ItemInTable(1, values["Title"],r) #服务名称
            self.ItemInTable(2, values["Command"],r) #服务路径
            self.ItemInTable(3, values["Workspace"],r) #工作目录
            self.ItemInTable(4, values["Environment"],r) #环境变量
            self.ItemInTable(5,values["Params"],r) #参数
            self.ItemInTable(6,values["StartedDelay"],r) #启动延时
            if values.has_key("Useable"):
                self.CheckBoxInTable(7,self.StrToBool(values["Useable"]),r)
            else:
                self.CheckBoxInTable(7,False,r)
            self.CheckBoxInTable(8,self.StrToBool(values["AutoRestart"]),r)
            self.CheckBoxInTable(9,self.StrToBool(values["OnlyOne"]),r)

            # for col in range(7, 10):
            #     self.CheckBoxInTable(col)
            r +=1

    def StrToBool(self,str):
        if str.lower() == "true":
            return True
        elif str.lower() == "1":
            return True
        else:
            return False

    def ItemInTable(self,col,text="",row=0):
        item = QtGui.QTableWidgetItem()
        item.setText(text)
        self.tableWidgetServers.setItem(row,col,item)
        item.setSelected(False)

    # def NoEditItemInTable(self,col,text=""):
    #
    #     item = QtGui.QTableWidgetItem()
    #     item.setText("xxxxxxxxxx")
    #     # item.setFlags(QtCore.Qt.ItemIsEditable)
    #     self.tableWidgetServers.setItem(0,col,item)

    def CheckBoxInTable(self,col,isselect=False,r=0):
        chekboxwidget = QtGui.QWidget()
        isEnableChekBox = QtGui.QCheckBox()
        VLayout = QtGui.QVBoxLayout()
        VLayout.addWidget(isEnableChekBox)
        VLayout.setMargin(0)
        VLayout.setAlignment(QtCore.Qt.AlignCenter)
        chekboxwidget.setLayout(VLayout)
        self.tableWidgetServers.setCellWidget(r,col,chekboxwidget)
        if isselect:
            isEnableChekBox.setChecked(isselect)


    def getServerCfgDict(self):
        jo = jsonParserOper.jsonOper()
        jdict = jo.getjsondict("server.json")
        serverdict = jdict["records"]
        return serverdict
    @QtCore.pyqtSlot(int,int)  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __ServerArgsDialog(self,row,col):
        # 初始化显示控制台相关qdialog部件
        print row,col
        if col == 5:
            item = self.tableWidgetServers.currentItem()
            #self.tableWidgetServers.currentItem().setFlags(QtCore.Qt.ItemIsEditable)
            dlgargs = DialogServerArgs()
            dlgargs.servername = self.tableWidgetServers.item(row,1).text()
            _TWOper = TableWidgetOpera.TableWidgetOpera(dlgargs)


            _TWOper.initDialogCfg(dlgargs.servername,FormatParams.nodes)
            dlgargs.setTWOper(_TWOper)

            self.connect(dlgargs, QtCore.SIGNAL("save_data_dict(PyQt_PyObject)"), self, QtCore.SLOT("__saveCfgData(PyQt_PyObject)"))

            dlgargs.exec_()
        # rInfo = dlginfo.sendredisConnInfo()
            dlgargs.destroy()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
    #
    #
    # @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    # def __DialogAccept(self):
    #
    #     print "__DialogAccept()"
    #
    # @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    # def __DialogReject(self):
    #
    #     print "__DialogReject()"

    @QtCore.pyqtSlot("PyQt_PyObject")
    def __saveCfgData(self,nodes):
        print "in __saveCfgData"
        print nodes

    def setTWOper(self,TWOpe):
        self.TWOper = TWOpe

if __name__ == '__main__':
    jo = jsonParserOper.jsonOper()
    jdict = jo.getjsondict("test.json")
    app = QtGui.QApplication(sys.argv)
    window = MainWindowTool()
    TWOper = TableWidgetOpera.TableWidgetOpera(window, True)
    window.setTWOper(TWOper)
    if jdict:
        TWOper.initDialogCfg("localConfig", {"localConfig":jdict})
    window.show()
    sys.exit(app.exec_())