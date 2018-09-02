"""This module includes some functions of manager."""
# coding=utf-8
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from backend import models


def add_manager(request):
    ##
    # Create a new manager account.
    # @param manager_name nickname of the new manager
    # @param password password of the new manager
    # @param manager_num id of the new manager
    # @retval manager_num
    # @retval password
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
    ##
    # Varify the login of the manager and superuser.
    # @param number id of the user
    # @param user_pwd password of the user
    # @param user the user information in the database
    # @retval status the status of the user
    number = request.POST.get('id', '')
    user_pwd = request.POST.get('password', '')
    user = authenticate(username=number, password=user_pwd)
    if not user:
        return JsonResponse({'status': 'error'})
    nowuser = models.User_info.objects.filter(username=number)
    if nowuser[0].is_manager:
        login(request, user)
        return JsonResponse({'status': 'right', 'is_superuser': 'false'})
    elif nowuser[0].is_superuser is True:
        return JsonResponse({'status': 'right', 'is_superuser': 'true'})
    else:
        return JsonResponse({'status': 'student'})


def change_manager(request):
    ##
    # Change the password of the manager
    # @param manager_name id of the manager to change
    # @param password old password of this manager
    # @param manager the manager information in the database
    # @retval success whether successfully change the password or not
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
    ##
    # Delete the manager account.
    # @param manager_name id of the manager to delete
    # @retval success whether successfully delete the manager or not
    manager_name = request.POST.get('username')
    try:
        models.User_info.objects.get(
            username=manager_name, is_manager=True).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


def get_managers(request):
    ##
    # Get the informations of the manager.
    # @param managers quaryset of the managers information in database
    # @param manager_names list of the manager names
    # @param manager_numbers list of the manager ids
    # @retval manager_names
    # @retval manager_numbers
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
    ##
    # Change the password of the current user.
    # @param manager_name id of current user
    # @param password new password of the user
    # @param oldpassword old password of the user
    # @retval success whether successfully change the password or not
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
    ##
    # Get the informations of a manager.
    # @param username id of the manager
    # @param manager informations of the manager in database
    # @retval nickname the nickname of the manager
    # @retval time the created time of the manager account
    # @retval power is superuser or not
    username = request.POST.get('username')
    manager = models.User_info.objects.get(username=username)
    return JsonResponse({
        "nickname": manager.nickname,
        "time":
            str(manager.date_joined.year)+'年'+str(manager.date_joined.month) +
            '月'+str(manager.date_joined.day)+'日',
        "power": '超级管理员' if manager.is_superuser else '普通管理员'
    })
