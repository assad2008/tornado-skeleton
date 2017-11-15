#/usr/bin/python
# coding=utf-8

import sys
import os
import time
import socket
from src.libs import logsys
from config import LOG_PATH, LOG_PRE


def load_class(s):
    path, klass = s.rsplit('.', 1)
    __import__(path)
    mod = sys.modules[path]
    return getattr(mod, klass)


def wlog(logpath, notice, string):
    lf = time.strftime("%Y-%m-%d", time.localtime())
    log_dir = LOG_PATH + '/wlog/'
    mkdir(log_dir)
    log = logsys.Logsys(LOG_PRE, log_dir + 'log_' + lf)
    log.w(notice, string)


def debug(string):
    lf = time.strftime("%Y-%m-%d", time.localtime())
    log_dir = LOG_PATH + '/debug/'
    mkdir(log_dir)
    log = logsys.Logsys(LOG_PRE, log_dir + 'debug_' + lf)
    log.w('DEBUG', string)


def mkdir(newdir):
    if os.path.isdir(newdir):
        pass
    elif os.path.isfile(newdir):
        raise OSError("a file with the same name as the desired "
                      "dir, '%s', already exists." % newdir)
    else:
        head, tail = os.path.split(newdir)
        if head and not os.path.isdir(head):
            mkdir(head)
        if tail:
            os.mkdir(newdir)


def random_string(length):
    from random import choice
    from string import digits, letters
    return ''.join(choice(digits + letters) for i in xrange(length))


def makeorderid(lenth=7):
    from datetime import datetime
    from random import choice
    from string import digits, letters
    dt = datetime.utcnow()
    orderid = dt.strftime("%y%m%d%H") + ''.join(choice(digits) for i in xrange(lenth))
    return orderid
