#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = 2-7Clnt.py
__author__ = Hughe
__time__   = 2017-04-23 19:04
"""
from socket import *

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
            print data
        tcpCliSock.close()

if __name__ == '__main__':
    c=CliSock()
    c()