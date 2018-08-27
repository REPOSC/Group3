from django.http import JsonResponse
from backend import models


def del_comment(request):
    item = request.POST.get('item')
    comment = request.POST.get('comment')
    try:
        models.User_comment.objects.get(book_number = item.book_num,
            user_number = item.user_name,comment_user_number = comment.shuo_user_id).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})
