from django.http import JsonResponse
from django.contrib.auth.models import User
from backend import models
from . import tools
from . import debug


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
