#! /usr/bin/evn python
#! -*-coding:utf-8 -*-
 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import os 
import web

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/study_manage_video/(.*)", "Managevideo",   #管理视频
    "/study_del_video/(.*)","Delvideo",         #删除视频
)

class Managevideo:
    def GET(self,username):
        """
        显示已经存在的视频
        """
        username=username.encode("utf-8")
        
        try:
            lessonname=web.input()["lessonname"]
            video_item=select_like_string_by_where("videoname","videoname",lessonname,"editor",username)
            return render.study_manage_video_search(username,video_item)
        except:
            path="/alidata/www/cutvideo/static/video/"+username+"/"
            files=os.listdir(path)
            for f in files:
                #insert_video_into_videoname(f,"yesterday",username,"No")
                f_extention=f.split(".")[1]
                if f_extention=="ogv":
                    f_name_in_videoname=select_all_by_where("videoname","videoname",f)
                    if bool(f_name_in_videoname) is False:
                        head_filename=f.split(".")[0]
                        insert_video_into_videoname(f,head_filename,username,"No")
            #video_item=select_all_by_where("videoname","editor",username)
            
            
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
        #finally:
            return render.study_manage_video(username,video_item,lastpage,nextpage)

    def POST(self,username):
        """
        按照关键词搜索视频并显示结果
        """
        lessonname=web.input()["lessonname"].encode("utf-8")
        username=username.encode("utf-8")
        check_item=select_like_string_by_where("videoname","videoname",lessonname,"editor",username)
        if bool(check_item) is False:
            return False
        else:
            return True

class Delvideo:
    def GET(self,username):
        """
        删除某个视频课程
        """
        username=username.encode("utf-8")
        videoname=web.input()["video_filename"].encode("utf-8")
        del_item("videoname", "videoname", videoname)
        return_url=web.ctx.homedomain+"/study_manage_video/"+username
        raise web.seeother(return_url)


app_study_manage_video=web.application(urls, globals())

