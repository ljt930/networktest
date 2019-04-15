#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 12:57
# @Author  : Aries
# @Site    : 
# @File    : CharactersConversion.py
# @Software: PyCharm

class CharactersConversion():
    def QString2PyString(self, qStr):
        # # QString，如果内容是中文，则直接使用会有问题，要转换成 python string
        # print type(qStr)
        return unicode(qStr.toUtf8(), 'utf-8', 'ignore')


if __name__ == '__main__':
    b =False