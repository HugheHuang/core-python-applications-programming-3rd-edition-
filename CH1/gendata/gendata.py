#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    > File Name: gendata.py
    > Author: Hughe
    > Created Time: 2017年04月20日 星期四 22时13分22秒
    > Mail:1044829783@qq.com
"""

"""
为正则表达式创建随机数据，并输出屏幕
py3 print->print() xrange()->range() sys.maxint->sys.maxsize
"""

from random import randrange,choice
from string import ascii_lowercase as lc
#from sys import maxint
from time import ctime


tlds=('com','edu','net','org','gov')



def getAStr():
    for i in xrange(randrange(5,11)):
        adtint = randrange(2**32)
        adtstr = ctime(adtint)
        allen = randrange(4,8)
        alogin = ''.join(choice(lc) for j in range(allen))
        adlen = randrange(allen,13)
        adom = ''.join(choice(lc) for j in xrange(adlen))
        print '%s::%s@%s.%s::%d-%d-%d' % (adtstr,alogin,adom
            ,choice(tlds),adtint,allen,adlen)
        
def strToFile():
    f=open('redata.txt','w+')
    for i in xrange(randrange(5,11)):
        adtint = randrange(2**32)
        adtstr = ctime(adtint)
        allen = randrange(4,8)
        alogin = ''.join(choice(lc) for j in range(allen))
        adlen = randrange(allen,13)
        adom = ''.join(choice(lc) for j in xrange(adlen))
        f.writelines('%s::%s@%s.%s::%d-%d-%d\r\n' % (adtstr,alogin,adom
            ,choice(tlds),adtint,allen,adlen))
    
    f.close()



