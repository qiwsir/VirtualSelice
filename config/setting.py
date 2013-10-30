#!/usr/bin/env python
# -*-coding:utf-8-*-
import web
t_globals={'datestr':web.datestr,'cookies':web.cookies}

render=web.template.render("templates",base="base",globals=t_globals)

