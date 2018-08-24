from django.http import JsonResponse
from backend import models


def show_level(request):
    number = request.POST.get('id', '')
    levels = models.User_level.objects.filter(number=number)
    level_list = []
    for onelevel in levels:
        level_list.append(onelevel.level)
    return JsonResponse({"levels": level_list})


def change_last_level(request):
    number = request.POST.get('id', '')
    new_last_level = request.POST.get('newlevel', '')
    try:
        user = models.User_info.objects.get(username=number)
        user.lasttime_level = new_last_level
        user.save()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})
