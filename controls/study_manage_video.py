#! /usr/bin/evn python
#! -*-coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
The header of teacher can manage the video or delete video that he uploed or the administrator uploaed.
"""

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import os 
import web

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/study_manage_video/(.*)", "Managevideo",   
    "/study_del_video/(.*)","Delvideo",         
)

class Managevideo:
    def GET(self,username):
        username=username.encode("utf-8")
        
        try:
            lessonname=web.input()["lessonname"]
            video_item=select_like_string_by_where("videoname","videoname",lessonname,"editor",username)
            return render.study_manage_video_search(username,video_item)
        except:
            path="/alidata/www/cutvideo/static/video/"+username+"/"    #this URL is the path of video store that the administrator manage it in service.You shuld name it like this.
            files=os.listdir(path)
            for f in files:
                f_extention=f.split(".")[1]
                if f_extention=="ogv":
                    f_name_in_videoname=select_all_by_where("videoname","videoname",f)
                    if bool(f_name_in_videoname) is False:
                        head_filename=f.split(".")[0]
                        insert_video_into_videoname(f,head_filename,username,"No")
            
            
            params = web.input()
            page = params.page if hasattr(params, 'page') else 1
            perpage =10 
            offset = (int(page) - 1) * perpage
            try:
                video_item=select_all_by_where2("videoname","editor",username,perpage,offset)
                postcount = select_item_number("videoname")
            except:
                return error_url()
            pages = postcount.count / perpage
            lastpage=int(page)-1
            nextpage=int(page)+1
            return render.study_manage_video(username,video_item,lastpage,nextpage)

    def POST(self,username):
        lessonname=web.input()["lessonname"].encode("utf-8")
        username=username.encode("utf-8")
        check_item=select_like_string_by_where("videoname","videoname",lessonname,"editor",username)
        if bool(check_item) is False:
            return False
        else:
            return True

class Delvideo:
    def GET(self,username):
        username=username.encode("utf-8")
        videoname=web.input()["video_filename"].encode("utf-8")
        del_item("videoname", "videoname", videoname)
        return_url=web.ctx.homedomain+"/study_manage_video/"+username
        raise web.seeother(return_url)


app_study_manage_video=web.application(urls, globals())

