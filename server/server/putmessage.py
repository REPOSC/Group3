from django.http import JsonResponse
from django.contrib.auth.models import User
from backend import models
from . import tools
from . import debug


def put_message(request):
    text = request.POST.get('content')
    message = models.Message.objects.create(message=text)
    message.save()
    return JsonResponse({'success': True})
