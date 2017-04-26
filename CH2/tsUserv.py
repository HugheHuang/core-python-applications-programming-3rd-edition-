#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = tsUserv.py
__author__ = Hughe
__time__   = 2017-04-22 21:48
"""

from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)
"""
无连接，不需要监听
"""
udpSerSock=socket(AF_INET,SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message ...'
    data,addr=udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (ctime(),data),addr)
    print '...received from and return to:',addr
udpSerSock.close()


if __name__ == '__main__':
    pass