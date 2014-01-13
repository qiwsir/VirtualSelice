# ! /usr/bin/evn python
# -*-coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
User logout from system.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import web

from model.comfunction import *

from config import setting
render=setting.render
     
urls=("/logout", "Logout", 
    )

class Logout:

    def GET(self,username):
        username=username.encode("utf-8")
        if username=="headmaster":
            update_value_by_where("adminuser", "handshake", "", "username", username)
        else:
            update_value_by_where("commonuser", "handshake", "", "username", username)
        del_cookie(username)
        raise web.seeother(web.ctx.homedomain)


app_userlogout=web.application(urls, globals())
