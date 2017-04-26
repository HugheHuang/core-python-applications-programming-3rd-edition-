#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = tsUclnt.py
__author__ = Hughe
__time__   = 2017-04-22 22:36
"""

from socket import *

HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpClnSock=socket(AF_INET,SOCK_DGRAM)

while True:
    data=raw_input('> ')
    if not data:
        break
    udpClnSock.sendto(data,ADDR)
    data,ADDR=udpClnSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data
udpClnSock.close()

if __name__ == '__main__':
    pass