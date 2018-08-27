from django.http import JsonResponse
from backend import models


def del_punch(request):
    item = request.POST.get('item')
    try:
        models.User_punch.objects.get(book_number=item.book_num,
                                         user_number=item.user_name).delete()
        models.User_comment.objects.get(book_number=item.book_num,
                                         user_number=item.user_name).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})
