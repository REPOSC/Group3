from django.http import JsonResponse
from backend import models


def change_password(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        student = models.User_info.objects.get(
            username=username, is_manager=False)
        student.set_password(password)
        student.save()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})
