from django.http import JsonResponse
from django.contrib.auth.models import User
from backend import models
from . import tools


def create_student(request):
    student_num = models.User_info.objects.filter(is_manager=False).count()
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
            is_manager=False)
        student.save()
        student_levels = request.POST.getlist('values')
        for j in student_levels:

            student_level = models.User_level.objects.create(
                number=student, level=j)
            student_level.save()
    return JsonResponse({"number": student_names, "password": student_pwds})
