# -*-coding:utf-8 -*-
#
# Copyright (C) 2012-2014 Lianbi TECH Co., Ltd. All rights reserved.
# Created on May 8, 2014, by tom
#
#
__author__ = 'tom'

from django.contrib import admin

from core.models import Themes


def preview(obj):
    preview.allow_tags = True
    return "<a href='%s' target=_blank><img src=%s width=300 height=119 />" % (obj.preview.url, obj.preview.url)
preview.short_description = u'预览图'


class ThemesAdmin(admin.ModelAdmin):
    list_display = ('name', preview, 'is_valid')
    list_editable = ('is_valid',)


admin.site.register(Themes, ThemesAdmin)
