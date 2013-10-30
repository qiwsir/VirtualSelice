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
 
urls=("/study_edit_video/(.*)", "Editvideo",   #编辑视频
)

class Editvideo:
    def GET(self,username):
        """
        显示新上传了的视频
        允许在本页面虚拟切片
        """
        username=username.encode("utf-8")
        all_filename=web.input()["video_filename"].encode("utf-8")

        head_filename=all_filename.split(".")[0]
        video_id=web.input()["video_id"]
        
        video_chip_table="video_chip"+video_id
        if check_table(video_chip_table) is False:
            create_table_video_chip(video_chip_table)

        video_attach_table="video_attach"+video_id
        if check_table(video_attach_table) is False:
            create_table_video_attach(video_attach_table)

        video_bbs_table="video_bbs"+video_id
        if check_table(video_bbs_table) is False:
            create_table_video_bbs(video_bbs_table)
        
        video_postnumber=select_all_by_where("videoname","id",video_id)[0].postnumber
        if video_postnumber==-1:
            update_value_by_where("videoname", "postnumber", '0', "id",video_id)

        return render.study_edit_video(username,all_filename,head_filename,video_id)
    
    def POST(self,username):
        """
        接收时间点信息
        并存储切片开始和结束点
        """
        input_list=web.data().split("&")
        video_id=input_list[0].split("=")[1].encode("utf-8")
        del input_list[0]
        username=input_list[0].split("=")[1].encode("utf-8")
        del input_list[0]
        video_filename=str(input_list[0].split("=")[1].encode("utf-8"))
        del input_list[0]
        
        time_list=input_list
        start_arry=[]
        end_arry=[]
        for n in range(len(time_list)):
            if n%2==0:
                start_arry.append(time_list[n].split("=")[1])
            else:
                end_arry.append(time_list[n].split("=")[1])
        
        video_chip_tablename="video_chip"+str(video_id)
        try:
            video_chip_item=select_all(video_chip_tablename)
        
            if bool(video_chip_item) is True:
                del_all(video_chip_tablename)
            for i in range(len(start_arry)):
                starttime=str(start_arry[i])
                endtime=str(end_arry[i])
                insert_video_chip_tablename_time(video_chip_tablename,starttime,endtime)
        
            return True
        except:
            error_url()


app_study_edit_video=web.application(urls, globals())

