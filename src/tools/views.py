# -*-coding:utf-8 -*-
'''
Created on Oct 24, 2015

@author: jingyang <tom@kliyes.com>
'''
import re
import string
import hashlib

from django.http.response import Http404, HttpResponseRedirect

from tools import models
from core.views import render_and_response


URL_REGEX = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


CHAR_RANGE = string.uppercase + string.lowercase + string.digits + '_'


def catalog(req):
    return render_and_response(req, 'catalog.html')


def get_short_url(url):
    key = 'kliy.es'
    h = hashlib.md5(key+url).hexdigest()
    res = [0 for i in range(4)]
    for i in range(4):
        hexint = 0x3FFFFFFF & int("0x"+h[i*8: i*8+8], 16)
        outChars = ""
        for j in range(7):
            index = 0x0000003D & hexint
            outChars += CHAR_RANGE[index]
            hexint = hexint >> 5
        res[i] = outChars
    return res[0]


def shorten(req):
    """
    Generate a short url from a long url
    """
    t = 'shorten.html'
    if req.method == 'GET':
        return render_and_response(req, t)
    ori_url = req.POST.get('url')
    name = req.POST.get('name')
    if not re.search(URL_REGEX, ori_url):
        return render_and_response(req, t, {'msg': 'invalid url'})
    code = get_short_url(ori_url)
    obj = models.ShortLink.objects.get_or_create(code=code,
                                                 defaults={'name': name,
                                                           'link': ori_url})[0]
    return render_and_response(req, t, {'result': obj.get_short_url()})


def redirect(req, code):
    """
    Redirect short url to real url
    """
    objs = models.ShortLink.objects.filter(code=code, valid=True)
    if not objs.exists():
        raise Http404
    return HttpResponseRedirect(objs[0].link)
