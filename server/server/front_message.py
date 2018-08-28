# coding=utf-8
from django.http import JsonResponse
from backend import models
from . import debug


def get_key(message):
    return (message['isread'], -message['number'])


def get_message(request):
    user_number = int(request.POST.get('username'))
    user = models.User_info.objects.get(number=user_number)
    messages = []
    all_messages = models.Message.objects.filter(time__gte=user.date_joined)
    for i in all_messages:
        message_index = i.id
        message_status = models.Message_user.objects.filter(
            number=user_number, message=message_index)
        if message_status.count() == 0:
            messages.append({'number': i.id,
                             'time': i.time,
                             'content': i.message,
                             'isread': 'false'})
        elif not message_status[0].del_status:
            messages.append({'number': i.id,
                             'time': i.time,
                             'content': i.message,
                             'isread': 'true'})
    messages.sort(key=get_key)
    return JsonResponse({'messages': messages})


def read_message(request):
    user_number = int(request.POST.get('username'))
    user = models.User_info.objects.get(number=user_number)
    message_number = int(request.POST.get('message'))
    message = models.Message.objects.get(id=message_number)
    try:
        models.Message_user.objects.get(
            number=user,
            message=message
        )
        return JsonResponse({'success': 'true'})
    except:
        message_status = models.Message_user.objects.create(
            number=user,
            message=message,
            del_status=False
        )
        message_status.save()
        return JsonResponse({'success': 'true'})


def unread_message(request):
    user_number = int(request.POST.get('username'))
    message_number = int(request.POST.get('message'))
    try:
        models.Message_user.objects.get(
            number=user_number,
            message=message_number
        ).delete()
        return JsonResponse({'success': 'true'})
    except:
        return JsonResponse({'success': 'true'})


def delete_message(request):
    user_number = int(request.POST.get('username'))
    user = models.User_info.objects.get(number=user_number)
    message_number = int(request.POST.get('message'))
    message = models.Message.objects.get(id=message_number)
    try:
        message_user_item = models.Message_user.objects.get(
            number=user,
            message=message
        )
        message_user_item.del_status = True
        message_user_item.save()
        return JsonResponse({'success': 'true'})
    except:
        message_status = models.Message_user.objects.create(
            number=user,
            message=message,
            del_status=True
        )
        message_status.save()
        return JsonResponse({'success': 'true'})
