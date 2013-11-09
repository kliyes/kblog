#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def render_and_response(request, t, data={}):
    return render_to_response(t, RequestContext(request, data))
