#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-6, by Tom
#
#
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    url(r'^(\d+)$', 'blog.views.detail', name='blog_detail'),
    url(r'^search$', 'blog.views.search', name='blog_search'),
    url(r'^attachment/(\d+)$', 'blog.views.download_attachment', name='blog_attachment_download'),
    url(r'^(\w+)/(\d+)$', 'blog.views.filter_by', name='blog_filter'),
)
