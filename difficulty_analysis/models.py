from django.db import models
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='タグ名')
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='作成日')

    def __str__(self):
        return "%s %s" % (self.name, self.created_at)

class Vocabulary(models.Model):
    word = models.CharField(max_length=128, default='', verbose_name='単語/語彙')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='タグ')
    level = models.BigIntegerField(verbose_name='難易度')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日')
    used_status = models.BooleanField(default=False, verbose_name='利用可否')


docs = np.array([
        '牛乳        を 買う',
        'パン         を 買う',
        'パン         を 食べる',
        'お菓子       を 食べる',
        '本           を 買う',
        'パン と お菓子 を 食べる',
        'お菓子        を 買う',
        'パン と パン   を 食べる'
        ])

class Sentence(models.Model):
    title = models.CharField(max_length=128, default='', verbose_name='タイトル')
    text = models.TextField(max_length=100000, default='', verbose_name='文章')
    memo = models.CharField(max_length=1024, default='', verbose_name='メモ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日')
    used_status = models.BooleanField(default=False, verbose_name='利用可否')

    @classmethod
    def analysis(cls):
        print("単語マッチ分析 : ", cls.pk)
        return str("")

    @classmethod
    def analysis_tf_idf(cls):
        print("TF-IDF分析 : ", cls.pk)

        # 参考　URL : http://ailaby.com/tfidf/
        # ベクトル化
        vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')
        vecs = vectorizer.fit_transform(docs)
        print(vecs.toarray())
        # クラスタリング
        clusters = KMeans(n_clusters=2, random_state=0).fit_predict(vecs)
        for doc, cls in zip(docs, clusters):
            print(cls, doc)

        return str("")