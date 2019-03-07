# coding:utf-8
import json
from django.http import JsonResponse
from rest_framework.response import Response

# from django.forms.models import model_to_dict
from django.core.paginator import Paginator

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from .utils.db_util import from_sql_get_data

from website.settings import MPP_CONFIG, DATABASES

LOCAL_DBCONFIG = MPP_CONFIG.copy()
LOCAL_DBCONFIG["db"] = DATABASES["default"]["NAME"]

@api_view(['GET'])
@permission_classes(( IsAuthenticated, ))
def get_all_users(request):
    # data = json.loads(request.body.decode())
    data = request.GET
    pager = data["page"] if "page" in data.keys() else 1
    query_sql = """select auth_user.id as uid, username, date_joined, email, identity, last_login, truename from auth_user 
      left join userprofile on auth_user.id = userprofile.user_id order by date_joined desc;"""
    p = Paginator(from_sql_get_data(query_sql, MPP_CONFIG=LOCAL_DBCONFIG)["data"], 10)

    all_counts = p.count  # 对象总数
    page_count = p.num_pages  # 总页数
    pj = p.page(pager)
    objs = pj.object_list
    res_data = objs ## 主要的对象
    return Response({"res": res_data, "page_count": page_count, "pager": pager, "all_counts": all_counts})
