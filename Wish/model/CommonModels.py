#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2012-10-13

@author: yyang21
'''
from django.db import models
class User(models.Model):
    # 用户ID
    user_id = models.CharField(max_length=20)
    # 用户名
    user_name = models.CharField(max_length=90)
    # 用户地址
    user_address = models.CharField(max_length=300)
    # 用户手机
    user_mobile = models.CharField(max_length=11)
    # 用户座机
    user_tel = models.CharField(max_length=11)
    # 用户微博ID
    user_wbId = models.CharField(max_length=20)
    # 用户微博显示名称
    user_srNm = models.CharField(max_length=90)
    # 其他
    comments = models.CharField(max_length=300)

class Wish(models.Model):
    # 用户ID
    user_id = models.CharField(max_length=20)
    # ID
    wish_id = models.CharField(max_length=20)
    # wish物品链接(U)
    wish_url = models.CharField(max_length=200)
    # wish物品名称(U)
    wish_name = models.CharField(max_length=200)
    # wish物品描述(U)
    wish_comments = models.CharField(max_length=420)
