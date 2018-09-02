"""This module is about write new message by manager."""
from django.http import JsonResponse
from backend import models


def put_message(request):
    ##
    # Send messages to all persons.
    # @param text the content we send to all persons
    # @param message the content we send to all persons
    # @retval success whether send messages successfully
    text = request.POST.get('content')
    message = models.Message.objects.create(message=text)
    message.save()
    return JsonResponse({'success': True})
