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
        booknumbers.append(i.book_number.number)
        usernumbers.append(i.user_number.number)
        comments.append(i.punch_text)
        riqis.append(i.time)
        nowlikenumber = models.User_like.objects.filter(
            user_number=i.user_number.number,
            book_number=i.book_number.number
        ).count()
        likenums.append(nowlikenumber)
    return JsonResponse({
        'booknums': booknumbers,
        'usernums': usernumbers,
        'likenums':likenums,
        'riqis':riqis,
        'comments':comments
    })


def daka_comment(request):
    book_num = request.POST.get('book_num')
    user_name = request.POST.get('user_name')
    bookdakas = models.User_comment.objects.filter(book_number=book_num,
                                                   user_number=user_name)
    comments = []
    comment_user_number_ids = []
    commentids = []
    for i in bookdakas:
        comment_user_number_ids.append(i.comment_user_number.number)
        comments.append(i.comment)
        commentids.append(i.id)
    return JsonResponse({
        'comments':comments,
        'comment_user_numbers': comment_user_number_ids,
        'commentids': commentids
    })


def daka_like(request):
    book_num = request.POST.get('book_num')
    user_name = request.POST.get('user_name')
    dakalikes = models.User_like.objects.filter(book_number=book_num,
                                                user_number=user_name)
    str1 = []
    str2 = ''
    like_user_numbers = []
    like_user_nicknames = ''
    for i in dakalikes:
        like_user_numbers.append(i.like_user_number.number)
        nicknames = models.User_info.objects.filter(number=i.user_number.number)
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
    comment_id = request.POST.get('commentid')
    try:
        models.User_comment.objects.filter(id=comment_id).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


def del_punch(request):
    book_num = request.POST.get('book_num')
    user_name = request.POST.get('user_name')
    try:
        models.User_punch.objects.get(book_number=book_num,
                                      user_number=user_name).delete()
        models.User_comment.objects.get(book_number=book_num,
                                        user_number=user_name).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})
