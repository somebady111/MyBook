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
from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'MyBook'
    site_title = 'MyBook管理后台'
    index_title = '欢迎来到MyBook管理后台'

custom_site = CustomSite(name='cus_admin')