# coding=utf-8
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils import timezone
from backend import models


def get_punch_info(request):
    ##
    # Get the punch info of a user and the corresponding book
    # @param username id of the user
    # @param booknumber id of the book
    # @param punch_require the punch requirement object of the book
    # @param punch_info the punch info object of the book and the user
    # @retval is_punched whether the user is punched for the book or not
    # @retval requirement the punch requirement of the book
    # @retval content the text content of the punch if the user has punched the book
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
    ##
    # Upload the punch content for the user with the book(including one file)
    # @param myfile one file of the files for the user to upload
    # @param username the id of the user
    # @param booknumber the id of the book
    # @param textcontent the text part of the punch content
    # @param is_video judge whether the file is a video or a picture
    # @param user the object of user_info got by username
    # @param book the object of book_info got by booknumber
    # @param punch_info object of the user_punch for the user and the book
    # @param contentnumber number of how many files for the book have been uploaded by the user
    # @param content file content of the corrent punch
    # @retval success whether successfully uploaded the file
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
    ##
    # Clear all the punch content of the user with the book
    # @param username the id of the user
    # @param booknumber the id of the book
    # @retval status whether successfully delete all the punch content
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
    ##
    # Get all the punch information of the level in the database
    # nowusername id of the current user (To judge whether he has liked, comment or not)
    # level the current level of the current user
    # books all the books in the current level
    # allpunch list all of the punch of all the books
    # retval status whether successfully got the punch
    # retval info all the punch contents
    nowusername = request.POST.get('username', '')
    level = request.POST.get('level', '')
    books = models.Book_info.objects.filter(level=level)
    allpunch = []
    bookscount = books.count()
    try:
        for i in books:
            onebookpunchs = models.User_punch.objects.filter(
                book_number=i)
            for j in onebookpunchs:
                onepieceinfo = get_one_punch(nowusername, j)
                allpunch.append(onepieceinfo)
        allpunch.sort(key=mysort('punchtime'))
        allpunch.reverse()
        return JsonResponse({'status': True, 'info': allpunch})
    except:
        return JsonResponse({'status': False})


def get_file_numbers(request):
    ##
    # Get all file contents of a specific punch
    # @param usernumber id of the punched user
    # @param booknumber id of the corresponding book
    # @param imgs image file punch_content objects of the punch
    # @param videos video file punch_content objects of the punch
    # @param imgfiles image files of the punch content
    # @param videofiles video files of the punch content
    # @retval imgfiles
    # @retval videofiles
    usernumber = request.POST.get('usernumber')
    booknumber = request.POST.get('booknumber')
    imgs = models.Punch_content.objects.filter(
        user_number=usernumber,
        book_number=booknumber,
        is_video=False
    )
    videos = models.Punch_content.objects.filter(
        user_number=usernumber,
        book_number=booknumber,
        is_video=True
    )
    imgfiles = []
    videofiles = []
    for i in imgs:
        imgfiles.append({'number': i.content_number, 'src': None})
    for i in videos:
        videofiles.append({'number': i.content_number, 'src': None})
    return JsonResponse({'imgfiles': imgfiles, 'videofiles': videofiles})


def get_one_punch(nowusername, punch):
    ##
    # Get all the content of a punch
    # @param usernumber id of the punched user
    # @param booknumber id of the corresponding book
    # @param punch_content punch_content object of the user with the book
    # @param likenumber the amount of user who liked the punch
    # @param contentnumber the amount of the files of the punch
    # @param imgs image file punch_content objects of the punch
    # @param videos video file punch_content objects of the punch
    # @param imgfiles image files of the punch content
    # @param videofiles video files of the punch content
    # @param has_liked judge if another user has liked the current punch
    # @param commentslist all the comments of the punch
    # @param onepieceinfo the dict of all the info of the punch
    # @retval onepieceinfo
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
    ##
    # Get all the comment of a punch
    # @param commentslist all the comment of the punch
    # @param comments all the user_comment objects of the punch
    # @retval commentslist
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
    ##
    # A user add a comment to a punch
    # @param username the id of the user to generate the punch
    # @param booknumber the id of the book of the punch
    # @param commentusername the id of the user to comment the punch
    # @param comment the comment content
    # @param user the user object to generate the punch
    # @param book the book object of the punch
    # @param commenter the user object to comment the punch
    # @param newcomment the new user_comment object of the punch and the comment user
    # @param commentlist all the comment of the punch
    # @retval status whether successfully comment the punch
    # @retval commentlist
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
    ##
    # sort a list by a key
    def sortbypro(obj):
        return obj[myproperty]
    return sortbypro


def like(request):
    ##
    # A user to like or dislike a punch
    # @param username the id of the user to generate the punch
    # @param booknumber the id of the book of the punch
    # @param likeusername the id of the user to like or dislike the punch
    # @param user the user object to generate the punch
    # @param book the book object of the punch
    # @param likeuser the user object to like or dislike the punch
    # @param has_like whether the user has liked the punch or not
    # @retval status whether successfully like the punch
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
    ##
    # Judge if the user has liked the punch
    # @param user the user object to generate the punch
    # @param book the book object of the punch
    # @param has_liked the number of the user has liked the punch
    # @retval true if the user has liked the punch else false
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
    ##
    # Get a specific image binary of a punch
    # @param user the user object to generate the punch
    # @param book the book object of the punch
    # @param imgfilenumber the number of the image of the punch
    # @param imgfile the punch_content object of the specific image
    # @retval the image binary of the punch
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
    ##
    # Get a specific video binary of a punch
    # @param user the user object to generate the punch
    # @param book the book object of the punch
    # @param imgfilenumber the number of the video of the punch
    # @param imgfile the punch_content object of the specific image
    # @retval the video binary of the punch
    usernumber = int(request.GET.get('username'))
    booknumber = request.GET.get('booknumber')
    videofilenumber = request.GET.get('videofile')
    videofile = models.Punch_content.objects.get(
        user_number=usernumber,
        book_number=booknumber,
        content_number=videofilenumber,
        is_video=True)
    return HttpResponse(videofile.content)
