#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 19:22
# @Author  : Aries
# @Site    : 
# @File    : ConfigFileParserOper.py
# @Software: PyCharm


import ConfigParser
import sys

class ReadConfig():
    def __init__(self):
        self.filePath = "./Servers.ini"
        self.config = ConfigParser.ConfigParser()
        self.__isfileexit()

        self.servercfg = {}
        self.servers = {}
    def __isfileexit(self):

        try:
            fp = open(self.filePath)
            fp.close()
            self.__readfiel()
        except IOError , arg:
            print arg
    def __readfiel(self):

        self.config.read(self.filePath)
        self.sections = self.config.sections()
        print 'all sections:', self.sections

    def getoptions(self):
        for section in self.sections:
            otps = self.config.options(section)
            print "%s is: %s"%(section,otps)

    def getitems(self):
        items = self.config.items("servers")
        for item in items:
            print item

    def getServerSize(self):
        self.serversize = self.config.get("servers","size")
        print self.serversize
        return self.serversize
    def createopt(self):
        size = int(self.serversize)
        titlename =""
        i=1
        while i < size+1:
            servercfg ={}
            title = str(i)+"\\title"
            command = str(i) + "\\command"
            params = str(i) + "\\params"
            workspace = str(i) + "\\workspace"
            environment = str(i) + "\\environment"
            autorestart = str(i) + "\\autorestart"
            starteddelay = str(i) + "\\starteddelay"
            onlyone = str(i) + "\\onlyone"
            codecname = str(i)+"\\codecname"
            filename = str(i)+"\\filename"
            filepath = str(i)+"\\filepath"

            opts = [title,command,params,workspace,environment,autorestart,starteddelay,onlyone,codecname,filename,filepath]

            for opt in opts :
                optValue = self.getServerOptValue(opt)

                sopt = opt.split("\\")[1]
                servercfg[sopt] = optValue
                if  sopt== "title":
                    titlename = optValue
            if titlename != "":
                self.servers[titlename] = servercfg

            i +=1

    def getServerOptValue(self,opt):
        try:
            _optValue = self.config.get("servers",opt)
        except Exception as e:
            print e
            _optValue = ""

        print "%s is : %s"%(opt,_optValue)
        return _optValue


if __name__ == '__main__':
    rc = ReadConfig()
    # rc.getitems()
    # rc.getServerSize()
    rc.createopt()
    print rc.servers
