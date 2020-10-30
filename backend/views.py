import json
import socket
import requests

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from backend.models import Article

from djangoProject.libs import config
from django.contrib.auth.models import User  # 导入自带用户模块


def article_detail(request, article_title, article_id):
    article = get_object_or_404(Article, pk=article_id)  # 获取对象,pk表示主键
    content = {'article_obj': article}
    return render(request, 'article_detail.html', content)


def article_list(request):
    articles = Article.objects.filter(is_online=True)  # 通过条件过滤出需要的内容
    content = {'article_list': articles}
    return render(request, 'article_list.html', content)


def dns(request):
    return render(request, 'dns.html', )


def make_data(request):
    return render(request, 'make_data.html', )


def http_request(request):
    return render(request, 'http_request.html', )


# 接口,用于前端展示脚本处理结果
def get_ip_list(request):
    params = request.GET
    domain = params['domain']
    ip_list = []
    try:
        addrs = socket.getaddrinfo(domain, None)
        for item in addrs:
            if item[4][0] not in ip_list:
                ip_list.append(item[4][0])
        content = {'code': 200, 'msg': 'success', }
    except Exception as e:
        print(e)
        content = {'code': 500, 'msg': str(e), }
    content['ip_list'] = ip_list
    return HttpResponse(json.dumps(content), content_type="application/json")


def cur_request(request):
    params = request.GET
    print(params)
    if params['header'].strip().replace("\n", "") == '' or params['header'] is None:
        # 在很多时候我们想修改Django项目的request中属性值,该对象是一个不可修改对象, 那我们此时还想继续尝试修改其中的数值怎么办？此时你再需要对request对象修改数据值的时候就可以实现你想要的理想效果了。
        request.GET._mutable = True
        params['header'] = '{}'
    if params['data'].strip().replace("\n", "") == '' or params['header'] is None:
        request.GET._mutable = True
        params['data'] = '{}'
    if params['method'] == 'post':
        print("11" + params['header'])
        res = requests.post(url=params['url'], data=json.dumps(eval(params['data'])), headers=eval(params['header']), )
        r = res.json()
    elif params['method'] == 'get':
        res = requests.get(url=params['url'], params=eval(params['data']), headers=eval(params['header']), )
        r = res.json()
        print(r)
    else:
        r = {'msg': '参数有误'}
    return HttpResponse(json.dumps(r), content_type="application/json")


def sql_insert(request):
    params = request.GET
    try:
        if get_object_or_404(User, username=params['usr']):
            print("用户存在")
        else:
            print("用户不存在")
    except Exception as e:
        print(e)
    sql = params['sql']
    r = config.link_mysql(sql)
    print(r)
    if r[0] == 'success':
        print(r[1])
        return HttpResponse(json.dumps(r[1]))
    elif r[0] == 'fail':
        print(r[1])
        return HttpResponse(r[1])

