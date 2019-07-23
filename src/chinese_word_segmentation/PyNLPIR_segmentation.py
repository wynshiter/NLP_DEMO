#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#-------------------------------------------------------------------------------
'''
@Author  :   {SEASON}
@License :   (C) Copyright 2013-2022, {OLD_IT_WANG}
@Contact :   {shiter@live.cn}
@Software:   PyCharm
@File    :   NLP_DEMO -- PyNLPIR_segmentation
@Time    :   2019/7/17 0:06
@Desc    :

'''
#-------------------------------------------------------------------------------

import pynlpir
pynlpir.open()

s = '欢迎科研人员、技术工程师、企事业单位与个人参与NLPIR平台的建设工作。'
s2 = '乙肝大三阳冠心病都是慢性病'
print(pynlpir.segment(s))
print(pynlpir.segment(s2))