"""This module is to manage the forum by manager."""
# coding=utf-8
from django.http import JsonResponse
from backend import models


def all_daka(request):
    ##
    # Get all punchs of every book.
    # @param dakas objects including all information of every punch
    # @param booknames all names of every book
    # @param booknumbers the number of every book
    # @param usernumbers the number of every punch person
    # @param comments the texts of every punch
    # @param times the time when all person punched
    # @param likenums the number of persons who liked every punched
    # @retval booknames
    # @retval booknums booknumbers
    # @retval usernums usernumbers
    # @retval likenums
    # @retval times
    # @retval comments
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
    ##
    # Get all comments of one book punch.
    # @param book_num the number of one book
    # @param user_name the name of the punch person
    # @param bookdakas objects including all information of punchs which we need
    # @param comments the texts of every punch
    # @param comment_user_number_ids the id of the person who comment the punch
    # @param commentids the id of punch comment
    # @retval comments
    # @retval comment_user_number_ids
    # @retval commentids
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
    ##
    # Get the people who like one book punch.
    # @param book_num the number of one book
    # @param user_name the number of book punch person
    # @param daka_people the people who like one book punch
    # @retval like_nicknames the people who like one book punch
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
    ##
    # Delete comment of one book punch.
    # @param comment_id the id of one book punch comment
    # @retval success whether delete the comment successfully
    comment_id = request.POST.get('commentid')
    try:
        models.User_comment.objects.filter(id=comment_id).delete()
    except:
        return JsonResponse({"success": False})
    return JsonResponse({"success": True})


def del_punch(request):
    ##
    # Delete one book punch.
    # @param book_num the number of one book
    # @param user_name the number of book punch person
    # @retval success whether delete the book punch successfully
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
