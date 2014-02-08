#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-6, by Tom
#
#
from core.models import BaseModel
from django.db import models
from ckeditor.fields import RichTextField
from core.managers import BaseManager


class Blog(BaseModel):
    author = models.CharField(u'作者', max_length=32, default=u'Tom')
    title = models.CharField(u'标题', max_length=512)
    content = RichTextField(u'内容')
    tags = models.ManyToManyField('tags.Tag', verbose_name=u'标签', null=True,
                                  blank=True)
    cate = models.ForeignKey('tags.Category', verbose_name=u'分类', null=True,
                             blank=True)
    source = models.CharField(u'出处', max_length=1024, null=True, blank=True)
    is_draft = models.BooleanField(u'是否为草稿', default=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'博客'
        verbose_name_plural = u'博客'
        ordering = ('-update_time',)

    def count_comments(self):
        """
        获取某博客的评论数量
        """
        return self.comment_set.count()

    def get_comments(self):
        """
        获取某博客的评论列表
        """
        return self.comment_set.all()


class Links(BaseModel):
    url = models.URLField(u'链接地址')
    alias = models.CharField(u'名称', max_length=16)
    available = models.BooleanField(u'是否可用', default=True)

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = u'友情链接'


class ISays(BaseModel):
    sig = models.CharField(u'签名', max_length=256)
    words = models.CharField(u'说说', max_length=1024)

    class Meta:
        verbose_name = u'个性'
        verbose_name_plural = u'个性'
        ordering = ('-create_time',)
