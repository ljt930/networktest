#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 13:04
# @Author  : Aries
# @Site    : 
# @File    : CfgDataStorage.py
# @Software: PyCharm
import CharactersConversion

class CfgDataStorage(object):

    def __init__(self):
        self.conver = CharactersConversion.CharactersConversion()
        self.nodes = {}
        pass

    def QString2PyString(self,qStr):
        return self.conver.QString2PyString(qStr)
    def getNodes(self):
        return self.nodes

    def createAgrs(self, WidgetObj, nodename, isupdata=False):
        arg = {}
        # nodename = self.conver.QString2PyString(nodenameqstr)
        _rows = WidgetObj.rowCount()
        if _rows > 0:
            for row in range(0, _rows):
                item_0 = WidgetObj.item(row, 0)
                item_1 = WidgetObj.item(row, 1)
                if item_0 !=None:
                    argname = self.conver.QString2PyString(WidgetObj.item(row, 0).text())
                else:
                    break
                if arg.has_key(argname):
                    return -2

                if item_1 !=None:
                    argvalue = self.conver.QString2PyString(WidgetObj.item(row, 1).text())
                else:
                    argvalue = "default"

                # print "argname is %s,argvalue is %s"%(argname,argvalue)
                arg[argname] = argvalue
        return self.createNodes(nodename, isupdata, arg)

    def createNodes(self, nodename, isupdata, arg):
        if isupdata :
            self.nodes[nodename] = arg
            print self.nodes
            return 0
        if self.nodes.has_key(nodename):
            return -1
        self.nodes[nodename] = arg
        # print "%s is %s"%(nodename,self.nodes)
        return 0

    def isexistname(self,WidgetObj,name):
        rows = WidgetObj.rowCount()
        i = 0
        for row in range(0,rows):
            if WidgetObj.item(row,0).text() == name:
                i+=1
        return i
