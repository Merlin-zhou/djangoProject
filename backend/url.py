#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 14:45 00
# @Author  : ji.zhou

from django.urls import path, re_path
from . import views


urlpatterns = [
    path(r'list/<int:article_id><article_title>', views.article_detail, name='article_detail'),
    path(r'list/', views.article_list, name='article_list'),
    path(r'dns', views.dns, name='dns_resolver'),
    path(r'make_data', views.make_data, name='make_data'),
    path(r'http_request', views.http_request, name='http_request'),
]
