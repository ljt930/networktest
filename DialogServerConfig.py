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
import TableWidgetOpera
# 修改默认编码为"utf-8"
default_encoding = "utf-8"
if (default_encoding != sys.getdefaultencoding()):
    reload(sys)
    sys.setdefaultencoding(default_encoding)

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class DialogServerArgs(QtGui.QDialog, Ui_DialogServerArgs):
    """b
    #方法二：先把ui文件转换成py文件。
    再通过继承 ui中的类Ui_MainWindow，直接初始化
    """

    def __init__(self):
        super(DialogServerArgs, self).__init__()
        self.setupUi(self)
        # self.TWOper =TableWidgetOpera.TableWidgetOpera(self,self.tableWidgetCfgArg,self.tableWidgetCfgNode)


        self.__initQdialogSetting()
        self.__initsinglbond()
        # self.__initwidget()

    def __initQdialogSetting(self):
        self.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
    # def getfileNode(self):
    #     self.servername = self.CDS.QString2PyString(self.servername).encode('utf-8')
        # self.node = self.FP.nodes[self.servername]
        # print self.node
    # def __initwidget(self):
    #     self.__initCfgArgTable()
    #     self.__initsinglbond()
    #     self.CDS = CfgDataStorage.CfgDataStorage()
    #     ###最后一行自适应
    #     self.tableWidgetCfgNode.horizontalHeader().setStretchLastSection(True)
    #     self.tableWidgetCfgArg.horizontalHeader().setStretchLastSection(True)
    #
    #     self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  ######允许右键产生子菜单
    #
    # def initDialogCfg(self,servername,nodes={}):
    #     servername = self.CDS.QString2PyString(servername).encode('utf-8')
    #     self.__showItemInTable(nodes, servername,True)
    #
    #     # self.tableWidgetCfgNode.setItemSelected(self.tableWidgetCfgNode.item(0,0),True)
    #
    def __initsinglbond(self):
        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self,
                     QtCore.SLOT("__DialogAccept()"))  # 确认或者OK按钮
        # self.customContextMenuRequested.connect(self.generateMenu)  ####右键菜单


        # self.connect(self, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT(""))
        # self.connect(self.tableWidgetCfgNode, QtCore.SIGNAL("itemSelectionChanged()"), self, QtCore.SLOT("__slotSelectChanged()"))
        # self.connect(self.tableWidgetCfgArg, QtCore.SIGNAL("itemSelectionChanged()"), self, QtCore.SLOT("__slotSelectChangedArg()"))
        # self.connect(self.tableWidgetCfgNode, QtCore.SIGNAL("currentCellChanged(int,int)"), self,
        #              QtCore.SLOT("on_tableWidget_currentCellChanged(int,int)"))
        # self.tableWidgetCfgNode.cellClicked()
        # self.tableWidgetCfgNode.currentItemChanged.connect(self.current_item_changed)
    #
    # def __initCfgArgTable(self):
    #
    #
    #     self.tableWidgetCfgArg.clear()
    #     self.tableWidgetCfgArg.setColumnCount(2)
    #     self.tableWidgetCfgArg.setRowCount(0)
    #
    #     item = QtGui.QTableWidgetItem()
    #     self.tableWidgetCfgArg.setHorizontalHeaderItem(0, item)
    #     item = QtGui.QTableWidgetItem()
    #     self.tableWidgetCfgArg.setHorizontalHeaderItem(1, item)
    #
    #     item = self.tableWidgetCfgArg.horizontalHeaderItem(0)
    #     item.setText(_translate("self", "配置节点名称", None))
    #     item = self.tableWidgetCfgArg.horizontalHeaderItem(1)
    #     item.setText(_translate("self", "参数名称", None))
    #
    # def __showItemInTable(self,nodes,nodename,isNodeTable=False):
    #     row = 0
    #     for key, values in nodes[nodename].items():
    #         # print key," : ",values
    #         if isNodeTable:
    #             widget = self.tableWidgetCfgNode
    #             self.CDS.createNodes(key, True, values)
    #         else:
    #             widget = self.tableWidgetCfgArg
    #         widget.setRowCount(row + 1)
    #         self.__CreateItemInTable(widget, row, key, values)
    #         row += 1
    #
    # def __CreateItemInTable(self, WidgetObj, row, name, value="defalut"):
    #     item = QtGui.QTableWidgetItem()
    #     item.setText(name)
    #     WidgetObj.setItem(row,0,item)
    #     item.setSelected(False)
    #
    #     if WidgetObj == self.tableWidgetCfgArg:
    #         item_1 = QtGui.QTableWidgetItem()
    #         item_1.setText(value)
    #         WidgetObj.setItem(row, 1, item_1)
    #         item_1.setSelected(False)
    #
    # def generateMenu(self, pos):
    #     print pos
    #     if self.widget_Node.geometry().contains(pos): #判断鼠标当前坐标是否在控件范围中
    #         WidgetObj = self.tableWidgetCfgNode
    #         print "in tableWidgetCfgNode"
    #     elif self.widget_Arg.geometry().contains(pos):
    #         WidgetObj = self.tableWidgetCfgArg
    #         print "in tableWidgetCfgArg"
    #     else:
    #         return
    #
    #     menu = QtGui.QMenu()
    #     item_add = menu.addAction(u"添加")
    #     item_del = menu.addAction(u"删除")
    #
    #     # item_edit = menu.addAction(u"修改")
    #     action = menu.exec_(self.mapToGlobal(pos))
    #
    #     # for i in self.tableWidgetCfgNode.selectionModel().selection().indexes():
    #     #     row_num = i.row()
    #     #     print row_num
    #
    #     rows = WidgetObj.rowCount()
    #     if action == item_add:
    #         isexist = self.CDS.isexistname(WidgetObj,u"默认值")
    #         if isexist == 1 :
    #             return
    #         WidgetObj.setRowCount(rows + 1)
    #         self.__CreateItemInTable(WidgetObj, rows, u"默认值")
    #
    #         if WidgetObj == self.tableWidgetCfgNode:
    #             self.__initCfgArgTable()
    #
    #     elif action == item_del:
    #         WidgetObj.removeRow(rows-1)
    #
    #         print u'您选了删除，当前行数是：', rows
    #     # elif action == item_edit:
    #     #
    #     #     print u'您选了修改，当前行内容是：', WidgetObj.item(row_num,0).text()
    #     #     WidgetObj.item(row_num, 0).setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
    #     else:
    #         return
    #
    # def msgboxWarning(self,ret):
    #
    #     if ret == -1:
    #         msg = u"updata nodes is failed,nodename 重复"
    #     elif ret == -2:
    #         msg = u"updata arg is failed,argname 重复"
    #     elif ret == -3:
    #         msg = u"updata arg is failed,参数不全"
    #     else:
    #         print u"updata nodes is success"
    #         return
    #
    #     QtGui.QMessageBox.warning(self,"警告",msg,QtGui.QMessageBox.Ok)
    #
    # @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    # def __slotSelectChanged(self):
    #     # self.tableWidgetCfgNode.se
    #     self.__initCfgArgTable()
    #     nodenamesqtr= self.tableWidgetCfgNode.currentItem().text()
    #     nodename = self.CDS.QString2PyString(nodenamesqtr)
    #
    #     isexistNode = self.CDS.isexistname(self.tableWidgetCfgNode, nodename)
    #     if isexistNode == 2:
    #         row = self.tableWidgetCfgNode.row(self.tableWidgetCfgNode.currentItem())
    #         self.tableWidgetCfgNode.removeRow(row)
    #         return
    #     nodes = self.CDS.getNodes()
    #     if nodes.has_key(nodename):
    #         print nodes[nodename]
    #         self.__showItemInTable(nodes,nodename)
    #
    #     else:
    #         # print "NULL"
    #         if nodename == u"默认值":
    #             return
    #         ret =self.CDS.createNodes(nodename, True, {})
    #         self.msgboxWarning(ret)
    #
    # @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    # def __slotSelectChangedArg(self):
    #     # self.tableWidgetCfgNode.se
    #     item = self.tableWidgetCfgNode.currentItem()
    #     if item == None:
    #         return
    #     nodename = self.CDS.QString2PyString(self.tableWidgetCfgNode.currentItem().text())
    #     argname = self.tableWidgetCfgArg.currentItem().text()
    #     print "slotSelectChangedArg:",argname
    #
    #     isexistArg = self.CDS.isexistname(self.tableWidgetCfgArg, argname)
    #     if isexistArg == 2:
    #         self.tableWidgetCfgArg.removeRow(self.tableWidgetCfgArg.row(self.tableWidgetCfgArg.currentItem()))
    #         return
    #
    #     ret = self.CDS.createAgrs(self.tableWidgetCfgArg, nodename, True)
    #     self.msgboxWarning(ret)



    @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __DialogAccept(self):
        print self.TWOper.CDS.getNodes()
        # self.emit(QtCore.SIGNAL("save_data_dict(PyQt_PyObject)"), self.CDS.getNodes())
        self.emit(QtCore.SIGNAL("save_data_dict(PyQt_PyObject)"),self.TWOper.CDS.nodes)

    def setTWOper(self,TWOpe):
        self.TWOper = TWOpe
    def delTWOper(self):
        del self.TWOper

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = DialogServerArgs()

    TWOper = TableWidgetOpera.TableWidgetOpera(window)
    # window.customContextMenuRequested.connect(TWOper.generateMenu)  ####右键菜单
    window.show()
    sys.exit(app.exec_())