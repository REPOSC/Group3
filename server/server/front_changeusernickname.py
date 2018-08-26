from django.http import JsonResponse
from backend import models


def change_user_nickname(request):
    username = request.POST.get('username')
    nickname = request.POST.get('nickname')
    user = models.User_info.objects.get(username=username)
    user.nickname = nickname
    user.save()
    return JsonResponse({'success': True})
