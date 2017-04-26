#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = UClint.py
__author__ = Hughe
__time__   = 2017-04-23 16:30
"""
#test 2-6
from socket import *

HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpCli=socket(AF_INET,SOCK_DGRAM)

while True:
    data=raw_input('> ')
    if not data:
        break
    udpCli.sendto(data,ADDR)
    data,ADDR=udpCli.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpCli.close()

if __name__ == '__main__':
    pass