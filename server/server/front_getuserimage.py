from django.http import HttpResponse
from backend import models


def get_user_image(request):
    username = request.GET.get('username')
    user = models.User_info.objects.get(username=username)
    try:
        return HttpResponse(user.image)
    except:
        return HttpResponse('None')
