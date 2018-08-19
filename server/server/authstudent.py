from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from backend import models

def auth_student(request):
    number = request.POST.get('id', '')
    user_pwd = request.POST.get('password', '')
    user = authenticate(username=number, password=user_pwd, is_manager=False)
    if user is None:
        return JsonResponse({'status': 'error'})
    else:
        login(request, user)
        last_levels = models.User_info.objects.filter(username=number)
        last_level = last_levels[0].lasttime_level
        return JsonResponse({'status': 'right', 'last_level':last_level})
