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
import sqlite3
import pandas as pd

###-----以下导入 其他文件夹的包


from Database import mySQLiteForblog,blog
import character_processing_tool




CURRENT_URL = os.path.dirname(__file__)
PARENT_URL = os.path.abspath(os.path.join(CURRENT_URL, os.pardir))
sys.path.append(PARENT_URL)



#可以使用pandas read_sql
def database_to_pandas_dataframe(str_path_sqlite):
    '''

    :param str_path_sqlite:  # sql_order is a string
    :return:
    '''

    try:
        conn = sqlite3.connect(str_path_sqlite)
        str_sql = '''select * from CSDN_Blog'''
        frame = pd.read_sql(str_sql, conn, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None,
                 chunksize=None)

        return  frame
    except Exception as e:
        print(e)

def add_feature_for_blog(dataframe):
    '''
    将文章内容分割，中文一列，英文字符一列，增加中文字数，英文字数，总字数
    :param dataframe: 从sqlite 中查出所有列，放在pandas dataframe 中
    :return:
    '''
    dataframe['content'] = dataframe['content'].astype(str)
    dataframe['中文'] = dataframe['content'].apply(character_processing_tool.get_all_chinese_string_and_punctuation)
    dataframe['英文'] = dataframe['content'].apply(character_processing_tool.contents_other_than_chinese_characters)
    dataframe['中文字数'] = dataframe['中文'].apply(len)
    dataframe['英文字数'] = dataframe['英文'].apply(len)

    return  dataframe




def main():
    '''
    主函数
    :return:
    '''

    # list_customer = ...
    # 创建对象的基类:
    # Base = declarative_base()
    # DBSession = scoped_session(sessionmaker())
    # engine = None

    str_path_sqlite = r'../Database/NLP_demo.db'

    #DBSession = My_sqlite.get_conn('sqlite:///../Database/NLP_demo.db?check_same_thread=False', True, blog.CSDN_Blog())

    #table_and_column_name = blog.CSDN_Blog
    #filter = (blog.CSDN_Blog.title == '2')

    #all_blog = DBSession.query(table_and_column_name).all()
    #print(one_blog)

    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)
    dataframe = database_to_pandas_dataframe(str_path_sqlite)
    dataframe = add_feature_for_blog(dataframe)
    print(dataframe.head(1))

if __name__ == '__main__':
    main()