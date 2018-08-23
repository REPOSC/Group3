from django.http import JsonResponse
from backend import models


def change_manager(request):
    manager_name = request.POST.get('username')
    password = request.POST.get('password')
    try:
        manager = models.User_info.objects.get(
            username=manager_name, is_manager=True)
        manager.set_password(password)
        manager.save()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})
