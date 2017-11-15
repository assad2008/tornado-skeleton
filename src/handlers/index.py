# -*- coding: utf-8 -*-
# @Author: assad
# @Date:   2017-11-15 12:02:16
# @Last Modified by:   assad
# @Last Modified time: 2017-11-15 16:42:31

from src.handlers import BaseHandler
from src.common import functions


class indexHandler(BaseHandler):

    def get(self):
        self.jsonecho(None, -1, "params is miss")

    def post(self):
        pass


routes = [
    (r"/", indexHandler),
    (r"/index\.html", indexHandler),
]
