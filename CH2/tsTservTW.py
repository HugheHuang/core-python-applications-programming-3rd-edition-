#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = tsTservTW.py
__author__ = Hughe
__time__   = 2017-04-23 09:39
"""

from twisted.internet import protocol,reactor
from time import ctime

PORT=21567

class TSServProtrol(protocol.Protocol):
    def connectionMade(self):
        clnt=self.clnt=self.transport.getPeer().host
        print '...connected from:',clnt

    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(),data))

factory=protocol.Factory()
factory.protocol=TSServProtrol
print 'waiting for connection ...'
reactor.listenTCP(PORT,factory)
reactor.run()

if __name__ == '__main__':
    pass