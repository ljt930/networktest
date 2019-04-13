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
        self.__initCfgArgTable()
        self.__initsinglbond()
        ###最后一行自适应
        self.tableWidgetCfgNode.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetCfgArg.horizontalHeader().setStretchLastSection(True)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)  ######允许右键产生子菜单



        self.params=""

        self.nodes = {}
    def __initsinglbond(self):
        self.customContextMenuRequested.connect(self.generateMenu)  ####右键菜单

        self.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self,
                     QtCore.SLOT("__DialogAccept()"))  # 确认或者OK按钮
        # self.connect(self, QtCore.SIGNAL("clicked()"), self, QtCore.SLOT(""))
        self.connect(self.tableWidgetCfgNode, QtCore.SIGNAL("itemSelectionChanged()"), self, QtCore.SLOT("__slotSelectChanged()"))
        self.connect(self.tableWidgetCfgArg, QtCore.SIGNAL("itemSelectionChanged()"), self,
                     QtCore.SLOT("__slotSelectChangedArg()"))
        # self.connect(self.tableWidgetCfgNode, QtCore.SIGNAL("currentCellChanged(int,int)"), self,
        #              QtCore.SLOT("on_tableWidget_currentCellChanged(int,int)"))
        # self.tableWidgetCfgNode.cellClicked()
        # self.tableWidgetCfgNode.currentItemChanged.connect(self.current_item_changed)

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


    def QString2PyString(self, qStr):
        # # QString，如果内容是中文，则直接使用会有问题，要转换成 python string
        return unicode(qStr.toUtf8(), 'utf-8', 'ignore')

    def StoredParams(self):
        print self.params
    def __keepNodes(self,nodename,arg,isupdata):
        if isupdata :
            self.nodes[nodename] = arg
            print self.nodes
            return 0
        if self.nodes.has_key(nodename):
            return -1
        self.nodes[nodename] = arg
        # print "%s is %s"%(nodename,self.nodes)
        return 0

    def __keepAgrs(self,nodenameqstr,isupdata=False):
        arg = {}
        nodename = self.QString2PyString(nodenameqstr)
        _rows = self.tableWidgetCfgArg.rowCount()
        if _rows > 0:

            for row in range(0, _rows):
                item_0 = self.tableWidgetCfgArg.item(row, 0)
                item_1 = self.tableWidgetCfgArg.item(row, 1)
                if item_0 ==None:
                    return -3
                if item_1 ==None:
                    return -3
                argname = self.QString2PyString(self.tableWidgetCfgArg.item(row, 0).text())
                argvalue = self.QString2PyString(self.tableWidgetCfgArg.item(row, 1).text())
                # print "argname is %s,argvalue is %s"%(argname,argvalue)
                if arg.has_key(argname):
                    return -2
                arg[argname] = argvalue

        return self.__keepNodes(nodename,arg,isupdata)



    def ItemInTable(self,WidgetObj,row,name,value="mrz"):
        item = QtGui.QTableWidgetItem()
        item.setText(name)
        WidgetObj.setItem(row,0,item)
        item.setSelected(False)

        if WidgetObj == self.tableWidgetCfgArg:
            item_1 = QtGui.QTableWidgetItem()
            item_1.setText(value)
            WidgetObj.setItem(row, 1, item_1)
            item_1.setSelected(False)

    def generateMenu(self,pos):
        print pos
        if self.widget_Node.geometry().contains(pos): #判断鼠标当前坐标是否在控件范围中
            WidgetObj = self.tableWidgetCfgNode
            print "in tableWidgetCfgNode"
        elif self.widget_Arg.geometry().contains(pos):
            WidgetObj = self.tableWidgetCfgArg
            print "in tableWidgetCfgArg"
        else:
            return

        menu = QtGui.QMenu()
        item_add = menu.addAction(u"添加")
        item_del = menu.addAction(u"删除")

        # item_edit = menu.addAction(u"修改")
        action = menu.exec_(self.mapToGlobal(pos))

        # for i in self.tableWidgetCfgNode.selectionModel().selection().indexes():
        #     row_num = i.row()
        #     print row_num

        rows = WidgetObj.rowCount()
        if action == item_add:
            isexist = self.__isexistname(WidgetObj,u"默认值")
            if isexist == 1 :
                return
            WidgetObj.setRowCount(rows + 1)
            self.ItemInTable(WidgetObj, rows, u"默认值")

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
    def __isexistname(self,WidgetObj,name):
        rows = WidgetObj.rowCount()
        i = 0
        for row in range(0,rows):
            if WidgetObj.item(row,0).text() == name:
                i+=1

        return i

    @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __slotSelectChanged(self):
        # self.tableWidgetCfgNode.se
        self.__initCfgArgTable()
        nodename= self.QString2PyString(self.tableWidgetCfgNode.currentItem().text())
        isexist = self.__isexistname(self.tableWidgetCfgNode, nodename)
        if isexist == 2:
            row = self.tableWidgetCfgNode.row(self.tableWidgetCfgNode.currentItem())
            self.tableWidgetCfgNode.removeRow(row)
            return
        if self.nodes.has_key(nodename):
            print self.nodes[nodename]
            row = 0
            for key, values in self.nodes[nodename].items():
                print key," : ",values
                self.tableWidgetCfgArg.setRowCount(row + 1)
                self.ItemInTable(self.tableWidgetCfgArg,row,key,values)
                row+=1

        else:
            print "NULL"

    @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __slotSelectChangedArg(self):
        # self.tableWidgetCfgNode.se
        item = self.tableWidgetCfgNode.currentItem()
        if item == None:
            return
        nodename = self.tableWidgetCfgNode.currentItem().text()
        argname = self.tableWidgetCfgArg.currentItem().text()
        print "slotSelectChangedArg:",argname
        isexist = self.__isexistname(self.tableWidgetCfgArg, argname)
        if isexist == 2:
            self.tableWidgetCfgArg.removeRow(self.tableWidgetCfgArg.row(self.tableWidgetCfgArg.currentItem()))
            return
        res = self.__keepAgrs(nodename, True)
        if res == -1:
            print "updata nodes is failed,nodename 重复"
        elif res == -2:
            print "updata nodes is failed,argname 重复"
        elif res == -3:
            print "updata nodes is failed,参数不全"
        else:
            print "updata nodes is success"


    @QtCore.pyqtSlot()  # 需要使用装饰器@QtCore.pyqtSlot()，把函数声明为槽函数
    def __DialogAccept(self):
        print self.nodes


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = DialogServerArgs()
    window.show()
    sys.exit(app.exec_())