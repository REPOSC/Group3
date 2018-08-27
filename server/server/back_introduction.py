from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from backend import models


def add_introduction_video(request):
    name = request.POST.get('name')
    video = request.FILES.get('video')
    try:
        function_video = models.Function_video.objects.get(function=name)
        function_video.video = video
        function_video.save()
    except:
        function_video = models.Function_video.objects.create(
            function=name, video=video)
        function_video.save()
    return JsonResponse({'success': 'true'})
