"""This module include some functions about system message."""
from django.http import JsonResponse
from backend import models


def get_key(message):
    ##
    # Get the key of 'isread' and 'number'.
    return (message['isread'], -message['number'])


def get_message(request):
    ##
    # Get all the messages.
    # @param user_number id of the user
    # @param user user information in database
    # @param messages the list of all the message
    # @param all_messages quary set of all the messages in database
    # @param message_index index of message in the list
    # @param message_status the status of one message
    # @retval messages
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
    ##
    # Mark one message as read.
    # @param user_number id of the user
    # @param user user information in database
    # @param message_number index of the message
    # @param message quary set of messages in database
    # @retval success whether successfully change the status or not
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
    ##
    # Mark a message as unread.
    # @param user_number id of the user
    # @param message_number id of the message
    # @retval success whether successfully change the status or not
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
    ##
    # Delete one message.
    # @param user_number id of the user
    # @param message_number id of the message
    # @param user user information in database
    # @param message message information in database
    # @retval success whether successfully delete the information or not
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
