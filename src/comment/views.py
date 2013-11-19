#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-15, by Tom
#
#
from comment.forms import CommentForm
from blog.models import Blog
from django.http.response import Http404, HttpResponseRedirect, HttpResponse
from core.views import render_and_response, get_ip
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


def comment(request, blog_id):
    """
    提交评论
    """
    blog = Blog.objects.get_by_id(blog_id)
    if blog is None:
        return Http404
    form = CommentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            cmt = form.post(blog)
            cmt.ip = get_ip(request)
            cmt.save()
            return HttpResponseRedirect('/blog/%s' % blog.id)
    return render_and_response(request, 'blog/detail.html',
                               {'blog': blog, 'form': form})


def refresh_captcha(request):
    """
    刷新验证码图片
    """
    new_key = CaptchaStore.generate_key()
    new_img = captcha_image_url(new_key)
    return HttpResponse(new_img)
