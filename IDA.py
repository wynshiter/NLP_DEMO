# encoding: utf-8
'''
@author: season
@contact: shiter@live.cn

@file: IDA.py
@time: 2018/12/9 23:33
@desc:
'''


import  jieba


file_path = u'''D:\work\知识库\医院\hospital_info20180605.csv'''
col_names = ["addr","bus_qq_acc","email","establish_date","fax","hosp_type","insur_type","level","name","qq_acc","serv_object","serv_property","serv_type","summary","tel","web","wechat_acc","weibo","zipcode","lng","lat","geohash"]
data = pd.read_csv(file_path, names=col_names, header = 0,engine='python', dtype=str,encoding='utf-8')
# 返回前n行
# 返回前n行
first_rows = data.head(n=2)
print(first_rows)

data.info()

#分词，暂时没有去停用词
def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))


#没有简介的医院替换句号
data['summary'] = data['summary'].fillna('.').astype('str')
#新增分词后的字段
data["content_cutted"] =data['summary'].apply(chinese_word_cut)

data.content_cutted.head()

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
#从文本中提取1000个最重要的特征关键词
n_features = 1000
tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                max_features=n_features,
                                stop_words='english',
                                max_df = 0.5,
                                min_df = 10)
tf = tf_vectorizer.fit_transform(data.content_cutted)

from sklearn.decomposition import LatentDirichletAllocation

n_topics = 5
lda = LatentDirichletAllocation(n_topics=n_topics, max_iter=50,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)


lda.fit(tf)

#
def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()


n_top_words = 20

tf_feature_names = tf_vectorizer.get_feature_names()
print_top_words(lda, tf_feature_names, n_top_words)

import pyLDAvis
import pyLDAvis.sklearn
pyLDAvis.enable_notebook()
pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)


data = pyLDAvis.sklearn.prepare(lda, tf, tf_vectorizer)
pyLDAvis.show(data)
#pyLDAvis.display()