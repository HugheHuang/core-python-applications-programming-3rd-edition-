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
"""
host空白的是对bind()的标识，标识可以使用任何地址
随机端口号
缓冲区大小
地址->(主机，端口号)
bind() 绑定地址
listen(监听数)开启监听
"""
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
        tcpCliSock.send('[%s] %s' % (ctime(),data))

    tcpCliSock.close()


if __name__ == '__main__':
    main()