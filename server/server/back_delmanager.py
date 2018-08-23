from django.http import JsonResponse
from backend import models


def del_manager(request):
    manager_name = request.POST.get('username')
    try:
        models.User_info.objects.get(
            username=manager_name, is_manager=True).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})
