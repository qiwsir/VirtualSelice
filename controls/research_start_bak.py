#! /usr/bin/evn python
#! -*-coding:utf-8 -*-
 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import web
import re


from urllib import unquote
from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/research_start/(.*)", "ResearchStart",   #研修某课
)

class ResearchStart:
    def GET(self,input_string):
        input_arry=input_string.split("&")

        username=input_arry[0].encode("utf-8")

        all_filename=input_arry[1].encode("utf-8")
        head_filename=all_filename.split(".")[0]

        video_id=input_arry[2].encode("utf-8")

        video_chip_tablename="video_chip"+str(video_id)
        video_chip_all_item=select_all_item(video_chip_tablename)

        video_attach_tablename="video_attach"+str(video_id)
        video_attach=select_all_item(video_attach_tablename)

        video_bbs_tablename="video_bbs"+str(video_id)
        video_bbs=select_all_item(video_bbs_tablename)

        return render.research_start(username,all_filename,head_filename,video_id,video_chip_all_item,video_attach,video_bbs)

    def POST(self,postinfor):
        post_web=web.data()
        post_content=re.escape(unquote(post_web.split("=")[1]))

        postinfor_arry=postinfor.split("&")
        
        username=postinfor_arry[0].encode("utf-8")
        video_filename=postinfor_arry[1].encode("utf-8")
        video_id=postinfor_arry[2].encode("utf-8")

        video_bbs_tablename="video_bbs"+str(video_id)
        insert_post_into_bbs(video_bbs_tablename,post_content,username)
        return True
        #return postinfor_arry

app_research_start=web.application(urls, globals())
