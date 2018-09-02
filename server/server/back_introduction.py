"""This module is to add new function videos."""
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from backend import models


def add_introduction_video(request):
    ##
    # Add a introduction video for books.
    # @param name the name of the video
    # @param video the video we should add for one book
    # @retval success whether add introduction video successfully
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
