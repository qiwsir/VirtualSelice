#!/usr/bin/env/ python
# -*- coding:utf-8 -*-

"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
"""

pre_fix="controls."

urls=(
    "/",                        "Index",
    "/logindex",                pre_fix+"logindex.Login",       #the user login
    "/logout/(.*)",             pre_fix+"logout.Logout",
    
    "/adminuser/(.*)",          pre_fix+"adminuser.Adminuser",  #admin all the user of the system
    "/adminuser_look/(.*)",     pre_fix+"adminuser_look.Lookuser",   #look for the user and administrate them
    "/adminuser_add/(.*)",      pre_fix+"adminuser.Adduser",    #add new user
    "/adminuser_del_user/(.*)", pre_fix+"adminuser_look.Deluser",  #del user
    "/adminuser_newpassword/(.*)",pre_fix+"adminuser_look.Newpassword", #setting up the password of user


    "/study/(.*)",              pre_fix+"study.Study",#the header of teacher login
    "/study_manage_video/(.*)", pre_fix+"study_manage_video.Managevideo",   #manage video
    "/study_del_video/(.*)",    pre_fix+"study_manage_video.Delvideo",      #del video
    "/study_new_video/(.*)",    pre_fix+"study_new_video.Newvideo",     #add video
    "/study_edit_video/(.*)",   pre_fix+"study_edit_video.Editvideo",   #edit video
    "/study_edit_video_second/(.*)",pre_fix+"study_edit_video_second.EditvideoSecond",  #edit sclice of video
    "/study_view_video/(.*)",   pre_fix+"study_view_video.Viewvideo",   #preview
    "/study_attachment/(.*)",   pre_fix+"study_attachment.Attachment",  #uploading attachment
    "/study_attachment_del/(.*)",pre_fix+"study_attachment.DelAttach",  #del attachment
    "/study_del_videochip/(.*)",pre_fix+"study_del_videochip.DelChip",  #del sclice

    "/error",                   pre_fix+"error.Error",      #error page

    "/teacher/(.*)",            pre_fix+"teacher.Teacher",  #teacher login

    "/research/(.*)",           pre_fix+"research.Research",    #reaseache and study index page
    "/research_start/(.*)",     pre_fix+"research_start.ResearchStart",   #start to study a lesson
    "/research_one/(.*)",       pre_fix+"research.ResearchOne", #search lesson

)
