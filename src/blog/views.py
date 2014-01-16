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
from comment.forms import CommentForm
from utils import pages


def home_page(request):
    """
    博客首页
    """
    return render_and_response(request, 'index.html', pager(request,
        get_data_list('blogs'), 'blogs'))


def detail(request, blog_id):
    """
    博客详情
    """
    blog = Blog.objects.get_by_id(blog_id)
    if blog is None or blog.is_draft:
        raise Http404
    return render_and_response(request, 'blog/detail.html',
                               {'blog': blog, 'form': CommentForm()})


def search(request):
    """
    搜索博客
    """
    k = request.REQUEST.get('k')
    blogs = get_data_list('name', k)
    blogs = sorted(list(set(blogs)), key=lambda x: x.update_time, reverse=True)
#    return render_and_response(request, 'index.html', {'blogs': blogs})
    return render_and_response(request, 'index.html', pager(request, blogs, 'name'))


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


def get_data_list(paging_key, k=0):
    if paging_key == 'blogs':
        return Blog.objects.filter(is_draft=False)
    elif paging_key == 'cate':
        cate = Category.objects.get_by_id(k)
        if cate:
            return cate.blog_set.filter(is_draft=False)
    elif paging_key == 'tag':
        tag = Tag.objects.get_by_id(k)
        if tag:
            return tag.blog_set.filter(is_draft=False)
    elif paging_key == 'name':
        tags = Tag.objects.filter(text__contains=k)
        return Blog.objects.filter(Q(Q(title__contains=k) |
                                     Q(content__contains=k) |
                                     Q(cate__text__contains=k) |
                                     Q(tags__in=tags)), is_draft=False)
    return []


def pager(request, data_list, paging_key):
    """
    分页
    """
    page = request.REQUEST.get('p')
    if not page or not page.isdigit():
        page = 1
    page = int(page)
    paging = pages.get_paging(request, paging_key)
    if not paging:
        paging = pages.set_paging(request, paging_key, data_list)
    return paging.result(page)
