#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 0:31
# @Author  : Aries
# @Site    : 
# @File    : FormatParams.py
# @Software: PyCharm



Params = ""

CommonConfig = {"AutoCancelForceDWTimeout":"1",
                "AutoLogoutTimeout":"0",
                "DelayToSendRFID":"3000",
                "IsAllowRFIDRepeat":"0",
                "IsAutoSelectKey":"0",
                "IsCheckKeyOnSeat":"1",
                "IsContinueUseOnlineKey":"1"}
RTDB = {"ip":"127.0.0.1",
        "localCoding":"28D2440228C80000",
        "localName":"client",
        "localType":"client",
        "port":"6379"}
RTDBServer = {"DBIP":"10.7.3.10",
              "DBName":"gzpw",
              "DBPort":"3306",
              "DBPsw":"A92364CBF6D4EA6B0A31CE4C3BDBE8BE",
              "DBUID":"root",
              "centerIP":"10.7.3.10",
              "centerPort":"6379",
              "isSyncTicket":"0",
              "isSyncYK":"0",
              "isUpdateGK":"1",
              "localStationNum":"1"}

nodesDict = {"CommonConfig":CommonConfig,
             "RTDB":RTDB,
             "RTDBServer":RTDBServer,
             "text":"11111111111"}


class FormatParam():
    def __init__(self):
        self.coding = "28D2440228C80000"
        self.servername= "RTDBServer"

        #self.argsDict = {"a": "11", "b": "22"}
        #self.argsDict2 = {"abc": "11bc", "bdef": "22ddff"}

        # self.nodesDict = {"serverone": self.argsDict, "servertow": self.argsDict2}
        self.nodesDict = {}
        pass
    def setNodesDict(self,nodesDict):
        self.nodesDict = nodesDict

    def getParamStr(self):
        return self.__FormatParamStr()

    def __FormatArgsStr(self, argsDict):
        if type(argsDict) is not dict:
            return ""
        names = argsDict.keys()
        argStr = ",".join( "\\n\\t\\t\\\""+ name +"\\\" : \\\"" + argsDict[name] +"\\\"" for name in names)
        #print argStr
        return argStr

    def __FormatNodeArgsStr(self):
        ###需要增加判断self.nodesDic
        if type(self.nodesDict) is not dict:
            return ""
        nodes = self.nodesDict.keys()

        # nodeargsStr = ",".join( "\\n\\t\\\"" + node +"\\\" : \\n\\t{" + self.__FormatArgsStr(self.nodesDict[node]) + "\\n\\t}" for node in nodes)
        nodeargsStr = ",".join(self.__FormatNodeStr(node) for node in nodes)
        #print nodesStr
        return nodeargsStr

    def __FormatNodeStr(self,node):
        return "\\n\\t\\\"" + node +"\\\" : \\n\\t{" + self.__FormatArgsStr(self.nodesDict[node]) + "\\n\\t}"

    def __FormatParamStr(self):
        nodesStr = self.__FormatNodeArgsStr()

        param = "\""+self.servername+"#NEXT#"+self.coding+"#NEXT#"+self.servername+"Service#NEXT#{"+nodesStr+"\\n}\\n\""
        return param

if __name__ == '__main__':
    #nodesDict = {"serverone": "xxxxxxxxxxx", "servertow": "zzzzzzzzzzzzzz"}
    fc = FormatParam()
    fc.setNodesDict(nodesDict)
    print fc.getParamStr()