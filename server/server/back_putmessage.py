from django.http import JsonResponse
from backend import models

def put_message(request):
    text = request.POST.get('content')
    message = models.Message.objects.create(message=text)
    message.save()
    return JsonResponse({'success': True})
