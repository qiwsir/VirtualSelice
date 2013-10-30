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
 
urls=("/research/(.*)", "Research",   #研修首页
    "/research_one/(.*)","ResearchOne"  #搜索课程
)

class Research:
    def GET(self,username):
        """
        研修首页
        列表显示所有发布的研修课程
        """
        username=username.encode("utf-8")
        try:
            user_item=select_all_by_where("commonuser","username",username)
        except:
            error_url()
        
        params = web.input()
        page = params.page if hasattr(params, 'page') else 1
        perpage =20 
        offset = (int(page) - 1) * perpage
        try:
            video_item = select_where_no_equal2("videoname","postnumber",'-1',perpage,offset)
            postcount = select_item_number("videoname")
        except:
            return error_url()
        pages = postcount.count / perpage
        lastpage=int(page)-1
        nextpage=int(page)+1
        
        return render.research(username,video_item,user_item,lastpage,nextpage)



    def POST(self,username):
        """
        接收查询字符串
        按照关键词查询并返回值
        """
        lesson=web.input()["lesson"]
        username=web.input()["username"]
        try:
            select_item=select_like_string("videoname","headvideoname",str(lesson))
        except:
            return False
        if bool(select_item):
            return True
        else:
            return False
        
class ResearchOne:
    def GET(self,username):
        """
        显示关键词查询结果
        """
        username=username.encode("utf-8")
        lesson=web.input()["keyword"]
        try:
            video_item=select_like_string("videoname","headvideoname",str(lesson))
            user_item=select_all_by_where("commonuser","username",username)
        except:
            error_url()
        return render.research(username,video_item,user_item) 

app_research=web.application(urls, globals())

