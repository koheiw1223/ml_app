from django.db import models

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

class Sentence(models.Model):
    title = models.CharField(max_length=128, default='', verbose_name='タイトル')
    text = models.TextField(max_length=100000, default='', verbose_name='文章')
    memo = models.CharField(max_length=1024, default='', verbose_name='メモ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日')
    used_status = models.BooleanField(default=False, verbose_name='利用可否')

    @classmethod
    def analysis(cls):
        print("難易度分析 : ", cls.pk)
        return str("")