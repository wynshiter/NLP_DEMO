# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: character_processing_tool.py
@time: 2019/3/11 16:18
@desc:对文本字符串进行一些操作，中文提取，英文提取等
汉字处理的工具:
判断unicode是否是汉字，数字，英文，或者其他字符。
全角符号转半角符号。
'''



import re


def is_chinese(uchar):
    '''
    判断一个unicode是否是汉字
    :param uchar:
    :return:
    '''
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


def is_number(uchar):
    '''
    判断一个unicode是否是数字
    :param uchar:
    :return:
    '''
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False




def is_alphabet(uchar):
    '''
    判断一个unicode是否是英文字母
    :param uchar:
    :return:
    '''
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

def get_all_english_string(temp_string):
    '''
    获取一个字符串的所有英文字符,包括空格
    :param temp_string:
    :return:
    '''
    unicodeEnglish = re.compile(r'[\u0041-\u005a,\u0061-\u007a,\u0020]')
    english_string = "".join(unicodeEnglish.findall(temp_string))
    return  english_string

def get_all_chinese_string(temp_string):
    '''
    获取一个字符串的所有英文字符,包括空格
    :param temp_string:
    :return:
    '''
    unicodeChinese = re.compile(r'[\u4e00-\u9fa5]')
    english_string = "".join(unicodeChinese.findall(temp_string))
    return  english_string


def is_other(uchar):
    '''
    判断是否是（汉字，数字和英文字符之外的）其他字符
    :param uchar:
    :return:
    '''
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return True
    else:
        return False





def B2Q(uchar):
    '''
    半角转全角
    :param uchar:
    :return:
    '''
    inside_code = ord(uchar)
    if inside_code < 0x0020 or inside_code > 0x7e:  # 不是半角字符就返回原来的字符
        return uchar
    if inside_code == 0x0020:  # 除了空格其他的全角半角的公式为:半角=全角-0xfee0
        inside_code = 0x3000
    else:
        inside_code += 0xfee0
    return unichr(inside_code)


"""全角转半角"""


def Q2B(uchar):
    inside_code = ord(uchar)
    if inside_code == 0x3000:
        inside_code = 0x0020
    else:
        inside_code -= 0xfee0
    if inside_code < 0x0020 or inside_code > 0x7e:  # 转完之后不是半角字符返回原来的字符
        return uchar
    return unichr(inside_code)





def stringQ2B(ustring):
    '''
    把字符串全角转半角
    :param ustring:
    :return:
    '''
    return "".join([Q2B(uchar) for uchar in ustring])





def convert_toUnicode(string):
    '''
    """将UTF-8编码转换为Unicode编码"""
    :param string:
    :return:
    '''
    ustring = string
    if not isinstance(string, str):
        ustring = string.decode('UTF-8')
    return ustring


if __name__ == "__main__":

    ustring1 = u'收割季节 麦浪和月光 洗着快镰刀'
    string1 = 'Sky0天地Earth1*'
    string2 = "China's Legend Holdings will split its several business arms to go public on stock markets, " \
              "the group's president Zhu Linan said on Tuesday." \
              "该集团总裁朱利安周二表示，中国联想控股将分拆其多个业务部门在股市上市。"

    ustring1 = convert_toUnicode(ustring1)
    string1 = convert_toUnicode(string1)

    print(get_all_english_string(string2))
    # for item in string1:
    #     print(is_chinese(item))
    #     print(is_number(item))
    #     print(is_alphabet(item))
    #     print(is_other(item))

