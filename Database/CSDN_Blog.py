# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: CSDN_Blog.py
@time: 2019/1/7 10:34
@desc:
'''

import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
#print(parentUrl)
sys.path.append(parentUrl)

from sqlalchemy import Column, String, create_engine,TEXT, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()
# 定义blog 文章对象:
class CSDN_Blog(Base):
    # 表的名字:
    __tablename__ = 'CSDN_Blog'
    column_name = ['id','title','contend','create_time','click_number','comment_number','label']

    # 表的结构:

    id = Column(String(64), primary_key=True,unique=True)
    title = Column(String(256))
    contend = Column(TEXT)
    create_time = Column(String(64))
    click_number = Column(String(64))
    comment_number = Column(String(64))
    label = Column(String(256))

    # def __int__(self, id, title,contend,create_time,click_number,comment_number,label):
    #     self.id = id
    #     self.title = title
    #     self.contend = contend
    #     self.create_time =create_time
    #     self.click_number = click_number
    #     self.comment_number = comment_number
    #     self.label = label

    def __repr__(self):
        return "<CSDN_Blog(id ='%s' , title = '%s', contend = '%s',create_time = '%s', click_number = '%s',comment_number = '%s',label = '%s' )>" % (
            self.id, self.title,self.contend,self.create_time,self.click_number,self.comment_number,self.label)


