#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from django.contrib import admin
from blog.models import Blog
from django.contrib.sessions.models import Session


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'cate', 'is_draft', 'update_time']
    actions = ['make_draft', 'make_pub']
    list_filter = ['cate', 'tags']
    filter_horizontal = ('tags',)

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(is_draft=True)
        self.message_user(request, u'%s篇文章成功转为草稿' % rows_updated)
    make_draft.short_description = u'转为草稿'

    def make_pub(self, request, queryset):
        rows_updated = queryset.update(is_draft=False)
        self.message_user(request, u'%s篇文章正式发布' % rows_updated)
    make_pub.short_description = u'正式发布'

#    def response_add(self, request, obj, post_url_continue=None):
#        Session.objects.all().delete()
#        return super(BlogAdmin, self).response_add(request, obj, post_url_continue)

admin.site.register(Blog, BlogAdmin)
