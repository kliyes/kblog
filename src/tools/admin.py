# -*-coding:utf-8 -*-
'''
Created on Oct 24, 2015

@author: jingyang <tom@kliyes.com>
'''
from django.contrib import admin
from tools.models import ShortLink


class ShortLinklAdmin(admin.ModelAdmin):
    list_display = ('get_short_url', 'name', 'link', 'valid')
    list_filter = ('valid',)
    list_editable = ('valid',)
    search_fields = ('name', 'link')


admin.site.register(ShortLink, ShortLinklAdmin)
