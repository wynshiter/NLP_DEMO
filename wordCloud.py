# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: wordCloud.py
@time: 2018/11/6 22:38
@desc:
'''



import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import jieba.analyse
import file_operator


file_path = r'''blog'''

file_list = file_operator.all_Absolute_pathfile_name(file_path,'.txt')



str_summary = ''

def get_all_strFromTxt(file_name):
    str_blog = ''
    with open(file_name,'r',encoding='utf-8') as f:
        str_blog = f.read()
    return str_blog

for i in file_list:
    str_summary = str_summary + get_all_strFromTxt(i)



# wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
# wl_space_split = " ".join(wordlist_after_jieba)

#print(wl_space_split)

stop_words = [' ','版权','声明','博主','原创','转载','本文','未经']


def getTopkeyWordsTFIDF(stop_word_file_path,topK=100,content = ''):
    try:
        jieba.analyse.set_stop_words(stop_word_file_path)
        tags = jieba.analyse.extract_tags(content, topK, withWeight=True,allowPOS=('ns', 'n', 'vn', 'v'))
        for v, n in tags:
            print (v + '\t' + str((n )))
            top_word_dict_TFIDF[v] = n * 100
            #tfidf *100 作为词频
    except Exception as e:
        print(e)
    finally:
        pass


def getTopkeyWordsTextRank(stop_word_file_path, topK=100, content=''):
    try:
        jieba.analyse.set_stop_words(stop_word_file_path)

        tags = jieba.analyse.textrank(content, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
        for v, n in tags:
            print(v + '\t' + str(int((n))))
            top_word_dict_TEXTRANK[v] = n * 100
            # tfidf *100 作为词频
    except Exception as e:
        print(e)
    finally:
        pass


top_word_dict_TFIDF = {}
top_word_dict_TEXTRANK = {}

getTopkeyWordsTFIDF('stop_words.txt',150,str_summary)
getTopkeyWordsTextRank('stop_words.txt',150,str_summary)
print(top_word_dict_TEXTRANK)

# my_wordcloud = WordCloud(background_color = "white",width = 1000,height = 860,font_path = "msyh.ttc",
#                 # 不加这一句显示口字形乱码
#                 margin = 2,
# max_words=150, # 设置最大现实的字数
#     stopwords=stop_words,# 设置停用词
#     max_font_size=250,# 设置字体最大值
#     random_state=50# 设置有多少种随机生成状态，即有多少种配色方案
#
#                          )
# #my_wordcloud = my_wordcloud.generate(wl_space_split)
# # max_words=2000, # 设置最大现实的字数
# #     stopwords=STOPWORDS,# 设置停用词
# #     max_font_size=150,# 设置字体最大值
# #     random_state=30# 设置有多少种随机生成状态，即有多少种配色方案
# my_wordcloud = my_wordcloud.generate_from_frequencies(top_word_dict)

# 可以指定字体，或者按照词频生成
def show_WordCloud(str_all,top_word):
    wordlist_after_jieba = jieba.cut(str_all, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    my_wordcloud = WordCloud(background_color = "white",width = 1000,height = 860,font_path = "msyh.ttc",
                # 不加这一句显示口字形乱码
                margin = 2,
    max_words=150, # 设置最大现实的字数
    stopwords=stop_words,# 设置停用词
    max_font_size=250,# 设置字体最大值
    random_state=50# 设置有多少种随机生成状态，即有多少种配色方案

    )
    #my_wordcloud = my_wordcloud.generate(wl_space_split)
    my_wordcloud = my_wordcloud.generate_from_frequencies(top_word)

    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()

show_WordCloud(str_summary,top_word_dict_TFIDF)


