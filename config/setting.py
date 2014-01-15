#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
The Code was made by Yeashape Software.The Author is QiWei.
Our website is www.itdiffer.com.The Email is it@itdiffer.com
"""

import web
t_globals={'datestr':web.datestr,'cookies':web.cookies}

render=web.template.render("templates",base="base",globals=t_globals)

