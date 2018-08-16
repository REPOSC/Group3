from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_manager(request):
  return render(request, 'login_manager.html')

def auth_manager(request):
  number = request.POST.get('id', '')
  user_pwd = request.POST.get('password', '')
  user = authenticate(username=number, password=user_pwd, is_manager=True)
  if user is None:
    return JsonResponse({'status': 'error'})
  else:
    login(request, user)
    return JsonResponse({'status': 'right'})

def auth_student(request):
  number = request.POST.get('id','')
  user_pwd = request.POST.get('password','')
  user = authenticate(username=number, password=user_pwd, is_manager=False)
  if user is None:
    return JsonResponse({'status':'error'})
  else:
    login(request,user)
    return JsonResponse({'status':'right'})

@login_required
def main(request):
  return render(request,'index.html')


