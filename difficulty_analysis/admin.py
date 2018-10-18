from django.contrib import admin

from .models import Tag, Vocabulary, Sentence
from django.utils.html import format_html

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

    get_tags.short_description = 'タグ'

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('text', 'memo', 'created_at', 'updated_at', 'used_status', 'analysis_action', 'tf_idf_action')
    pass

    def analysis_action(self, obj):
        return format_html(
            '<a class="button" href="{}">単語マッチ分析</a>&nbsp;',
            obj.analysis(),
        )
    analysis_action.short_description = ''
    analysis_action.allow_tags = True

    def tf_idf_action(self, obj):
        return format_html(
            '<a class="button" href="{}">TF-IDF分析</a>&nbsp;',
            obj.analysis_tf_idf(),
        )
    tf_idf_action.short_description = ''
    tf_idf_action.allow_tags = True

