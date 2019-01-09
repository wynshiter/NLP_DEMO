# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: __init__.py.py
@time: 2019/1/9 9:56
@desc:
'''

import sys
import os
currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))
#print(parentUrl)
sys.path.append(parentUrl)