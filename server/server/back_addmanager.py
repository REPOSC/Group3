from django.http import JsonResponse
from django.contrib.auth.models import User
from backend import models
from . import tools
from . import debug


def add_manager(request):
    manager_name = request.POST.get('username')
    password = request.POST.get('password')
    manager_num = 100001
    try:
        manager_num = models.User_info.objects.filter(is_manager=True).latest('number').number
        manager_num += 1
    except:
        pass

    student = models.User_info.objects.create_user(
        number=manager_num,
        password=password,
        username=str(manager_num),
        nickname=manager_name,
        is_manager=True)
    student.save()
    return JsonResponse({'username': str(manager_num), 'password': password})
