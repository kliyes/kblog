#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-6, by Tom
#
#
from django.db import models

import settings
from core.models import BaseModel
from ckeditor.fields import RichTextField


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

    def count_attachments(self):
        """
        获取某博客的附件数量
        """
        return self.attachment_set.count()


class Attachment(BaseModel):
    blog = models.ForeignKey(Blog, verbose_name=u'博客', null=True, blank=True)
    name = models.CharField(u'名称', max_length=32)
    file = models.FileField(u'附件文件', upload_to=settings.ATTACHMENT_FOLDER)
    download_count = models.IntegerField(u'下载次数', default=0)

    class Meta:
        verbose_name = u'附件'
        verbose_name_plural = u'附件'


class Links(BaseModel):
    url = models.URLField(u'链接地址')
    alias = models.CharField(u'名称', max_length=16)
    available = models.BooleanField(u'是否可用', default=True)

    class Meta:
        verbose_name = u'友情链接'
        verbose_name_plural = u'友情链接'
