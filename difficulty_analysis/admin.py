from django.contrib import admin

# Register your models here.
from .models import Tag, Vocabulary, Sentence

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    pass

@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('word', 'get_tags', 'level', 'created_at', 'updated_at', 'used_status')
    pass

    def get_tags(self, obj):
         return "\n, ".join([tag.name for tag in obj.tags.all()])

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('text', 'memo', 'created_at', 'updated_at', 'used_status')
    pass
