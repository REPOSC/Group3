from django.http import JsonResponse
from backend import models


def get_student(request):
    student_name = request.POST.get('value')
    student = models.User_info.objects.get(username=student_name, is_manager=False)
    levels = models.User_level.objects.filter(number=student)
    student_levels = []
    for i in levels:
        student_levels.append(str(i))
    return JsonResponse({"level":student_levels})
