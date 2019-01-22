# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: visualization.py
@time: 2019/1/20 22:48
@desc: 可视化相关代码

'''




import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
#print(parentUrl)
sys.path.append(parentUrl)

import pandas as pd
import numpy as np

import sqlite3

# 导入:
from sqlalchemy import Column, String, create_engine,TEXT, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker


###-----以下导入 其他文件夹的包
from Database import blog
from src import assistance_tool
from Database import My_sqlite

#可以使用pandas read_sql
def database_to_pandas_Dataframe(str_path_sqlite):
     # sql_order is a string
    try:
        conn = sqlite3.connect(str_path_sqlite)
        str_sql = '''select * from CSDN_Blog'''
        frame = pd.read_sql(str_sql, conn, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None,
                 chunksize=None)



        return  frame
    except:  # , e:
        frame = pd.DataFrame()
        # print e
        # continue


    return pdf


def main():
    # list_customer = ...
    # 创建对象的基类:
    Base = declarative_base()
    DBSession = scoped_session(sessionmaker())
    engine = None

    str_path_sqlite = 'sqlite:///../Database/NLP_demo.db?check_same_thread=False'

    DBSession = My_sqlite.get_conn('sqlite:///../Database/NLP_demo.db?check_same_thread=False', True, blog.CSDN_Blog())

    table_and_column_name = blog.CSDN_Blog
    #filter = (blog.CSDN_Blog.title == '2')

    all_blog = DBSession.query(table_and_column_name).all()
    print(one_blog)


if __name__ == '__main__':
    main()