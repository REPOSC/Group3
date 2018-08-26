from django.http import JsonResponse
from backend import models


def get_user_nickname(request):
    username = request.POST.get('username')
    user = models.User_info.objects.get(username=username)
    return JsonResponse({'nickname': user.nickname})
