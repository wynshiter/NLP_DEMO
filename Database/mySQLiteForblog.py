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


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import blog

CURRENT_URL = os.path.dirname(__file__)
PARENT_URL = os.path.abspath(os.path.join(CURRENT_URL, os.pardir))
sys.path.append(PARENT_URL)


STR_PATH_SQLITE = 'sqlite:///NLP_demo.db?check_same_thread=False'


def init_sqlalchemy(dbname='sqlite:///demo.db',
                    Echo=True,
                    Base=declarative_base(),
                    DBSession=scoped_session(sessionmaker())):

    engine = create_engine(dbname, echo=Echo)
    DBSession.remove()
    DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return  engine



def insert_list(list_obj, DBSession):
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


def get_conn(dbname='sqlite:///demo.db',
             Echo=True,
             Base=declarative_base(),
             DBSession=scoped_session(sessionmaker())):


    try:
        engine = create_engine(dbname, echo=Echo)
        DBSession.remove()
        DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)


        return DBSession


    except:
        DBSession.rollback()
        raise
    # finally:
    #     DBSession.close()


if __name__ == '__main__':
    # list_customer = ...
    #创建对象的基类:
    Base = declarative_base()
    DBSession = scoped_session(sessionmaker())
    engine = None

    # engine = init_sqlalchemy(str_path_sqlite,True,blog.CSDN_Blog(),DBSession)
    # ed_user = blog.CSDN_Blog(id = '1', title = '2', content = '3', create_time = '4', click_number = '5', comment_number = '6',label = '7')
    # DBSession.add(ed_user)
    # DBSession.flush()
    # DBSession.commit()
    # DBSession.close()
    # print(one_blog)
    # sql = "select * from CSDN_Blog"
    #
    # # sqlalchemy使用execute方法直接执行SQL
    # records = DBSession.execute(sql).first()
    # print(records)
    DBSession = get_conn(STR_PATH_SQLITE, True, blog.CsdnBlog())


    table_and_column_name = blog.CsdnBlog
    filter = (blog.CsdnBlog.title == 'TEST')

    one_blog = DBSession.query(table_and_column_name).filter(filter).all()
    print(one_blog)
