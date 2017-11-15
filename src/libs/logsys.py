#/usr/bin/python
# coding=utf-8

import time
import types


class Logsys:

    def __init__(self, project, logfilename='sys_log.txt'):
        self.project = project
        self.logfilename = logfilename

    def get_log_time(self):
        return time.strftime("%Y-%m-%d %X", time.localtime())

    def write2file(self, *formart):
        s = self.formart_string(*formart)
        if s:
            encoding = 'utf8'
            out = open(self.logfilename, 'a+')
            out.write(s + "\n")
            out.close()
        else:
            pass

    def w2f(self, perfix, strings):
        encoding = 'utf8'
        out = open(self.logfilename, 'a+')
        out.write(perfix + '|' + strings + "\n")
        out.close()

    def formart_string(self, *formart):
        string = ''
        encoding = 'utf8'
        for str in formart:
            if not type(str) in [types.UnicodeType, types.StringTypes, types.StringType]:
                s = repr(str)
            else:
                s = str
            if type(s) == type(u''):
                string += s.encode(encoding) + "\t"
            else:
                string += s + "\t"
        return string

    def w(self, notice, *formart):
        self.write2file(self.get_log_time(), '[' + notice + ']', self.project, *formart)

    def wfile(self, notice, *formart):
        self.w2f(notice + '|' + self.get_log_time(), *formart)
