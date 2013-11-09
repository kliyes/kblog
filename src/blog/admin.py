#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from django.contrib import admin
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)


admin.site.register(Blog, BlogAdmin)
