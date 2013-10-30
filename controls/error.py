#! /usr/bin/evn python
#! -*-coding:utf-8 -*-
 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
 
import web

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/error", "Error",   #错误页面
)

class Error:
    def GET(self):
        tell_user="很遗憾的告诉您，当看到这个页面的时，您在操作中必然出现了错误。"
        return render.error(tell_user)
    
app_error=web.application(urls, globals())

