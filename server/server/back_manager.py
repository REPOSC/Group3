# coding=utf-8
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from backend import models


def add_manager(request):
    manager_name = request.POST.get('username')
    password = request.POST.get('password')
    manager_num = 100001
    try:
        manager_num = models.User_info.objects.filter(
            is_manager=True).latest('number').number
        manager_num += 1
    except:
        pass
    student = models.User_info.objects.create_user(
        number=manager_num,
        password=password,
        username=str(manager_num),
        nickname=manager_name,
        is_manager=True)
    student.save()
    return JsonResponse({'username': str(manager_num), 'password': password})


def auth_manager(request):
    number = request.POST.get('id', '')
    user_pwd = request.POST.get('password', '')
    user = authenticate(username=number, password=user_pwd)
    if not user:
        return JsonResponse({'status': 'error'})
    else:
        login(request, user)
        nowuser = models.User_info.objects.filter(username=number)
        if nowuser[0].is_superuser is True:
            return JsonResponse({'status': 'right', 'is_superuser': 'true'})
        else:
            return JsonResponse({'status': 'right', 'is_superuser': 'false'})


def change_manager(request):
    manager_name = request.POST.get('username')
    password = request.POST.get('password')
    try:
        manager = models.User_info.objects.get(
            username=manager_name, is_manager=True)
        manager.set_password(password)
        manager.save()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


def del_manager(request):
    manager_name = request.POST.get('username')
    try:
        models.User_info.objects.get(
            username=manager_name, is_manager=True).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


def get_managers(request):
    managers = models.User_info.objects.filter(is_manager=1)
    manager_names = []
    manager_numbers = []
    for i in managers:
        manager_names.append(i.nickname)
        manager_numbers.append(i.username)
    return JsonResponse({
        'user_names': manager_names,
        'user_numbers': manager_numbers
    })


def change_selfpassword(request):
    manager_name = request.POST.get('username')
    password = request.POST.get('password')
    oldpassword = request.POST.get('oldpassword')
    try:
        manager = authenticate(
            username=manager_name, password=oldpassword)
        manager.set_password(password)
        manager.save()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


def get_manager_info(request):
    username = request.POST.get('username')
    manager = models.User_info.objects.get(username=username)
    return JsonResponse({
        "nickname": manager.nickname,
        "time": str(manager.date_joined.year)+'年'+str(manager.date_joined.month)+'月'+str(manager.date_joined.day)+'日',
        "power": '超级管理员' if manager.is_superuser else '普通管理员'
    })
