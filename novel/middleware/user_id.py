#!/usr/bin/env python3
# __*__ coding: utf-8 __*__
"""
__title__ = '临时存储用户ID，uuid模块'
__author__ = 'Administrator'
__mtime__ = '2021/6/3'

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

import uuid

USER_KEY = 'uid'
TEN_YEARS = 60 * 60 * 24 * 365 * 10

class UserIdMiddleware():
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        uid = self.generate_uid(request)
        response = self.get_response(request)
        response.set_cookie(USER_KEY,uid,max_age=TEN_YEARS,httponly=True)
        return response

    def generate_uid(self,request):
        try:
            uid = request.COOKIES(USER_KEY)
        except KeyError:
            uid = uuid.uuid4().hex
        return uid