#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
This is the first page.
"""

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import web

from config.url import urls

from config import setting
render=setting.render

class Index:
    def GET(self):
        return render.index()

app=web.application(urls,globals())
if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)    
    app.run()
