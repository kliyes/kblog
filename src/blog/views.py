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


def _get_data_list(paging_key, k=0):
    if paging_key == 'all':
        return Blog.objects.filter(is_draft=False)
    elif paging_key == 'cate':
        cate = Category.objects.get_by_id(k)
        if cate:
            return Blog.objects.filter(cate=cate)
    elif paging_key == 'tag':
        tag = Tag.objects.get_by_id(k)
        if tag:
            return tag.blog_set.filter(is_draft=False)
    elif paging_key == 'search':
        tags = Tag.objects.filter(text__contains=k)
        return Blog.objects.filter(Q(Q(title__contains=k) |
            Q(content__contains=k) |
            Q(cate__text__contains=k) |
            Q(tags__in=tags)), is_draft=False).distinct().order_by('-update_time')

    return []


def pager(request, sk, k=0):
    """
    分页器
    """
    page = request.REQUEST.get('p')
    if not page or not page.isdigit():
        page = 1
    page = int(page)
    paging = pages.get_paging(request, '%s_%s' % (sk, k))
    if not paging:
        paging = pages.set_paging(request, '%s_%s' % (sk, k),
                                  _get_data_list(sk, k))
    ctx = paging.result(page)
    ctx.update({'sk': sk, 'k': k})
    return ctx


def home_page(request):
    """
    博客首页
    """
    return render_and_response(request, 'index.html', pager(request, 'all'))


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
    return render_and_response(request, 'index.html',
                               pager(request, 'search', request.REQUEST.get('k')))


def filter_by(request, by, id):
    """
    按标签或分类筛选博客
    """
    if by == 'tag':
        tag = Tag.objects.get_by_id(id)
        if tag is None:
            raise Http404
        return render_and_response(request, 'index.html', pager(request, 'tag',
                                                                id))
    elif by == 'cate':
        cate = Category.objects.get_by_id(id)
        if cate is None:
            raise Http404
        return render_and_response(request, 'index.html', pager(request, 'cate',
                                                                id))
    else:
        raise Http404
