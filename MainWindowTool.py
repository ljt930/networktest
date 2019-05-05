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
import CharactersConversion
import TableWidgetOpera
import ConfigFileParserOper
import ComboCheckBox
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

        self.m_SettingCfgDict = ""
        self.CC = CharactersConversion.CharactersConversion() # 字符转换类
        self.selectrow = 0
        self.Serverrowcount = 0
        self.__initwidget()

    def __initwidget(self):
        self.tableWidgetServers.horizontalHeader().setStretchLastSection(True)

        self.__creatServersCfgTable()
        self.__iniStyleSheet()
        self.__initToolBar()
        self.__init_tableWidgetServers()

        self.__initsinglbond()


    def __initToolBar(self):

        self.m_pToolBar = QtGui.QToolBar()
        self.m_pToolBar.setIconSize(QtCore.QSize(32, 32))
        self.m_pToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.m_pToolBar.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.m_pActionAdd = self.m_pToolBar.addAction(QtGui.QIcon("./Images/action_edit.png"), u"添加")
        # m_pActionAdd.setVisible(False)
        self.m_pActionRefres = self.m_pToolBar.addAction(QtGui.QIcon("./Images/action_refresh.png"),u"刷新")
        self.m_pActionSave = self.m_pToolBar.addAction(QtGui.QIcon("./Images/action_save.png"),u"保存")
        self.m_pActionExport = self.m_pToolBar.addAction(QtGui.QIcon("./Images/action_export.png"),u"导出")
        # m_pActionDel.setVisible(False)
        self.horizontalLayout_toolbar.addWidget(self.m_pToolBar)

        self.m_lToolBar = QtGui.QToolBar()
        self.m_lToolBar.setIconSize(QtCore.QSize(32, 32))
        self.m_lToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.m_lToolBar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.m_lActionSave = self.m_lToolBar.addAction(QtGui.QIcon("./Images/action_save.png"), u"保存")

        self.horizontalLayout_toolBar_local.addWidget(self.m_lToolBar)

    def __init_tableWidgetServers(self):
        self.tableWidgetServers.setColumnWidth(0,200)
        self.tableWidgetServers.setColumnWidth(1, 180)
        self.tableWidgetServers.setColumnWidth(2, 180)
        self.tableWidgetServers.setColumnWidth(3, 70)
        self.tableWidgetServers.setColumnWidth(4, 260)
        self.tableWidgetServers.setColumnWidth(5, 280)
        self.tableWidgetServers.setColumnWidth(6, 70)
        self.tableWidgetServers.setColumnWidth(7, 65)
        self.tableWidgetServers.setColumnWidth(8, 65)
        self.tableWidgetServers.setColumnWidth(9, 70)
        self.tableWidgetServers.setColumnWidth(10, 65)

        self.tableWidgetServers.setColumnWidth(11, 200)


        # self.tableWidgetServers.setStyleSheet("gridline-color: #cad7e3;alternate-background-color: transparent;background: #transparent;")


    def __iniStyleSheet(self):
        # 开始装载样式表
        qss_file = open("UI/style.qss").read()
        self.setStyleSheet(qss_file)

        self.tableWidgetServers.setAlternatingRowColors(True)  # 设置交替颜色起作用

    def __initsinglbond(self):
        self.connect(self.tableWidgetServers, QtCore.SIGNAL("cellDoubleClicked(int,int)"),
                     self, QtCore.SLOT("__ServerArgsDialog(int,int)"))
        self.connect(self.m_pActionAdd, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("__AddServerConfig()"))


        self.connect(self.m_pActionExport,QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("__ExportConfigFile()"))

        self.connect(self.m_pActionSave, QtCore.SIGNAL("triggered()"), self, QtCore.SLOT("__SaveJsonToFile()"))

    def __creatServersCfgTable(self):
        # listServerCfg = getServerCfgDict("server.json","records")
        listServerCfg = getServerCfgDict("tt.txt","records")
        # print "ServersTableInit:\n",listServerCfg
        self.Serverrowcount = len(listServerCfg)

        self.tableWidgetServers.setRowCount(self.Serverrowcount)
        r = 0

        for ServerCfg in listServerCfg :
            self.__creatOneRowInTable(r,True,ServerCfg)
            r +=1
        # self.tableWidgetServers.item(0, 7).setTextAlignment(QtCore.Qt.AlignCenter)

    def __creatOneRowInTable(self,r ,isloadfile, ServerCfg={}):
        if ServerCfg.has_key("title"):
            self.__creatItemInTable(1, ServerCfg["title"], r)  # 服务名称

            localparamnode = ServerCfg["isEnableLocalParam"]
            # listnode = localparamnode.keys()
        else:
            if isloadfile :
                return
            else:
                self.__creatItemInTable(1, "", r)
                localparamnode = {}

        if ServerCfg.has_key("serviceType"):
            self.__creatItemInTable(0, ServerCfg["serviceType"], r)  # 服务类型
        else:
            self.__creatItemInTable(0, "", r)
        if ServerCfg.has_key("path"):
            self.__creatItemInTable(2, ServerCfg["path"], r)  # 服务路径
        else:
            self.__creatItemInTable(2, "", r)
        if ServerCfg.has_key("workDir"):
            self.__creatItemInTable(3, ServerCfg["workDir"], r)  # 工作目录
        else:
            self.__creatItemInTable(3, "", r)
        if ServerCfg.has_key("environment"):
            self.__creatItemInTable(4, ServerCfg["environment"], r)  # 环境变量
        else:
            self.__creatItemInTable(4, "", r)
        if ServerCfg.has_key("josnStartParam"):
            self.__creatItemInTable(5, ServerCfg["josnStartParam"], r)  # 参数
        else:
            self.__creatItemInTable(5, "", r)
        if ServerCfg.has_key("StartedDelay"):
            self.__creatItemInTable(6, ServerCfg["StartedDelay"], r)  # 启动延时
        else:
            self.__creatItemInTable(6, "", r)
        if ServerCfg.has_key("isEnable"):
            self.__creatCheckBoxInTable(7, self.CC.StrToBool(ServerCfg["isEnable"]), r)  # 是否启用
        else:
            self.__creatCheckBoxInTable(7, False, r)
        if ServerCfg.has_key("autoStart"):
            self.__creatCheckBoxInTable(8, self.CC.StrToBool(ServerCfg["autoStart"]), r)  # 自动启动
        else:
            self.__creatCheckBoxInTable(8, False, r)
        if ServerCfg.has_key("single"):
            self.__creatCheckBoxInTable(9, self.CC.StrToBool(ServerCfg["single"]), r)  # 不重复启动
        else:
            self.__creatCheckBoxInTable(9, False, r)
        if ServerCfg.has_key("isWaitStartupOK"):
            self.__creatCheckBoxInTable(10, self.CC.StrToBool(ServerCfg["isWaitStartupOK"]), r)  # 不重复启动
        else:
            self.__creatCheckBoxInTable(10, False, r)
        self._createComboCheckBox(r, localparamnode)

    def __creatItemInTable(self, col, text="", row=0):
        item = QtGui.QTableWidgetItem()
        item.setText(text)
        self.tableWidgetServers.setItem(row,col,item)
        item.setSelected(False)

    def __creatCheckBoxInTable(self, col, isselect=False, row=0):

        chekboxwidget = QtGui.QWidget()
        isEnableChekBox = QtGui.QCheckBox()
        VLayout = QtGui.QVBoxLayout()
        VLayout.addWidget(isEnableChekBox)
        VLayout.setMargin(0)
        VLayout.setAlignment(QtCore.Qt.AlignCenter)
        chekboxwidget.setLayout(VLayout)
        # isEnableChekBox.setAutoFillBackground(True)
        chekboxwidget.setStyleSheet("background-color:transparent ")
        self.tableWidgetServers.setCellWidget(row,col, chekboxwidget)
        if isselect:
            isEnableChekBox.setChecked(isselect)
    def _createComboCheckBox(self,r , listnode):

        CCB = ComboCheckBox.ComboCheckBox(listnode)
        self.tableWidgetServers.setCellWidget(r, 11, CCB)


    @QtCore.pyqtSlot(int,int)  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __ServerArgsDialog(self,row,col):
        # 初始化显示控制台相关qdialog部件
        print row,col
        self.selectrow = row
        if col == 5:
            item = self.tableWidgetServers.currentItem()
            #self.tableWidgetServers.currentItem().setFlags(QtCore.Qt.ItemIsEditable)
            dlgargs = DialogServerArgs()
            serverparm = self.tableWidgetServers.item(row,5).text()
            # QStr转str
            serverparm = self.CC.QString2PyString(serverparm)
            serverparm = jo.jsonloads(serverparm)

            _TWOper = TableWidgetOpera.TableWidgetOpera(dlgargs)
            _TWOper.initDialogCfg("serverparm",{"serverparm":serverparm})
            dlgargs.setTWOper(_TWOper)

            self.connect(dlgargs, QtCore.SIGNAL("save_data_dict(PyQt_PyObject)"), self, QtCore.SLOT("__saveCfgData(PyQt_PyObject)"))

            dlgargs.exec_()
        # rInfo = dlginfo.sendredisConnInfo()
            dlgargs.destroy()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
            self.disconnect(dlgargs, QtCore.SIGNAL("save_data_dict(PyQt_PyObject)"), self, QtCore.SLOT("__saveCfgData(PyQt_PyObject)"))
            dlgargs.delTWOper()
            del _TWOper
            del dlgargs

    @QtCore.pyqtSlot()
    def __SaveJsonToFile(self):
        ##保存按钮触发
        rowCount = self.tableWidgetServers.rowCount()
        ServerCfg ={}
        ServerCfgList = []
        fp = open("tt.txt","w")
        header = {"type":"stringTable"}
        for row in range(0,rowCount):

            title = self.tableWidgetServers.item(row, 1).text()
            #优先转换title为python string类型
            title = self.CC.QString2PyString(title)
            if title == "":
                # print type(title)
                continue
            serviceType = self.tableWidgetServers.item(row,0).text()


            path = self.tableWidgetServers.item(row, 2).text()
            workDir = self.tableWidgetServers.item(row, 3).text()
            environment = self.tableWidgetServers.item(row, 4).text()
            josnStartParam = self.tableWidgetServers.item(row, 5).text()
            StartedDelay = self.tableWidgetServers.item(row, 6).text()
            isEnable = self.tableWidgetServers.cellWidget(row,7).children()[1].isChecked()
            autoStart = self.tableWidgetServers.cellWidget(row,8).children()[1].isChecked()
            single = self.tableWidgetServers.cellWidget(row,9).children()[1].isChecked()
            isWaitStartupOK = self.tableWidgetServers.cellWidget(row,10).children()[1].isChecked()

            ServerCfg["serviceType"] = self.CC.QString2PyString(serviceType)
            ServerCfg["title"] = title
            ServerCfg["path"] = self.CC.QString2PyString(path)
            ServerCfg["workDir"] = self.CC.QString2PyString(workDir)
            ServerCfg["environment"] = self.CC.QString2PyString(environment)
            ServerCfg["josnStartParam"] = self.CC.QString2PyString(josnStartParam)
            # ServerCfg["josnStartParam"] = jo.jsondumps(self.CC.QString2PyString(josnStartParam), indent=4, separators=(',', ': '))
            ServerCfg["StartedDelay"] = self.CC.QString2PyString(StartedDelay)
            ServerCfg["isEnable"] = self.CC.BoolToStr(isEnable)
            ServerCfg["autoStart"] = self.CC.BoolToStr(autoStart)
            ServerCfg["single"] = self.CC.BoolToStr(single)
            ServerCfg["isWaitStartupOK"] = self.CC.BoolToStr(isWaitStartupOK)

            isEnableLocalParam = {}
            self.LocalParamtext = ""
            qCheckBoxList = self.tableWidgetServers.cellWidget(row, 11).qCheckBox
            for qCheckBox in qCheckBoxList:
                # print qCheckBox.text() + ":" + self.CC.BoolToStr(qCheckBox.isChecked())
                self.LocalParamtext = self.CC.QString2PyString(qCheckBox.text())
                if self.LocalParamtext == u"全部":
                    continue
                isEnableLocalParam[self.LocalParamtext] = self.CC.BoolToStr(qCheckBox.isChecked())
            ServerCfg["isEnableLocalParam"] = isEnableLocalParam


            # print ServerCfg
            # s = jo.jsondumps(ServerCfg, sort_keys=True, indent=4, separators=(',', ': '))
            # print s
            #ServerCfgList.append(jo.jsondumps(ServerCfg, sort_keys=True, indent=4, separators=(',', ': ')))
            ServerCfgList.append(ServerCfg)
            ServerCfg = {}
        # print ServerCfgList
        localConfigDict = self.TWOper.CDS.getNodes()
        self.m_SettingCfgDict = {"header":header,"records":ServerCfgList,"localConfig":localConfigDict}
        ServerCfgJson = jo.jsondump(self.m_SettingCfgDict,fp, sort_keys=True, indent=2)
        # print self.m_SettingCfgDict

    @QtCore.pyqtSlot()
    def __AddServerConfig(self):

        self.tableWidgetServers.insertRow(self.Serverrowcount)
        self.__creatOneRowInTable(self.Serverrowcount,False)
        self.tableWidgetServers.setCurrentCell(self.Serverrowcount,0,QtGui.QItemSelectionModel.Select)
        self.Serverrowcount +=1

    @QtCore.pyqtSlot()
    def __ExportConfigFile(self):
        # 保存为服务配置文件
        if self.m_SettingCfgDict == "":
            QtGui.QMessageBox.information(self, u"警告", u"数据未保存")
        else:
            import FormatConfig
            FC = FormatConfig.FormatConfig()
            localnodelist = self.LocalParamtext.split(";")
            FC.FormatSettingConfig(self.m_SettingCfgDict,localnodelist)
            pass

    @QtCore.pyqtSlot("PyQt_PyObject")
    def __saveCfgData(self,nodes):
        print "in __saveCfgData"
        serverparm = jo.jsondumps(nodes)
        # serverparm = str(nodes)
        # serverparm.replace("\\","")
        self.tableWidgetServers.item(self.selectrow,5).setText(serverparm)
        del serverparm

    def setTWOper(self,TWOpe):
        self.TWOper = TWOpe

jo = jsonParserOper.jsonOper()
def getServerCfgDict(file,Node=None):

    jdict = jo.getjsondict(file)
    if Node == None:
        serverdict =jdict
    else:
        serverdict = jdict[Node]
    return serverdict

if __name__ == '__main__':
    # jo = jsonParserOper.jsonOper()

    # jdict = getServerCfgDict("jsonstrBaseStartupParam.json")
    jdict = getServerCfgDict("tt.txt", "localConfig")
    app = QtGui.QApplication(sys.argv)
    window = MainWindowTool()
    TWOper = TableWidgetOpera.TableWidgetOpera(window.localTab, True, window)
    window.setTWOper(TWOper)
    if jdict:
        TWOper.initDialogCfg("localConfig", {"localConfig": jdict})
    window.show()
    del TWOper
    sys.exit(app.exec_())
