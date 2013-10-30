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

#非数据库函数或者类

def md5_string(string):
    return hashlib.md5(string).hexdigest()


def create_handshake_md5(username):
    handshake="".join(random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(27))
    md5_handshake=md5_string(handshake)
    return md5_handshake


def del_cookie(username):
    web.setcookie("username","",-1)
    web.setcookie("handshake","",-1)


#--------------------
#数据库有关函数或者类
def check_table(tablename):
    db=conn()
    check_result=bool(db.query("show tables like '%s%%'"%(tablename)))
    return check_result
    

def select_all(tablename):
    db=conn()
    return db.query("select * from %s order by id desc"%(tablename))

def select_all_item(tablename):
    db=conn()
    return db.query("select * from %s" %tablename)

def select_all_by_where(tablename,column,columnvalue):
    db=conn()
    return db.query("select * from %s where %s='%s' order by id desc"%(tablename,column,columnvalue))

def select_all_perpage(tablename,offset,perpage):
    db=conn()
    return db.select("%s"%tablename, order="id DESC", offset=offset, limit=perpage)
#return db.query("select * from %s oder by id desc limit %s offset %s"%(tablename,perpage,offset))

def select_item_number(tablename):
    db = conn()
    return db.query("select COUNT(*) AS count from %s"%tablename)[0]

def select_one_column(column,tablename):
    db=conn()
    return db.query("select %s from %s order by id desc"%(column,tablename))


def select_one_column_by_where(column,tablename,wcolumn,wvalue):
    db=conn()
    return db.query("select %s from %s where %s='%s' order by id desc"%(column,tablename,wcolumn,wvalue))


def select_like_string(tablename,column,string):
    db=conn()
    return db.query("select * from %s where %s like '%%%s%%' order by id desc"%(tablename,column,string))


def select_like_string_by_where(tablename,column,string,wcolumn,wvalue):
    db=conn()
    return db.query("select * from %s where %s like '%%%s%%' and %s='%s' order by id desc"%(tablename,column,string,wcolumn,wvalue))

def select_where_no_equal(tablename,column,columnvalue):
    db=conn()
    return db.query("select * from %s where %s!='%s' order by id desc"%(tablename,column,columnvalue))


def select_where_no_equal2(tablename,column,columnvalue,limit,offset):
    db=conn()
    return db.query("select * from %s where %s!='%s' order by id desc limit %d offset %d"%(tablename,column,columnvalue,limit,offset))

def get_id_by_value(tablename, column, columnvalue):
    db=conn()
    one_id=db.query("select * from %s where %s='%s'"%(tablename,column,columnvalue))
    one_list=[]
    for one in one_id:
        one_list.append(one)
    return one_list


def update_value_by_where(tablename, column, value, wcolumn, wvalue):
    db=conn()
    db.query("update %s set %s='%s' where %s='%s'"%(tablename, column, value, wcolumn, wvalue))


def update_cookies_and_handshake(tablename,md5_handshake, username):
    db=conn()
    update_value_by_where(tablename,"handshake",md5_handshake,"username",username)
    web.setcookie("username",username)
    web.setcookie("handshake",md5_handshake)


def del_item(tablename, column, value):
    db=conn()
    db.query("delete from %s where %s='%s'"%(tablename, column, value))

def del_all(tablename):
    db=conn()
    db.query("delete from %s"%tablename)
    db.query("truncate table %s"%tablename)

def check_username_and_password(tablename,username,userpassword):
    md5_password=md5_string(userpassword)
    try:
        one_item=select_all_by_where(tablename,"username",username)
    except:
        return False
    if bool(one_item) is False:
        return False
    else:
        table_password=one_item[0].password
        if md5_password==table_password:
            return True
        else:
            return False
    

def check_username_logined(tablename, username):
    cookied_username=web.cookies().get("username")
    cookied_handshake=web.cookies().get("handshake")
    t={"cookies":web.cookies(),}
    return "%s"%t
    #if bool(cookied_username) and bool(cookied_handshake):
    #tabled_handshake=select_all_by_where(tablename, 'username', username)[0].handshake
    #if tabled_handshake==cookied_handshake:
    #    return "YES"
    #else:
    #    return "NO1"
    #else:
    #    return 'NO2'


def check_value_in_table(tablename, column, columnvalue):
    check_result=select_all_by_where(tablename, column, columndvalue)
    if bool(check_result) is True:
        return True
    else:
        return False


def insert_value(tablename,column,columnvalue):
    db=conn()
    db.query("insert into %s (%s) values ('%s')"%(tablename,column,columnvalue))
            
