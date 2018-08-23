from django.http import JsonResponse
from backend import models


def get_managers(request):
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
