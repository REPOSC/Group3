from django.http import JsonResponse
from backend import models


def daka_comment(request):
    item = request.POST.get('item', '')
    bookdakas = models.User_comment.objects.filter(book_number_id=item.book_num,
                                                user_number_id=item.user_name)
    comments = []
    comment_user_number_ids = []
    for i in bookdakas:
        comment_user_number_ids.append(i.comment_user_number)
        comments.append(i.comment)
    return JsonResponse({
        'comments':comments,
        'comment_user_numbers': comment_user_number_ids
    })
