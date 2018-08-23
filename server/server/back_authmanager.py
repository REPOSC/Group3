from django.http import JsonResponse
from django.contrib.auth import authenticate, login


def auth_manager(request):
    number = request.POST.get('id', '')
    user_pwd = request.POST.get('password', '')
    user = authenticate(username=number, password=user_pwd, is_manager=True)
    if user is None:
        return JsonResponse({'status': 'error'})
    else:
        login(request, user)
        return JsonResponse({'status': 'right'})
