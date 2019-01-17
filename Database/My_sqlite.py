# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: sqlite.py
@time: 2019/1/2 17:01
@desc:  使用爬虫将数据缓存到本地数据库中，以便后续分析，可以只用pandas 直接加载数据库到dataframe
    参考：https://www.cnblogs.com/lsdb/p/9835894.html
'''

import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
#print(parentUrl)
sys.path.append(parentUrl)

import sqlite3

# 导入:
from sqlalchemy import Column, String, create_engine,TEXT, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker
import blog




str_path_sqlite = 'sqlite:///NLP_demo.db?check_same_thread=False'


def init_sqlalchemy(dbname = 'sqlite:///demo.db',Echo=True,Base= declarative_base(),DBSession = scoped_session(sessionmaker())):

    engine = create_engine(dbname, echo=Echo)
    DBSession.remove()
    DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return  engine



def insert_list(list_obj,DBSession):
    try:
        #init_sqlalchemy(str_path_sqlite)
        DBSession.add_all(list_obj)
        DBSession.flush()
        DBSession.commit()

    except:
        DBSession.rollback()
        raise
    finally:
        DBSession.close()


def get_conn():
#https://www.jianshu.com/p/25fde93c2fb9
    conn = sqlite3.connect('NLP_demo.db')
    cursor = conn.cursor()
# 执行查询语句:
    cursor.execute('select * from CSDN_Blog ')

# 获得查询结果集:
    values = cursor.fetchall()
    print(values)


if __name__ == '__main__':
    # list_customer = ...
    #创建对象的基类:
    Base = declarative_base()
    DBSession = scoped_session(sessionmaker())
    engine = None

    engine = init_sqlalchemy(str_path_sqlite,True,blog.CSDN_Blog(),DBSession)
    ed_user = blog.CSDN_Blog(id = '1', title = '2', content = '3', create_time = '4', click_number = '5', comment_number = '6',label = '7')
    DBSession.add(ed_user)
    DBSession.flush()
    DBSession.commit()
    DBSession.close()

    table_and_column_name = blog.CSDN_Blog
    filter = (blog.CSDN_Blog.title == '2')



    one_blog = DBSession.query(table_and_column_name).first()
    print(one_blog)
    sql = "select * from CSDN_Blog"

    # sqlalchemy使用execute方法直接执行SQL
    records = DBSession.execute(sql).first()
    print(records)
    get_conn()



