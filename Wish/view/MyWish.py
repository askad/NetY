#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2012-9-20

@author: yyang21

1.查看自己的愿望列表。（展示形式：陈列）
2.添加一个愿望。
3.删除愿望。
4.标记愿望为已实现（匿名实现，或者指定人）
5.愿望形式：文字，图片，或者产品链接
6.分享愿望：手机，微博，私信，邮件

'''
from Wish.constants import SqlConstants
from Wish.constants import Constants
from Wish.util.DBUtil import DBConnector
from Wish.vo.commonTableVo import WishTableVo
from Wish.vo.commonVo import MyWishVo
from django.shortcuts import render_to_response

def hello(request):
    return render_to_response('mywish.html', {'current_date': 123})

def init_page(request):
    myWishVo = MyWishVo()
    myWishVo.user_name = "yy"
    tableVo1 = WishTableVo()
    tableVo1.wish_name = "askad"
    tableVo2 = WishTableVo()
    tableVo2.wish_name = "askadyy"
    wishTableVoList = [tableVo1,tableVo2]
    return render_to_response('mywish.html', {'myWishVo': myWishVo,"wishTableVoList":wishTableVoList})


def addWish(request):
    pass

def delWish(request):
    pass

def listWish(request):
    con = DBConnector()
    result = con.qureySql(SqlConstants.LIST_WISH)
    result[Constants.SQL_RESULT_DATA]
    pass