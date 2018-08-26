from django.http import JsonResponse
from backend import models
from . import debug


def change_user_image(request):
    username = request.POST.get('username')
    picture = request.FILES.get('image')
    user = models.User_info.objects.get(username=username)
    user.image = picture
    user.save()
    return JsonResponse({'success': 'true'})
