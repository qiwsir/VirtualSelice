# ! /usr/bin/evn python
# -*-coding:utf-8 -*-

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
        """
        用户退出并删除cookie等
        """
        username=username.encode("utf-8")
        if username=="headmaster":
            update_value_by_where("adminuser", "handshake", "", "username", username)
        else:
            update_value_by_where("commonuser", "handshake", "", "username", username)
        del_cookie(username)
        raise web.seeother(web.ctx.homedomain)


app_userlogin=web.application(urls, globals())
