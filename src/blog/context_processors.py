#coding=utf-8
'''
Created on 2013-11-10

@author: Tom Kliyes
'''
from tags.models import Category, Tag


def tags_and_cates(request):
    cates = Category.objects.used()
    tags = Tag.objects.used()
    return {'tags': tags, 'cates': cates}
