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

#nex is the upload
import cgi
import cStringIO
import json
import mimetypes
import os
from pprint import pprint
from uuid import uuid4

try:
    import magic
except ImportError:
    magic =None

osp=os.path
PWD=osp.dirname(os.path.realpath(__file__))
SAVE_UPLOAD_PATH=os.path.join(PWD,"u")
#end uploadify 1part

urls=("/study_new_video/(.*)", "Newvideo",   #新增视频
)

#start:uploadify part2
prefer_ext_list={
    'image/jpeg':'.jpg',
    }

def guess_filename_ext_by_mime_name(mime_name):
    if mime_name in prefer_ext_list:
        return prefer_ext_list[mime_name]
    ext=mimetypes.guess_extension(mime_name)
    return ext

def parse_boundary_from_str(src):
    CRLF='\r\n'
    NOT_FOUND=-1
    src=src[2:]
    end=src.find(CRLF)

    if end==NOT_FOUND:
        print "!!!Error:parse boundary failed,CRLF not found"
        return None

    return src[:end]

def parse_multipart(s):
    fp = cStringIO.StringIO(s)
    c = fp.read()
    fp.seek(0)

    boundary = parse_boundary_from_str(c)
    pdict = {
        'boundary' : boundary
    }
    parses = cgi.parse_multipart(fp, pdict)
    fp.close()

    return parses

def parse_webpy_files(datas, return_fullpath=True):
    resps = []
    parses = parse_multipart(datas)
    # print "parses:", parses

    for fname, buf in parses.iteritems():
        fcontnet = buf[0]
        ext = os.path.splitext(fname)[-1]
        new_filename = str(uuid4()) + ext
        body_len = len(fcontnet)
        resp = {
            "origin_name" : fname,
            "new_name" : new_filename,
            "content_type" : None,
            "mime" : None,
            "encoding" : None,
            "length" : body_len,
        }
        save_to = osp.join(SAVE_UPLOAD_PATH, new_filename)
        f = file(save_to, "w")
        f.write(fcontnet)
        f.close()

        if ext:
            mime_type, encoding = mimetypes.guess_type(save_to)
            if mime_type:
                resp["mime"] = mime_type
            if encoding:
                resp["encoding"] = encoding
        else:
            if not magic:
                print "!!! WARNING: import magic failed"
                continue

            mime = magic.Magic(mime=True)
            resp["mime"] = mime.from_file(save_to)
            resp["content_type"] = resp["mime"]

            mime_encoding = magic.Magic(mime_encoding=True)
            resp["encoding"] = mime_encoding.from_file(save_to)

            if resp["mime"]:
                # uploadify plugin POST some data we don't need, filter non-image MIME response
                if not _is_image(resp):
                    os.remove(save_to)
                    continue

                ext = guess_filename_ext_by_mime_name(resp["mime"])
                old_filename = save_to
                new_filename = "%s%s" % (save_to, ext)
                os.rename(old_filename, new_filename)
                if return_fullpath:
                    resp["new_name"] = new_filename
                else:
                    resp["new_name"] = new_filename.replace(SAVE_UPLOAD_PATH, "").strip("/")

        resps.append(resp)
    return resps

def _is_image(resp):
    return resp["mime"] in ("image/png","image/jpeg", "image/jpg", "image/jpe", "image/gif")

##end part2 of uploadify

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
        datas=web.data()
        results=parse_webpy_files(datas,False)
        print "results:"
        pprint(results)
        web.header("Content-Type","application/json")
        web.header("Access-Control-Allow-Origin","*")
        return json.dumps(results)


"""
        username=username.encode("utf-8")
        editor=web.input()["username"]
        head_filename=web.input()["videotitle"]
        filename_result=re.match(r"^[a-zA-Z0-9_\u4e00-\u9fa5]+$",head_filename)
        if bool(filename_result) is False:
            tell_user="标题只能是数字、字母或者汉字，不能含其它字符"
            return render.study_new_video(username,tell_user)
        else:
            x= web.input(videofile={})
        #videotitle=web.input()
            filedir=u"/alidata/www/cutvideo/static/video" #视频存储物理位置
        
            if 'videofile' in x:
                filepath=x.videofile.filename.replace('\\','/')
                all_filename=filepath.split('/')[-1]
                end_filename=all_filename.split(".")[-1]
                if end_filename!='ogv':
                    tell_user="再次提醒：本系统只允许上传扩展名为.ogv格式的视频文件"
                    return render.study_new_video(username,tell_user)
            #head_filename=videotitle.videotitle
                filename=head_filename+"."+end_filename
                fout = open(filedir +'/'+ filename,'wb')
                fout.write(x.videofile.file.read()) 
                fout.close() 
        #editor=videotitle.username
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
"""
app_study_new_video=web.application(urls, globals())

