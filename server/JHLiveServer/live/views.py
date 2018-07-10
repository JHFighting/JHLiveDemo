# -*- encoding=utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .models import UserInfo
# Create your views here.

@csrf_exempt
def register(request):
    # 注册
    if request.method == "POST":
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        nickname = request.POST.get('nickname', '')
        if phone:
            try:
                UserInfo.objects.get(phone=phone)
                return response({'ret':0, 'error':'该账号已存在'})
            except UserInfo.DoesNotExist:
                user = UserInfo.objects.create(phone=phone,password=password,nickname=nickname)
                return response({'ret':1,'userInfo':{'phone':phone,'nickname':user.nickname}})

@csrf_exempt
def login(request):
    # 登录
    if request.method == "POST":
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        try:
            user = UserInfo.objects.get(phone=phone)
            if password == user.password:
                return response({'ret':1, 'userInfo':{'phone':phone,'nickname':user.nickname}})
            else:
                return response({'ret':0, 'error':'用户名或密码错误'})
        except UserInfo.DoesNotExist:
            return response({'ret':0, 'error':'该用户未注册'})

@csrf_exempt
def beginLive(request):
    # 开启直播
    if request.method == "POST":
        phone = request.POST.get('phone', '')
        try:
            user = UserInfo.objects.get(phone=phone)
            user.haveLive = 2
            user.save()
            return response({'ret':1})
        except UserInfo.DoesNotExist:
            return response({'ret':0, 'error':'该用户未注册'})

@csrf_exempt
def endLive(request):
    # 直播结束
    if request.method == "POST":
        phone = request.POST.get('phone', '')
        try:
            user = UserInfo.objects.get(phone=phone)
            user.haveLive = 1
            user.save()
            return response({'ret':1})
        except UserInfo.DoesNotExist:
            return response({'ret':0, 'error':'该用户未注册'})

@csrf_exempt
def getLiveList(request):
    # 获取直播列表
    # if request.method == "POST":
    userList = UserInfo.objects.filter(haveLive=2)
    dataList = []
    for data in userList:
        dic = {'phone':data.phone, 'nickname':data.nickname}
        dataList.append(dic)
    return response({'ret':1, 'dataList':dataList})

def response(dict):
    return HttpResponse(json.dumps(dict,ensure_ascii=False), content_type="application/json")
    