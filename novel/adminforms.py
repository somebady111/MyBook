#!/usr/bin/env python3
# __*__ coding: utf-8 __*__
"""
__title__ = ''
__author__ = 'Administrator'
__mtime__ = '2021/5/19'

┏┓ ┏┓
┏┛┻━━━┛┻┓
┃ ☃ ┃
┃ ┳┛ ┗┳ ┃
┃ ┻ ┃
┗━┓ ┏━┛
┃ ┗━━━┓
┃ 神兽保佑 ┣┓
┃　永无BUG！ ┏┛
┗┓┓┏━┳┓┏┛
┃┫┫ ┃┫┫
┗┻┛ ┗┻┛
"""
from django import forms

class NovelAdmin(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea,label='摘要',required=False)

