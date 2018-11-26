import urllib
import urllib.request
import random
from bs4 import BeautifulSoup

import urllib.error

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]

import re

#windows 创建文件替换特殊字符
def validateTitle(title):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替换为下划线
    return new_title.replace('\r','').replace('\n','').replace('\t','')

#csdn 的网页解析
def get_Content(url,contend_box_id,title_id,contend_id):
    try:
        randdom_header = random.choice(my_headers)

        req = urllib.request.Request(url)

        req.add_header("User-Agent", randdom_header)
        req.add_header("GET", url)

        response = urllib.request.urlopen(req)
    # html = response.read().decode('utf-8')
    #     # print(html)
        bsObj = BeautifulSoup(response.read(), "html.parser")
    # 获取文章的文字内容
    # 获取网页信息
    #此处逻辑应为：首先获取文章box 的id 之后获取，title 的，之后是content 的
    # 将每一篇博客分别保存为一个文件
        title = bsObj.findAll(name='h1',attrs={'class':title_id})
        str_title = validateTitle(title[0].get_text() + '.txt')
        print(str_title.encode('gbk'))
        f_blog = open('blog//' + str_title, 'w', encoding='utf-8')

        for content_box in bsObj.findAll(name='div',attrs={'class':contend_box_id}):  # 正则表达式匹配博客包含框 标签

            for contend in bsObj.findAll(name='div',id = contend_id):#内容,注意此处用了bsobj 因为如果缩小范围可能找不到

                str_content = 'content' + '\n'+ contend.get_text() + '\n'
                f_blog.write(str_content)

        f_blog.close()

        response.close()  # 注意关闭response
    except OSError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e.reason)

# url = 'https://blog.csdn.net/wangyaninglm/article/details/45676169'
# #
# get_Content(url,'blog-content-box','title-article','article_content')