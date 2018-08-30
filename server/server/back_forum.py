# coding=utf-8
from django.http import JsonResponse
from backend import models
from . import debug


def all_daka(request):
    dakas = models.User_punch.objects.all()
    booknumbers = []
    booknames = []
    usernumbers = []
    comments = []
    times = []
    likenums = []
    for i in dakas:
        booknumbers.append(i.book_number.number)
        booknames.append(i.book_number.name)
        usernumbers.append(i.user_number.number)
        comments.append(i.punch_text)
        times.append(str(i.time.year) + (str(i.time.month)
                                         if i.time.month >= 10 else ('0'+str(i.time.month))) +
                     (str(i.time.day) if i.time.day >= 10 else ('0'+str(i.time.day))))
        nowlikenumber = models.User_like.objects.filter(
            user_number=i.user_number.number,
            book_number=i.book_number.number
        ).count()
        likenums.append(nowlikenumber)
    return JsonResponse({
        'booknums': booknumbers,
        'booknames': booknames,
        'usernums': usernumbers,
        'likenums': likenums,
        'times': times,
        'comments': comments
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
        'comments': comments,
        'comment_user_numbers': comment_user_number_ids,
        'commentids': commentids
    })


def daka_like(request):
    book_num = request.POST.get('book_num')
    user_name = request.POST.get('user_name')
    dakalikes = models.User_like.objects.filter(book_number=book_num,
                                                user_number=user_name)
    daka_people = ''
    if dakalikes.count() == 0:
        pass
    elif dakalikes.count() > 3:
        for i in range(2):
            daka_people += dakalikes[i].like_user_number.username
            daka_people += '、'
        daka_people += dakalikes[2].like_user_number.username
        daka_people += ' 等人赞了这个打卡'
    else:
        for i in range(dakalikes.count()-1):
            daka_people += dakalikes[i].like_user_number.username
            daka_people += '、'
        daka_people += dakalikes[dakalikes.count()-1].like_user_number.username
        daka_people += ' 赞了这个打卡'
    return JsonResponse({
        'like_nicknames': daka_people
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
