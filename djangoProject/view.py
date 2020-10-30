#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 14:01 35
# @Author  : ji.zhou

from django.shortcuts import render


def home(request):
    content = {}
    return render(request, 'home.html', content)
