#! /usr/bin/evn python
#! -*-coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
User start study a lesson in this page and look the video of slices.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import web
import re

import urllib 

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/research_start/(.*)", "ResearchStart",
)

class ResearchStart:
    def GET(self,username):
        username=username.encode("utf-8")
        all_filename=web.input()["videoname"].encode("utf-8")
        head_filename=all_filename.split(".")[0]
        video_id=web.input()["video_id"].encode("utf-8")
        video_chip_tablename="video_chip"+str(video_id)
        try:
            video_chip_all_item=select_all_item(video_chip_tablename)
            video_attach_tablename="video_attach"+str(video_id)
            video_attach=select_all_item(video_attach_tablename)
            user_item=select_all_by_where("commonuser","username",username)
            video_editor=select_all_by_where("videoname","id",video_id)[0].editor
        except:
            error_url()
        
        params = web.input()
        page = params.page if hasattr(params, 'page') else 1
        perpage =10 
        offset = (int(page) - 1) * perpage
        video_bbs_tablename="video_bbs"+str(video_id)
        video_bbs = select_all_perpage(video_bbs_tablename,offset,perpage)
        postcount = select_item_number("commonuser")
        pages = postcount.count / perpage
        lastpage=int(page)-1
        nextpage=int(page)+1

        return render.research_start(username,all_filename,head_filename,video_id,video_chip_all_item,video_attach,video_bbs,user_item,video_editor,lastpage,nextpage)

    def POST(self,username):
        try:
            post_web=urllib.unquote_plus(web.data())
            post_content=post_web.split("=")[1]
            username=username.encode("utf-8")
            video_filename=web.input()["videoname"].encode("utf-8")
            video_id=web.input()["video_id"].encode("utf-8")
            video_bbs_tablename="video_bbs"+str(video_id)
            insert_post_into_bbs(video_bbs_tablename,post_content,username)
            video_postnumber=select_all_by_where("videoname","id",video_id)[0].postnumber
            video_postnumber=int(video_postnumber)+1
            update_value_by_where("videoname", "postnumber", video_postnumber, "id",video_id)
            return True
        except:
            error_url()

app_research_start=web.application(urls, globals())
