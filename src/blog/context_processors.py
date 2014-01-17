#coding=utf-8
'''
Created on 2013-11-10

@author: Tom Kliyes
'''
from tags.models import Category, Tag
import settings


def tags_and_cates(request):
    return {'tags': Tag.objects.used(), 'cates': Category.objects.used()}


def signature_and_words(request):
    return {'sig': settings.SIG, 'words': settings.WORDS}
