#! /usr/bin/evn python
#! -*-coding:utf-8 -*-
 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import web
import datetime
import re

import urllib

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/study_new_video/(.*)", "Newvideo",   #新增视频
)

class Newvideo:
    def GET(self,username):
        """
        添加视频首页
        """
        username=username.encode("utf-8")
        tell_user="特别提醒：本系统只接收扩展名为.ogv格式的视频文件"
        return render.study_new_video(username,tell_user)

    def POST(self,username):
        """
        接收上传的视频文件并存到指定服务器位置
        接收视频名称并存储到数据库
        """
        username=username.encode("utf-8")

        x= web.input(videofile={})
        videotitle=web.input()
        filedir=u"/alidata/www/cutvideo/static/video" #视频存储物理位置
        
        if 'videofile' in x:
            filepath=x.videofile.filename.replace('\\','/')
            all_filename=filepath.split('/')[-1]
            end_filename=all_filename.split(".")[-1]
            if end_filename!='ogv':
                tell_user="再次提醒：本系统只允许上传扩展名为.ogv格式的视频文件"
                return render.study_new_video(username,tell_user)
            head_filename=videotitle.videotitle
            filename=head_filename+"."+end_filename
            fout = open(filedir +'/'+ filename,'wb')
            fout.write(x.videofile.file.read()) 
            fout.close() 
        editor=videotitle.username
        attachment=u"no"
        try:
            insert_video_into_videoname(filename,head_filename,editor,attachment)
        
            video_id=select_all_by_where("videoname","videoname",filename)[0].id
        
            video_chip_tablename="video_chip"+str(video_id)
            create_table_video_chip(video_chip_tablename)

            video_attach_tablename="video_attach"+str(video_id)
            create_table_video_attach(video_attach_tablename)
        
            video_bbs_tablename="video_bbs"+str(video_id)
            create_table_video_bbs(video_bbs_tablename)

            #filename_quote=urllib.quote(filename)
            return_url=web.ctx.homedomain+"/study_edit_video/"+username+"?video_filename="+filename+"&video_id="+str(video_id)
            return web.seeother(return_url)
            #return return_url
        except:
            error_url()

app_study_new_video=web.application(urls, globals())

