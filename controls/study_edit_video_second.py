#! /usr/bin/evn python
#! -*-coding:utf-8 -*-
 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import web

from urllib import unquote

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/study_edit_video_second/(.*)", "EditvideoSecond",   #片段的名称
)

class EditvideoSecond:
    def GET(self,username):
        """
        显示片段分割结果
        等待输入切片名称
        """
        username=username.encode("utf-8")
        all_filename=web.input()["video_filename"].encode("utf-8")
        head_filename=all_filename.split(".")[0]
        
        video_id=web.input()["video_id"]
        video_chip_tablename="video_chip"+str(video_id)
        try:
            video_chip_all_item=select_all_item(video_chip_tablename)
        except:
            error_url()
        return render.study_edit_video_second(username,all_filename,head_filename,video_id,video_chip_all_item)

    def POST(self,username):
        """
        接收并存储切片标题名称
        """
        input_list=web.data().split("&")
        username=input_list[0].split("=")[1].encode("utf-8")
        del input_list[0]
        all_filename=input_list[0].split("=")[1].encode("utf-8")
        del input_list[0]
        video_id=input_list[0].split("=")[1].encode("utf-8")
        del input_list[0]
        video_chip_tablename="video_chip"+str(video_id)

        titlename_list=input_list
        titlename_arry=[]
        for n in range(len(titlename_list)):
            titlename_arry.append(titlename_list[n].split("=")[1])
        
        try:
            for i in range(len(titlename_arry)):
                titlename=unquote(titlename_arry[i])
                #titlename=u"这是汉字"
                titlename_id=int(i+1)
                update_value_by_where(video_chip_tablename, "title", titlename, "id", titlename_id)
        
            return True
        except:
            return False

app_study_edit_video_second=web.application(urls, globals())

