# ! /usr/bin/evn python
# -*-coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
The user go into the system through this page:login.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import web

from model.comfunction import *

from config import setting
render=setting.render
     
urls=("/logindex", "Login", 
    )

class Login:
    def POST(self):
        username=web.input()["username"].encode("utf-8")
        userpassword=web.input()["userpwd"].encode("utf-8")
        md5_handshake=create_handshake_md5(username)
        
        if username=="headmaster":
            if check_username_and_password("adminuser",username,userpassword):
                try:
                    update_cookies_and_handshake("adminuser",md5_handshake, username)
                except:
                    error_url()
                return "1"
            else:
                return "0"
        else:
            if check_username_and_password("commonuser",username,userpassword):
                try:
                    update_cookies_and_handshake("commonuser",md5_handshake, username)
                    user_role=select_all_by_where("commonuser","username",username)[0].role
                except:
                    error_url()
                if user_role=="教研员":
                    return "2"
                elif user_role=="教师":
                    return "3"
                else:
                    return "0"
            else:
                return "0"

app_userlogin=web.application(urls, globals())
