# 输出学生等级

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from backend import models


@login_required
def show_level(request):
    number = request.user.number
    levels = models.User_level.objects.filter(number=number)
    level_list = []
    for onelevel in levels:
        level_list.append(onelevel.level)
    return JsonResponse({"levels": level_list})
