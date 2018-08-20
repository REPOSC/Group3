from django.http import JsonResponse
from django.contrib.auth.models import User
from backend import models
from . import tools
from . import debug


def all_student(request):
    students = models.User_info.objects.filter(is_manager=0)
    debug.debug(students)
    stu_nicknames = []
    stu_numbers = []
    for i in students:
        stu_nicknames.append(i.nickname)
        stu_numbers.append(i.username)
    return JsonResponse({
        'user_nicknames': stu_nicknames,
        'user_numbers': stu_numbers
    })
