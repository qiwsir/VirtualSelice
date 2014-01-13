#! /usr/bin/evn python
#! -*-coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
The administrator can go into this page.He/She can look for users,or delete users,or setting up the password of users.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
 
import web

import random
import string

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render

urls=("/adminuser_look/(.*)", "Lookuser",   
    "/adminuser_del_user/(.*)","Deluser",
    "/adminuser_newpassword/(.*)","Newpassword",
)

class Lookuser:
    def GET(self,username):
        username=username.encode("utf-8")

        params = web.input()
        page = params.page if hasattr(params, 'page') else 1
        perpage =10 
        offset = (int(page) - 1) * perpage
        try:
            all_user = select_all_perpage("commonuser",offset,perpage)
            postcount = select_item_number("commonuser")
        except:
            return "还没有添加用户"
        pages = postcount.count / perpage
        lastpage=int(page)-1
        nextpage=int(page)+1
        page3=[]
        for p in range(0,10):
            page3.append(p+int(page))
        
        return render.adminuser_look(username,all_user,lastpage,nextpage)

    def POST(self,username):
        check_user=web.input()["username"].encode("utf-8")
        try:
            user_item=select_all_by_where("commonuser","username",check_user)
        except:
            return False
        if bool(user_item) is False:
            return False
        else:
            return True

class Deluser:
    def GET(self,username):
        username=username.encode("utf-8")
        del_username=web.input()["deluser"]
        try:
            del_item("commonuser", "username", del_username)
        except:
            error_url()
        return_url=web.ctx.homedomain+"/adminuser_look/headmaster"
        raise web.seeother(return_url)

class Newpassword:
    def POST(self,username):
        username=web.input()["username"].encode("utf-8")
        newpassword=string.join(random.sample(['2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','m','n','p','r','s','t','u','v','w','x','y','z'], 6)).replace(" ","")
        md5_password=md5_string(str(newpassword))
        try:
            update_value_by_where("commonuser", "password", md5_password, "username", username)
            return "%s"%newpassword
        except:
            error_url()

app_adminuser_look=web.application(urls, globals())

