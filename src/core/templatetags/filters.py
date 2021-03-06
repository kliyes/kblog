#coding=utf-8
#
# Copyright (C) 2013  Kliyes.com  All rights reserved.
#
# author: JingYang.
#
# This file is part of BookStore.

from django.template import Library
from django.template.defaultfilters import stringfilter
import settings

register = Library()


@stringfilter
def truncatehanzi(value, arg):
    """
    Truncates a string after a certain number of words including
    alphanumeric and CJK characters.

    Argument: Number of words to truncate after.
    """
    from truncate_hanzi import truncate_hanzi
    try:
        length = int(arg)
    except ValueError:  # Invalid literal for int().
        return value  # Fail silently.
    return truncate_hanzi(value, length)
truncatehanzi.is_safe = True

register.filter('truncatehanzi', truncatehanzi)


def url_target_blank(text):
    return text.replace('<a ', '<a target="_blank" ')
url_target_blank = register.filter(url_target_blank)
url_target_blank.is_safe = True


def trans_app_label(app_label):
    """
    translate app label to Chinese
    """
    return settings.APP_LABEL_LOCAL.get(app_label.lower(), app_label)
trans_app_label = register.filter(trans_app_label)
