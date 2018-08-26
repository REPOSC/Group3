from django.http import JsonResponse
from django.contrib.auth import authenticate
from backend import models


def change_user_password(request):
    username = request.POST.get('username')
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')
    user = authenticate(username=username, password=old_password)
    if user is None:
        return JsonResponse({'success': 'false'})
    else:
        user.set_password(new_password)
        user.save()
        return JsonResponse({'success': 'true'})
