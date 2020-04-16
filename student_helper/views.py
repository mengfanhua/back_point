from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from student_helper.models import *
from django.db import transaction


@csrf_exempt
def get_class(request):
    # if request.method == "POST":
    list1 = [{"a": "1", "b": "数据库"}]
    return HttpResponse(json.dumps(list1, ensure_ascii=False))

# use this module to build api for software
# 视图模块
@csrf_exempt
def get_one_data(request):  # test for connecting database
    list1 = []
    try:
        curr = Users.objects.filter(password="1234567")
        for i in range(len(curr)):  # 多条数据用循环提取
            data = dict()
            data["uid"] = curr[i].__dict__["uid"]
            data["password"] = curr[i].__dict__["password"]
            list1.append(data)
    except Exception as e:
        print(e)
    return HttpResponse(json.dumps(list1, ensure_ascii=False))


@csrf_exempt
def refuse(requset):
    return HttpResponse("403 Forbidden<br/><br/>您没有权限。")


@csrf_exempt
def save_database(request):
    if request.method == "POST":
        list1 = {}
        try:
            uid = request.POST.get("uid", None)
            password = request.POST.get("password", None)
            semester = request.POST.get("semester", None)
            plan_str = request.POST.get("plan", None)
            plan = json.loads(plan_str)
        except:
            list1["status"] = "error"
            list1["message"] = "数据解析失败，请检查您的信息是否正确，如确认无误，请反馈给管理员。ERROR:0001"
            return HttpResponse(json.dumps(list1, ensure_ascii=False))

        s1 = transaction.savepoint()
        flag = 0
        for i in range(5):
            try:
                curr = Users.objects.get(uid=uid)
                Users.objects.filter(uid=uid).update(password=password)
                flag = flag + 1
                break
            except:
                transaction.savepoint_rollback(s1)
        if flag == 0:
            flag1 = 0
            for j in range(5):
                try:
                    Users.objects.create(uid=uid, password=password)
                    flag1 = flag1 + 1
                    break
                except:
                    transaction.savepoint_rollback(s1)
            if flag1 == 0:
                list1["status"] = "error"
                list1["message"] = "数据库同步失败，希望您将错误信息反馈给管理员。ERROR:0002"
                return HttpResponse(json.dumps(list1, ensure_ascii=False))
            else:
                pass
        else:
            pass

        s2 = transaction.savepoint()
        for i in range(5):
            try:
                curr = ClassPlan.objects.get(uid=uid, semester=semester)
                ClassPlan.objects.filter(uid=uid, semester=semester).delete()
                break
            except:
                transaction.savepoint_rollback(s2)

        s3 = transaction.savepoint()
        flag = 0
        for i in range(5):
            try:
                for j in range(len(plan)):
                    ClassPlan.objects.create(uid=uid, semester=semester, cid=plan[j]["cid"],
                                             cname=plan[j]["cname"], pid=plan[j]["pid"],
                                             pname=plan[j]["pname"], week=plan[j]["week"],
                                             position=plan[j]["position"])
                flag = flag + 1
                break
            except:
                transaction.savepoint_rollback(s3)
        if flag == 0:
            transaction.savepoint_rollback(s1)
            list1["status"] = "error"
            list1["message"] = "数据库同步失败，希望您将错误信息反馈给管理员。ERROR:0003"
            return HttpResponse(json.dumps(list1, ensure_ascii=False))
        else:
            list1["status"] = "success"
            list1["message"] = ""
            return HttpResponse(json.dumps(list1, ensure_ascii=False))
    else:
        return HttpResponse("403 Forbidden<br/><br/>您没有权限。")


@csrf_exempt
def load_database(request):
    if request.method == "POST":
        list1 = []
        dict1 = {}
        try:
            uid = request.POST.get("uid", None)
            password = request.POST.get("password", None)
            semester = request.POST.get("semester", None)
        except:
            dict1["status"] = "error"
            dict1["message"] = "数据解析失败，请检查您的信息是否正确，如确认无误，请反馈给管理员。ERROR:0004"
            return HttpResponse(json.dumps(dict1, ensure_ascii=False))

        s1 = transaction.savepoint()
        flag = 0
        for i in range(5):
            try:
                curr = Users.objects.get(uid=uid, password=password)
                flag = flag + 1
                break
            except:
                transaction.savepoint_rollback(s1)
        if flag == 0:
            dict1["status"] = "error"
            dict1["message"] = "密码验证失败，如您近期修改过密码，请先将新密码同步到数据库。"
            return HttpResponse(json.dumps(dict1, ensure_ascii=False))
        else:
            pass

        s2 = transaction.savepoint()
        flag = 0
        curr = ""
        for i in range(5):
            try:
                curr = ClassPlan.objects.filter(uid=uid, semester=semester)
                flag = flag + 1
                break
            except:
                transaction.savepoint_rollback(s2)
        if flag == 0:
            dict1["status"] = "error"
            dict1["message"] = "数据库未知错误，请反馈给管理员。ERROR:0005"
            return HttpResponse(json.dumps(dict1, ensure_ascii=False))
        else:
            pass
        for i in range(len(curr)):
            temp = dict()
            temp["cid"] = curr[i].__dict__["cid"]
            temp["cname"] = curr[i].__dict__["cname"]
            temp["pid"] = curr[i].__dict__["pid"]
            temp["pname"] = curr[i].__dict__["pname"]
            temp["week"] = curr[i].__dict__["week"]
            temp["position"] = curr[i].__dict__["position"]
            list1.append(temp)
        dict1["status"] = "success"
        dict1["message"] = list1
        return HttpResponse(json.dumps(dict1, ensure_ascii=False))
    else:
        return HttpResponse("403 Forbidden<br/><br/>您没有权限。")


@csrf_exempt
def update_database(request):
    if request.method == "POST":
        list1 = {}
        try:
            uid = request.POST.get("uid", None)
            password = request.POST.get("password", None)
        except:
            list1["status"] = "error"
            list1["message"] = "数据解析失败，请检查您的信息是否正确，如确认无误，请反馈给管理员。ERROR:0006"
            return HttpResponse(json.dumps(list1, ensure_ascii=False))

        s1 = transaction.savepoint()
        flag = 0
        for i in range(5):
            try:
                curr = Users.objects.get(uid=uid)
                Users.objects.filter(uid=uid).update(password=password)
                flag = flag + 1
                break
            except:
                transaction.savepoint_rollback(s1)
        if flag == 0:
            flag1 = 0
            for j in range(5):
                try:
                    Users.objects.create(uid=uid, password=password)
                    flag1 = flag1 + 1
                    break
                except:
                    transaction.savepoint_rollback(s1)
            if flag1 == 0:
                list1["status"] = "error"
                list1["message"] = "数据库同步失败，希望您将错误信息反馈给管理员。ERROR:0007"
                return HttpResponse(json.dumps(list1, ensure_ascii=False))
        else:
            list1["status"] = "success"
            list1["message"] = ""
            return HttpResponse(json.dumps(list1, ensure_ascii=False))
    else:
        return HttpResponse("403 Forbidden<br/><br/>您没有权限。")
