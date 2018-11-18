#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-18
# @Author  : flying

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(111)
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('pwd')
        if u == 'flying' and e == 'flying@qq.com' and p == '1223':
            self.write("OK")
        else:
            self.write("滚")
        self.write("GET")
    def post(self, *args, **kwargs):
        print(123)
        u = self.get_argument('user')
        e = self.get_argument('email')
        p = self.get_argument('pwd')
        if u == 'flying' and e == 'flying@qq.com' and p == '1223':
            self.write("OK")
        else:
            self.write("滚")
        self.write('POST')

application = tornado.web.Application([
    (r"/index",MainHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()