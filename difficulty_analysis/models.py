from django.db import models

class Vocabulary(models.Model):
    word = models.CharField(max_length=128, default='')
    level = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    used_status = models.BooleanField(default=False)

class Sentence(models.Model):
    title = models.CharField(max_length=128, default='')
    text = models.TextField(max_length=100000, default='')
    memo = models.CharField(max_length=1024, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    used_status = models.BooleanField(default=False)
