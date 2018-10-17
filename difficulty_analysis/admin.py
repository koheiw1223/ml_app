from django.contrib import admin

# Register your models here.
from .models import Vocabulary, Sentence

@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('word', 'level', 'created_at', 'updated_at', 'used_status')
    pass

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('text', 'memo', 'created_at', 'updated_at', 'used_status')
    pass
