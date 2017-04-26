#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = 2-8Clnt.py
__author__ = Hughe
__time__   = 2017-04-23 19:28
"""
from socket import *
import threading
#未完成
class CliSock:

    def __init__(self,HOST='localhost',PORT=21567,BUFSIZ=1024):
        self.HOST=HOST
        self.PORT=PORT
        self.BUFSIZ=BUFSIZ
        self.ADDR=(HOST,PORT)

    def display(self):
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(self.ADDR)

        thread1 = threading.Thread(target=self.read , args=(tcpCliSock,))
        thread2 = threading.Thread(target=self.write , args=(tcpCliSock,))
        thread1.setDaemon(True)
        thread2.setDaemon(True)
        thread1.start()
        thread2.start()

    def write(self,tcpCliSock):
        while True:
            data = raw_input('> ')
            if data=='quit':
                self.tcpCliSock.close()
                break
            self.tcpCliSock.send(data)
        self.tcpCliSock.close()
    def read(self,tcpCliSock):
        while True:
            data = self.tcpCliSock.recv(self.BUFSIZ)
            if data:
                print data

if __name__ == '__main__':
    c=CliSock()
    c.display()