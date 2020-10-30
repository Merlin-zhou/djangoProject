#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 14:35 56
# @Author  : ji.zhou

import pymysql
import configparser
import os
import sys


def link_mysql(sql):
    base_dir = os.path.split(os.path.abspath(__file__))[0]   # 获取当前文件路径
    con = configparser.ConfigParser()
    con.read(base_dir + "/config.ini", encoding='utf-8')
    HOST = con.get("AppUpdate_mysql", "host")
    USR = con.get("AppUpdate_mysql", "usr")
    PSD = con.get("AppUpdate_mysql", "psd")
    PORT = eval(con.get("AppUpdate_mysql", "port"))
    # database = con.get("AppUpdate_mysql", "database")
    print("开始连接数据库......")
    try:
        db = pymysql.connect(host=HOST, user=USR, password=PSD, port=PORT, charset="utf8")
        print("数据库连接成功，可以开始进行数据库操作......")
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return 'success', results
        except Exception as e:
            return 'fail', e
    except Exception as e:
        return "fail", "连接数据库失败,原因为：{}".format(e)




