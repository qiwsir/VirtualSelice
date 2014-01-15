#! /usr/bin/evn python
#! -*-coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
This page is the index when the header of teacher who reasearch teaching login in this system.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import web

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/study/(.*)", "Study",
)

class Study:
    def GET(self,username):
        username=username.encode("utf-8")
        return render.study(username)
    
    def POST(self,username):
        newpassword=web.input()["newpassword"].encode("utf-8")
        username=web.input()["username"].encode('utf-8')
        md5_newpassword=md5_string(str(newpassword))
        try:
            update_value_by_where("commonuser", "password", md5_newpassword, "username", username)
            return True
        except:
            return False

app_study=web.application(urls, globals())

