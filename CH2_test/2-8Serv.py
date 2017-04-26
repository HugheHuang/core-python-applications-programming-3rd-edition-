#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = 2-8Serv.py
__author__ = Hughe
__time__   = 2017-04-23 19:28
"""
#未完成
from socket import *
from time import ctime
import threading
class SerSock:

    def __init__(self,HOST='',PORT=21567,BUFSIZ=1024):
        self.HOST=HOST
        self.PORT=PORT
        self.BUFSIZ=BUFSIZ
        self.ADDR=(HOST,PORT)

    def display(self):
        self.tcpSerSock=socket(AF_INET,SOCK_STREAM)
        self.tcpSerSock.bind(self.ADDR)
        self.tcpSerSock.listen(5)
        while True:
            print 'waiting for connection ...'
            tcpCliSock, addr = self.tcpSerSock.accept()
            print '...connected from:', addr
            self.createp(tcpCliSock)
        tcpSerSock.close()

    def createp(self,tcpCliSock):
        thread1 = threading.Thread(target=self.read, args=(tcpCliSock,))
        thread2 = threading.Thread(target=self.write, args=(tcpCliSock,))
        thread1.setDaemon(True)
        thread2.setDaemon(True)
        thread1.start()
        thread2.start()

    def read(self,tcpCliSock):
        while True:
            data = tcpCliSock.recv(self.BUFSIZ)
            if not data:
                break
            print 'clnt:',data
        tcpCliSock.close()
    def write(self,tcpCliSock):
         while True:
            data=raw_input('> ')
            tcpCliSock.send('[%s]\n%s' % (ctime(), data))






if __name__ == '__main__':
    s=SerSock()
    s.display()
