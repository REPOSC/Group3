from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from backend import models

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
