# encoding: utf-8
'''
@author: season
@contact: seasonwang@insightzen.com

@file: spider_for_csdn.py
@time: 2018/10/16 21:32
@desc:
使用时候，需要替换博客链接

'''
import io

import urllib
from urllib.request import urlopen
from urllib import request
from bs4 import BeautifulSoup
import random
import re
from lxml import etree
import socket

from sqlalchemy import Column, String, create_engine,TEXT, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

import sys
import os

CURRENT_URL = os.path.dirname(__file__)
PARENT_URL = os.path.abspath(os.path.join(CURRENT_URL, os.pardir))

sys.path.append(PARENT_URL)

###-----以下导入 其他文件夹的包
from Database import blog
from src import assistance_tool
from Database import My_sqlite


STR_PAGE_URL_PREFIX = 'https://blog.csdn.net/wangyaninglm/'

COPYRIGHT_NOTICE = '版权声明：本文为博主原创文章，未经博主允许不得转载。'

socket.setdefaulttimeout(5000)  # 设置全局超时函数

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]


# windows 创建文件替换特殊字符
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title.replace('\r', '').replace('\n', '').replace('\t', '')


# csdn 的网页解析
def get_Content(blog_obj, contend_box_id, title_id, contend_id):
    try:
        blog_url = STR_PAGE_URL_PREFIX + '''article/details/''' + blog_obj.id
        randdom_header = random.choice(my_headers)
        req = urllib.request.Request(blog_url)
        req.add_header("User-Agent", randdom_header)
        req.add_header("GET", blog_url)

        response = urllib.request.urlopen(req)
        # html = response.read().decode('utf-8')
        #     # print(html)
        page_content = response.read()
        #下面代码使用了两种方法混合解析，后序还要探索更合适一些的办法
        bsObj = BeautifulSoup(page_content, "html.parser")
        etree_obj = etree.HTML(page_content)



        title = bsObj.findAll(name='h1', attrs={'class': title_id})
        str_title = validateTitle(title[0].get_text() + '.txt')

        xpath_label = '''//*[@id="mainBox"]/main/div[1]/div/div/div[2]/div[1]/span[3]/span[1]'''
        label = ','.join([obj.text for obj in etree_obj.xpath(xpath_label)])

        label= label+','+','.join([obj.text for obj in bsObj.findAll(name='a', attrs={'class': 'tag-link'})])

        f_blog = open(r'../blog/' + str_title, 'w', encoding='utf-8')
        str_content = ''
        for content_box in bsObj.findAll(name='div', attrs={'class': contend_box_id}):  # 正则表达式匹配博客包含框 标签

            for content in bsObj.findAll(name='div', id=contend_id):  # 内容,注意此处用了bsobj 因为如果缩小范围可能找不到

                str_content = (content.get_text() + '\n').replace(COPYRIGHT_NOTICE,'').replace(blog_url,'')
                f_blog.write(str_content)

        f_blog.close()
        blog_obj.title = title[0].get_text()
        blog_obj.label = label
        blog_obj.content = str_content

        response.close()  # 注意关闭response
    except OSError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e.reason)
    except Exception as e:
        print(e)


# 获取每个分页的博客链接，及创建时间，评论数量
def getPage_AllBlogLinks(url, url_pattern):
    try:

        randdom_header = random.choice(my_headers)
        req = urllib.request.Request(url)
        req.add_header("User-Agent", randdom_header)
        req.add_header("GET", url)
        response = urllib.request.urlopen(req)
        # html = response.read().decode('utf-8')
        #     # print(html)
        page_content = response.read()
        bsObj = BeautifulSoup(page_content, "html.parser")
        # etree_obj = etree.HTML(page_content)

        list_blog_obj = []

        list_page_title = bsObj.findAll(name='div', attrs={'class': 'article-item-box csdn-tracking-statistics'})
        page_link_pattern = "(" + url_pattern + ")"

        for page_obj in list_page_title:
            page_link = page_obj.findAll(name='a')[0].attrs['href']

            if re.match(page_link_pattern, page_link):  # csdn 反爬虫机制，给分页中隐藏了一个不显示的博客链接，所以要进行剔除
                id = page_link.split('/')[-1]
                create_time = page_obj.findAll(name='div')[0].findAll(name='span')[0].get_text()
                click_number = page_obj.findAll(name='div')[0].findAll(name='span')[1].get_text().replace('阅读数：', '')
                comment_number = page_obj.findAll(name='div')[0].findAll(name='span')[2].get_text().replace('评论数：', '')
                # 构造博客类的对象
                temp_blog = blog.CSDN_Blog(id=id, title='', content='', create_time=create_time,
                                                click_number=click_number, comment_number=comment_number, label='')

                list_blog_obj.append(temp_blog)
            else:
                pass
        response.close()  # 注意关闭response
        return list_blog_obj

    except OSError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e.reason)
    except Exception as e:
        print(e)


# 先获取所有博客的id 和链接，然后按照链接依次爬取
def main():
    start_time = assistance_tool.set_starttime()

    # 得到CSDN博客某一个分页的所有文章的链接

    list_page_str = STR_PAGE_URL_PREFIX + 'article/list/'
    # 装载博客类的所有对象
    list_blog_obj = []

    # 获取分页数量, 由于这部分分页代码为自动生成 ，所以需要使用 selenium，如果觉的麻烦可以直接把分页数量作为输入

    # import spider_selenium
    # page_index = spider_selenium.get_csdn_page_index(str_page_url_prefix,'ui-pager')
    page_index = 17
    # 输入分页数据量
    for i in range(1, page_index + 1):

        temp_blog_obj = getPage_AllBlogLinks((list_page_str + str(i)), STR_PAGE_URL_PREFIX)
        list_blog_obj.extend(temp_blog_obj)


    for blog_obj in list_blog_obj:
        # 参数分别 为,博客对象，博客，标题名，内容的div 名称
        get_Content(blog_obj, 'blog-content-box', 'title-article', 'article_content')

    print(len(list_blog_obj))

    Base = declarative_base()
    DBSession = scoped_session(sessionmaker())
    engine = None

    engine = My_sqlite.init_sqlalchemy('sqlite:///../Database/NLP_demo.db?check_same_thread=False', True, blog.CSDN_Blog(), DBSession)
    My_sqlite.insert_list(list_blog_obj,DBSession)

    assistance_tool.get_runtime(start_time)


if __name__ == '__main__':
    main()




