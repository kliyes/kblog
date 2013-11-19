#coding=utf-8
#
# Copyright (C) 2012-2013 XIZHI TECH Co., Ltd. All rights reserved.
# Created on 2013-11-15, by Tom
#
#
from django import forms
from captcha.fields import CaptchaField
from comment.models import Comment


class CommentForm(forms.ModelForm):
    captcha = CaptchaField(label=u'验证码')

    class Meta:
        model = Comment
        exclude = ('blog', 'ip')

    def post(self, blog):
        data = self.cleaned_data
        return Comment.objects.create(blog=blog, contact=data['contact'],
                                      name=data['name'], text=data['text'])
