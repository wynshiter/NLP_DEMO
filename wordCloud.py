# encoding: utf-8
'''
@author: season
@contact: seasonwang@insightzen.com

@file: wordCloud.py
@time: 2018/11/6 22:38
@desc:
'''




import matplotlib.pyplot as plt
from wordcloud import WordCloud


import file_operator


file_path = u'''blog'''

file_list = file_operator.all_file_name_with_extension(file_path,'.txt')



str_summary = ''

for i in range(0, len(data)):
    #print(data.iloc[i]['summary'])
    str_summary = str_summary+data.iloc[i]['summary']

text_from_file_with_apath = str_summary

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

print(wl_space_split)

stop_words = [' ','现代','合性','医院','民医院']

top_word_dict = {}

def getTopkeyWordsTFIDF(stop_word_file_path,topK=100,content = ''):
    try:
        jieba.analyse.set_stop_words(stop_word_file_path)
        tags = jieba.analyse.extract_tags(content, topK, withWeight=True,allowPOS=('ns', 'n', 'vn', 'v'))
        for v, n in tags:
            print (v + '\t' + str((n )))
            top_word_dict[v] = n * 100
            #tfidf *100 作为词频
    except Exception as e:
        print(e)
    finally:
        pass

getTopkeyWordsTFIDF('stop_words.txt',150,text_from_file_with_apath)
print(top_word_dict)

my_wordcloud = WordCloud(background_color = "white",width = 1000,height = 860,font_path = "msyh.ttc",
                # 不加这一句显示口字形乱码
                margin = 2,
max_words=150, # 设置最大现实的字数
    stopwords=stop_words,# 设置停用词
    max_font_size=250,# 设置字体最大值
    random_state=50# 设置有多少种随机生成状态，即有多少种配色方案

                         )
#my_wordcloud = my_wordcloud.generate(wl_space_split)
# max_words=2000, # 设置最大现实的字数
#     stopwords=STOPWORDS,# 设置停用词
#     max_font_size=150,# 设置字体最大值
#     random_state=30# 设置有多少种随机生成状态，即有多少种配色方案
my_wordcloud = my_wordcloud.generate_from_frequencies(top_word_dict)



plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()