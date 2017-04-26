#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = tsTserv.py
__author__ = Hughe
__time__   = 2017-04-22 19:13
"""

from socket import *
from time import ctime
import threading
import os

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
def main():
    while True:
        print 'waiting for connection ...'
        tcpCliSock,addr=tcpSerSock.accept()
        print '...connected from:', addr
        createp(tcpCliSock)
    tcpSerSock.close()
#创建新线程
def createp(tcpCliSock):
    thread = threading.Thread(target=display,args=(tcpCliSock,))
    thread.setDaemon(True)
    thread.start()
#线程运行内容
def display(tcpCliSock):


    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        if data == 'os':
            tcpCliSock.send('[%s] [%s] ' % (ctime(),os.name))
        elif data == 'time' or data=='date':
            tcpCliSock.send('%s' % (ctime()))
        elif data == 'ls':
            tcpCliSock.send('[%s] \n %s ' % (ctime(), os.curdir))

        else:
            tcpCliSock.send('[%s] %s' % (ctime(), data))

    tcpCliSock.close()


if __name__ == '__main__':
    main()