#! /usr/bin/evn python
#! -*-coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
The header of teacher can del the slices of video that he uplaoding or the administartor help him uploading.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import web

from urllib import unquote

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/study_del_videochip/(.*)", "DelChip",   
)

class DelChip:
    def GET(self,username):
        username_filename=username.encode("utf-8")
        all_filename=web.input()["videofilename"]
        video_id=web.input()["video_id"]
        chip_value=web.input()["chip"]
        head_filename=all_filename.split(".")[0]
        video_chip_tablename="video_chip"+str(video_id)
        try:
            del_item(video_chip_tablename, "endtime", chip_value)
            video_chip_all_item=select_all_item(video_chip_tablename)
        except:
            error_url()

        return render.study_edit_video_second(username,all_filename,head_filename,video_id,video_chip_all_item)


app_study_edit_video_second=web.application(urls, globals())

