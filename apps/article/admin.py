from django.contrib import admin

from apps.article.models import Article, Specification

admin.site.register(Article)
admin.site.register(Specification)
