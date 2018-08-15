from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_manager(request):
  return render(request, "login_manager.html")


def auth_manager(request):
  user_id = request.POST.get('id', '')
  user_pwd = request.POST.get('password', '')

  f = open('poem.txt', 'w')
  print(request.POST, file=f)
  f.close()

  user = authenticate(username=user_id, password=user_pwd)
  if user is None:
    return JsonResponse({"status": "error", "user_id": user_id, "user_pwd": user_pwd})
  else:
    login(request, user)
    return JsonResponse({"status": "right"})




