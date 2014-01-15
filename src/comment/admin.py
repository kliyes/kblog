#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-15, by Tom
#
#
from django.contrib import admin
from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'contact', 'name']
    list_filter = ['blog']

admin.site.register(Comment, CommentAdmin)
