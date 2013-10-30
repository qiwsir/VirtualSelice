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
 
urls=("/study/(.*)", "Study",   #教研员首页
)

class Study:
    def GET(self,username):
        """
        教研员身份用户登录后的首页
        """
        username=username.encode("utf-8")
        return render.study(username)
    
    def POST(self,username):
        """
        接收新密码并存储于数据库
        """
        newpassword=web.input()["newpassword"].encode("utf-8")
        username=web.input()["username"].encode('utf-8')
        md5_newpassword=md5_string(str(newpassword))
        try:
            update_value_by_where("commonuser", "password", md5_newpassword, "username", username)
            return True
        except:
            return False

app_study=web.application(urls, globals())

