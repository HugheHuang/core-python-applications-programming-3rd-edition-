#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = tsTclnt.py
__author__ = Hughe
__time__   = 2017-04-22 21:23
"""

from socket import *
"""
在同一台主机上使用localhost
端口号与服务器相同
"""
HOST='localhost'
PORT=21567
BUFFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data=raw_input('>')
    if not data:
        break
    tcpCliSock.send(data)
    data=tcpCliSock.recv(BUFFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()

if __name__ == '__main__':
    pass