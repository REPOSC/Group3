from django.http import JsonResponse
from backend import models


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
