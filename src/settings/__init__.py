#coding=utf-8
from local import *
try:
    from django.contrib.auth.models import User
    from core.models import Themes

    themes = Themes.objects.filter(is_valid=True)
    THEME_DIRS = 'themes/templates_%s' % (themes[0].templates_id if themes else '4')
    TEMPLATE_DIRS = os.path.join(os.path.dirname(__file__), '../', THEME_DIRS).replace('\\','/'),
    User._meta.verbose_name_plural = u'用户'
    User._meta.verbose_name = u'用户'
except:
    pass
