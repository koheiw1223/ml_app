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
    list_display = ('text', 'memo', 'created_at', 'updated_at', 'used_status', 'analysis_actions')
    pass

    def analysis_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">難易度分析</a>&nbsp;',
            obj.analysis()
        )

    analysis_actions.short_description = 'Action'
