from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from student_helper.models import *

@csrf_exempt
def get_class(request):
    # if request.method == "POST":
    list1 = [{"a": "1", "b": "2"}]
    return HttpResponse(json.dumps(list1, ensure_ascii=False))

# use this module to build api for software
# 视图模块
@csrf_exempt
def get_one_data(request):  # test for connecting database
    data = {}
    curr = Users.objects.get(uid="20174529")
    data["uid"] = curr.__dict__["uid"]
    data["password"] = curr.__dict__["password"]
    return HttpResponse(json.dumps(data, ensure_ascii=False))


def refuse(requset):
    return HttpResponse("403 Forbidden<br/><br/>您没有权限。")
