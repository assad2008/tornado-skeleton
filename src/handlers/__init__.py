#/usr/bin/python
# coding=utf-8

import os
import sys
import glob
import json
import traceback

from config import LOG_PATH
from config.redis import *
import time
from tornado.web import RequestHandler, HTTPError
from src.common import recv, functions
import redis


class BaseHandler(RequestHandler):

    def debug(self, string):
        functions.debug(string)

    def initapirequest(self):
        recvpost = self.request.body
        if recvpost == None:
            self.recvdict = None
        try:
            self.recvdict = recvpost
            functions.wlog(LOG_PATH, 'INFO-API', self.recvdict)
        except:
            functions.wlog(LOG_PATH, "ERROR-API", "JSON IS ERROR")
        return self.recvdict

    def initrequest(self):
        recvpost = self.request.body
        if recvpost == None:
            self.recv_string = None
        try:
            self.recv_string = recv.dordata(recvpost)
            try:
                self.recvdict = json.loads(self.recv_string)
                functions.wlog(LOG_PATH, 'INFO', json.dumps(self.recvdict))
            except:
                functions.debug(LOG_PATH, "ERROR", "JSON IS ERROR")
                self.params = {}
                self.deviceinfo = {}
                self.gameinfo = {}
                self.serviceinfo = {}
                self.accountinfo = {}
                self.sdkinfo = {}
                self.recv_string = None
                return
            self.params = self.recvdict.get("parameter")
            self.deviceinfo = self.recvdict.get("deviceinfo")
            self.gameinfo = self.recvdict.get("gameinfo")
            self.serviceinfo = self.recvdict.get("serviceinfo")
            self.accountinfo = self.recvdict.get("accountinfo")
            self.sdkinfo = self.recvdict.get("sdkinfo")
        except:
            traceback.print_exc()
            self.recv_string = None

    def echo(self, reponse={}, code=0, tips=''):
        response_dict = {}
        if code == 0:
            response_dict['code'] = '0'
            response_dict['msg'] = tips
            if reponse != {}:
                response_dict['result'] = reponse
        else:
            response_dict['code'] = '-' + str(abs(code))
            response_dict['msg'] = tips
            if reponse != {}:
                response_dict['result'] = reponse
        logdict = dict()
        logdict["request"] = self.recvdict
        logdict['date'] = time.strftime("%Y-%m-%d %X", time.localtime())
        redata = json.dumps(response_dict)
        logdict["response"] = response_dict
        rds = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
        rds.lpush(REDIS_QUEUENAME, json.dumps(logdict))
        self.debug(json.dumps(logdict))
        del logdict
        redata_bin = recv.dopdata(redata)
        self.write(redata_bin)

    def jsonecho(self, reponse={}, code=0, tips='secuss'):
        response_dict = {}
        if code == 0:
            response_dict['code'] = '0'
            response_dict['msg'] = tips
            if reponse:
                response_dict['result'] = reponse
        else:
            response_dict['code'] = '-' + str(abs(code))
            response_dict['msg'] = tips
            self.debug(reponse)
            if reponse:
                response_dict['result'] = reponse
        functions.debug(response_dict)
        redata = json.dumps(response_dict)
        self.write(redata)


class ErrorHandler(BaseHandler):

    def prepare(self):
        super(ErrorHandler, self).prepare()
        self.set_status(404)
        raise HTTPError(404)
