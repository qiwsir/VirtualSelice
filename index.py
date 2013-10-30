#!/usr/bin/env python
# -*- coding:utf-8 -*-
import web
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from config.url import urls

from config import setting
render=setting.render

class Index:
    def GET(self):
        tell="这是一个让你明白他为什么就那么好的系统"
        return render.index(tell)

app=web.application(urls,globals())
if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)    
    app.run()
