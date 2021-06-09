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
from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        return super(BaseOwnerAdmin, self).save_model(request,obj,form,change)