#! /usr/bin/evn python
#! -*-coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
The user who uploaded the video can preview the result that he/she edited.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import web

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/study_view_video/(.*)", "Viewvideo",   
)

class Viewvideo:
    def GET(self,username):
        username=username.encode("utf-8")

        all_filename=web.input()["video_filename"].encode("utf-8")
        head_filename=all_filename.split(".")[0]

        video_id=web.input()["video_id"]
        try:
            video_chip_tablename="video_chip"+str(video_id)
            video_chip_all_item=select_all_item(video_chip_tablename)

            video_attach_tablename="video_attach"+str(video_id)
            video_attach=select_all_item(video_attach_tablename)
        except:
            error_url()

        tell_user=""

        return render.study_view_video(username,all_filename,head_filename,video_id,video_chip_all_item,video_attach,tell_user)


app_study_view_video=web.application(urls, globals())

