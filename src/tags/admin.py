#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from django.contrib import admin
from tags.models import Tag, Category


class TagAdmin(admin.ModelAdmin):
    list_display = ['text', 'used_count']

    def used_count(self, obj):
        return obj.used_count()
    used_count.short_description = u'标签被引用次数'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['text', 'used_count']

    def used_count(self, obj):
        return obj.used_count()
    used_count.short_description = u'分类下博客数量'

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
