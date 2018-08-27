from django.http import JsonResponse
from backend import models
from . import tools


def create_student(request):
    student_num = models.User_info.objects.filter(
        is_manager=False, is_superuser=False).count()
    student_num += 10000000
    count = int(request.POST.get('number'))
    student_names = []
    student_pwds = []
    for i in range(count):
        student_num += 1
        student_names.append(str(student_num))
        student_pwds.append(tools.random_string(15))
        student = models.User_info.objects.create_user(
            number=student_num,
            password=student_pwds[i],
            username=student_names[i],
            nickname=student_names[i],
            is_manager=False)
        student.save()
        student_levels = request.POST.getlist('values')
        for j in student_levels:
            student_level = models.User_level.objects.create(
                number=student, level=j)
            student_level.save()
    return JsonResponse({"number": student_names, "password": student_pwds})


def all_student(request):
    students = models.User_info.objects.filter(is_manager=0)
    stu_nicknames = []
    stu_numbers = []
    levels = []
    success = []
    str1 = []
    str2 = ''
    for i in students:
        user = models.User_process.objects.filter(user_number=i.username)
        usernum = user.count()
        for n in usernum:
            if n.process == 0:
                usernum -= 1
        success.append(usernum)
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
        'booknums': success
    })


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


def set_level(request):
    student_name = request.POST.get('username')
    try:
        student = models.User_info.objects.get(
            username=student_name, is_manager=False)
        models.User_level.objects.filter(number=student).delete()
        student_levels = request.POST.getlist('values')
        for i in student_levels:
            student_level = models.User_level.objects.create(
                number=student, level=i)
            student_level.save()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


def get_student(request):
    student_name = request.POST.get('value')
    student = models.User_info.objects.get(
        username=student_name, is_manager=False)
    levels = models.User_level.objects.filter(number=student)
    student_levels = []
    for i in levels:
        student_levels.append(str(i))
    return JsonResponse({"level": student_levels})
