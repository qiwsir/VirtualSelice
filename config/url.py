#!/usr/bin/env/ python
# -*- coding:utf-8 -*-

pre_fix="controls."

urls=(
    "/",                        "Index",
    "/logindex",                pre_fix+"logindex.Login",       #用户登录相关判断
    "/logout/(.*)",             pre_fix+"logout.Logout",
    
    "/adminuser/(.*)",          pre_fix+"adminuser.Adminuser",  #用户管理首页
    "/adminuser_look/(.*)",     pre_fix+"adminuser_look.Lookuser",   #察看所有的用户以及管理
    "/adminuser_add/(.*)",      pre_fix+"adminuser.Adduser",    #新增加用户
    "/adminuser_del_user/(.*)", pre_fix+"adminuser_look.Deluser",  #删除用户
    "/adminuser_newpassword/(.*)",pre_fix+"adminuser_look.Newpassword", #重置用户密码


    "/study/(.*)",              pre_fix+"study.Study",#教研员登录首页
    "/study_manage_video/(.*)", pre_fix+"study_manage_video.Managevideo",   #管理视频
    "/study_del_video/(.*)",    pre_fix+"study_manage_video.Delvideo",      #删除视频
    "/study_new_video/(.*)",    pre_fix+"study_new_video.Newvideo",     #新增视频
    "/study_edit_video/(.*)",   pre_fix+"study_edit_video.Editvideo",   #编辑视频
    "/study_edit_video_second/(.*)",pre_fix+"study_edit_video_second.EditvideoSecond",  #编辑片段名称
    "/study_view_video/(.*)",   pre_fix+"study_view_video.Viewvideo",   #预览编辑结果
    "/study_attachment/(.*)",   pre_fix+"study_attachment.Attachment",  #上传附件
    "/study_attachment_del/(.*)",pre_fix+"study_attachment.DelAttach",  #删除附件
    "/study_del_videochip/(.*)",pre_fix+"study_del_videochip.DelChip",  #删除切片

    "/error",                   pre_fix+"error.Error",      #错误页面

    "/teacher/(.*)",            pre_fix+"teacher.Teacher",  #教师登录首页

    "/research/(.*)",           pre_fix+"research.Research",    #研修首页
    "/research_start/(.*)",     pre_fix+"research_start.ResearchStart",   #某课程
    "/research_one/(.*)",       pre_fix+"research.ResearchOne", #搜索课程

)
