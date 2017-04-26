#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = tsTservSS.py
__author__ = Hughe
__time__   = 2017-04-23 06:49
"""

from SocketServer import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime

HOST=''
PORT=21567
ADDR=(HOST,PORT)
"""
请求处理程序，重写handle方法
"""
class MyRequsetHandler(SRH):
    def handle(self):
        print '...connected from:',self.client_address
        self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))

tcpServ=TCP(ADDR,MyRequsetHandler)
print 'waiting for connection...'
tcpServ.serve_forever()

if __name__ == '__main__':
    pass