#-*- coding:utf-8 -*-
from django.contrib import admin
from models import  *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','description','click_count',)
    list_display_links = ('title','description')
    list_editable = ('click_count',)
    list_filter = ('is_recommend',)

    fieldsets = (
        (None, {
            'fields': ( 'title','description', 'content','user','category','tag')
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend')
        }),
    )

    class Media:
        js = (
            '/static/admin/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/admin/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/admin/js/kindeditor-4.1.10/config.js',
        )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content','user','article',)
    list_editable = ('content',)





admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Links)
admin.site.register(Ip)
