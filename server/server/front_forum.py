# coding=utf-8
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils import timezone
from backend import models
from . import debug


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
    myfile = request.FILES.get('file', '')
    username = request.POST.get('username', '')
    booknumber = request.POST.get('booknumber', '')
    textcontent = request.POST.get('content', '')
    is_video = request.POST.get('is_video')
    user = models.User_info.objects.get(username=username)
    book = models.Book_info.objects.get(number=booknumber)
    punch_info = models.User_punch.objects.filter(
        user_number=username,
        book_number=booknumber)
    contentnumber = models.Punch_content.objects.filter(
        user_number=username,
        book_number=booknumber
    ).count()
    content = models.Punch_content.objects.create(
        user_number=user,
        book_number=book,
        content_number=contentnumber,
        content=myfile,
        is_video=True if is_video == 'true' else False
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
        models.User_like.objects.filter(
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
    # try:
    for i in books:
        onebookpunchs = models.User_punch.objects.filter(
            book_number=i)
        for j in onebookpunchs:
            onepieceinfo = get_one_punch(nowusername, j)
            allpunch.append(onepieceinfo)
    allpunch.sort(key=mysort('punchtime'))
    allpunch.reverse()
    return JsonResponse({'status': True, 'info': allpunch})
    # except:
    #     return JsonResponse({'status': False})


def get_one_punch(nowusername, punch):
    usernumber = punch.user_number
    booknumber = punch.book_number
    punch_content = models.Punch_content.objects.filter(
        user_number=usernumber.number,
        book_number=booknumber.number
    )
    likenumber = models.User_like.objects.filter(
        user_number=usernumber.number,
        book_number=booknumber.number
    ).count()
    contentnumber = models.Punch_content.objects.filter(
        user_number=usernumber.number,
        book_number=booknumber.number
    ).count()
    imgs = models.Punch_content.objects.filter(
        user_number=usernumber.number,
        book_number=booknumber.number,
        is_video=False
    )
    videos = models.Punch_content.objects.filter(
        user_number=usernumber.number,
        book_number=booknumber.number,
        is_video=True
    )
    imgfiles = []
    videofiles = []
    for i in imgs:
        imgfiles.append({'number': i.content_number, 'src': None})
    for i in videos:
        videofiles.append({'number': i.content_number, 'src': None})

    has_liked = judge_like(usernumber.number, booknumber.number, nowusername)
    commentslist = get_comment(usernumber.number, booknumber.number)
    onepieceinfo = {
        'username': usernumber.username,
        'booknumber': booknumber.number,
        'bookname': booknumber.name,
        'punchtime': punch.time,
        'likenumber': likenumber,
        'punchtext': punch.punch_text,
        'imgfiles': imgfiles,
        'videofiles': videofiles,
        'has_liked': has_liked,
        'commentslist': commentslist,
        'newcomment': '',
        'commented': False,
        'comment_info': '评论'
    }
    return onepieceinfo


def get_comment(usernumber, booknumber):
    commentslist = []
    comments = models.User_comment.objects.filter(
        user_number=usernumber, book_number=booknumber)
    for i in comments:
        commentusername = models.User_info.objects.get(
            number=i.comment_user_number.number).number
        onepiececomment = {
            'commentid': i.id,
            'commentusername': commentusername,
            'commenttext': i.comment
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


def judge_like(usernumber, booknumber, likeusername):
    user = models.User_info.objects.get(number=usernumber)
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


def get_punch_image(request):
    usernumber = int(request.GET.get('username'))
    booknumber = request.GET.get('booknumber')
    imgfilenumber = request.GET.get('imgfile')
    imgfile = models.Punch_content.objects.get(
        user_number=usernumber,
        book_number=booknumber,
        content_number=imgfilenumber,
        is_video=False)
    return HttpResponse(imgfile.content)


def get_punch_video(request):
    usernumber = int(request.GET.get('username'))
    booknumber = request.GET.get('booknumber')
    videofilenumber = request.GET.get('videofile')
    videofile = models.Punch_content.objects.get(
        user_number=usernumber,
        book_number=booknumber,
        content_number=videofilenumber,
        is_video=True)
    return HttpResponse(videofile.content)
