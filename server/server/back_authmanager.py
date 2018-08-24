from django.http import JsonResponse
from django.contrib.auth import authenticate, login


def auth_manager(request):
    number = request.POST.get('id', '')
    user_pwd = request.POST.get('password', '')
    user = authenticate(username=number, password=user_pwd, is_manager=True)
    if user:
        login(request, user)
        return JsonResponse({'status': 'right'})
    else:
        user = authenticate(
            username=number, password=user_pwd, is_superuser=True)
        if user:
            login(request, user)
            return JsonResponse({'status': 'right'})
        else:
            return JsonResponse({'status': 'error'})
