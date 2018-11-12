#!/usr/bin/env python
#-*- coding:utf-8 -*-

from scrapy.cmdline import execute
import os
import sys

#添加当前项目的绝对地址
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#执行 scrapy 内置的函数方法execute，  使用 crawl 爬取并调试，最后一个参数maomaogougou是我的爬虫名
execute(['scrapy', 'crawl', 'maomaogougou'])