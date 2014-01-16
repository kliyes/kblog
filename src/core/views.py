#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.sessions.models import Session
from django.http.response import HttpResponse


def render_and_response(request, t, data={}):
    return render_to_response(t, RequestContext(request, data))


def get_ip(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip


def clear_session(request):
    Session.objects.all().delete()
    return HttpResponse('session clear!')
