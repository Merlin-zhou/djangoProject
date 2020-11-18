"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from . import view
from backend import views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    # path(r'', TemplateView.as_view(template_name="index.html")),
    path(r'test/', include('backend.url')),
    path(r'', view.home, name='home'),

    # 接口
    re_path(r'api/dns', views.get_ip_list),
    re_path(r'api/http-post', views.url_request),
    re_path(r'api/sql_insert', views.sql_insert),
    re_path(r'api/sql_project', views.sql_project),
]
