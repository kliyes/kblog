# -*-coding:utf-8 -*-
'''
Created on Dec 1, 2015

@author: jingyang <tom@kliyes.com>
'''
import hashlib
from django.http.response import HttpResponse
TOKEN = 'wechat.kliy.es'


def wechat_check(req):
    sig = req.GET.get('signature', '')
    ts = req.GET.get('timestamp', '')
    nonce = req.GET.get('nonce', '')
    echostr = req.GET.get('echostr', '')

    secret = hashlib.sha1(nonce + ts + TOKEN).hexdigest()
    if sig == secret:
        return HttpResponse(echostr)
    err_msg = 'sig: {sig}<br />ts: {ts}<br />nonce: {nonce}<br />echostr: {echostr}'\
        .format(sig=sig, ts=ts, nonce=nonce, echostr=echostr)
    return HttpResponse(err_msg)
