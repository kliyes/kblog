#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-15, by Tom
#
#
from core.models import BaseModel
from django.db import models
from ckeditor.fields import RichTextField


class Comment(BaseModel):
    blog = models.ForeignKey('blog.Blog', verbose_name=u'博客')
    contact = models.CharField(u'联系方式', max_length=64)
    name = models.CharField(u'称呼', max_length=32, null=True, blank=True)
    text = RichTextField(u'评论内容', config_name='comment')
    ip = models.IPAddressField(u'评论者IP', null=True, blank=True)

    def __unicode__(self):
        return "%s, %s" % (self.contact, self.name)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'
        ordering = ('-create_time',)
