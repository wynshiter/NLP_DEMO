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
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义blog 文章对象:
class CSDN_Blog(Base):
    # 表的名字:
    __tablename__ = 'CSDN_Blog'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    contend = Column(String(1024000))
    create_time = Column(String(20))
    click_number = Column(String(20))
    comment_number = Column(String(20))

    def __repr__(self):
        return "<CSDN_Blog(id='%s', name='%s', contend='%s', create_time='%s', click_number='%s',comment_number='%s')>" % (
            self.id, self.name,self.contend,self.create_time,self.click_number,self.comment_number)


str_path_sqlite = 'sqlite:///NLP_demo.db?check_same_thread=False'


# def init_sqlalchemy(dbname = 'sqlite:///demo.db',Echo=True):
#     global engine
#     engine = create_engine(dbname, echo=Echo)
#     DBSession.remove()
#     DBSession.configure(bind=engine, autoflush=False, expire_on_commit=False)
#     Base.metadata.drop_all(engine)
#     Base.metadata.create_all(engine)
#
#
# init_sqlalchemy(str_path_sqlite)




# 初始化数据库连接:
#Windows alternative using raw string
#engine = create_engine(r'sqlite:///C:\path\to\foo.db')
engine = create_engine(str_path_sqlite, echo=True)
# format 2 内存数据库
#engine = create_engine('sqlite:///:memory:', echo=True)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建Session类实例
session = DBSession()
# 创建数据表
Base.metadata.create_all(engine)
# 创建User类实例
ed_user = CSDN_Blog(id='1', name='2', contend='3', create_time='4', click_number='5',comment_number='6')

# 将该实例插入到users表
session.add(ed_user)

# # 一次插入多条记录形式
# session.add_all(
#     [CSDN_Blog(name='wendy', fullname='Wendy Williams', password='foobar')]
# )

# 当前更改只是在session中，需要使用commit确认更改才会写入数据库
session.commit()

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

