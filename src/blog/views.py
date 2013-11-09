#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-6, by Tom
#
#
from blog.models import Blog
from core.views import render_and_response


def home_page(request):
    blogs = Blog.objects.filter(is_draft=False, is_deleted=False)
    return render_and_response(request, 'index.html', {'blogs': blogs})
