# -*-coding:utf-8 -*-
'''
Created on Oct 24, 2015

@author: jingyang <tom@kliyes.com>
'''
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^shorten/$', 'tools.views.shorten', name='shoten_url'),
                       )
