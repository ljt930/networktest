#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 11:16
# @Author  : Aries
# @Site    : 
# @File    : jsonParserOper.py
# @Software: PyCharm

import json

class jsonOper():
    def __init__(self):

        self.filepath = "test.json"

    def loadfile(self,filepath):
        try :
            fp = open(filepath,"r")
            self.jsondict = json.load(fp)
            fp.close()
        except IOError,e:
            print e
            return 0
        return 1

    def getjsondict(self,filepath):
        if self.loadfile(filepath):
            return self.jsondict
        else:
            return 0

if __name__ == '__main__':
    jo = jsonOper()
    jo.getjsondict()