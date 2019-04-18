#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 16:06
# @Author  : Aries
# @Site    : 
# @File    : TableWidgetOpera.py
# @Software: PyCharm

from PyQt4 import QtCore, QtGui
import CfgDataStorage
import json
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class TableWidgetOpera(QtGui.QDialog):

    def __init__(self,parent,islocal=False,topparent=None):

        # self = parent
        super(TableWidgetOpera, self).__init__()
        self.parent = parent
        if islocal:
            self.tableWidgetCfgNode = topparent.tableWidgetLocaleCfgNode
            self.tableWidgetCfgArg = topparent.tableWidgetLocaleCfgArg
        else:
            self.tableWidgetCfgNode = parent.tableWidgetCfgNode
            self.tableWidgetCfgArg = parent.tableWidgetCfgArg
        self.__initwidget()


    def __initwidget(self):
        self.__initCfgArgTable()
        self.__initsinglbond()
        self.CDS = CfgDataStorage.CfgDataStorage()
        ###最后一行自适应
        self.tableWidgetCfgNode.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetCfgArg.horizontalHeader().setStretchLastSection(True)

        self.parent.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  ######允许右键产生子菜单

        self.tableWidgetCfgArg.verticalHeader().setHidden(True)

    def initDialogCfg(self,servername,nodes={}):
        if type(servername) != str:
            servername = self.CDS.QString2PyString(servername).encode('utf-8')

        self.__showItemInTable(nodes, servername,True)

        # self.tableWidgetCfgNode.setItemSelected(self.tableWidgetCfgNode.item(0,0),True)

    def __initsinglbond(self):
        # print self
        # print self.parent
        self.parent.customContextMenuRequested.connect(self.generateMenu)  ####右键菜单
        # self.connect(self.parent, QtCore.SIGNAL("customContextMenuRequested()"), self, QtCore.SLOT("generateMenu()"))
        # self.connect(self, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT(""))
        self.connect(self.tableWidgetCfgNode, QtCore.SIGNAL("itemSelectionChanged()"), self, QtCore.SLOT("__slotSelectChanged()"))
        self.connect(self.tableWidgetCfgArg, QtCore.SIGNAL("itemSelectionChanged()"), self,
                     QtCore.SLOT("__slotSelectChangedArg()"))
        # self.connect(self.tableWidgetCfgNode, QtCore.SIGNAL("currentCellChanged(int,int)"), self,
        #              QtCore.SLOT("on_tableWidget_currentCellChanged(int,int)"))


    def __initCfgArgTable(self):


        self.tableWidgetCfgArg.clear()
        self.tableWidgetCfgArg.setColumnCount(2)
        self.tableWidgetCfgArg.setRowCount(0)

        item = QtGui.QTableWidgetItem()
        self.tableWidgetCfgArg.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetCfgArg.setHorizontalHeaderItem(1, item)

        item = self.tableWidgetCfgArg.horizontalHeaderItem(0)
        item.setText(_translate("self", "配置节点名称", None))
        item = self.tableWidgetCfgArg.horizontalHeaderItem(1)
        item.setText(_translate("self", "参数名称", None))

    def __showItemInTable(self,nodedicts,nodename,isNodeTable=False):
        row = 0
        # if type(nodes[nodename]) != dict:
        #     nodecfg = self.CDS.QString2PyString(nodes[nodename]).encode('utf-8')
        #     nodecfg = json.loads(nodecfg)
        #     print nodecfg
        # else:
        #     nodecfg = nodes[nodename]
        parmdict = nodedicts[nodename]
        keys = parmdict.items()
        keys.sort()

        for key ,values in keys:
            # print key," : ",values
            if isNodeTable:

                widget = self.tableWidgetCfgNode
                self.CDS.createNodes(key, True, values)
            else:
                widget = self.tableWidgetCfgArg
            widget.setRowCount(row + 1)
            self.__CreateItemInTable(widget, row, key, values)
            row += 1

    def __CreateItemInTable(self, WidgetObj, row, name, value="defalut"):
        item = QtGui.QTableWidgetItem()
        item.setText(name)
        WidgetObj.setItem(row,0,item)
        item.setSelected(False)

        if WidgetObj == self.tableWidgetCfgArg:
            item_1 = QtGui.QTableWidgetItem()
            item_1.setText(value)
            WidgetObj.setItem(row, 1, item_1)
            item_1.setSelected(False)

    # @QtCore.pyqtSlot()
    def generateMenu(self, pos):
        print pos
        print self.tableWidgetCfgNode.geometry()
        if self.tableWidgetCfgNode.geometry().contains(pos): #判断鼠标当前坐标是否在控件范围中
            WidgetObj = self.tableWidgetCfgNode
            print "in tableWidgetCfgNode"
        elif self.tableWidgetCfgArg.geometry().contains(pos):
            WidgetObj = self.tableWidgetCfgArg
            print "in tableWidgetCfgArg"
        else:
            return

        menu = QtGui.QMenu()
        item_add = menu.addAction(u"添加")
        item_del = menu.addAction(u"删除")

        # item_edit = menu.addAction(u"修改")
        action = menu.exec_(self.parent.mapToGlobal(pos))

        # for i in self.tableWidgetCfgNode.selectionModel().selection().indexes():
        #     row_num = i.row()
        #     print row_num

        rows = WidgetObj.rowCount()
        if action == item_add:
            isexist = self.CDS.isexistname(WidgetObj,u"默认值")
            if isexist == 1 :
                return
            WidgetObj.setRowCount(rows + 1)
            self.__CreateItemInTable(WidgetObj, rows, u"默认值")

            if WidgetObj == self.tableWidgetCfgNode:
                self.__initCfgArgTable()

        elif action == item_del:
            WidgetObj.removeRow(rows-1)

            print u'您选了删除，当前行数是：', rows
        # elif action == item_edit:
        #
        #     print u'您选了修改，当前行内容是：', WidgetObj.item(row_num,0).text()
        #     WidgetObj.item(row_num, 0).setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
        else:
            return

    def msgboxWarning(self,ret):

        if ret == -1:
            msg = u"updata nodes is failed,nodename 重复"
        elif ret == -2:
            msg = u"updata arg is failed,argname 重复"
        elif ret == -3:
            msg = u"updata arg is failed,参数不全"
        else:
            print u"updata nodes is success"
            return

        QtGui.QMessageBox.warning(self.parent,"警告",msg,QtGui.QMessageBox.Ok)

    @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __slotSelectChanged(self):
        # self.tableWidgetCfgNode.se
        self.__initCfgArgTable()
        nodenamesqtr= self.tableWidgetCfgNode.currentItem().text()
        nodename = self.CDS.QString2PyString(nodenamesqtr)

        isexistNode = self.CDS.isexistname(self.tableWidgetCfgNode, nodename)
        if isexistNode == 2:
            row = self.tableWidgetCfgNode.row(self.tableWidgetCfgNode.currentItem())
            self.tableWidgetCfgNode.removeRow(row)
            return
        nodes = self.CDS.getNodes()
        if nodes.has_key(nodename):
            # print nodes[nodename]
            self.__showItemInTable(nodes,nodename)

        else:
            # print "NULL"
            if nodename == u"默认值":
                return
            ret =self.CDS.createNodes(nodename, True, {})
            self.msgboxWarning(ret)

    @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __slotSelectChangedArg(self):
        # self.tableWidgetCfgNode.se
        item = self.tableWidgetCfgNode.currentItem()
        if item == None:
            return
        nodename = self.CDS.QString2PyString(self.tableWidgetCfgNode.currentItem().text())
        argname = self.tableWidgetCfgArg.currentItem().text()
        print "slotSelectChangedArg:",argname

        isexistArg = self.CDS.isexistname(self.tableWidgetCfgArg, argname)
        if isexistArg == 2:
            self.tableWidgetCfgArg.removeRow(self.tableWidgetCfgArg.row(self.tableWidgetCfgArg.currentItem()))
            return

        ret = self.CDS.createAgrs(self.tableWidgetCfgArg, nodename, True)
        self.msgboxWarning(ret)
