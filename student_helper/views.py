from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def get_class(request):
    # if request.method == "POST":
    list1 = [{"a": "1", "b": "2"}]
    return HttpResponse(json.dumps(list1, ensure_ascii=False))

# use this module to build api for software
# 视图模块
