#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from django.db import models
from core.managers import BaseManager


class BaseModel(models.Model):
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract = True
        ordering = ('-create_time',)
