#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from django.db import models
from core.managers import BaseManager
import settings


class BaseModel(models.Model):
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    objects = BaseManager()

    class Meta:
        abstract = True
        ordering = ('-create_time',)


class Themes(BaseModel):
    name = models.CharField(u'风格名称', max_length=64)
    preview = models.ImageField(u'预览图', upload_to=settings.THEME_PREVIEW_FOLDER)
    templates_id = models.CharField(u'模板id', max_length=4)
    is_valid = models.BooleanField(u'生效', default=False)

    class Meta:
        verbose_name = u'主题风格'
        verbose_name_plural = u'主题风格'
