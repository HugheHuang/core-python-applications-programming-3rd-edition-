#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = 2-7Serv.py
__author__ = Hughe
__time__   = 2017-04-23 19:04
"""


from socket import *
from time import ctime

class SerSock:
    def __init__(self,HOST='',PORT=21567,BUFSIZ=1024):
        self.HOST=HOST
        self.PORT=PORT
        self.BUFSIZ=BUFSIZ
        self.ADDR=(HOST,PORT)
    def __call__(self):
        tcpSerSock=socket(AF_INET,SOCK_STREAM)
        tcpSerSock.bind(self.ADDR)
        tcpSerSock.listen(5)
        while True:
            print 'waiting for connection ...'
            tcpCliSock, addr = tcpSerSock.accept()
            print '...connected from:', addr

            while True:
                data = tcpCliSock.recv(self.BUFSIZ)
                if not data:
                    break
                print 'clnt:', data
                data = raw_input('> ')
                tcpCliSock.send('[%s] %s' % (ctime(), data))
            tcpCliSock.close()

        tcpSerSock.close()


if __name__ == '__main__':
    s=SerSock()
    s()