#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-7, by Tom
#
#
from django.contrib import admin
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'cate', 'is_draft', 'update_time']
    actions = ['make_draft', 'make_pub']
    list_filter = ['cate', 'tags']
    filter_horizontal = ('tags',)

    def make_draft(self, request, queryset):
        rows_updated = queryset.update(is_draft=True)
        self.message_user(request, u'%s篇文章成功转为草稿' % rows_updated)
    make_draft.short_description = u'转为草稿'

    def make_pub(self, request, queryset):
        rows_updated = queryset.update(is_draft=False)
        self.message_user(request, u'%s篇文章正式发布' % rows_updated)
    make_pub.short_description = u'正式发布'

#     def save_model(self, request, obj, form, change):
#         old_obj = self.get_object(request, obj.id)
#         if not old_obj.cate == obj.cate:
#             if old_obj.cate:
#                 old_obj.cate.used_count -= 1
#                 old_obj.cate.save()
#             if obj.cate:
#                 obj.cate.used_count += 1
#                 obj.cate.save()
#         old_tags = obj.tags.all()
#         new_tags = form.cleaned_data['tags']
#         if not old_tags == new_tags:
#             if old_tags:
#                 for ot in old_tags:
#                     if not ot in new_tags:
#                         ot.used_count -= 1
#                         ot.save()
#             if new_tags:
#                 for nt in new_tags:
#                     if not nt in old_tags:
#                         nt.used_count += 1
#                         nt.save()
#         super(BlogAdmin, self).save_model(request, obj, form, change)

admin.site.register(Blog, BlogAdmin)
