#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from django.db.models.manager import Manager


class BaseManager(Manager):
    def __init__(self):
        super(BaseManager, self).__init__()

    def get_by_id(self, id):
        try:
            return self.get(id)
        except Exception, e:
            print e
            return None
