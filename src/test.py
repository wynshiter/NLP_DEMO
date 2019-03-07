# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: test.py
@time: 2019/1/7 10:34
@desc:
'''

import myLog

# logging.basicConfig(                                                                #通过具体的参数来更改logging模块默认行为；
#     level=logging.DEBUG,                                                            #设置告警级别为ERROR；
#     format="%(asctime)s---%(lineno)s----%(name)s: %(message)s",                     #自定义打印的格式；
#     filename="spider_log.txt",                                                      #将日志输出到指定的文件中；
#     filemode="a",                                                                   #以追加的方式将日志写入文件中，w是以覆盖写的方式哟;
# )



def main():
    log = myLog.Logger('all.log', level='debug')
    # log.logger.debug('debug')
    # log.logger.info('info')
    # log.logger.warning('警告')
    # log.logger.error('报错')
    # log.logger.critical('严重')
    myLog.Logger('error.log', level='error').logger.error('error')


if __name__ == '__main__':
    main()