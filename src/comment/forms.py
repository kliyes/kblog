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
    captcha = CaptchaField(label=u'验证码',
                           error_messages={'invalid': u'验证码错误',
                                           'required': u'请输入验证码'})

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['contact'].error_messages = {
            'required': u'请输入您的联系方式, 邮箱、QQ等均可(仅为方便交流)'}
        self.fields['text'].error_messages = {'required': u'请输入您想评论的内容'}

    class Meta:
        model = Comment
        exclude = ('blog', 'ip')

    def post(self, blog):
        data = self.cleaned_data
        return Comment.objects.create(blog=blog, contact=data['contact'],
                                      name=data['name'], text=data['text'])
