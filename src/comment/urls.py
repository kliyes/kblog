#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-15, by Tom
#
#
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^(\d+)$', 'comment.views.comment', name='post_comment'),
)
