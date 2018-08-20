from django.http import JsonResponse
from django.contrib.auth.models import User
from backend import models
from . import tools


def del_manager(request):
    manager_name = request.POST.get('username')
    try:
        models.User_info.objects.get(
            username=manager_name, is_manager=True).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})
