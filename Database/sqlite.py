# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: sqlite.py
@time: 2019/1/2 17:01
@desc:  使用爬虫将数据缓存到本地数据库中，以便后续分析，可以只用pandas 直接加载数据库到dataframe
'''

import sqlite3

# 导入:
from sqlalchemy import Column, String, create_engine,TEXT, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

# 创建对象的基类:
Base = declarative_base()
DBSession = scoped_session(sessionmaker())
engine = None





str_path_sqlite = 'sqlite:///NLP_demo.db?check_same_thread=False'


def init_sqlalchemy(dbname = 'sqlite:///demo.db',Echo=True):
    global engine
    engine = create_engine(dbname, echo=Echo)
    DBSession.remove()
    DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)





if __name__ == '__main__':
    init_sqlalchemy(str_path_sqlite)
    #list_customer = ...
    ed_user = CSDN_Blog(id='1', name='2', contend='3', create_time='4', click_number='5', comment_number='6')
    DBSession.add(ed_user)
    DBSession.commit()
    one_blog = DBSession.query(CSDN_Blog).filter_by(id='1').first()
    print(one_blog)
   # DBSession.add_all(list_customer)

    #DBSession.commit()
    DBSession.close()






#
# # 初始化数据库连接:
# #Windows alternative using raw string
# #engine = create_engine(r'sqlite:///C:\path\to\foo.db')
# engine = create_engine(str_path_sqlite, echo=True)
# # format 2 内存数据库
# #engine = create_engine('sqlite:///:memory:', echo=True)
#
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)
#
# # 创建Session类实例
# session = DBSession()
# # 创建数据表
# Base.metadata.create_all(engine)
# # 创建User类实例
# ed_user = CSDN_Blog(id='1', name='2', contend='3', create_time='4', click_number='5',comment_number='6')
#
# # 将该实例插入到users表
# session.add(ed_user)
# #查询
# # 指定User类查询users表，查找name为'ed'的第一条数据
# our_user = session.query(CSDN_Blog).filter_by(id='1').first()
#
# print(our_user)
#
# # # 一次插入多条记录形式
# # session.add_all(
# #     [CSDN_Blog(name='wendy', fullname='Wendy Williams', password='foobar')]
# # )
#
# # 当前更改只是在session中，需要使用commit确认更改才会写入数据库
# session.commit()

#
# # 创建数据表
# Base.metadata.create_all(engine)

#
# with sqlite3.connect(":memory:") as con:
#
#     c = con.cursor()
#
#     c.execute(''' CREATE TABLE blog_content(data text,code text)''')
#     c.execute('''INSERT INTO blog_content VALUES ('LALAL','DDD')''')
#     c.execute('''SELECT * FROM blog_content''')
#     print(c.fetchone())

