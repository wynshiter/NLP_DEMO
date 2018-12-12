# encoding: utf-8
'''
@author: season
@contact: seasonwang@insightzen.com

@file: spider_for_csdn.py
@time: 2018/10/16 21:32
@desc:
'''
import io
import os
import sys
import urllib
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
import datetime
import random
import re
import requests
import socket

socket.setdefaulttimeout(5000)  # 设置全局超时函数

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')
headers1 = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

# 得到CSDN博客某一个分页的所有文章的链接
articles = set()


def getArticleLinks(pageUrl):
    # 设置代理IP
    # 代理IP可以上http://ip.zdaye.com/获取
    proxy_handler = urllib.request.ProxyHandler({'post': '49.51.195.24:1080'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)
    urllib.request.install_opener(opener)
    # 获取网页信息
    req = request.Request(pageUrl, headers=headers1 or headers2 or headers3)
    html = urlopen(req)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    global articles

    for articlelist in bsObj.findAll("h4"):  # 正则表达式匹配每一篇文章链接(比较硬编码h4 这个四级标题里面藏了所有链接)
        # print(articlelist)
        if 'href' in articlelist.a.attrs:
            if articlelist.a.attrs["href"] not in articles:
                # 遇到了新界面
                newArticle = articlelist.a.attrs["href"]
                # print(newArticle)
                articles.add(newArticle)
                #print(newArticle)


# 得到CSDN博客每一篇文章的文字内容,title-article 为标题，id="article_content" 里面为文章内容
def getArticleText(articleUrl,articletitle):
    # 设置代理IP
    # 代理IP可以上http://ip.zdaye.com/获取
    proxy_handler = urllib.request.ProxyHandler({'https': '120.132.52.89:8888'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)
    urllib.request.install_opener(opener)
    # 获取网页信息
    req = request.Request(articleUrl, headers=headers1 or headers2 or headers3)
    print(articleUrl)
    html = urlopen(req)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    # 获取文章的文字内容
    for textlist in bsObj.findAll(articletitle):  # 正则表达式匹配文字内容标签
        print(textlist.get_text())
        # data_out(textlist.get_text())


# 得到CSDN博客某个博客主页上所有分页的链接，根据分页链接得到每一篇文章的链接并爬取博客每篇文章的文字
pages = set()


def getPageLinks(bokezhuye):
    # 设置代理IP
    # 代理IP可以上http://ip.zdaye.com/获取
    proxy_handler = urllib.request.ProxyHandler({'post': '49.51.195.24:1080'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    opener = urllib.request.build_opener(urllib.request.HTTPHandler, proxy_handler)
    urllib.request.install_opener(opener)
    # 获取网页信息
    req = request.Request(bokezhuye, headers=headers1 or headers2 or headers3)
    html = urlopen(req)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    # 获取当前页面(第一页)的所有文章的链接
    getArticleLinks(bokezhuye)
    # 去除重复的链接
    global pages
    for pagelist in bsObj.findAll("a", href=re.compile("^/([A-Za-z0-9]+)(/article)(/list)(/[0-9]+)*$")):  # 正则表达式匹配分页的链接
        if 'href' in pagelist.attrs:
            if pagelist.attrs["href"] not in pages:
                # 遇到了新的界面
                newPage = pagelist.attrs["href"]
                # print(newPage)
                pages.add(newPage)
                # 获取接下来的每一个页面上的每一篇文章的链接
                newPageLink = "http://blog.csdn.net/" + newPage
                getArticleLinks(newPageLink)
                # 爬取每一篇文章的文字内容
                for articlelist in articles:
                    newarticlelist = "http://blog.csdn.net/" + articlelist
                    print(newarticlelist)
                    getArticleText(newarticlelist)



####获取到每一个分页列表的所有文章
str_page_url_prefix = 'https://blog.csdn.net/wangyaninglm/'

list_page_str = str_page_url_prefix + 'article/list/'

#输入分页数据量
for i in range(1,18):

    #print(list_page_str + str(i))
    getPageLinks(list_page_str+ str(i))

page_url_list = []
page_url_pattern = "(" + str_page_url_prefix + "article/details)(/[0-9]+)*$"

for page_link in articles:

    if re.match(page_url_pattern,page_link):
        page_url_list.append(page_link)
    else:
        pass

#print(page_url_list)
print(len(page_url_list))

dict_page_content = {'title':'','content':''}
list_page_content = []

import spider_for_403

for url in page_url_list:
    spider_for_403.get_Content(url,'blog-content-box','title-article','article_content')

#所有内容class：blog-content-box 标题class：title-article， 内容id： article_content


#需要改进的地方：title 中存在重复，
# 报错：EOF occurred in violation of protocol (_ssl.c:777)

