# -*-coding:utf-8 -*-
#
# Copyright (C) 2012-2014 Lianbi TECH Co., Ltd. All rights reserved.
# Created on May 8, 2014, by tom
#
#
from django.contrib import admin
from core.models import Themes
__author__ = 'tom'


class ThemesAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'is_valid')
    list_editable = ('is_valid',)


admin.site.register(Themes, ThemesAdmin)
