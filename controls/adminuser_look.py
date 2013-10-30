#! /usr/bin/evn python
#! -*-coding:utf-8 -*-
 
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

urls=("/adminuser_look/(.*)", "Lookuser",   #查看用户
    "/adminuser_del_user/(.*)","Deluser",#删除用户
    "/adminuser_newpassword/(.*)","Newpassword",    #重置用户密码
)

class Lookuser:
    def GET(self,username):
        """
        显示系统中所有用户
        提供对用户的删除和重置密码操作
        """
        username=username.encode("utf-8")
#        try:
#            check_user=web.input()["user"]
#            all_user=select_all_by_where("commonuser","username",check_user)
#        except:
#            all_user=select_all("commonuser")
#        finally: 
#            return render.adminuser_look(username,all_user)


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
        """
        接收要查询的用户名
        如果数据库中存在则返回值并显示
        """
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
        """
        接收删除用户名并在数据库中删除
        """
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
        """
        接收要重置密码的用户名
        按照规则生成新的用户密码并存储于数据库
        """
        username=web.input()["username"].encode("utf-8")
        newpassword=string.join(random.sample(['2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','m','n','p','r','s','t','u','v','w','x','y','z'], 6)).replace(" ","")
        md5_password=md5_string(str(newpassword))
        try:
            update_value_by_where("commonuser", "password", md5_password, "username", username)
            return "%s"%newpassword
        except:
            error_url()

app_adminuser_look=web.application(urls, globals())

