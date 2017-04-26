
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__  = getLatestFTP.py \n
__author__ = Hughe            \n
__time__   = 2017-04-24 22:48  \n
"""

import ftplib
import os
import socket

HOST='ftp.mozilla.org'
DIRN='pub/mozilla.org/webtools'
FILE='bugzilla-LATEST.tar.gz'

def main():
    try:
        f=ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print 'ERROR: cannot reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Changed to "%s"' % DIRN

    try:
        f.retrbinary('RETR %s' % FILE,open(FILE,'wb').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CMD' % FILE
    f.quit()

if __name__ == '__main__':
    main()