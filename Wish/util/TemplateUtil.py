#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2012-9-25

@author: yyang21
'''
from django.template.loader import get_template
def getTemplate(name):
    get_template('current_datetime.html')