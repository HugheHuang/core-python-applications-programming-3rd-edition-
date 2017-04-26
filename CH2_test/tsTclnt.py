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





class CliSock:
    def __init__(self,HOST='localhost',PORT=21567,BUFSIZ=1024):
        self.HOST=HOST
        self.PORT=PORT
        self.BUFSIZ=BUFSIZ
        self.ADDR=(HOST,PORT)

    def __call__(self):
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(self.ADDR)
        while True:
            data = raw_input('> ')
            if not data:
                break
            tcpCliSock.send(data)
            data = tcpCliSock.recv(self.BUFSIZ)
            if not data:
                break
            print 'Serv:',data
        tcpCliSock.close()



if __name__ == '__main__':
    p=CliSock()
    p()