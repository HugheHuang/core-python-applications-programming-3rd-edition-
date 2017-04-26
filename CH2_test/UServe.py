#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = UServe.py
__author__ = Hughe
__time__   = 2017-04-23 16:30
"""
#test 2-6
from socket import *
from time import ctime
import re
HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpServ=socket(AF_INET,SOCK_DGRAM)
udpServ.bind(ADDR)

while True:
    print 'waiting for message... '
    data,addr=udpServ.recvfrom(BUFSIZ)
    try:
        portNum=getservbyname(data)
        udpServ.sendto('%s is %d'%(data,portNum),addr)
    except:
        udpServ.sendto('%s is not found'%data,addr)
    else:
        print 'receive address is ',addr

udpServ.close()

if __name__ == '__main__':
    pass