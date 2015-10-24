# -*-coding:utf-8 -*-
'''
Created on Oct 24, 2015

@author: jingyang <tom@kliyes.com>
'''
from core.models import BaseModel
from django.db import models


class ShortLink(BaseModel):
    name = models.CharField('Name', max_length=500, null=True, blank=True)
    code = models.CharField('Code', max_length=20, unique=True)
    link = models.URLField('Original Link')
    valid = models.BooleanField('Valid', default=True)

    def __unicode__(self):
        return self.name or self.code

    def get_short_url(self):
        return 'http://kliy.es/s/' + self.code
    get_short_url.short_description = 'Short URL'
