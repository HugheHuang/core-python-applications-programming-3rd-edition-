#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = tsTclntTW.py
__author__ = Hughe
__time__   = 2017-04-23 10:23
"""

from twisted.internet import protocol,reactor

HOST='localhost'
PORT=21567
class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data=raw_input('> ')
        if data:
            print '...sending %s... '%data
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol=TSClntProtocol
    clientConnectionLost=clientConnectionFailed= \
    lambda self,connector,reason:reactor.stop()

reactor.connectTCP(HOST,PORT,TSClntFactory())
reactor.run()

if __name__ == '__main__':
    pass