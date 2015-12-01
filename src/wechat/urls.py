# -*-coding:utf-8 -*-
'''
Created on Dec 1, 2015

@author: jingyang <tom@kliyes.com>
'''
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^echo/$', 'wechat.views.wechat_check'),
                       )
