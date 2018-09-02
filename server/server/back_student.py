"""This module include some functions about manage student."""
# coding=utf-8
from django.http import JsonResponse
from backend import models
from . import tools


def create_student(request):
    ##
    # Create a new manager account.
    # @param student_num the number of one student
    # @param count the number of all students
    # @param student_names the nicknames of all students
    # @param student_pwds the password of a student acount
    # @retval number the number of one student
    # @retval password the password of one student account
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
    ##
    # Get all students information.
    # @param stu_numbers the nicknames of all student
    # @param stu_numbers the numbers of all student
    # @param levels the level of all students
    # @param success the number of the book one student has read
    # @param srt1 the level of one students
    # @param srt2 the level of one students
    # @retval user_nicknames the nicknames of all students
    # @retval user_numbers the numbers of all students
    # @retval levelss the levels of all students
    # @retval booknums the number of the book one student has read
    students = models.User_info.objects.filter(is_manager=0, is_superuser=0)
    stu_nicknames = []
    stu_numbers = []
    levels = []
    success = []
    str1 = []
    str2 = ''
    for i in students:
        user = models.User_process.objects.filter(user_number=i.username)
        num = user
        usernum = user.count()
        for n in num:
            if n.process == 0:
                usernum -= 1
        success.append(usernum)
        lv = models.User_level.objects.filter(number=i.username)
        for j in lv:
            str1.append(str(j.level+1))
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
    ##
    # Change a student password.
    # @param username the number of one student
    # @param password the password of one student
    # @retval success whether a student change password successfully
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
    ##
    # Set a student level.
    # @param student_name the number of one student
    # @param levels the levels one student can learn
    # @param student_levels the levels one student can learn
    # @retval success whether a student set level successfully
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
    ##
    # Get a student level.
    # @param student_name the number of one student
    # @param student one student object which has all information
    # @param levels the levels one student can learn
    # @param student_levels the levels one student can learn
    # @retval level student_levels
    student_name = request.POST.get('value')
    student = models.User_info.objects.get(
        username=student_name, is_manager=False)
    levels = models.User_level.objects.filter(number=student)
    student_levels = []
    for i in levels:
        student_levels.append(str(i))
    return JsonResponse({"level": student_levels})


def get_student_info(request):
    ##
    # Get a student information.
    # @param user_name the number of one student
    # @param student one student object which has all information
    # @retval nickname the nickname of one student
    # @retval time the time when a student became one member
    # @retval lasttime_level the level one student learnt last time
    username = request.POST.get('username')
    student = models.User_info.objects.get(username=username)
    return JsonResponse({
        "nickname": student.nickname,
        "time":
            str(student.date_joined.year)+'年'+str(student.date_joined.month) +
            '月'+str(student.date_joined.day)+'日',
        "lasttime_level": student.lasttime_level
    })
