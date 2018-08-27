from django.http import JsonResponse
from backend import models


def all_daka(request):
    dakas = models.User_punch.objects.filter(is_punched=True)
    booknumbers = []
    usernumbers = []
    comments = []
    riqis = []
    likenums = []
    for i in dakas:
        booknumbers.append(i.book_number)
        usernumbers.append(i.user_number)
        punch = models.User_punch.objects.filter(
            user_number=i.user_number, book_number=i.book_number)
        comments.append(punch.punch_text)
        riqis.append(i.time)
        likenums.append(i.like_number)
    return JsonResponse({
        'booknums': booknumbers,
        'usernums': usernumbers,
        'likenums': likenums,
        'riqis': riqis,
        'contents': comments
    })


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
        'comments': comments,
        'comment_user_numbers': comment_user_number_ids
    })


def daka_like(request):
    item = request.POST.get('item', '')
    dakalikes = models.User_like.objects.filter(book_number=item.book_num,
                                                user_number=item.user_name)
    str1 = []
    str2 = ''
    like_user_numbers = []
    like_user_nicknames = ''
    for i in dakalikes:
        like_user_numbers.append(i.like_user_number)
        nicknames = models.User_info.objects.filter(number=i.user_number)
    for j in nicknames:
        str1.append(str(j.nickname))
    str2 = ','.join(str1)
    like_user_nicknames = str2
    str1 = []
    str2 = ''
    return JsonResponse({
        'like_nicknames': like_user_nicknames
    })


def del_comment(request):
    item = request.POST.get('item')
    comment = request.POST.get('comment')
    try:
        models.User_comment.objects.get(
            book_number=item.book_num, user_number=item.user_name, comment_user_number=comment.shuo_user_id).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


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
