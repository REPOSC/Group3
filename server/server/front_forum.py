# coding=utf-8
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils import timezone
from backend import models


def get_punch_info(request):
    username = request.POST.get('username', '')
    booknumber = request.POST.get('booknumber', '')
    punch_require = models.Book_punch_requirement.objects.filter(
        number=booknumber)
    punch_info = models.User_punch.objects.filter(
        user_number=username,
        book_number=booknumber)
    if punch_require:
        requirement = punch_require[0].requirement
        if punch_info:
            is_punched = punch_info[0].is_punched
            content = punch_info[0].punch_text
            if content is None:
                content = ''
            return JsonResponse({
                'is_punched': is_punched,
                'requirement': requirement,
                'content': content
            })
        else:
            return JsonResponse({
                'is_punched': False,
                'requirement': requirement
            })
    else:
        return JsonResponse({
            'is_punched': 'cannot',
            'requirement': 'No expanding yet!'
        })


def upload_homework(request):
    myfile = request.FILES.getlist('file', '')
    username = request.POST.get('username', '')
    booknumber = request.POST.get('booknumber', '')
    textcontent = request.POST.get('content', '')
    user = models.User_info.objects.get(username=username)
    book = models.Book_info.objects.get(number=booknumber)
    punch_info = models.User_punch.objects.filter(
        user_number=username,
        book_number=booknumber)
    contentnumber = models.Punch_content.objects.filter(
        user_number=username,
        book_number=booknumber
    ).count()
    try:
        content = models.Punch_content.objects.create(
            user_number=user,
            book_number=book,
            content_number=contentnumber,
            content=myfile[0]
        )
        content.save()
        models.User_punch.objects.filter(
            user_number=username,
            book_number=booknumber
        ).delete()
        punch_info = models.User_punch.objects.create(
            user_number=user,
            book_number=book,
            is_punched=True,
            punch_text=textcontent
        )
        punch_info.save()
        return JsonResponse({'status': 'true'})
    except:
        return JsonResponse({'status': 'error'})


def punch_reset(request):
    username = request.POST.get('username', '')
    booknumber = request.POST.get('booknumber', '')
    try:
        models.User_punch.objects.filter(
            user_number=username,
            book_number=booknumber
        ).delete()
        models.Punch_content.objects.filter(
            user_number=username,
            book_number=booknumber
        ).delete()
        models.User_comment.objects.filter(
            user_number=username,
            book_number=booknumber
        ).delete()
        return JsonResponse({'status': True})
    except:
        return JsonResponse({'status': False})


def get_community(request):
    nowusername = request.POST.get('username', '')
    level = request.POST.get('level', '')
    books = models.Book_info.objects.filter(level=level)
    booksid = []
    allpunch = []
    bookscount = books.count()
    try:
        for i in range(bookscount):
            booksid.append(books[i].number)
        for i in range(len(booksid)):
            onebookpunchs = models.User_punch.objects.filter(
                book_number=booksid[i])
            onebookpunchscount = onebookpunchs.count()
            for j in range(onebookpunchscount):
                onepieceinfo = get_one_comment(
                    nowusername, onebookpunchs, j, booksid, i)
                allpunch.append(onepieceinfo)
        allpunch.sort(key=mysort('punchtime'))
        allpunch.reverse()
        return JsonResponse({'status': True, 'info': allpunch})
    except:
        return JsonResponse({'status': False})


def get_one_comment(nowusername, onebookpunchs, j, booksid, i):
    usernumber = onebookpunchs[j].user_number
    user = models.User_info.objects.filter(username=usernumber)
    username = user[0].number
    punchtime = onebookpunchs[j].time
    punchtext = onebookpunchs[j].punch_text
    likenumber = models.User_like.objects.filter(
        user_number=username,
        book_number=booksid[i]
    ).count()
    contentnumber = models.Punch_content.objects.filter(
        user_number=username,
        book_number=booksid[i]
    ).count()
    has_liked = judge_like(username, booksid[i], nowusername)
    thisbook = models.Book_info.objects.filter(number=booksid[i])
    bookname = thisbook[0].name
    commentslist = get_comment(username, booksid[i])
    if punchtext is None:
        punchtext = ''
    onepieceinfo = {
        'username': username,
        'booknumber': booksid[i],
        'bookname': bookname,
        'punchtime': punchtime,
        'likenumber': likenumber,
        'punchtext': punchtext,
        'contentnumber': contentnumber,
        'has_liked': has_liked,
        'commentslist': commentslist,
        'newcomment': '',
        'commented': False,
        'comment_info': '评论'
    }
    return onepieceinfo


def get_comment(username, booknumber):
    commentslist = []
    comments = models.User_comment.objects.filter(
        user_number=username, book_number=booknumber)
    commentscount = comments.count()
    for i in range(commentscount):
        commentuser = models.User_info.objects.filter(
            username=comments[i].comment_user_number)
        commentusername = commentuser[0].number
        onepiececomment = {
            'commentid': comments[i].id,
            'commentusername': commentusername,
            'commenttext': comments[i].comment
        }
        commentslist.append(onepiececomment)
    commentslist.sort(key=mysort('commentid'))
    commentslist.reverse()
    return commentslist


def add_comment(request):
    username = request.POST.get('username', '')
    booknumber = request.POST.get('booknumber', '')
    commentuername = request.POST.get('commentusername', '')
    comment = request.POST.get('comment', '')
    try:
        user = models.User_info.objects.get(username=username)
        book = models.Book_info.objects.get(number=booknumber)
        commenter = models.User_info.objects.get(username=commentuername)
        newcomment = models.User_comment.objects.create(
            user_number=user,
            book_number=book,
            comment_user_number=commenter,
            comment=comment
        )
        newcomment.save()
        commentslist = get_comment(username, booknumber)
        return JsonResponse({'status': 'true', 'commentslist': commentslist})
    except:
        return JsonResponse({'status': 'false'})


def mysort(myproperty):
    def sortbypro(obj):
        return obj[myproperty]
    return sortbypro


def like(request):
    username = request.POST.get('username', '')
    booknumber = request.POST.get('booknumber', '')
    likeusername = request.POST.get('likeusername', '')
    user = models.User_info.objects.get(username=username)
    book = models.Book_info.objects.get(number=booknumber)
    likeuser = models.User_info.objects.get(username=likeusername)
    has_like = judge_like(username, booknumber, likeusername)
    if has_like:
        models.User_like.objects.get(
            user_number=user,
            book_number=book,
            like_user_number=likeuser
        ).delete()
    else:
        likeinfo = models.User_like.objects.create(
            user_number=user,
            book_number=book,
            like_user_number=likeuser
        )
        likeinfo.save()
    return JsonResponse({'status': 'true'})


def judge_like(username, booknumber, likeusername):
    user = models.User_info.objects.get(username=username)
    book = models.Book_info.objects.get(number=booknumber)
    likeuser = models.User_info.objects.get(username=likeusername)
    has_liked = models.User_like.objects.filter(
        user_number=user,
        book_number=book,
        like_user_number=likeuser
    ).count()
    if has_liked is 0:
        return False
    else:
        return True
