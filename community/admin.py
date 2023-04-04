from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  # fields = ['name', 'title', 'contents', 'url', 'email']
  fieldsets = [
    ('제목', {'fields': ['title']}),
    ('내용', {'fields': ['contents']}),
    ('작성자 정보', {'fields': ['name', 'url', 'email']}),
    ('작성자ID', {'fields': ['owner'], 'classes':['collapse']})
    # ('', {'fields': ['']}),
  ]

  list_display = ('pk', 'title', 'url', 'cdate')
  list_filter = ['cdate']
  search_fields = ['title', 'contents']

# 전달인자 순서 중요
# admin.site.register(데이터모델클래스, 어드민클래스)
admin.site.register(Article, ArticleAdmin)