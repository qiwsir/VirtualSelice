#!/usr/bin/evn python
# -*- conding:utf-8 -*-

import web

def conn():
    return web.database(dbn="mysql",host="localhost",db="cutvideo",user="root",pw="123123",charset="utf8",use_unicode=False)
