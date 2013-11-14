#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-6, by Tom
#
#
from blog.models import Blog
from core.views import render_and_response
from django.http import Http404
from tags.models import Tag, Category
from django.db.models.query_utils import Q


def home_page(request):
    """
    博客首页
    """
    blogs = Blog.objects.filter(is_draft=False)
    return render_and_response(request, 'index.html', {'blogs': blogs})


def detail(request, blog_id):
    """
    博客详情
    """
    blog = Blog.objects.get_by_id(blog_id)
    if blog is None or blog.is_draft:
        raise Http404
    return render_and_response(request, 'blog/detail.html', {'blog': blog})


def search(request):
    """
    搜索博客
    """
    k = request.REQUEST.get('k')
    tags = Tag.objects.filter(text__contains=k)
    blogs = Blog.objects.filter(Q(Q(title__contains=k) |
                                  Q(content__contains=k) |
                                  Q(cate__text__contains=k) |
                                  Q(tags__in=list(tags))), is_draft=False)
    blogs = sorted(list(set(blogs)), key=lambda x: x.update_time, reverse=True)
    return render_and_response(request, 'index.html', {'blogs': blogs})


def filter(request, by, id):
    """
    按标签或分类筛选博客
    """
    if by == 'tag':
        tag = Tag.objects.get_by_id(id)
        if tag is None:
            raise Http404
        blogs = tag.blog_set.filter(is_draft=False)
    elif by == 'cate':
        cate = Category.objects.get_by_id(id)
        if cate is None:
            raise Http404
        blogs = cate.blog_set.filter(is_draft=False)
    else:
        raise Http404
    return render_and_response(request, 'index.html', {'blogs': blogs})
