# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: sqlite.py
@time: 2019/1/2 17:01
@desc:
'''

import sqlite3

with sqlite3.connect(":memory:") as con:

    c = con.cursor()

    c.execute(''' CREATE TABLE blog_content(data text,code text)''')
    c.execute('''INSERT INTO blog_content VALUES ('LALAL','DDD')''')
    c.execute('''SELECT * FROM blog_content''')
    print(c.fetchone())