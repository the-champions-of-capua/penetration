# coding:utf-8
import re
from django.shortcuts import render, redirect

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


def put_log(request):
    from .utils.url_configs import URL_CFGS
    from wafmanage.models import PlatOptHistory
    current_url = request.META["PATH_INFO"]
    request_method = request.method
    conn_methods = {"GET": "获取", "POST": "增加", "PUT": "修改", "DELETE": "删除"}

    for url_cfg in URL_CFGS:
        matched = re.match(".*?" + url_cfg["url_prefix"] + "(.*?)", current_url)
        if matched and request_method != "GET":
            PlatOptHistory.objects.create(
                desc=url_cfg["cate"],
                type=url_cfg["type"],
                extra=conn_methods[request_method] + url_cfg["desc"],
                opreatername=request.user.username,
                conn_file=current_url,
            )


## 操作记录中间件
class OptRecodeMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        put_log(request)
        return view_func(request, *view_args, **view_kwargs)
