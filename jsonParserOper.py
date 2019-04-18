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
    def jsonloads(self,strdata):
        return json.loads(strdata)
    def jsondumps(self, dictdata, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        encoding='utf-8', default=None, sort_keys=False, **kw):

        return json.dumps(dictdata, skipkeys, ensure_ascii, check_circular,
        allow_nan, cls, indent, separators,
        encoding, default, sort_keys, **kw)

    def jsondump(self,obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        encoding='utf-8', default=None, sort_keys=False, **kw):

        return json.dump(obj, fp, skipkeys, ensure_ascii, check_circular,
        allow_nan, cls, indent, separators,
        encoding, default, sort_keys, **kw)

    def getjsondict(self,filepath):
        if self.loadfile(filepath):
            return self.jsondict
        else:
            return 0

if __name__ == '__main__':
    jo = jsonOper()
    jo.getjsondict("jsonstrBaseStartupParam.json")
    s = json.dumps(str({"WFServer":{"port":"5555"}}), indent=4)
    print s