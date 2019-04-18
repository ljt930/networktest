#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 19:22
# @Author  : Aries
# @Site    : 
# @File    : ConfigFileParserOper.py
# @Software: PyCharm


import ConfigParser
import sys

class myConfigParser(ConfigParser.ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr
    def write(self, fp):
        """Write an .ini-format representation of the configuration state."""
        if self._defaults:
            fp.write("[%s]\n" % ConfigParser.DEFAULTSECT)
            for (key, value) in self._defaults.items():
                fp.write("%s=%s\n" % (key, str(value).replace('\n', '\n\t')))
            fp.write("\n")
        for section in self._sections:
            fp.write("[%s]\n" % section)
            for (key, value) in self._sections[section].items():
                if key == "__name__":
                    continue
                if (value is not None) or (self._optcre == self.OPTCRE):
                    key = "=".join((key, str(value).replace('\n', '\n\t')))
                fp.write("%s\n" % (key))
            fp.write("\n")

class ReadConfig():
    def __init__(self):
        self.filePath = "./Servers.ini"
        self.config = myConfigParser()
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
            title = str(i)+"\\Title"
            command = str(i) + "\\Command"
            params = str(i) + "\\Params"
            workspace = str(i) + "\\Workspace"
            environment = str(i) + "\\Environment"
            autorestart = str(i) + "\\AutoRestart"
            starteddelay = str(i) + "\\StartedDelay"
            onlyone = str(i) + "\\OnlyOne"
            codecname = str(i)+"\\CodecName"
            filename = str(i)+"\\FileName"
            filepath = str(i)+"\\FilePath"

            opts = [title,command,params,workspace,environment,autorestart,starteddelay,onlyone,codecname,filename,filepath]

            for opt in opts :
                optValue = self.getServerOptValue(opt)

                sopt = opt.split("\\")[1]
                servercfg[sopt] = optValue
                if  sopt== "Title":
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
class WriteConfig():
    def __init__(self):
        self.filePath = "test.ini"
        self.config = myConfigParser()

        # try:
        #     self.config.add_section("Home")
        #     self.config.set("Home", "IP", "10.15.40.123")
        #     self.config.set("Home", "Mask", "255.255.255.0")
        #     self.config.set("Home", "Gateway", "10.15.40.1")
        #     self.config.set("Home", "DNS", "211.82.96.1")
        # except ConfigParser.DuplicateSectionError:
        #     print("Section 'Home' already exists")
        #
        # self.config.write(open(self.filePath,"w"))

    def add_section(self, section):
        self.config.add_section(section)

    def set(self,section, opt, value):
        try:
            self.config.set(section, opt,value)
        except :
            print("Section '%s' already exists") % (section)
        pass

    def writetoFile(self,file):
        fp = open(file,"w")
        self.config.write(fp)

if __name__ == '__main__':
    # rc = ReadConfig()
    # rc.getitems()
    # rc.getServerSize()
    # rc.createopt()
    # print rc.servers
    WriteConfig()
    import  json

    fp = open("test.json",'r')
    # print json.dumps({"a": "Runoob", 'b': 7}, indent=4, separators=(',', ': '))
    # jdata = '{\n    "a": \"Runoob",\n    "b": 7\n}'
    data = json.load(fp)
    print data["RTDB"]