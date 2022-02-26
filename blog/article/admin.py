from django.contrib import admin
from article.models import articlemodel, commments
# Register your models here.


class articleadmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'adesc', 'pdate', 'mdate']


admin.site.register(articlemodel, articleadmin)


class commentsadmin(admin.ModelAdmin):
    list_display = ['article', 'content', 'cdate', 'comname']


admin.site.register(commments, commentsadmin)
