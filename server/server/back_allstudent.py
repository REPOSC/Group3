from django.http import JsonResponse
from backend import models

def all_student(request):
    students = models.User_info.objects.filter(is_manager=0)
    stu_nicknames = []
    stu_numbers = []
    levels = []
    success = []
    str1 = []
    str2 = ''
    for i in students:
        aaa = models.User_process.objects.filter(user_number=i.username)
        success.append(aaa)
        lv = models.User_level.objects.filter(number=i.username)
        for j in lv:
            str1.append(str(j.level))
        str2 = ','.join(str1)
        levels.append(str2)
        str1 = []
        str2 = ''
        stu_nicknames.append(i.nickname)
        stu_numbers.append(i.username)
    return JsonResponse({
        'user_nicknames': stu_nicknames,
        'user_numbers': stu_numbers,
        'levelss': levels,
        # 'booknums':success
    })
