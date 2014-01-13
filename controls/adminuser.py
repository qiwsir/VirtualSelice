#! /usr/bin/evn python
#! -*-coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
The Administrator of this system can go into this page when he/she logined.
And she/he can add new users for the system,include teacher and reasearcher.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
 
import web

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/adminuser/(.*)", "Adminuser",   #administrator index
    "/adminuser_add/(.*)","Adduser",    #add new users
)

class Adminuser:
    def GET(self,username):
        username=username.encode("utf-8")
        return render.adminuser(username)
    
    def POST(self,username):
        newpassword=web.input()["newpassword"].encode("utf-8")
        md5_newpassword=md5_string(str(newpassword))
        
        try:
            update_value_by_where("adminuser", "password", md5_newpassword, "username", "headmaster")
            return True
        except:
            return False


class Adduser:
    def GET(self,username):
        username=username.encode("utf-8")
        return render.adminuser_add(username)

    def POST(self,username):
        newusername=web.input()["newusername"].encode("utf-8")
        newuserrole=web.input()["newuserrole"].encode("utf-8")
        
        if newuserrole=="教研员":
            newdir="/alidata/www/cutvideo/static/video/"+newusername
            os.mkdir(newdir)

        try:
            newuser_item=select_all_by_where("commonuser","username",newusername)
            if bool(newuser_item) is True:
                return False
            else:
                md5_password=md5_string("123456")
                insert_newuser_into_commonuser(newusername,md5_password,newuserrole)
                return True
        except:
            return False


app_adminuser=web.application(urls, globals())

