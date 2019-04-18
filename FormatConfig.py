#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 0:31
# @Author  : Aries
# @Site    : 
# @File    : FormatConfig.py
# @Software: PyCharm

import re
import ConfigFileParserOper
import CharactersConversion
import json


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
             "RTDBServer":RTDBServer}
nodes = {"RTDBServer":nodesDict}

class FormatConfig():
    def __init__(self):
        # self.coding = ""
        # self.servername= ""

        self.m_Size = 0
        self.nodesDict = {}
        self.CC = CharactersConversion.CharactersConversion()
        self.WC = ConfigFileParserOper.WriteConfig()

    def FormatSettingConfig(self,dconfig,types="server",filename="test.ini"):

        # print dconfig
        ServerCfgList = dconfig["records"]
        LocalCfgDict = dconfig["localConfig"]
        # self.m_Size = len(ServerCfgList)

        print LocalCfgDict
        self.WC.add_section("server")
        self.WC.set("server", "size", 0)
        i = 1
        for ServerCfg in ServerCfgList:
            isEnable = self.CC.StrToBool(ServerCfg["isEnable"])
            if not isEnable:
                continue
            Title = ServerCfg["title"]
            self.__setOption(i,"Title",Title)

            # serviceType = ServerCfg["serviceType"]

            Command = ServerCfg["path"]
            self.__setOption(i, "Command", Command)

            Params = self.__formatparms(ServerCfg,types,Title,LocalCfgDict)
            self.__setOption(i, "Params", Params)

            Workspace = ServerCfg["workDir"]
            self.__setOption(i, "Workspace", Workspace)
            Environment = ServerCfg["environment"]
            self.__setOption(i, "Environment", Environment)
            AutoRestart = ServerCfg["autoStart"]
            self.__setOption(i, "AutoRestart", AutoRestart)
            StartedDelay = ServerCfg["StartedDelay"]
            self.__setOption(i, "StartedDelay", StartedDelay)
            OnlyOne = ServerCfg["single"]
            self.__setOption(i, "OnlyOne", OnlyOne)
            CodecName = ""
            self.__setOption(i, "CodecName", CodecName)
            FileName = ""
            self.__setOption(i, "FileName", FileName)
            FilePath =""
            self.__setOption(i, "FilePath", FilePath)
            i +=1
        self.WC.set("server", "size", i-1)
        self.WriteConfig(filename) #写文件
    def __formatparms(self,servercfg,types,Title,localcfg,isConfig=True):
        localnodelist = ["CommonConfig","RTDB","DataBase"]
        lparams = {}
        for node in localnodelist:
            # 按列表重新生产需要的本地配置参数
            lparams[node] = localcfg[node]

        lparams.update(eval(servercfg["josnStartParam"])) #把服务param更新到本地配置param字典中

        if isConfig: #Params有两种格式，默认配置文件中的格式
            Params = self.__creatConfigParam(servercfg["serviceType"], types, Title, lparams)
            # _params = json.dumps(lparams, sort_keys=True, indent=4, separators=(',', ': ')) #序列化lparams
            #
            # Params = "\"%s#NEXT#%s#NEXT#%s#NEXT#%s\"" % (servercfg["serviceType"], types, Title, json.dumps(_params)) #拼接字符串，需再次序列化_params
        else:
            Params =self.__creatSriptParam(servercfg["serviceType"], types, Title, lparams)
        del lparams

        return Params
    def __creatConfigParam(self,serType,types,Title, _params):
        # 序列化lparams
        _params = json.dumps(_params, sort_keys=True, indent=4)
        # 强制不转义\n
        _params = _params.replace("\n",r"\n")
        # 拼接字符串
        Params = "\"%s#NEXT#%s#NEXT#%s#NEXT#%s\\n\"" % (serType, types, Title, _params)
        return Params

    def __creatSriptParam(self, serType, types, Title, _params):
        _params = json.dumps(_params)
        Params = "%s %s %s %s" % (serType, types, Title, json.dumps(_params))
        return Params

    def __setOption(self,i , name, value):

        opt = "%d\\%s"%(i,name) #组合配置文件中的opt
        self.WC.set("server", opt, value) #设置参数


    def WriteConfig(self,file):
        self.WC.writetoFile(file)

    def SriptToConfig_Arg(self,strarg):

        try:
            arglist = strarg.split()
            # 去掉前后字符“”
            _params = arglist[3][1:-1]
            # 配合__creatConfigParam 先反序列化一次
            _params = json.loads(_params)
            Params = self.__creatConfigParam(arglist[0], arglist[1], arglist[2], _params)
        except:
            Params ="format-invalid"
        return Params

    def ConfigToSript_Arg(self, strarg):

        try:
            # 先去掉前后字符
            strarg = strarg[1:-1]
            # 按#NEXT#分割字符串“”
            arglist = strarg.split("#NEXT#")
            # 配合__creatConfigParam 先反序列化一次
            _params = json.loads(arglist[3])
            Params = self.__creatSriptParam(arglist[0], arglist[1], arglist[2],_params)
        except:
            Params = "format-invalid"
        return Params



if __name__ == '__main__':





    s = '"RTDBServer#NEXT#client#NEXT#RTDBServerService#NEXT#{\n    "RTDB": {\n        "ip": "127.0.0.1", \n        "localCoding": "client", \n        "localName": "client", \n        "localType": "client", \n        "port": "6379"\n    }, \n    "RTDBServer": {\n        "centerIP": "10.7.3.108", \n        "centerPort": "6379", \n        "localStationNum": "0"\n    }\n}\n"'

    P = FormatConfig().ConfigToSript_Arg(s)
    print P


    pass