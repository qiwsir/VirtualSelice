#! /usr/bin/evn python
# -*-coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import web
import hashlib
import random
import datetime,time

from model.db import *
from model.comfunction import *


def insert_newuser_into_commonuser(newusername,md5_password,userrole):
    db=conn()
    db.query("insert into commonuser set username='%s',password='%s',role='%s'"%(newusername,md5_password,userrole))


def insert_video_into_videoname(videoname,head_filename,editor,attachment):
    db=conn()
    db.query("insert into videoname set videoname='%s',headvideoname='%s',editor='%s',edittime=now(),attachment='%s',postnumber='-1'"%(videoname,head_filename,editor,attachment))


def insert_post_into_bbs(bbstablename,content,poster):
    db=conn()
    db.query("insert into %s set content='%s',poster='%s',posttime=now()"%(bbstablename,content,poster))


def create_table_video_chip(tablename):
    db=conn()
    db.query("create table %s(id int(2) not null primary key auto_increment,starttime text,endtime text,title text) default charset=utf8"%tablename)


def create_table_video_attach(tablename):
    db=conn()
    db.query("create table %s(id int(2) not null primary key auto_increment,attachname text) default charset=utf8"%tablename)

def create_table_video_bbs(tablename):
    db=conn()
    db.query("create table %s(id int(2) not null primary key auto_increment,content text,poster text,posttime datetime) default charset=utf8"%tablename)

def insert_video_chip_tablename_time(tablename,starttime,endtime):
    db=conn()
    db.query("insert into %s set starttime='%s',endtime='%s'"%(tablename,starttime,endtime))

def error_url():
    error_url=web.ctx.homedomain+"/error"
    raise web.seeother(error_url)
