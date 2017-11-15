#/usr/bin/python
# coding=utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options
from config import LOG_PATH


class Application(tornado.web.Application):

    def __init__(self):
        from src import routes as handlers
        tornado.web.Application.__init__(self, handlers)

define("port", default=9876, help="miss port", type=int)
define("host", default="0.0.0.0", help="miss host")
define("log_file_prefix", default=LOG_PATH + "web.log", help="miss log path")


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.bind(options.port, options.host)
    http_server.start(num_processes=1)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
