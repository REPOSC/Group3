from django.http import JsonResponse
from django.contrib.auth.models import User
from backend import models
from . import tools

def create_student(request):
  student_num = models.User_info.objects.filter(is_teacher=False).count()
  student_num += 1
  student_num += 1000000
  student_name = str(student_num)
  student_pwd = tools.random_string(15)
  student = models.User_info.objects.create_user(user_id=student_num,
                                                 password=student_pwd,
                                                 username=student_name)
  student.save()
  return JsonResponse({"user_id": student_name, "password": student_pwd})
