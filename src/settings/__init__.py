#coding=utf-8
from local import *
from django.contrib.auth.models import User


User._meta.verbose_name_plural = u'用户'
User._meta.verbose_name = u'用户'
