#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from core.models import BaseModel
from django.db import models
from core.managers import BaseManager


class TagManager(BaseManager):
    def used(self):
        return [tag for tag in self.all() if tag.used_count() > 0][:10]


class Tag(BaseModel):
    text = models.CharField(u'标签', max_length=32)
    #used_count = models.IntegerField(u'被使用次数', default=0)

    objects = TagManager()

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = u'标签'
        #ordering = ('-used_count',)

    def used_count(self):
        """
        返回某标签被引用次数
        """
        return self.blog_set.filter(is_draft=False).count()


class CateManager(BaseManager):
    def used(self):
        return [cate for cate in self.all() if cate.used_count() > 0][:10]


class Category(BaseModel):
    text = models.CharField(u'分类', max_length=32)
    #used_count = models.IntegerField(u'该分类下博客数', default=0)

    objects = CateManager()

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = u'分类'
        #ordering = ('-used_count',)

    def used_count(self):
        """
        返回某分类下博客总数
        """
        return self.blog_set.filter(is_draft=False).count()
