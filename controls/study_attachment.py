#! /usr/bin/evn python
#! -*-coding:utf-8 -*-
 
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
 
import web
import datetime
import re

from model.comfunction import *
from model.spefunction import *
 
from config import setting
render=setting.render
 
urls=("/study_attachment/(.*)", "Attachment",   #新增附件
    "/study_attachment_del/(.*)","DelAttach",   #删除附件
)

class Attachment:

    def POST(self,username):
        """
        接收上传的附件
        """
        x= web.input(attachfile={})
        username=x.username
        video_all_filename=x.videofilename
        video_head_filename=video_all_filename.split(".")[0].encode("utf-8")
        video_id=x.video_id
        
        head_filename=x.attachtitle
        filename_result=re.match(r"^[a-zA-Z0-9_\u4e00-\u9fa5]+$",head_filename)
        if bool(filename_result) is False:
            tell_user="标题只能是数字、字母或者汉字，不能含其它字符"
            video_chip_tablename="video_chip"+str(video_id)
            video_chip_all_item=select_all_item(video_chip_tablename)
            video_attach_tablename="video_attach"+str(video_id)
            video_attach=select_all_item(video_attach_tablename)
            return render.study_view_video(username,video_all_filename,video_head_filename,video_id,video_chip_all_item,video_attach,tell_user)
        else:
        
            filedir=u"/alidata/www/cutvideo/static/attachment"
            if 'attachfile' in x:
                filepath=x.attachfile.filename.replace('\\','/')
                all_filename=filepath.split('/')[-1]
                end_filename=all_filename.split(".")[-1]
            
            #head_filename=attachtitle.attachtitle
                filename=head_filename+"."+end_filename
                fout = open(filedir +'/'+ filename,'wb')
                fout.write(x.attachfile.file.read()) 
                fout.close() 
        
            attachtitle=x.attachtitle

        
            video_attach_tablename="video_attach"+str(video_id)
            insert_value(video_attach_tablename,"attachname",filename)

            update_value_by_where("videoname", "attachment", "Yes", "id", video_id)


            return_url=web.ctx.homedomain+"/study_view_video/"+username+"?video_filename="+video_all_filename+"&video_id="+str(video_id)
            raise web.seeother(return_url)


class DelAttach:
    def GET(self,getinfor):
        """
        删除附件
        """
        video_id=getinfor.encode("utf-8")
        attachment_name=web.input()["attachname"].encode("utf-8")

        try:
            video_item=select_all_by_where("videoname","id",video_id)[0]
            username=video_item.editor
            video_filename=video_item.videoname

            video_attach_tablename="video_attach"+str(video_id)
            del_item(video_attach_tablename, "attachname", attachment_name)
        except:
            error_url()
        return_url=web.ctx.homedomain+"/study_view_video/"+username+"?video_filename="+video_filename+"&video_id="+str(video_id)
        raise web.seeother(return_url)


app_attachment=web.application(urls, globals())

