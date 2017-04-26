#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = tsTclntSS.py
__author__ = Hughe
__time__   = 2017-04-23 06:59
"""

from socket import *

HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)
"""
SS请求处理程序默认的行为是接受连接，获取请求，然后关闭连接

"""
while True:
    tcpCliSock=socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data=raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n'% data)
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()


if __name__ == '__main__':
    pass